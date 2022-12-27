from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Relacionamento de muitos para muitos.


class Post(models.Model):

    # Escolhas para cada objeto.
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # 'on_delete.CASCADE', se o usuário for deletado o banco também deletará cada post do usuário.
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)  # uma coluna DATETIME no db.
    created = models.DateTimeField(auto_now_add=True)  # Salva automágicamente ao criar um objeto.
    updated = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        verbose_name_plural = "Postagens"  # Corrige a exibição do nome em plural.
        ordering = ['-publish']  # Ordenar pela data do campo 'publish'. O '-' significa ordem decrescente.
        indexes = [models.Index(fields=['-publish']), ]

    def __str__(self):
        return self.title
