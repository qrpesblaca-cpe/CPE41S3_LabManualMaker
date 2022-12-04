from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Laboratory manual model
# ---------------------------
class labmanual(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    act_no = models.IntegerField()
    lab_title = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    course_title = models.CharField(max_length=100)
    objective = models.TextField()
    ilos = models.TextField()
    discussion = models.TextField()
    res = models.TextField()
    procedures = RichTextField(blank=True, null=True)
    questions = models.TextField()
    supplementary = models.TextField()
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.lab_title

class course_code_db(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class course_title_db(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.ForeignKey(course_code_db, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
