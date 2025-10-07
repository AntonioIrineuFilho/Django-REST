from rest_framework.viewsets import ModelViewSet
from ..serializers import CategoriasSerializer
from ..models import Categorias

class CategoriasViewSet(ModelViewSet):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer