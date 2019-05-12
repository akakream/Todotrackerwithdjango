from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.      

class TodoList(ListView):
    model = Todo

class TodoView(DetailView):
    model = Todo

class TodoCreate(CreateView):
    model = Todo
    fields = ['name', 'deadline', 'progress']
    success_url = reverse_lazy('todo_list')

class TodoUpdate(UpdateView):
    model = Todo
    fields = ['name', 'deadline', 'progress']
    success_url = reverse_lazy('todo_list')

class TodoDelete(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_list')

def contact(request):
    return render(request, 'todos/contact.html')        