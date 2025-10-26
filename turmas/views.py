from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Turma

class TurmaCreateView(CreateView):
    model = Turma
    fields = '__all__'
    template_name = 'turmas/cadastroTurmas.html'
    success_url = reverse_lazy('index')
