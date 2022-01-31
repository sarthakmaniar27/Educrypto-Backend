from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
	# def get_absolute_url(self):
	# 	return reverse('post-detail',kwargs={'pk':self.pk})
    name=models.CharField(max_length=100)
    uid=models.CharField(max_length=100)
    password=models.CharField(max_length=8,default='123456')
    branch=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    address=models.TextField()
    dob=models.DateField()

    def __str__(self):
	    return self.uid

class StudentDocument(models.Model):
	# def get_absolute_url(self):
	# 	return reverse('post-detail',kwargs={'pk':self.pk})
    student_uid=models.OneToOneField(Student,on_delete=models.CASCADE)
    tenth_marksheet=models.CharField(max_length=200, blank=True)
    twelfth_marksheet=models.CharField(max_length=200, blank=True)
    leaving_certificate=models.CharField(max_length=200, blank=True)
    cet_scorecard=models.CharField(max_length=200, blank=True)
    aadhar_card=models.CharField(max_length=200, blank=True)

    def __str__(self):
	    return self.student_uid.uid