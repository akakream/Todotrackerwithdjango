from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='todos-home'),
    path('viewtodo/', views.viewtodo, name='todos-viewtodo'),
    path('addtodo/', views.addtodo, name='todos-addtodo'),
    path('deletetodo/<int:pk>', views.deletetodo, name='todos-deletetodo'),
    path('edittodo/<int:pk>', views.edittodo, name='todos-edittodo'),
    path('contact/', views.contact, name='todos-contact'),
]