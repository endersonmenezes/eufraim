from rest_framework import routers
from .viewsets import OcorrenciaViewSet
router = routers.DefaultRouter()

router.register(r'ocorrencia', OcorrenciaViewSet, basename='api_ocorrencia')
