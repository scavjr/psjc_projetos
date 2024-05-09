from django.urls import path
from . import views


urlpatterns = [
    path('', views.ListarAuditoria.as_view(), name= 'listar_auditoria')
]
