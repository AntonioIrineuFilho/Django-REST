from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .serializers import UserRegisterSerializer, UserLoginSerializer, TaskSerializer
from .services import TaskService
from .models import Task

class UserRegisterAPIView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if (serializer.is_valid()):
            try:
                serializer.save()
                return Response({"message":"Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED)
            except Exception as error:
                return Response({"error":str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if (serializer.is_valid()):
            try:
                user = serializer.validated_data.get("user")
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token":token.key}, status=status.HTTP_200_OK)
            except Exception as error:
                return Response({"error":str(error)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateReadTaskAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tasks = TaskService.userTasks(user=self.request.user)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if (serializer.is_valid()):
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as error:
                return Response({"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteTaskAPI(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        task = TaskService.getOne(pk, self.request.user)
        if (task):
            serializer = TaskSerializer(instance=task, data=request.data)
            if (serializer.is_valid()):
                try:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Exception as error:
                    return Response({"error":str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Tarefa não encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        task_deleted = TaskService.deleteTask(pk, self.request.user)
        if (task_deleted):
            return Response({"message": "Tarefa deletada com sucesso!", status=status.HTTP_204_NO_CONTENT})
        return Response({"message": "Tarefa não encontrada!"}, status=status.HTTP_404_NOT_FOUND)


    

