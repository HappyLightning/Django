# Generated by Django 4.1.6 on 2023-02-28 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0014_jogo_imagem_in_game1_jogo_imagem_in_game2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='imagem',
            field=models.ImageField(upload_to='<django.db.models.fields.CharField>/'),
        ),
    ]