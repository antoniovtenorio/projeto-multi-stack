# Generated by Django 3.2 on 2021-06-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20210615_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarista',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]