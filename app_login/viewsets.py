from django_filters import rest_framework as rfilters
from rest_framework import pagination
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAdminUser
from .models import Ocorrencia
from .serializers import OcorrenciaSerializer

# DEFINITIONS AFTER HERE


class PaginationPagina20(pagination.PageNumberPagination):
    page_size = 20
    page_query_description = 'page'


class OcorrenciaViewSet(viewsets.ModelViewSet):
    queryset = Ocorrencia.objects.all().order_by('id')
    serializer_class = OcorrenciaSerializer
    pagination_class = PaginationPagina20
    filter_backends = (filters.SearchFilter, rfilters.DjangoFilterBackend,)
    search_fields = ('contrato_numero',)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        actions = list | create | retrieve | update | partial_update | destroy
        """
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == 'create':
            permission_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [IsAdminUser]
        elif self.action == 'update':
            permission_classes = [IsAdminUser]
        elif self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'destroy':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]