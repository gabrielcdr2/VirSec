from django.db import models
from alunos.models import Aluno
from turmas.models import Disciplina
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


def validate_nota_range(value):
    if not (0 <= value <= 10):
        raise ValidationError(
            f'{value} não é uma nota válida. A nota deve estar entre 0 e 10.',
            params={'value': value},)

class Nota(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='notas')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='notas')
    valor = models.FloatField(
        # Substitua a lambda por validadores serializáveis
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        help_text="Nota deve estar entre 0 e 10"
    )
    data_lancamento = models.DateTimeField(auto_now_add=True)

