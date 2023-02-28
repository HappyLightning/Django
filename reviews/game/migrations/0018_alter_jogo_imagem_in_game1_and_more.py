# Generated by Django 4.1.6 on 2023-02-28 15:17

from django.db import migrations, models
import game.models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_alter_jogo_imagem_alter_jogo_imagem_in_game1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='imagem_in_game1',
            field=models.ImageField(null=True, upload_to=game.models.caminho_imagens),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='imagem_in_game2',
            field=models.ImageField(null=True, upload_to=game.models.caminho_imagens),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='imagem_in_game3',
            field=models.ImageField(null=True, upload_to=game.models.caminho_imagens),
        ),
    ]