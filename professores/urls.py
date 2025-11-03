from django.urls import path
from .views import ProfessorCreateView

app_name = 'professores'

urlpatterns = [
    path('cadastrar/', ProfessorCreateView.as_view(), name='professor_cadastrar'),
    # Adicionaremos outras URLs aqui no futuro (listar, editar, etc.)
]