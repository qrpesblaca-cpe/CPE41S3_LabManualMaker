from .models import labmanual
from .forms import RegistrationForm, LabManualForm
from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from docx import *
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from io import BytesIO


# Requires user to sign up 
# before accessing /home
# -----------------------------
@login_required(login_url='/')
def home(response):
    return render(response, "main/home.html", {})

# Function for inserting data 
# from forms into the labmanual 
# model
# -----------------------------
@login_required(login_url='/')
def insertlab(request):
	if request.method == "POST":
		labmanual_form = LabManualForm(request.POST, request.FILES)
		if labmanual_form.is_valid():
			labmanual_form.save()
		else:
			messages.error(request, 'Error saving form')

		return redirect("insertlab")
	labmanual_form = LabManualForm()
	manual = labmanual.objects.all()
	return render(request=request, template_name="main/insertlab.html", context={'labmanual_form':labmanual_form, 'manual':manual})

# View existing lab manuals
# -----------------------------
@login_required(login_url='/')
def viewlab(request):
    labmanual_list = labmanual.objects.all()
    return render(request, 'main/view.html',
        {'labmanual_list': labmanual_list})

# Function for creating user
# -----------------------------
def signup(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Signup successful.", extra_tags='valid')
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.", extra_tags='invalid')
	form = RegistrationForm()
	return render (request=request, template_name="main/signup.html", context={"register_form":form})

# Function for user sign in
# ---------------------------
def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				#messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.", extra_tags='invalid')
		else:
			messages.error(request,"Invalid username or password.", extra_tags='invalid')
	form = AuthenticationForm()
	return render(request=request, template_name="main/signin.html", context={"login_form":form})

# Function for user sign out
# ---------------------------
def signout(request):
	logout(request)
	return redirect("/")

# Download lab manual template
# ---------------------------
def downloadTemp(request):

    # Create document
    # -----------------------------
    document = Document()
    docx_title = "LAGO-test.docx"
    core_properties = document.core_properties

    # Insert author & comment
    # -----------------------------
    core_properties.author = 'Laboratory Manual Maker'
    core_properties.comments = 'created by Laboratory Manual Maker'

    # Create table
    # -----------------------------
    table = document.add_table(rows=26, cols=2)
    table.style = 'Table Grid'
    style = document.styles['Normal']
    font = style.font
    font.name = 'Arial Narrow'
    font.size = Pt(12)
    font.bold = True

    # Merge specific rows
    # -----------------------------
    table.cell(0,0).merge(table.cell(0,1))
    table.cell(1,0).merge(table.cell(1,1))
    x = 6
    for x in range(6,26):
        table.cell(x,0).merge(table.cell(x,1))

    p=table.columns[0].cells[0].add_paragraph('Activity No. ')
    p.paragraph_format.space_after = Pt(12)
    p.alignment=WD_PARAGRAPH_ALIGNMENT.CENTER

    # Insert labels into cells
    # -----------------------------
    table.columns[0].cells[2].text = 'Course Code: ' 
    table.columns[0].cells[3].text = 'Course Title: '
    table.columns[0].cells[4].text = 'Section: '
    table.columns[0].cells[5].text = 'Name/s: '

    table.columns[1].cells[2].text = 'Program: '
    table.columns[1].cells[3].text = 'Date Performed: '
    table.columns[1].cells[4].text = 'Date Submitted: '
    table.columns[1].cells[5].text = 'Instructor: \n\n'

    table.columns[0].cells[6].text = '1. Objective:'
    table.columns[0].cells[8].text = '2. Intended Learning Outcomes (ILOs):'
    table.columns[0].cells[10].text = '3. Discussion:'
    table.columns[0].cells[12].text = '4. Resources:'
    table.columns[0].cells[14].text = '5. Procedures:'
    table.columns[0].cells[16].text = '6. Results:'
    table.columns[0].cells[18].text = '7. Observations:'
    table.columns[0].cells[20].text = '8. Questions:'
    table.columns[0].cells[22].text = '9. Conclusions:'
    table.columns[0].cells[24].text = '10. Supplementary Activity:'


    # Prepare document for download        
    # -----------------------------
    f = BytesIO()

    document.save(f)
    length = f.tell()
    f.seek(0)
    response = HttpResponse(
        f.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = 'attachment; filename=' + docx_title
    response['Content-Length'] = length
    return response

