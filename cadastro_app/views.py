from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Cargos, Fases, Regioes, Setores
import cadastro_app.utils as utils
from cadastro_app import cadastro_form
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def cadastros_list_view(request):
    return render(
        request,
        "cadastro_app/cadastro_lista.html",
    )

@login_required
def cadastro_view(request, id=None, nome_model=None):
    nome_model = request.resolver_match.kwargs['nome_model']
    model1 = apps.get_model('cadastro_app', nome_model)
    if request.method == "GET":
        nome_url = nome_model.lower()
        if id is not None:
            registro = get_object_or_404(model1, id=id)
            form = modelform_factory(model1, fields='__all__', )
            form = form(instance=registro)
            return render(
                request,
                "cadastro_app/cadastro.html",
                context={
                    "nome_url": nome_url,
                    "form": form,
                    "nome_title": nome_model,
                    "lista_campos": ["sigla", "nome"],
                },
            )
        else:
            tabela = "cadastro_app."+ nome_model
            todos_registros = utils.obter_todos(tabela)
            nome_url = nome_model.lower()
            
            if len(todos_registros) != 0:
                lista_campos = todos_registros.values()[0]
            else:
                lista_campos = ['id','sigla','nome']
            return render(
                request,
                "cadastro_app/lista.html",
                context={
                    "nome_url": nome_url,
                    "lista": todos_registros,
                    "nome_title": nome_model,
                    "lista_campos": lista_campos
                },
            )
    else:
        form = modelform_factory(model1, fields='__all__')
        nome_model = request.resolver_match.kwargs['nome_model']
        nome_url = nome_model.lower()
        return render(
            request,
            "cadastro_app/cadastro.html",
            context={
                "nome_url": nome_url,
                "form": form,
                "nome_title": nome_model,
                "lista_campos": ["sigla", "nome"],
                    },
                )

@login_required
def cadastro_excluir_view(request, id=None, nome_model=None, acao=None):
    nome_model: str = request.resolver_match.kwargs['nome_model']
    model1 = apps.get_model('cadastro_app', nome_model)
    if acao == 'excluir':
        registro = get_object_or_404(model1, id=id)
        registro_deletado = registro.delete()
        messages.add_message(request, messages.WARNING, "Você excluir o item " + str(registro_deletado))
    url_name = nome_model.lower()
    return redirect(url_name)

@login_required
def cadastro_novo_view(request, nome_model=None, novo=None):
    novo_registro = request.POST
    nome_model: str = request.resolver_match.kwargs['nome_model']
    url_nome = nome_model.lower()
    model1 = apps.get_model('cadastro_app', nome_model)
    instance = model1()
    for nome_campo, valor_campo in novo_registro.items():
        if nome_campo == 'setor':
            valor_campo = Setores.objects.get(id=valor_campo)
        if nome_campo == 'cargo':
            valor_campo = Cargos.objects.get(id=valor_campo)
        if nome_campo == 'fase':
            valor_campo = Fases.objects.get(id=valor_campo)
        setattr(instance, nome_campo, valor_campo)
    instance.save()
    return redirect(url_nome)

@login_required
def cancel_view(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
