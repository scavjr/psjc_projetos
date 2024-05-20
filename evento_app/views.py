from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from evento_app.forms import EventoForm
from .models import EventoRegistro, Solicitacao


class EventoCreateView(LoginRequiredMixin, CreateView):
    model = EventoRegistro
    # fields = ['data_evento', 'descricao','documento', 'responsavel', 'tipo_evento','solicitacao']
    form_class = EventoForm
    template_name = 'evento_app/evento_form.html'
    success_url = 'evento_app/evento_success'+'?tipo_acao=criado'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['solicitacao'].choices = [(item.id, item.nome_referencia) for item in Solicitacao.objects.all()]
        return form
    


class EventoListView(LoginRequiredMixin,ListView):
    model = EventoRegistro
    paginate_by = 10
    template_name = 'evento_app/evento_lista.html'


class EventoDetailView(LoginRequiredMixin,DetailView):
    model = EventoRegistro
    template_name = 'evento_app/evento_registro_detalhe.html'


class EventoUpdateView(LoginRequiredMixin,UpdateView):
    model = EventoRegistro
    # fields = ['data_evento', 'descricao','documento', 'responsavel', 'tipo_evento','solicitacao']
    form_class = EventoForm
    template_name = 'evento_app/evento_form.html'
    success_url = 'evento_success' + '?tipo_acao=Alteração'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_acao'] = 'Alterado'
        return context

class FormSuccessView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        print(request.GET)
        acao = request.GET['tipo_acao']
        if acao == 'Alteração':
            return render(request, 'evento_app/modal.html', {'sucesso_enviar': True, 'tipo_acao': 'alterado', 'nome_formulario' : 'Alteração','nome_url': 'evento_lista', 'tipo_cadastro': 'Evento'})
        else:
            return render(request, 'evento_app/modal.html', {'sucesso_enviar': True, 'tipo_acao': 'criado', 'nome_formulario' : 'Criação','nome_url': 'evento_lista','tipo_cadastro': 'Evento'})

class EventoDeleteView(LoginRequiredMixin,DeleteView):
    model = EventoRegistro
    template_name = 'evento_app/evento_delete_form.html'
    success_url = 'delete_success' + '?tipo_acao=deletado'

class FormSuccessDeleteView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        print(request.GET)
        acao = request.GET['tipo_acao']
        if acao == 'deletado':
            return render(request, 'evento_app/modal.html', {'sucesso_enviar': True, 'tipo_acao': 'excluído', 'nome_formulario' : 'Exclusão', 'nome_url':'evento_lista', 'tipo_cadastro': 'Evento'})
        else:
            return render(request, 'evento_app/modal.html', {'sucesso_enviar': True, 'tipo_acao': 'criado', 'nome_formulario' : 'Criação', 'nome_url':'evento_lista', 'tipo_cadastro': 'Evento'})

 