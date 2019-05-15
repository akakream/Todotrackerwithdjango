from django.urls import path
from . import views
from .views import (
    TodoListView, 
    TodoDetailView, 
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView
)

urlpatterns = [
    path('', TodoListView.as_view(), name='todos-home'),
    path('viewtodo/<int:pk>/detail', TodoDetailView.as_view(), name='todos-viewtodo'),
    path('todo/new/', TodoCreateView.as_view(), name='todos-addtodo'),
    path('todo/<int:pk>/edit', TodoUpdateView.as_view(), name='todos-edittodo'),
    path('todo/<int:pk>/delete', TodoDeleteView.as_view(), name='todos-deletetodo'),
    path('contact/', views.contact, name='todos-contact'),
]