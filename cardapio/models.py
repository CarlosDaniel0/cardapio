from django.db import models

# Create your models here.


class Item(models.Model):
    imagem = models.FileField(upload_to='documents/')
    nome = models.CharField(max_length=200)
    valor = models.FloatField()
    descricao = models.TextField()
    ingredientes = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
