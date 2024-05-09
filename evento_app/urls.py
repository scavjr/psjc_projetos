from django.urls import path
from .views import EventoCreateView, EventoDetailView, EventoListView, EventoUpdateView, FormSuccessDeleteView, FormSuccessView, EventoDeleteView
urlpatterns = [
    path('evento_lista', EventoListView.as_view(), name='evento_lista'),
    path('evento_detalhe/<int:pk>', EventoDetailView.as_view(), name='evento_detalhe'),
    path('evento_update/<int:pk>', EventoUpdateView.as_view(), name='evento_atualiza'),
    path('evento_update/evento_success', FormSuccessView.as_view(), name='form_success_update'),
    path('evento_delete/<int:pk>', EventoDeleteView.as_view(), name='evento_delete'),
    path('evento_create', EventoCreateView.as_view(), name='evento_create'),
    path('evento_app/evento_success/<str:tipo_acao>', FormSuccessView.as_view(), name='evento_success'),
    path('evento_app/evento_success', FormSuccessView.as_view(), name='evento_success'),
    path('evento_delete/delete_success', FormSuccessDeleteView.as_view(), name='evento_delete_success'),
]
