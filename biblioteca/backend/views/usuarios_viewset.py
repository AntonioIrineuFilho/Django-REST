from rest_framework.viewsets import ModelViewSet
from ..serializers import UsuariosSerializer
from ..models import Usuarios

class UsuariosViewSet(ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer