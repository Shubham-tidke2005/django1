from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def todolist(request):
    # return HttpResponse("<h1>Hello Shubham</h1>")
    # dic={
    #     "shubham":"hiii"
    # }
    # return JsonResponse(dic)
    
    return render(request,"main.html",{})