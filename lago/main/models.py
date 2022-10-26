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
    objective = models.CharField(max_length=200)
    ilos = models.CharField(max_length=200)
    discussion = models.CharField(max_length=500)
    res = models.CharField(max_length=100)
    procedures = RichTextField(blank=True, null=True)
    questions = models.CharField(max_length=200)
    supplementary = models.CharField(max_length=200)

    def __str__(self):
        return self.lab_title
