from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
# Create your views here.

# def todolist(request):
#     # return HttpResponse("<h1>Hello Shubham</h1>")
#     # dic={
#     #     "shubham":"hiii"
#     # }
#     # return JsonResponse(dic)
    
#     return render(request,"main.html",{})



def todolist(request):
    if(request.method=="POST"):
        from_data=TaskForm(request.POST or None)
        if from_data.is_valid():
            from_data.save()
            messages.success(request, "Task added.")
            return redirect("todolistpage")
        messages.error(request, "Something went wrong")
        
    all_task=Task.objects.all()
    cont={
        'page':'Todolist',
        'tasks':all_task
    }
    return render(request,"todolist.html",cont)


def delete_task(request,idd):
    curr_task=Task.objects.get(id=idd)
    curr_task.delete()
    messages.success(request,"Task deleted")
    return redirect("todolistpage")
    
def home(request):
    cont={
        'page':'Home'
    }
    return render(request,"home.html",cont)

def about(request):
    cont={
        'page':'About'
    }
    return render(request,"about.html",cont)

def contact(request):
    cont={
        'page':'Contact'
    }
    return render(request,"contact.html",cont)


