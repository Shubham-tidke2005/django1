from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

# def todolist(request):
#     # return HttpResponse("<h1>Hello Shubham</h1>")
#     # dic={
#     #     "shubham":"hiii"
#     # }
#     # return JsonResponse(dic)
    
#     return render(request,"main.html",{})

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

def todolist(request):
    cont={
        'page':'Todolist'
    }
    return render(request,"todolist.html",cont)

