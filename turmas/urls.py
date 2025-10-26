from django.urls import path
from .views import TurmaCreateView

app_name = 'turmas'

urlpatterns = [
    path('cadastrarTurma/', TurmaCreateView.as_view(), name='turma_cadastrar'),
]