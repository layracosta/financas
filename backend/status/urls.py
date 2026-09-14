from django.urls import path

from .views import listar_status_tarefas

urlpatterns = [
    path('status/', listar_status_tarefas),
]