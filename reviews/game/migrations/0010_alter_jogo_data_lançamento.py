# Generated by Django 4.1.6 on 2023-02-27 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_alter_jogo_data_lançamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='data_lançamento',
            field=models.DateTimeField(),
        ),
    ]
