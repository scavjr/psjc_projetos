from django.urls import path
from .views import RegistroUsuarioView
urlpatterns = [
    path('cadastro_usuario/', RegistroUsuarioView.as_view(), name='registroUsuarioForm'),
]