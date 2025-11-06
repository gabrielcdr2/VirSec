from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Professor

class ProfessorCreateView(CreateView):
    model = Professor
    fields = '__all__'
    template_name = 'professor_cadastrar.html'
    success_url = reverse_lazy('index')

class ProfessorListView(ListView):
    model = Professor
    template_name = 'professor_list.html'
    context_object_name = 'professores'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        
        if search_query:
            queryset = queryset.filter(nome__icontains=search_query)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Professores'
        context['search_query'] = self.request.GET.get('q', '')
        return context
    
class ProfessorUpdateView(UpdateView):
    model = Professor
    fields = '__all__'
    template_name = 'professor_cadastrar.html'
    success_url = reverse_lazy('professores:professor_list') 

class ProfessorDeleteView(DeleteView):
    model = Professor
    template_name = 'professor_confirm_delete.html'
    success_url = reverse_lazy('professores:professor_list')
