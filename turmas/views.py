from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Count
from django.urls import reverse_lazy
from .models import Turma
from alunos.models import Aluno # Importe o modelo Aluno

# ... (outras views, como TurmaListView e TurmaCreateView)
class TurmaCreateView(CreateView):
    model = Turma
    fields = '__all__'
    template_name = 'turma_cadastrar.html'
    success_url = reverse_lazy('index')


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

class TurmaDetailView(DetailView):
    model = Turma
    template_name = 'turmas/turma_detail.html'
    context_object_name = 'turma' # O objeto principal será chamado 'turma'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # O objeto 'turma' já está no contexto (self.object)
        turma = self.object 
        
        # Usamos o related_name='alunos' para buscar todos os alunos desta turma
        alunos_da_turma = turma.alunos.all().order_by('nome')
        
        # Adiciona a lista de alunos ao contexto
        context['alunos'] = alunos_da_turma
        
        return context

