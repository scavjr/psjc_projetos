from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Count
from cadastro_app.models import Eventos
from evento_app.models import EventoRegistro
from sol_app.models import Solicitacao
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin


# @login_required
class HistoricoListaView(LoginRequiredMixin, ListView):
    model = Solicitacao
    # paginate_by = 2
    template_name = "consulta_app/lista_historico.html"

    def get_queryset(self):
        queryset = self.model.objects.annotate(evento_registro_count=Count('eventoregistro')).prefetch_related('eventoregistro_set')
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dados'] = self.queryset
        return context

# Create your views here.
