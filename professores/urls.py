
from django.urls import path
from .views import ProfessorCreateView, ProfessorListView, ProfessorUpdateView, ProfessorDeleteView


app_name = 'professores'

urlpatterns = [
    path('cadastrar/', ProfessorCreateView.as_view(), name='professor_cadastrar'),
    path('lista/', ProfessorListView.as_view(), name='professor_list'),
    path('editar/<int:pk>/', ProfessorUpdateView.as_view(), name='professor_editar'),
    path('deletar/<int:pk>/', ProfessorDeleteView.as_view(), name='professor_deletar'),
]
