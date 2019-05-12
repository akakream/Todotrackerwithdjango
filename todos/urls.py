from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='todos-home'),
    path('addtodo/', views.addtodo, name='todos-addtodo'),
    path('deletetodo/', views.deletetodo, name='todos-deletetodo'),
    path('edittodo/', views.edittodo, name='todos-edittodo'),
]