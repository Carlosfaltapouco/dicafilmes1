# Generated by Django 4.0.2 on 2022-02-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dicas', '0003_dica_pessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='dica',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
