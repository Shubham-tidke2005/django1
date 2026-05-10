
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="homepage"),
    path('about/', views.about,name="aboutpage"),
    path('contact/', views.contact,name="contactpage"),
    path('todolist/', views.todolist,name="todolistpage"),
    path('delete_task/<idd>', views.delete_task,name="delete_task"),
    path('home/', views.home,name="homepage")
    
]