from rest_framework.viewsets import ModelViewSet
from ..serializers import MultasSerializer
from ..models import Multas

class MultasViewSet(ModelViewSet):
    queryset = Multas.objects.all()
    serializer_class = MultasSerializer