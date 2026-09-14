from django.http import JsonResponse

from .models import Status

def listar_status_tarefas(request):
    status = Status.objects.all().values('status')
    return JsonResponse(list(status), safe=False)