from rest_framework.viewsets import ModelViewSet
from ..serializers import LivrosSerializer
from ..models import Livros

class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer