from modulos.canciones.views import CancionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(u'canciones', CancionViewSet, base_name="canciones")

urlpatterns = router.urls
