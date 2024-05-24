from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views import View
from django.utils import timezone
from sol_app.models import Solicitacao
from .forms import SolForm
from django.db.models import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin


class SolRecordFormView(LoginRequiredMixin, FormView):
    template_name = "sol_app/sol_form.html"
    form_class = SolForm
    success_url = "entry_success" + '?tipo_acao=criado'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        print('haqui')
        
        context = super().get_context_data(**kwargs)
        context["tipo_solicitacao"] = 'Nova '
        context['tipo_acao'] = 'Criado'
        return context

    def form_valid(self, form):
        print('aqui')
        form.save()
        return super().form_valid(form)
    
    
    def form_invalid(self, form):
        print('O formulário é inválido!')
        print(form.errors)  # Imprime os erros de validação
        return super().form_invalid(form)
    

class FormSuccessView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        acao = request.GET['tipo_acao']
        print(acao)
        if acao == 'Alteração':
            return render(request, 'evento_app/modal.html', {'sucesso_enviar': True, 'tipo_acao': 'alterado', 'nome_formulario' : 'Alteração','nome_url': 'sol_list', 'tipo_cadastro': 'Solicitação'})
        else:
            return render(request, 'evento_app/modal.html', {'sucesso_enviar': True, 'tipo_acao': 'criado', 'nome_formulario' : 'Criação','nome_url': 'sol_list','tipo_cadastro': 'Solicitação'})


class SolListView(LoginRequiredMixin, ListView):
    model = Solicitacao
    paginate_by = 10
    template_name = "sol_app/sol_lista.html"
    ordering = ['-id']

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["agora"] = timezone.now()
        return context


class SolDetailView(LoginRequiredMixin, DetailView):
    model = Solicitacao
    template_name = "sol_app/sol_detail.html"


class SolUpdateView(LoginRequiredMixin, UpdateView):
    model = Solicitacao
    form_class = SolForm
    template_name = "sol_app/sol_form.html"
    success_url = "entry_success" + '?tipo_acao=Alteração'
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tipo_acao'] = 'Alterado'
        context["tipo_solicitacao"] = 'Atualização de '
        return context
    


class SolDeleteView(LoginRequiredMixin, DeleteView):
    model = Solicitacao
    template_name = "sol_app/sol_delete_form.html"
    success_url = "delete_success" + '?tipo_acao=deletado'
    error_url = reverse_lazy("delete_error")

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError as e:
            print(e)
            return HttpResponseRedirect(self.error_url)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['info_error'] = 'Tem eventos'
        return context


class FormErrorView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        msg = "Solicitação não pode ser excluída, pois há eventos registrados no histórico dela."
        return render(
            request, "sol_app/msg_erro_excluir.html", context={"info_error": msg}
        )
    

class FormSuccessDeleteView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        print(request.GET)
        acao = request.GET['tipo_acao']
        if acao == 'deletado':
            return render(request, 'evento_app/modal.html', {'sucesso_enviar': True, 'tipo_acao': 'excluído', 'nome_formulario' : 'Exclusão', 'nome_url':'sol_list', 'tipo_cadastro': 'Solicitação'})
        else:
            return render(request, 'evento_app/modal.html', {'sucesso_enviar': True, 'tipo_acao': 'criado', 'nome_formulario' : 'Criação', 'nome_url':'sol_list', 'tipo_cadastro': 'solicitação'})
