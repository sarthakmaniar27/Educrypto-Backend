from django.contrib import admin
from .models import Faculty, Student, ShareKey, FacultySubjectMap,StudentGrade
# Register your models here.

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(ShareKey)
admin.site.register(FacultySubjectMap)
admin.site.register(StudentGrade)