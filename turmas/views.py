from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Turma

class TurmaCreateView(CreateView):
    model = Turma
    fields = '__all__'
    template_name = 'turma_cadastrar.html'
    success_url = reverse_lazy('index')

from django.views.generic import ListView
from .models import Turma
from django.db.models import Count # Para contar os alunos

class TurmaListView(ListView):
    model = Turma
    template_name = 'turma_list.html'
    context_object_name = 'turmas'
    
    def get_queryset(self):
        # Otimiza a consulta para buscar o professor e contar os alunos
        queryset = Turma.objects.select_related('professor').annotate(
            num_alunos=Count('alunos') # 'alunos' é o related_name do ForeignKey em Aluno
        )
        return queryset
