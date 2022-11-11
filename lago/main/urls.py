from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PostListView,PostDetailView
from . import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("home/", views.home, name="home"),
    path("home/about/", views.about, name="about"),
    path("home/insert/", views.insertlab, name="insertlab"),
    path("home/settings/", views.settings, name="settings"),
    path("home/view/", login_required(PostListView.as_view(),login_url='/'), name="blog-home"),
    path("home/view/<int:pk>/", login_required(PostDetailView.as_view(), login_url='/'), name="post-detail"),
    #path("home/view/", views.viewlab, name="view"),
    #path("home/view/<int:Uid>/", views.preview, name="preview"),
]
