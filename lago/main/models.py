from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Laboratory manual model
# ---------------------------
class labmanual(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    act_no = models.IntegerField()
    lab_title = models.CharField(max_length=50)
    course_code = models.CharField(max_length=50)
    objective = models.TextField()
    ilos = models.TextField()
    discussion = models.TextField()
    res = models.TextField()
    procedures = RichTextField(blank=True, null=True)
    questions = models.TextField()
    supplementary = models.TextField()

    def __str__(self):
        return self.lab_title
