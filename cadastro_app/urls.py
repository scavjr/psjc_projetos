from django.urls import path
from cadastro_app.views import (
    cadastro_excluir_view,
    cadastro_novo_view,
    cadastro_view,
    cadastros_list_view,
    cancel_view,
)


urlpatterns = [
    path("", cadastros_list_view, name="cadastros_lista"),

    path("setores", cadastro_view, {'nome_model': 'Setores'}, name="setores"),
    path("setores/<int:id>", cadastro_view, {'nome_model': 'Setores'}, name="setores"),
    path("setores/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'Setores'}, name="setores"),
    path("setores/<str:novo>", cadastro_novo_view, {'nome_model': 'Setores'}, name="setores"),

    path("regioes", cadastro_view, {'nome_model': 'Regioes'}, name="regioes"),
    path("regioes/<int:id>", cadastro_view, {'nome_model': 'Regioes'}, name="regioes"),
    path("regioes/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'Regioes'}, name="regioes"),
    path("regioes/<str:novo>", cadastro_novo_view, {'nome_model': 'Regioes'}, name="regioes"),
    
    path("eventos", cadastro_view, {'nome_model': 'Eventos'}, name="eventos"),
    path("eventos/<int:id>", cadastro_view, {'nome_model': 'Eventos'}, name="eventos"),
    path("eventos/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'Eventos'}, name="eventos"),
    path("eventos/<str:novo>", cadastro_novo_view, {'nome_model': 'Eventos'}, name="eventos"),

    path("cargos", cadastro_view, {'nome_model': 'Cargos'}, name="cargos"),
    path("cargos/<int:id>", cadastro_view, {'nome_model': 'Cargos'}, name="cargos"),
    path("cargos/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'Cargos'}, name="cargos"),
    path("cargos/<str:novo>", cadastro_novo_view, {'nome_model': 'Cargos', 'setor': 'Cargo'}, name="cargos"),

    path("tipodoc", cadastro_view, {'nome_model': 'Tipodoc'}, name="tipodoc"),

    path("tipodoc", cadastro_view, {'nome_model': 'Tipodoc'}, name="tipodoc"),
    path("tipodoc/<int:id>", cadastro_view, {'nome_model': 'Tipodoc'}, name="tipodoc"),
    path("tipodoc/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'Tipodoc'}, name="tipodoc"),
    path("tipodoc/<str:novo>", cadastro_novo_view, {'nome_model': 'Tipodoc'}, name="tipodoc"),

    path("funcionarios", cadastro_view, {'nome_model': 'Funcionarios'}, name="funcionarios"),

    path("funcionarios", cadastro_view, {'nome_model': 'Funcionarios'}, name="funcionarios"),
    path("funcionarios/<int:id>", cadastro_view, {'nome_model': 'Funcionarios'}, name="funcionarios"),
    path("funcionarios/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'Funcionarios'}, name="funcionarios"),
    path("funcionarios/<str:novo>", cadastro_novo_view, {'nome_model': 'Funcionarios'}, name="funcionarios"),

    path("tiposos", cadastro_view, {'nome_model': 'TiposOS'}, name="tiposos"),

    path("tiposos", cadastro_view, {'nome_model': 'TiposOS'}, name="tiposos"),
    path("tiposos/<int:id>", cadastro_view, {'nome_model': 'TiposOS'}, name="tiposos"),
    path("tiposos/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'TiposOS'}, name="tiposos"),
    path("tiposos/<str:novo>", cadastro_novo_view, {'nome_model': 'TiposOS'}, name="tiposos"),

    path("fases", cadastro_view, {'nome_model': 'Fases'}, name="fases"),

    path("fases", cadastro_view, {'nome_model': 'Fases'}, name="fases"),
    path("fases/<int:id>", cadastro_view, {'nome_model': 'Fases'}, name="fases"),
    path("fases/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'Fases'}, name="fases"),
    path("fases/<str:novo>", cadastro_novo_view, {'nome_model': 'Fases'}, name="fases"),

    path("subfases", cadastro_view, {'nome_model': 'Subfases'}, name="subfases"),
    
    path("subfases", cadastro_view, {'nome_model': 'Subfases'}, name="subfases"),
    path("subfases/<int:id>", cadastro_view, {'nome_model': 'Subfases'}, name="subfases"),
    path("subfases/<str:acao>/<int:id>", cadastro_excluir_view, {'nome_model': 'Subfases'}, name="subfases"),
    path("subfases/<str:novo>", cadastro_novo_view, {'nome_model': 'Subfases'}, name="subfases"),

    path('cancelar/', cancel_view, name='cancelar'),
]
