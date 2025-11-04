from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjetoViewSet, TarefaViewSet # ColunaViewSet, EtiquetaViewSet, ComentarioViewSet

router = DefaultRouter()
router.register(r"user", UserViewSet, basename="user")
router.register(r"projeto", ProjetoViewSet, basename="projeto")
#router.register(r"coluna", ColunaViewSet, basename="coluna")
#router.register(r"etiqueta", EtiquetaViewSet, basename="etiqueta")
router.register(r"tarefa", TarefaViewSet, basename="tarefa")
#router.register(r"comentario", ComentarioViewSet, basename="comentario")

urlpatterns = router.urls