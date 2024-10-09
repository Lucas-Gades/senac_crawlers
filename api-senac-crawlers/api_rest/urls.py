# urls.py
from django.urls import path
from .views import (
    EditalListCreate,
    EditalDetail,
    SiteListCreate,
    SiteDetail,
    UsuarioListCreate,
    UsuarioDetail,
)

urlpatterns = [
    path('editais/', EditalListCreate.as_view(), name='edital-list-create'),  # Criação e listagem
    path('editais/deletar/<int:pk>/', EditalDetail.as_view(), name='edital-delete'),  # Deleção
    path('editais/atualizar/<int:pk>/', EditalDetail.as_view(), name='edital-update'),  # Atualização
    path('editais/<int:pk>/', EditalDetail.as_view(), name='edital-detail'),  # Detalhamento
    
    path('sites/', SiteListCreate.as_view(), name='site-list-create'),  # Criação e listagem
    path('sites/deletar/<int:pk>/', SiteDetail.as_view(), name='site-delete'),  # Deleção
    path('sites/atualizar/<int:pk>/', SiteDetail.as_view(), name='site-update'),  # Atualização
    path('sites/<int:pk>/', SiteDetail.as_view(), name='site-detail'),  # Detalhamento
    
    path('usuarios/', UsuarioListCreate.as_view(), name='usuario-list-create'),  # Criação e listagem
    path('usuarios/deletar/<int:pk>/', UsuarioDetail.as_view(), name='usuario-delete'),  # Deleção
    path('usuarios/atualizar/<int:pk>/', UsuarioDetail.as_view(), name='usuario-update'),  # Atualização
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),  # Detalhamento
]