from django.db import models
from cadastro_app.models import Funcionarios, Regioes, Setores, TiposOS


class Solicitacao(models.Model):
    nome_referencia = models.CharField(max_length=200, verbose_name='Referência',)
    nome_reduzido = models.CharField(max_length=50)
    doc_sol = models.CharField(max_length=100, verbose_name='Documento da Solicitação')
    data_sol = models.DateField(verbose_name='Data da Solicitação')
    endereco = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    regiao = models.ForeignKey(Regioes, on_delete=models.PROTECT)
    setor = models.ForeignKey(Setores, on_delete=models.PROTECT)
    responsavel = models.ForeignKey(Funcionarios, on_delete=models.PROTECT, related_name='funcionario_responsavel')
    contato = models.ForeignKey(Funcionarios, on_delete=models.PROTECT, related_name='funcionario_contato')
    tipoos = models.ForeignKey(TiposOS, on_delete=models.PROTECT)
    equipe_dpo = models.ManyToManyField(Funcionarios, through="SolicitacaoFuncionarios")
    nome_equipe = models.CharField(max_length=50)
    data_criacao = models.DateField(auto_now_add=True)


class SolicitacaoFuncionarios(models.Model):
    class EquipeFormacaoRegra(models.TextChoices): 
        CHEFE = "CHEFE", "Chefe"
        MEMBRO = "MEMBRO", "Membro" 
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE) 
    funcionario = models.ForeignKey(Funcionarios, on_delete=models.CASCADE)
    funcao = models.CharField(verbose_name="Posição na equipe", choices=EquipeFormacaoRegra.choices, max_length=20)
