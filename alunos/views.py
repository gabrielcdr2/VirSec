from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Aluno

class AlunoCreateView(CreateView):
    model = Aluno
    fields = '__all__'
    template_name = 'alunos/cadastroAlunos.html'
    success_url = reverse_lazy('index')