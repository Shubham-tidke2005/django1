
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="homepage"),
    path('about/', views.about,name="aboutpage"),
    path('contact/', views.contact,name="contactpage"),
    path('todolist/', views.todolist,name="todolist"),
    path('todolist/delete_task/<idd>', views.delete_task,name="delete_task"),
    path('todolist/complete_task/<idd>', views.complete_task,name="complete_task"),
    path('todolist/pending_task/<idd>', views.pending_task,name="pending_task"),
    path('todolist/edit_task/<idd>', views.edit_task,name="edit_task"),
    path('home/', views.home,name="homepage")
    
]