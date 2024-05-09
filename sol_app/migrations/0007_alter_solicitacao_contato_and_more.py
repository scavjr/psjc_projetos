# Generated by Django 5.0.4 on 2024-04-29 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_app', '0002_tipodoc'),
        ('sol_app', '0006_alter_solicitacaofuncionarios_funcionario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funcionario_contato', to='cadastro_app.funcionarios'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funcionario_responsavel', to='cadastro_app.funcionarios'),
        ),
    ]
