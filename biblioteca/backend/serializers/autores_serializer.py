from rest_framework import serializers
from ..models import Autores

class AutoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autores
        fields = "__all__"