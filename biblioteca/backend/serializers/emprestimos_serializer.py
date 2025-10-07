from rest_framework import serializers
from ..models import Emprestimos

class EmprestimosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = "__all__"