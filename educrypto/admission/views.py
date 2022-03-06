from django.http import JsonResponse
from django.shortcuts import render
from .models import Faculty, Student, ShareKey
from rest_framework.views import APIView
import random
import math
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

class facultylogin(APIView):
    def get(self,request):
        if request.method == 'GET':
            fid = request.GET.get('fid')
            password=request.GET.get('password')
            text="Invalid"
            try:
                faculty=Faculty.objects.get(faculty_fid=fid)
            except:
                return JsonResponse({'res':text})
            if(faculty and faculty.password==password):
                text="Valid"
            return JsonResponse({'res':text})

class share(APIView):
    def get(self,request):
        if request.method == 'GET':

            studentUID = request.GET.get('studentUID')
            third_party_name=request.GET.get('third_party_name')
            docType=request.GET.get('docType')
            digits = [i for i in range(0, 10)]
            random_str = ""
            for i in range(6):
                index = math.floor(random.random() * 10)
                random_str += str(digits[index])
            
            print(studentUID,random_str,third_party_name,docType)
            # add share key in database 
            sharekey= ShareKey.objects.create(student_uid=studentUID,atp=random_str,third_party=third_party_name,doc_type=docType)

            return JsonResponse({'atp':random_str})    

class validatethirdparty(APIView):
    def get(self,request):
        if request.method == 'GET':
            third_party_name = request.GET.get('third_party_name')
            atp=request.GET.get('atp')
            print(third_party_name,atp)
            text="Invalid"
            try:
                print(third_party_name)
                third_party = ShareKey.objects.get(third_party=third_party_name)
                print(third_party)
            except:
                print(text)
                return JsonResponse({'res':text})
            if(third_party and third_party.atp==atp):
                text="Valid"
                print(text)
            return JsonResponse({'res':text,'student_uid':third_party.student_uid,'doc_type':third_party.doc_type})



class getStudentBranch(APIView):
    def get(self,request):
        if request.method == 'GET':
            branch=''
            uid = request.GET.get('uid')
            try:
                student=Student.objects.get(uid=uid)
            except:
                return JsonResponse({'branch':'None'})
            if(student):
                branch=student.branch
            return JsonResponse({'branch':branch})