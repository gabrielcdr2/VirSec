from django.urls import path
from .views import TurmaCreateView, TurmaListView, TurmaDetailView, TurmaUpdateView, TurmaDeleteView

app_name = 'turmas'

urlpatterns = [
    path('cadastrar/', TurmaCreateView.as_view(), name='turma_cadastrar'),
    path('lista/', TurmaListView.as_view(), name='turma_list'),
    path('<int:pk>/', TurmaDetailView.as_view(), name='turma_detail'),
    path('editar/<int:pk>/', TurmaUpdateView.as_view(), name='turma_editar'),
    path('deletar/<int:pk>/', TurmaDeleteView.as_view(), name='turma_deletar'),
]