from django.urls import path
from .views import AlunoCreateView, AlunoListView

app_name = 'alunos'

urlpatterns = [
    path('cadastrar/', AlunoCreateView.as_view(), name='aluno_cadastrar'),
    path('lista/', AlunoListView.as_view(), name='aluno_list'),
    # Adicionaremos outras URLs aqui no futuro (listar, editar, etc.)
]