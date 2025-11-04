from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Projeto, Coluna, Etiqueta, Tarefa, Comentario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        write_only_fields = ("password")

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class ComentarioSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = ["id", "autor", "texto", "data_criacao"]


class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ["id", "nome", "cor"]


class TarefaSerializer(serializers.ModelSerializer):
    coluna_id = serializers.PrimaryKeyRelatedField(queryset=Coluna.objects.all(), source="coluna")
    criador_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="criador")
    tags_id = serializers.PrimaryKeyRelatedField(queryset=Etiqueta.objects.all(), source="tags", many=True)
    comentarios = ComentarioSerializer(source="comentario_set", read_only=True, many=True)
    total_comentarios = serializers.SerializerMethodField()

    class Meta:
        model = Tarefa
        fields = [
            "id",
            "titulo",
            "descricao",
            "coluna_id",
            "criador_id",
            "prioridade",
            "data_criacao",
            "data_conclusao",
            "tags_id",
            "comentarios",
            "total_comentarios",
        ]

    def get_total_comentarios(self, obj):
        return obj.comentario_set.count()


class ColunaSerializer(serializers.ModelSerializer):
    tarefas = TarefaSerializer(many=True, source="tarefa_set", read_only=True)
    nome_projeto = serializers.CharField(source="projeto.nome", read_only=True)

    class Meta:
        model = Coluna
        fields = ["id", "titulo", "ordem", "nome_projeto", "tarefas"]


class ProjetoSerializer(serializers.ModelSerializer):
    proprietario_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="proprietario")
    membros_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source="membros", many=True)
    total_tarefas = serializers.SerializerMethodField()
    # pega todas as colunas relacionadas ao projeto por meio da FK de projeto que está em coluna, basicamente o inverso do PrimaryKeyRelatedField
    coluna = ColunaSerializer(source="coluna_set", read_only=True, many=True)
    class Meta:
        model = Projeto
        fields = [
            "id",
            "nome",
            "descricao",
            "data_criacao",
            "proprietario_id",
            "membros_id",
            "total_tarefas",
            "coluna"
        ]

    def get_total_tarefas(self, obj):
        return Tarefa.objects.filter(coluna__projeto=obj).count()