from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here

def home(request):
    context = {
        "todos": Todo.objects.all()
    }
    return render(request, "todos/index.html", context)

def addtodo(request):
    return render(request, "todos/addtodo.html")

def deletetodo(request):
    return HttpResponse("<h1>This is the deletetodo page</h1>")    

def edittodo(request):
    return render(request, "todos/edit.html")        