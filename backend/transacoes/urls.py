from rest_framework.routers import SimpleRouter
from .views import TransacaoViewSet

router = SimpleRouter()
router.register('transacoes', TransacaoViewSet)

urlpatterns = router.urls
