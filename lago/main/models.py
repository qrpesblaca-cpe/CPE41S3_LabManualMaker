from dataclasses import Field
from typing import Optional
from django.db import models
from ckeditor.fields import RichTextField


# Laboratory manual model
# ---------------------------
class labmanual(models.Model):
    id = models.AutoField(primary_key=True)
    act_no = models.CharField(max_length=20, default="")
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
