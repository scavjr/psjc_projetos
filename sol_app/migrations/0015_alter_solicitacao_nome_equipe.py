# Generated by Django 5.0.4 on 2024-05-22 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sol_app', '0014_solicitacao_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='nome_equipe',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
