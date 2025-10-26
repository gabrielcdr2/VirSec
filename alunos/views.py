from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Aluno

class AlunoCreateView(CreateView):
    model = Aluno
    fields = '__all__'
    template_name = 'alunos/cadastroAlunos.html'
    success_url = reverse_lazy('index')


class AlunoListView(ListView):
    model = Aluno
    template_name = 'alunos/aluno_list.html'
    context_object_name = 'alunos'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Alunos'
        return context
