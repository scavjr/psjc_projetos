from django.forms import modelform_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import resolve
from .models import Cargos, Fases, Regioes, Setores
import cadastro_app.utils as utils
from cadastro_app import cadastro_form
from django.apps import apps
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from django.http import HttpResponseServerError


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
    nome_url = resolve(request.path).url_name
    if acao == 'excluir':
        registro = get_object_or_404(model1, id=id)
        try:
            registro_deletado = registro.delete()
            context = {'sucesso_enviar': True, 'tipo_acao': 'excluído', 'nome_formulario' : 'Exclusão', 'tipo_cadastro': nome_model, 'nome_url': nome_url}
            return render(request, 'evento_app/modal.html', context)
            # messages.add_message(request, messages.WARNING, "Você excluir o item " + str(registro_deletado))
        except ProtectedError as e:
            objetos_error = e.protected_objects
            for obj in objetos_error:
                msg_error = str(f"Não pode excluir essa dado, porque ele está sendo usado pela tabela {obj.__class__.__name__}. Exclua primeiro o registro dessa tabela.")
            return  HttpResponseServerError( msg_error)

    url_name = nome_model.lower()
    return redirect(url_name)



# class SolDeleteView(LoginRequiredMixin, DeleteView):
#     model = Solicitacao
#     template_name = "sol_app/sol_delete_form.html"
#     success_url = "delete_success"
#     error_url = reverse_lazy("delete_error")

#     def dispatch(self, request, *args, **kwargs):
#         try:
#             return super().dispatch(request, *args, **kwargs)
#         except ProtectedError as e:
#             print(e)
#             return HttpResponseRedirect(self.error_url)

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         context['info_error'] = 'Tem eventos'
#         return context





















@login_required
def cadastro_novo_view(request, nome_model=None, novo=None, setor=None):
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
