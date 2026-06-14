from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

# def todolist(request):
#     # return HttpResponse("<h1>Hello Shubham</h1>")
#     # dic={
#     #     "shubham":"hi"
#     # }
#     # return JsonResponse(dic)
    
#     return render(request,"main.html",{})


@login_required
def todolist(request):
    if(request.method=="POST"):
        from_data=TaskForm(request.POST or None)
        if from_data.is_valid():
            instance=from_data.save(commit=False)
            instance.owner=request.user
            instance.save()
            messages.success(request, "Task added.")
            return redirect("todolist")
        messages.error(request, "Something went wrong")
        
    task_list = Task.objects.filter(owner=request.user).order_by("id")
    paginator = Paginator(task_list, 5)   # 5 tasks per page
    page_number = request.GET.get("page")
    tasks = paginator.get_page(page_number)
    cont={
        'page':'Todolist',
        'tasks':tasks
    }
    return render(request,"todolist.html",cont)

@login_required
def edit_task(request,idd):
    curr_task=Task.objects.get(id=idd)
    if(request.method=="POST"):
        from_data=TaskForm(request.POST or None,instance=curr_task)
        if from_data.is_valid():
            from_data.save()
            messages.success(request, "Task edited")
            return redirect("todolist")
        messages.error(request, "Something went wrong")
    else:
        context={
            'curr_task':curr_task
        } 
        return render(request,"edit_task.html",context)
    
@login_required
def delete_task(request,idd):
    curr_task=Task.objects.get(id=idd)
    if(curr_task.owner == request.user):
        curr_task.delete()
        messages.success(request,"Task deleted")
    else: 
        messages.error(request,"can not delete others task")
    return redirect("todolist")

@login_required  
def complete_task(request,idd):
    curr_task=Task.objects.get(id=idd)
    if(curr_task.owner == request.user):
        curr_task.is_completed=True
        curr_task.save()
        messages.success(request,"Mark as Completed")
    else: 
        messages.error(request,"can not compete others task")
    return redirect("todolist")

@login_required
def pending_task(request,idd):
    curr_task=Task.objects.get(id=idd)
    if(curr_task.owner == request.user):
        curr_task.is_completed=False
        curr_task.save()
        messages.success(request,"Marked as Pending")
    else: 
        messages.error(request,"can not pending others task")
  
    return redirect("todolist")
    
    
def home(request):
    return render(request,"home.html")

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


