from django.contrib import admin

from .models import Professor, Student, Score

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Score)
