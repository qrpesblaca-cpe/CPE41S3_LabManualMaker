from django import forms
from .models import labmanual, course_code_db, course_title_db
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your forms here.
# Form for user registration
# ---------------------------
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	

	class Meta:
		model = User
		fields = (
			"username",
			"first_name",
			"last_name", 
			"email", 
			"password1", 
			"password2"
		)
		help_texts = { 
			'username': None, 
		}
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['password1'].help_text = '<p style="color:white">Must be 6 characters and above.</p>'
		self.fields['password2'].help_text = None

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

# Form for lab manual
# creation
# ---------------------------
class LabManualForm(forms.ModelForm):
	course_code = forms.ModelChoiceField(label='Course Code', queryset=course_code_db.objects.all())
	course_title = forms.ModelChoiceField(label='Course Title', queryset=course_title_db.objects.all())
	supplementary = forms.CharField(required=False)
	questions = forms.CharField(required=False)
	class Meta:
		model = labmanual
		widgets = {
          'objective': forms.Textarea(attrs={'rows':3, 'cols':3, 'placeholder':'Laboratory Objectives'}),
		  'ilos': forms.Textarea(attrs={'rows':3, 'cols':3, 'placeholder':'Intended Learning Outcome(s)'}),
		  'res': forms.Textarea(attrs={'rows':3, 'cols':3, 'placeholder':'Laboratory Resources'}),
		  'discussion': forms.Textarea(attrs={'rows':5, 'cols':5, 'placeholder':'Laboratory Discussion'}),
        }
		
		fields = (
			'id',
			'act_no',
			'lab_title',
			'course_code',
			'course_title',
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
		self.fields['course_title'].label = "Course Title:"
		self.fields['objective'].label = "Objectives:"
		self.fields['ilos'].label = "Intended Learning Outcome(s):"
		self.fields['discussion'].label = "Discussion:"
		self.fields['res'].label = "Resources:"
		self.fields['procedures'].label = "Procedures:"
		self.fields['questions'].label = "Questions:"
		self.fields['supplementary'].label = "Supplementary Activity:"

# Form for adding course code
# ---------------------------
class CourseCodeForm(forms.ModelForm):
	class Meta:
		model = course_code_db
		fields = (
            'id',
            'code',
        )
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['code'].label = "Course Code"

# Form for course title
# ---------------------------
class CourseTitleForm(forms.ModelForm):
	class Meta:
		model = course_title_db
		fields = (
            'id',
            'title',
        )
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['title'].label = "Course Title"