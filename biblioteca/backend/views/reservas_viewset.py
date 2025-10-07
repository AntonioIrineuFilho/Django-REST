from rest_framework.viewsets import ModelViewSet
from ..serializers import ReservasSerializer
from ..models import Reservas

class ReservasViewSet(ModelViewSet):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer