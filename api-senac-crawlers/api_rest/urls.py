from django.urls import path
from . import views

urlpatterns = [
    # Rota da página inicial
    path('', views.home, name='home'),

    # CRUD para Edital
    path('editais/', views.edital_list, name='edital-list'),  # Listar e criar editais
    path('editais/deletar/<int:pk>/', views.edital_delete, name='edital-detail'),  # Detalhar e deletar edital específico
    path('editais/atualizar/<int:pk>/', views.edital_list, name='edital-update'),  # Atualizar edital específico


    # CRUD para Site
    path('sites/', views.site_list, name='site-list'),  # Listar e criar sites
    path('sites/deletar/<int:pk>/', views.site_delete, name='site-detail'),  # Detalhar e deletar site específico
    path('sites/atualizar/<int:pk>/', views.site_list, name='site-update'),  # Atualizar site específico

    # CRUD para Usuario
    path('usuarios/', views.usuario_list, name='usuario-list'),  # Listar e criar usuários
    path('usuarios/deletar/<int:pk>/', views.usuario_delete, name='usuario-detail'),  # Detalhar e deletar usuário específico
    path('usuarios/atualizar/<int:pk>/', views.usuario_list, name='usuario-update'),  # Atualizar usuário específico

]
