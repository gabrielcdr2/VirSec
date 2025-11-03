from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import login_view, IndexView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'), 
    path('dashboard/', IndexView.as_view(), name='index'), 
    path('alunos/', include('alunos.urls')),
    path('turmas/', include('turmas.urls')),
    path('professores/', include('professores.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)