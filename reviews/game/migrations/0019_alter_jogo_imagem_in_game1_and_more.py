# Generated by Django 4.1.6 on 2023-02-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0018_alter_jogo_imagem_in_game1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='imagem_in_game1',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='imagem_in_game2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='imagem_in_game3',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
