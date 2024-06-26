# Generated by Django 5.0.4 on 2024-04-29 01:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro_app', '0002_tipodoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_referencia', models.CharField(max_length=200)),
                ('nome_reduzido', models.CharField(max_length=50)),
                ('doc_sol', models.CharField(max_length=100)),
                ('data_sol', models.DateField()),
                ('endereco', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('contato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funcionario_contato', to='cadastro_app.funcionarios')),
                ('regiao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro_app.regioes')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funcionario_responsavel', to='cadastro_app.funcionarios')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro_app.setores')),
                ('tipoos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro_app.tiposos')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitacaoFuncionarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_equipe', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('CHEFE', 'Chefe'), ('MEMBRO', 'Membro')], max_length=20, verbose_name='Posição na equipe')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastro_app.funcionarios')),
                ('solicitacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sol_app.solicitacao')),
            ],
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='equipe_dpo',
            field=models.ManyToManyField(through='sol_app.SolicitacaoFuncionarios', to='cadastro_app.funcionarios'),
        ),
    ]
