from django.shortcuts import render
from .tasks import go_to_sleep

def index(request):
    task_one = go_to_sleep.delay(1)
    return render(request, 'app/index.html', {'task_id' : task_one.task_id})