from django.urls import path
from .views import user_register, user_login

urlpatterns = [
    path("login/", user_login, name="login"),
    path("register/", user_register, name="register"),
]
