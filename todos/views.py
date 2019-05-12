from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from django.forms import ModelForm
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)

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

class TodoListView(ListView):
    model = Todo
    template_name = 'todos/index.html'
    context_object_name = 'todos'
    ordering = ['id']

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todos/view.html'

class TodoCreateView(CreateView):
    model = Todo
    fields = ['name', 'deadline', 'progress']

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['name', 'deadline', 'progress']

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = '/todos'

def contact(request):
    return render(request, "todos/contact.html", {'title': 'Contact | TODO-Tracker'})    