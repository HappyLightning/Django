# Generated by Django 4.1.6 on 2023-02-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_alter_jogo_data_lançamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='data_lançamento',
            field=models.DateTimeField(),
        ),
    ]
