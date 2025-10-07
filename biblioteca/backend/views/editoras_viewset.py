from rest_framework.viewsets import ModelViewSet
from ..serializers import EditorasSerializer
from ..models import Editoras

class EditorasViewSet(ModelViewSet):
    queryset = Editoras.objects.all()
    serializer_class = EditorasSerializer