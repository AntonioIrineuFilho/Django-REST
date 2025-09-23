from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password"
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # foge do padrão do create, portanto, deve ser sobrescrito
        return user

class UserLoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = authenticate(username=attrs.get("username"), password=attrs.get("password"))
        if not (user):
            serializers.ValidationError("Username ou password incorretos")
        attrs["user"] = user
        return attrs

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            "id",
            "title",
            "description",
            "is_completed",
            "user"
        )
        extra_kwargs = {
            "user": {"read_only": True}
        }