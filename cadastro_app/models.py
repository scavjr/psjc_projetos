from django.db import models


class Setores(models.Model):
    sigla = models.CharField(max_length=5, null=False, help_text='Sigla do setor')
    nome = models.CharField(max_length=50, null=False, help_text='Nome do setor')

    def __str__(self):
        return self.nome


class Regioes(models.Model):
    sigla = models.CharField(max_length=2, null=False)
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class TiposOS(models.Model):
    sigla = models.CharField(max_length=2, null=False, help_text='Sigla do tipo de obra ou serviço')
    nome = models.CharField(max_length=50, null=False, help_text='Sigla do tipo de obra ou serviço')

    def __str__(self):
        return self.nome


class Eventos(models.Model):
    sigla = models.CharField(max_length=3, null=False)
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class Cargos(models.Model):
    sigla = models.CharField(max_length=3, null=False)
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome

 
class Funcoes(models.Model):
    sigla = models.CharField(max_length=3, null=False)
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class Funcionarios(models.Model):
    nome = models.CharField(max_length=200, null=False)
    setor = models.ForeignKey(Setores, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargos, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Fases(models.Model):
    sigla = models.CharField(max_length=3, null=False)
    nome = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.nome


class Subfases(models.Model):
    sigla = models.CharField(max_length=3, null=False)
    nome = models.CharField(max_length=50, null=False)
    fase = models.ForeignKey(Fases, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Tipodoc(models.Model):
    sigla = models.CharField(max_length=3, null=False)
    nome = models.CharField(max_length=50, null=False)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
