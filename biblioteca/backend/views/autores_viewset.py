from rest_framework.viewsets import ModelViewSet
from ..serializers import AutoresSerializer
from ..models import Autores

class AutoresViewSet(ModelViewSet):
    queryset = Autores.objects.all()
    serializer_class = AutoresSerializer