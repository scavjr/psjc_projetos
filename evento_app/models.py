from django.db import models

from cadastro_app.models import Eventos
from sol_app.models import Solicitacao


class EventoRegistro(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.PROTECT)
    data_evento = models.DateField()
    tipo_evento = models.ForeignKey(Eventos, on_delete=models.PROTECT)
    descricao = models.TextField(max_length=200)
    documento = models.CharField(max_length=50)
    responsavel = models.CharField(max_length=100, null=True)