from django.db import models

from status.models import Status
from usuarios.models import Usuario

class Tarefas(models.Model):

    TIPO_CHOICES = [
        ('PRIORIDADE ALTA', 'Prioridade Alta'),
        ('PRIORIDADE MÉDIA','Prioridade Média'),
        ('PRIORIDADE BAIXA','Prioridade Baixa'),
    ]

    descricao = models.CharField(max_length=200)
    data = models.DateField()
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

#1 Tarefa só pode se vinculada a 1 status

    def __str__(self):
        return f"{self.descricao} - {self.status }"