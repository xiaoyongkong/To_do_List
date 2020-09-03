from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

@login_required 
def index(request):
    todo_list = Todo.objects.order_by('id').filter(user=request.user)
    form = TodoForm()
    context = {'todo_list' : todo_list, 'form' : form}
    
    return render(request, 'index.html', context)

@login_required
@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.user = request.user
        new_todo.save()

    return redirect('index')

@login_required
def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

@login_required
def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True, user=request.user).delete()

    return redirect('index')

@login_required
def deleteAll(request):
    Todo.objects.filter(user=request.user).delete()

    return redirect('index')