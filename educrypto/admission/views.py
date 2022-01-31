from django.http import JsonResponse
from django.shortcuts import render
from .models import Student
from rest_framework.views import APIView
# Create your views here.
class login(APIView):
    def get(self,request):
        if request.method == 'GET':
            uid = request.GET.get('uid')
            password=request.GET.get('password')
            text="Invalid"
            try:
                student=Student.objects.get(uid=uid)
            except:
                return JsonResponse({'res':text})
            if(student and student.password==password):
                text="Valid"
            return JsonResponse({'res':text})
    