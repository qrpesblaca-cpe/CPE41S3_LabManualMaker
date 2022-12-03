from django.contrib import admin
from .models import labmanual, course_code_db, course_title_db

# Register your models here.

admin.site.register(labmanual)
admin.site.register(course_code_db)
admin.site.register(course_title_db)