from django.urls import path
from .views import acesso_negado_view, ListarAuditoria


urlpatterns = [
    path("acesso_negado/", acesso_negado_view, name= "acesso_negado"),
    path('', ListarAuditoria.as_view(), name= 'listar_auditoria'),
 
]
