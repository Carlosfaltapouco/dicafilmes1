# Generated by Django 4.0.2 on 2022-02-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dica',
            name='comentarios',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
