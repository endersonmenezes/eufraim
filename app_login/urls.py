from django.urls import path, include
from .views import inicial, ocorrencias, ativador_spiders
from .routers import router

app_name = 'app_login'

urlpatterns = [
    path('', inicial, name='inicial'),
    path('ocorrencias/', ocorrencias, name='ocorrencias'),
    path('ativador/', ativador_spiders, name='ativador'),
    path('api/', include(router.urls)),
]
