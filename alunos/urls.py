from django.urls import path
from .views import AlunoCreateView, AlunoListView, AlunoUpdateView, AlunoDeleteView

app_name = 'alunos'

urlpatterns = [
    path('cadastrar/', AlunoCreateView.as_view(), name='aluno_cadastrar'),
    path('lista/', AlunoListView.as_view(), name='aluno_list'),
    path('editar/<int:pk>/', AlunoUpdateView.as_view(), name='aluno_editar'),
    path('deletar/<int:pk>/', AlunoDeleteView.as_view(), name='aluno_deletar'),
]