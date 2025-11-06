from django.urls import path
from . import views

app_name = 'notas'

urlpatterns = [
    path('lancar/', views.lancar_notas, name='lancar_notas'),
]