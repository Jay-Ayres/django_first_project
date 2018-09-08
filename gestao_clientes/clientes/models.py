from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    teste = models.IntegerField()


def __str__(self):
    return self.nome
