from rest_framework.routers import DefaultRouter
from .views import LivrosViewSet
from .views import AutoresViewSet
from .views import UsuariosViewSet
from .views import EmprestimosViewSet
from .views import ReservasViewSet
from .views import MultasViewSet
from .views import CategoriasViewSet
from .views import EditorasViewSet

router = DefaultRouter()
router.register(r"livros", LivrosViewSet, basename="livros")
router.register(r"autores", AutoresViewSet, basename="autores")
router.register(r"usuarios", UsuariosViewSet, basename="usuarios")
router.register(r"emprestimos", EmprestimosViewSet, basename="emprestimos")
router.register(r"reservas", ReservasViewSet, basename="reservas")
router.register(r"multas", MultasViewSet, basename="multas")
router.register(r"categorias", CategoriasViewSet, basename="categorias")
router.register(r"editoras", EditorasViewSet, basename="editoras")

urlpatterns = router.urls