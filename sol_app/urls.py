from django.urls import path
from .views import FormErrorView, FormSuccessDeleteView, SolDeleteView, SolRecordFormView, FormSuccessView, SolListView, SolDetailView, SolUpdateView
urlpatterns = [
    path('nova_sol', SolRecordFormView.as_view(), name='sol_record_form'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('sol_list', SolListView.as_view(), name='sol_list'),
    path('sol_detail/<int:pk>', SolDetailView.as_view(), name='sol_detalhe'),
    path('sol_detail/<str:excluir>/<int:pk>', SolDetailView.as_view(), name='sol_detalhe'),
    path('sol_form/<str:editar>/<int:pk>', SolUpdateView.as_view(), name='sol_form_editar'),
    path('sol_form/editar/entry_success', FormSuccessView.as_view(), name='sol_form_success'),
    path('sol_form_delete/<int:pk>', SolDeleteView.as_view(), name='sol_delete'),
    path('sol_form_delete/delete_success', FormSuccessDeleteView.as_view(), name='delete_success'),
    path('sol_form_delete/error', FormErrorView.as_view(), name='delete_error'),


]