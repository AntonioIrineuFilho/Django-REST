from rest_framework.viewsets import ModelViewSet
from ..serializers import EmprestimosSerializer
from ..models import Emprestimos

class EmprestimosViewSet(ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer