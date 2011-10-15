from django.db import models

class Palestrante(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    curriculo = models.TextField()
    twitter = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nome
