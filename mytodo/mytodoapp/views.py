from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def index(request):
    if request.method == 'POST':
        mytask = Task(
            name = request.POST['task_title']
        )
        mytask.save()
        return redirect('tasklist')
    else:
        return render(request, 'index.html')

def test(request):
    return render(request, 'starter.html')

def tasklist(request):
    tasks = Task.objects.all()
    return render(request, 'tasklist.html', {'tasklist':tasks})

