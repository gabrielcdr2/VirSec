from django.urls import path
from .views import TurmaCreateView, TurmaListView

app_name = 'turmas'

urlpatterns = [
    path('cadastrar/', TurmaCreateView.as_view(), name='turma_cadastrar'),
    path('lista/', TurmaListView.as_view(), name='turma_list'),
]