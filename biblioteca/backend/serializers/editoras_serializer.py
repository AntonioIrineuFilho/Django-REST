from rest_framework import serializers
from ..models import Editoras

class EditorasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editoras
        fields = "__all__"