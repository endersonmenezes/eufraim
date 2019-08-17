from django.urls import path, include
from .views import inicial
from .routers import router

app_name = 'app_login'

urlpatterns = [
    path('', inicial, name='inicial'),
    path('api/', include(router.urls)),
]
