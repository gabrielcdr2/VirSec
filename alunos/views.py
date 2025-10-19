from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Aluno

class AlunoCreateView(CreateView):
    model = Aluno
    fields = ['matricula', 'nome', 'idade', 'nascimento']
    template_name = 'alunos/cadastroAlunos.html'
    success_url = reverse_lazy('alunos:aluno_list')