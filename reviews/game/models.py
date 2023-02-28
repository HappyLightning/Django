from django.db import models

def caminho_imagens(instance, filename):
    return '{0}/{1}'.format(instance.titulo, filename)

class Genero(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome']),
        ]
        verbose_name = 'gênero'
        verbose_name_plural = 'gêneros'

    def __str__(self):
        return self.nome


class Jogo(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    genero = models.ManyToManyField(Genero, related_name='jogos')
    desenvolvedor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='')
    descrição = models.TextField()
    nota = models.DecimalField(max_digits=100, decimal_places=0)
    data = models.DateTimeField(auto_now_add=True)
    data_lançamento = models.DateTimeField(blank=True, null=True)
    selo_de_qualidade = models.BooleanField()
    imagem_in_game1 = models.ImageField(upload_to='')
    imagem_in_game2 = models.ImageField(upload_to='')
    imagem_in_game3 = models.ImageField(upload_to='')

    class Meta:
        ordering = ['titulo']
        indexes = [
            models.Index(fields=['titulo']),
        ]
