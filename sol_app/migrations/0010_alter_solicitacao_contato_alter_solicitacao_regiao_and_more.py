# Generated by Django 5.0.4 on 2024-05-06 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_app', '0002_tipodoc'),
        ('sol_app', '0009_alter_solicitacao_data_sol_alter_solicitacao_doc_sol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='contato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario_contato', to='cadastro_app.funcionarios'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='regiao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_app.regioes'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario_responsavel', to='cadastro_app.funcionarios'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='setor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_app.setores'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='tipoos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro_app.tiposos'),
        ),
    ]
