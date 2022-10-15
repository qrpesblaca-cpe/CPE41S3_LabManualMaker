from urllib import request
from django.shortcuts import  render, redirect
from .models import labmanual
from .forms import RegistrationForm, LabManualForm
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
@login_required(login_url='/')
def home(response):
    return render(response, "main/home.html", {})

@login_required(login_url='/')
def insertlab(request):
	if request.method == "POST":
		labmanual_form = LabManualForm(request.POST, request.FILES)
		if labmanual_form.is_valid():
			labmanual_form.save()
			messages.success(request, ('Your manual was successfully added!'))
		else:
			messages.error(request, 'Error saving form')

		return redirect("insertlab")
	labmanual_form = LabManualForm()
	manual = labmanual.objects.all()
	return render(request=request, template_name="main/insertlab.html", context={'labmanual_form':labmanual_form, 'manual':manual})


def signup(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Signup successful." )
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistrationForm()
	return render (request=request, template_name="main/signup.html", context={"register_form":form})

def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/signin.html", context={"login_form":form})

def signout(request):
	logout(request)
	return redirect("/")