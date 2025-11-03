from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Professor

class ProfessorCreateView(CreateView):
    model = Professor
    fields = '__all__'
    template_name = 'professor_cadastrar.html'
    success_url = reverse_lazy('index')
