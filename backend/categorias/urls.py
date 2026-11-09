from django.urls import path
from .views import categorias_lista, categoria_detalhe, listar_categorias_despesas

urlpatterns = [
    path('categorias/', categorias_lista),
    path('categorias/despesas/', listar_categorias_despesas),
    path('categorias/<int:id>/', categoria_detalhe),
]
