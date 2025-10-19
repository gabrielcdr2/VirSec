from django.urls import path
from .views import AlunoCreateView 

app_name = 'alunos'

urlpatterns = [
    path('cadastrar/', AlunoCreateView.as_view(), name='aluno_cadastrar'),
    # Adicionaremos outras URLs aqui no futuro (listar, editar, etc.)
]