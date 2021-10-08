from django.db import models


class Pergunta(models.Model):
    enunciado = models.TextField()
    disponivel = models.BooleanField(default=False)
    alternativas = models.JSONField()
    alternativa = models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ])

    def __str__(self):
        return self.enunciado
