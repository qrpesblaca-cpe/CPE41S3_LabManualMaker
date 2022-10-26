from django.urls import path
from . import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("signout", views.signout, name="signout"),
    path("home", views.home, name="home"),
    path("home/about", views.about, name="about"),
    path("home/insert", views.insertlab, name="insertlab"),
    path("home/view", views.viewlab, name="view"),
    path("home/view/preview", views.preview, name="preview"),
]
