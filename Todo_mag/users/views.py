from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"register sucessful")
            return redirect("/todolist/")
    else:
        form = RegisterForm()

    context = {
        "register_form": form
    }

    return render(request, "register.html", context)



def user_logout(request):
    logout(request)
    return redirect("login")