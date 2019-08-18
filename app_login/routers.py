from rest_framework import routers
from .viewsets import OcorrenciaViewSet
router = routers.DefaultRouter()

router.register(r'ocorrencias', OcorrenciaViewSet, basename='api_ocorrencias')
