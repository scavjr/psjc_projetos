# Generated by Django 5.0.4 on 2024-04-29 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol_app', '0002_rename_role_solicitacaofuncionarios_funcao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitacaofuncionarios',
            name='nome_equipe',
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='nome_equipe',
            field=models.CharField(default=25052024, max_length=50),
            preserve_default=False,
        ),
    ]
