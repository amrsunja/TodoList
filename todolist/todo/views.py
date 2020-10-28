from django.shortcuts import render, redirect
from .models import *
from .forms import *


# добавление задачи
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context= {'tasks': tasks, 'form': form}

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, 'todolist/task.html', context)

#изменение задачи
def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'task': task, 'form': form}
    return render(request, 'todolist/update_task.html', context)

#удаление задачи
def delete(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item': item}

    if request.method =='POST':
        item.delete()
        return redirect('/')

    return render(request, 'todolist/delete.html', context)