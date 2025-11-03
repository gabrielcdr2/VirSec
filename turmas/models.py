from django.db import models
# 1. NOVO MODELO: Professor

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nome

# 2. MODELO Turma (AGORA COM CHAVE ESTRANGEIRA PARA Professor)
class Turma(models.Model):
    nome = models.CharField(max_length=100, unique=True) # Turma 301, 302, etc.
    descricao = models.TextField(blank=True, null=True)
    
    # Chave estrangeira para o Professor
    professor = models.ForeignKey('professores.Professor', on_delete=models.SET_NULL, null=True, blank=True, related_name='turmas_lecionadas')

    
    # O campo 'quantidade_alunos' foi removido, será calculado na View

    def __str__(self):
        return self.nome
