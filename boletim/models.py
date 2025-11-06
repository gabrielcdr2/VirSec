from django.db import models

class Boletim(models.Model):
    aluno = models.ForeignKey(
        'alunos.Aluno', on_delete=models.SET_NULL, null=True, 
        blank=True, related_name='boletins')
    
    def __str__(self):
        return f"Boletim de {self.aluno.nome}"