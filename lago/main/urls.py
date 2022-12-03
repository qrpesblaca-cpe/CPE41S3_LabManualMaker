from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import labListView,labDetailView
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path("", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("home/", views.home, name="home"),
    path("home/about/", views.about, name="about"),
    path("home/insert/", views.insertlab, name="insertlab"),
    path("home/add_course/", views.addCourse, name="addCourse"),
    path("home/profile/", views.userProfile, name="userProfle"),
    path("home/profile/change_password/", views.change_password, name="change_password"),
    path("home/view/", login_required(labListView.as_view(),login_url='/'), name="view"),
    path("home/view/<int:pk>/", login_required(labDetailView.as_view(), login_url='/'), name="preview"),
    path("home/view/<int:pk>/update/", views.update, name="update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)