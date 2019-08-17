from django.urls import path, include
from .views import inicial

app_name = 'app_login'

urlpatterns = [
    path('', inicial, name='inicial')
]
