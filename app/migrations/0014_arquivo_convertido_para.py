# Generated by Django 5.1.2 on 2024-12-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_feedback_avaliacao_feedback_resposta'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='convertido_para',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
