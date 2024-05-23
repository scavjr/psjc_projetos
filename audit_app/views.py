from django.shortcuts import render
from django.views.generic import ListView
from easyaudit.models import CRUDEvent
from django.contrib.auth.mixins import LoginRequiredMixin




def acesso_negado_view(request):
    print('ok')
    return render(request, 'audit_app/so_admin.html')


class ListarAuditoria(LoginRequiredMixin,ListView):
    model = CRUDEvent
    template_name = 'audit_app/listar_auditoria.html'
    context_object_name = 'audits'


