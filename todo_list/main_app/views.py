from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, UserLoginSerializer, TaskSerializer

class UserRegisterAPIView(APIView):

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if (serializer.is_valid()):
            try:
                serializer.save()
                return Response({"message":"Usuário criado com sucesso!"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if (serializer.is_valid()):
            try:
                user = serializer.validated_data.get("user")
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token":token.key}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskAPIView(APIView):
    print("teste")