from django.shortcuts import render
from django.views.generic import ListView
from easyaudit.models import CRUDEvent



class ListarAuditoria(ListView):
    model = CRUDEvent
    template_name = 'audit_app/listar_auditoria.html'
    context_object_name = 'audits'


