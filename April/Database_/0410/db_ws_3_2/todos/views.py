from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }

    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
        context = {
            'form' : form,
        }
        return render(request, 'todos/create.html', context)
    
def delete(request, pk):
    todos = Todo.objects.get(pk=pk)
    todos.delete()
    return redirect('todos:index')