from django.db import models 

class Aluno(models.Model):
    matricula = models.CharField(max_length=9, unique=True)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)
    idade = models.IntegerField()
    nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    turma = models.ForeignKey(
        'turmas.Turma', 
        on_delete=models.SET_NULL, # Usar SET_NULL é mais seguro que CASCADE aqui
        null=True, 
        blank=True, 
        related_name='alunos'
    ) 

    def __str__(self):
        return self.nome