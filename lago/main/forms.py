from django import forms
from .models import labmanual
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your forms here.

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

		