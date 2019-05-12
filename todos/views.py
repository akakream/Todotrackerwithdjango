from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from django.forms import ModelForm

# Create your views here

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name', 'deadline', 'progress']

def home(request):
    context = {
        "todos": Todo.objects.all()
    }
    return render(request, "todos/index.html", context)

def viewtodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)    
    return render(request, "todos/view.html", {'object':todo})    

def addtodo(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "todos/addtodo.html", {'title': 'Add TODO | TODO-Tracker'}, {'form':form})

def deletetodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)    
    if request.method=='POST':
        todo.delete()
    context = {
        "todos": Todo.objects.all()
    }     
    return render(request, "todos/index.html", context)   

def edittodo(request, pk):
    todo= get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
    return render(request, "todos/edit.html", {'title': 'Edit TODO | TODO-Tracker'}, {'form':form})

def contact(request):
    return render(request, "todos/contact.html", {'title': 'Contact | TODO-Tracker'})    