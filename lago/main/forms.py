from django import forms
from .models import labmanual
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your forms here.

courses_cpe = [
	('CPE 003','CPE 003 - Computer-Aided Drafting'),
	('CPE 006','CPE 006 - Microprocessor Systems'),
	('CPE 007','CPE 007 - Programming Logic and Design'),
	('CPE 008','CPE 008 - Computer Engineering as a Discipline'),
	('CPE 009','CPE 009 - Object Oriented Programming'),
	('CPE 010','CPE 010 - Data Structures and Algorithms'),
	('CPE 011','CPE 011 - Database Management System'),
	('CPE 012','CPE 012 - Data and Digital Communications'),
	('CPE 013','CPE 013 - Logic Circuits and Design'),
	('CPE 014','CPE 014 - Embedded Systems'),
	('CPE 015','CPE 015 - Optimization Techniques'),
	('CPE 016','CPE 016 - Introduction to HDL'),
	('CPE 017','CPE 017 - Fundamentals of Mixed Signals and Sensors'),
	('CPE 018','CPE 018 - Emerging Technologies 1 in CpE'),
	('CPE 019','CPE 019 - Emerging Technologies 2 in CpE'),
	('CPE 020','CPE 020 - Methods of Research'),
	('CPE 021','CPE 021 - Computer Architecture and Organization'),
	('CPE 022','CPE 022 - Operating Systems'),
	('CPE 023','CPE 023 - CpE Laws and Professional Practice'),
	('CPE 024','CPE 024 - Basic Occupational Health and Safety'),
	('CPE 025','CPE 025 - Software Design'),
	('CPE 026','CPE 026 - Emerging Technologies 3 in CpE'),
	('CPE 027','CPE 027 - Digital Signal Processing and Application'),
	('CPE 028','CPE 028 - Developing Applications and Automation'),
	('CPE 029','CPE 029 - CpE Design Project 1'),
	('CPE 030','CPE 030 - CpE Design Project 2'),
	('CPE 101','CPE 101 - Internet of Things'),
	('CPE 102','CPE 102 - Machine Perception'),
	('CPE 103','CPE 103 - Robotics and Automation'),
	('CPE 201A','CPE 201A - Computer System Administration and Troubleshooting'),
	('CPE 231','CPE 231 - Systems Administration Fundamentals'),
	('CPE 232','CPE 232 - Managing Enterprise Servers'),
	('CPE 243','CPE 243 - Enterprise Security'),
	('CPE 302','CPE 302 - Computer Networks 1 '),
	('CPE 304','CPE 304 - Computer Engineering Drafting and Design'),
	('CPE 311','CPE 311 - Computational Thinking with Python'),
	('CPE 312','CPE 312 - Predictive Analytics using Machine Learning'),
	('CPE 313','CPE 313 - Advanced Machine Learning and Deep Learning'),
	('CPE 401','CPE 404 - Computer Networks 2'),
	('CPE 404','CPE 404 - Computer Networks 3'),
	('CPE 500','CPE 500 - On-the-Job- Training for CpE'),
	('CPE 502','CPE 502 - Plant Visits and Seminars for CPE'),
	('RWE 001','RWE 001 - Introduction to Railway Systems and Engineering'),
	('RWE 002','RWE 002 - Railway Management, Governance, and Operations'),
	('RWE 003','RWE 003 - Advanced Topic on Railway Engineering'),
	('TECH 101','TECH 101 - Introduction to Engineering Entrepreneurship'),
	('TECH 102','TECH 102 - Technopreneurship 2 '),
	('TECH 103','TECH 103 - Technopreneurship 3'),
	('TECH 104','TECH 104 - Technopreneurship 4'),
]

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)


	class Meta:
		model = User
		fields = (
			"username", 
			"email", 
			"password1", 
			"password2"
		)
		help_texts = { 
			'username': None, 
		}
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password1'].help_text = None
		self.fields['password2'].help_text = None

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class LabManualForm(forms.ModelForm):
	course_code = forms.CharField(label='Choose', widget=forms.Select(choices=courses_cpe))
	supplementary = forms.CharField(required=False)
	questions = forms.CharField(required=False)

	class Meta:
		model = labmanual
		fields = (
			'act_no',
			'lab_title',
			'course_code',
			'objective',
			'ilos',
			'discussion',
			'res',
			'procedures',
			'questions',
			'supplementary',
		)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['act_no'].label = "Activity No.:"
		self.fields['lab_title'].label = "Laboratory Title:"
		self.fields['course_code'].label = "Course Code:"
		self.fields['objective'].label = "Objectives:"
		self.fields['ilos'].label = "Intended Learning Outcome(s):"
		self.fields['discussion'].label = "Discussion:"
		self.fields['res'].label = "Resources:"
		self.fields['procedures'].label = "Procedures:"
		self.fields['questions'].label = "Questions:"
		self.fields['supplementary'].label = "Supplementary Activity:"

		