from django.urls import path
from . import views


urlpatterns = [
    path('lista_historico', views.HistoricoListaView.as_view(), name= 'lista_historico')
]
