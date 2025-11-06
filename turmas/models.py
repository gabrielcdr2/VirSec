from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=100, unique=True) 
    descricao = models.TextField(blank=True, null=True)
    
    professor = models.ForeignKey('professores.Professor', on_delete=models.SET_NULL, null=True, blank=True,related_name='turmas')
    
    

    def __str__(self):
        return self.nome
