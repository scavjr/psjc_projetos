# Generated by Django 5.0.4 on 2024-05-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol_app', '0016_alter_solicitacao_nome_equipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='nome_equipe',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
