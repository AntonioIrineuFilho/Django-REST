from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Projeto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    data_criacao = models.DateField(default=timezone.now)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projeto_proprietario")
    membros = models.ManyToManyField(User, related_name="projeto_membros")

    def __str__(self):
        return self.nome

class Coluna(models.Model):
    titulo = models.CharField(max_length=64)
    ordem = models.PositiveIntegerField(default=0)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Etiqueta(models.Model):
    nome = models.CharField(max_length=64)
    cor = models.CharField(max_length=16)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    TIPOS = [
        ('A', 'ALTA'),
        ('M', 'MÉDIA'),
        ('B', 'BAIXA')
    ]
    titulo = models.CharField(max_length=64)
    descricao = models.TextField()
    coluna = models.ForeignKey(Coluna, on_delete=models.CASCADE)
    criador = models.ForeignKey(User, on_delete=models.CASCADE)
    prioridade = models.CharField(max_length=1, choices=TIPOS)
    data_criacao = models.DateField(default=timezone.now)
    data_conclusao = models.DateField()
    tags = models.ManyToManyField(Etiqueta)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateField(default=timezone.now)

    def __str__(self):
        return self.texto