from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Projeto, Coluna, Etiqueta, Tarefa, Comentario
from .serializers import UserSerializer, UserLoginSerializer, ProjetoSerializer, ColunaSerializer, EtiquetaSerializer, TarefaSerializer, ComentarioSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["POST"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if (serializer.is_valid()):
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            user = User.objects.filter(username=username).first()
            if (user):
                if (user.check_password(password)):
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({"token": token.key, "user": UserSerializer(user).data})
            return Response({"message": "Credenciais inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=["POST"])
    def signup(self, request):
        serializer = UserSerializer(data=request.data)
        if (serializer.is_valid()):
            user_by_username = User.objects.filter(username=serializer.validated_data.get("username")).exists()
            user_by_email = User.objects.filter(email=serializer.validated_data.get("email")).exists()
            if (user_by_username and user_by_email):
                return Response({"message": "Username e email já utilizados"}, status=status.HTTP_401_UNAUTHORIZED)
            elif (user_by_username):
                return Response({"message": "Username já utilizado"}, status=status.HTTP_401_UNAUTHORIZED)
            elif (user_by_email):
                return Response({"message": "Email já utilizado"}, status=status.HTTP_401_UNAUTHORIZED)
            user = User(
                first_name=serializer.validated_data.get("first_name"),
                last_name=serializer.validated_data.get("last_name"),
                username=serializer.validated_data.get("username"),
                email=serializer.validated_data.get("email")
            )
            user.set_password(serializer.validated_data.get("password"))
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": UserSerializer(user).data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #@authentication_classes([TokenAuthentication])
    #@permission_classes([IsAuthenticated])

    #@action(detail=False, methods=["GET"])
    #def test_token(self, request):
        #return Response(f"passou para {request.user}")

class ProjetoViewSet(ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["POST"])
    def create_project(self, request):
        serializer = ProjetoSerializer(data=request.data)
        if (serializer.is_valid()):
            project = serializer.save()
            return Response(ProjetoSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["GET"])
    def list_tasks(self, request, pk=None):
        tasks = Tarefa.objects.filter(coluna__projeto_id=pk)
        return Response(TarefaSerializer(tasks, many=True).data, status=status.HTTP_200_OK)
    
class TarefaViewSet(ModelViewSet):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["POST"])
    def create_task(self, request):
        serializer = TarefaSerializer(data=request.data)
        if (serializer.is_valid()):
            task = serializer.save()
            return Response(TarefaSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            

