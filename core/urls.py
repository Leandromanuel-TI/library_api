from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, TecnicoViewSet, EquipamentoViewSet, ReparacaoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'tecnicos', TecnicoViewSet)
router.register(r'equipamentos', EquipamentoViewSet)
router.register(r'reparacoes', ReparacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
