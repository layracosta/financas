from django.http import JsonResponse

from .models import Tarefas

def listar_tarefas(request):
    tarefas = Tarefas.objects.all().values('descricao','tipo', 'data', 'status', 'usuario')
    return JsonResponse(list(tarefas), safe=False)