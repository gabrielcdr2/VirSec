from django.db import models

# Create your models here.
class Turma(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    professor = models.CharField(max_length=100)
    quantidade_alunos = models.IntegerField()

    def __str__(self):
        return self.nome