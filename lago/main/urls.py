from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("signout", views.signout, name="signout"),
    path("home", views.home, name="home"),
    path("home/insert", views.insertlab, name="insertlab"),
]
