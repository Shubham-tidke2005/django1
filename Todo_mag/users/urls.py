from django.urls import path,include
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/",views.register,name="register"),
    path('todolist/',include("todolist.urls")),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name="login"),
    path("logout/",views.user_logout,name="logout"),
]