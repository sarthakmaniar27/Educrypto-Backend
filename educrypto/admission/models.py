from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

from datetime import date

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    uid=models.CharField(max_length=100)
    password=models.CharField(max_length=8,default='123456')
    branch=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.TextField()
    dob=models.DateField(validators=[MaxValueValidator(date.today())])


    def __str__(self):
	    return self.uid




class ShareKey(models.Model):
    student_uid=models.CharField(max_length=200, blank=True)
    atp=models.CharField(max_length=200, blank=True)
    third_party=models.CharField(max_length=200, blank=True)
    doc_type=models.CharField(max_length=200, blank=True)

    def __str__(self):
	    return self.third_party


class Faculty(models.Model):
    faculty_name=models.CharField(max_length=100)
    faculty_fid=models.CharField(max_length=200, blank=True)
    department=models.CharField(max_length=200, blank=True)
    password=models.CharField(max_length=8,default='123456')
    
    def __str__(self):
	    return self.faculty_name

class FacultySubjectMap(models.Model):
    faculty_fid=models.CharField(max_length=200, blank=True)
    branch=models.CharField(max_length=200, blank=True)
    subject=models.CharField(max_length=200, blank=True)
    
    def __str__(self):
	    return self.faculty_fid+" "+self.branch

class StudentGrade(models.Model):
        student_uid=models.CharField(max_length=200, blank=True)
        testName=models.CharField(max_length=200, blank=True)
        branch=models.CharField(max_length=200, blank=True)
        subject=models.CharField(max_length=200, blank=True)
        marks=models.IntegerField()


    
