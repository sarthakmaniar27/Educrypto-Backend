from collections import defaultdict
from email import header
import os
from django.http import FileResponse, JsonResponse
from django.shortcuts import render
from .models import Faculty, Student, ShareKey, StudentGrade
from rest_framework.views import APIView
import random
import math
import csv
from django.http import HttpResponse
import ipfshttpclient
import requests


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
            return JsonResponse({'res':text,'name':faculty.faculty_name})

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

class gradeTest(APIView):
    def get(self,request):
        if request.method == 'GET':

            student_uid = request.GET.get('student_uid')
            testName = request.GET.get('testName')
            branch = request.GET.get('branch')
            subject = request.GET.get('subject')
            marks = request.GET.get('marks')

            student_grade= StudentGrade.objects.create(student_uid=student_uid,testName=testName,branch=branch,subject=subject,marks=marks)

            return JsonResponse({'res':'Succesfully Added Grade to database'}) 

class checkIfGraded(APIView):
    def get(self,request):
        if request.method == 'GET':

            student_uid = request.GET.get('student_uid')
            testName = request.GET.get('testName')
            branch = request.GET.get('branch')
            subject = request.GET.get('subject')
            print()
            try:
                student_grade= StudentGrade.objects.get(student_uid=student_uid,testName=testName,branch=branch,subject=subject)
            except:
                return JsonResponse({'res':'False'}) 
            if student_grade:
                    return JsonResponse({'res':'True','marks':student_grade.marks}) 

class createTestReport(APIView):
    def get(self,request):

        if request.method == 'GET':
            testName = request.GET.get('testName')
            branch = request.GET.get('branch')
            subject = request.GET.get('subject')
            response=[]
            try:
                student_grade= StudentGrade.objects.filter(testName=testName,branch=branch,subject=subject)
            except:
                return JsonResponse({'res':'False'}) 
            if student_grade:
                    file_path='D:/Users/tanvi/Eighth Semester/Major Project/Educrypto Frontend/csv_files/report.csv'
                    file =  open(file_path, 'w',encoding='UTF8', newline='')
                   
                    writer = csv.writer(file)
                    header=['Student UID','Test Name','Branch','Subject','Marks']
                    writer.writerow(header)
                    for record in student_grade.iterator():
                        response.append({'testName':record.testName,'branch':record.branch,'subject':record.subject,'marks':record.marks})
                        writer.writerow([record.student_uid,record.testName,record.branch,record.subject,record.marks])
                    return JsonResponse({'res':response}) 

class createSubjectReport(APIView):
    def get(self,request):

        if request.method == 'GET':
            branch = request.GET.get('branch')
            subject = request.GET.get('subject')
            response=[]
            try:
                student_grade= StudentGrade.objects.filter(branch=branch,subject=subject)
            except:
                return JsonResponse({'res':'False'}) 
            if student_grade:
                    file_path='D:/Users/tanvi/Eighth Semester/Major Project/Educrypto Frontend/csv_files/subject_report.csv'
                    file =  open(file_path, 'w',encoding='UTF8', newline='')
                   
                    writer = csv.writer(file)
                    header=['Student UID','ISE1 Marks','ISE2 Marks','MSE Marks','ESE Marks','Total']
                    writer.writerow(header)
                    ipfs_file="Student UID, ISE1 Marks, ISE2 Marks, MSE Marks , ESE Marks , Total \n"
                    ISE1={}
                    ISE2={}
                    MSE={}
                    ESE={}
                    student_list=[]
              

                    for record in student_grade.iterator():
                        if(record.student_uid not in student_list):
                            student_list.append(record.student_uid)
                        if(record.testName=="ISE 1"):
                            ISE1[record.student_uid]=record.marks
                        if(record.testName=="ISE 2"):
                            ISE2[record.student_uid]=record.marks
                        if(record.testName=="MSE"): 
                            MSE[record.student_uid]=record.marks
                        if(record.testName=="ESE"):
                            ESE[record.student_uid]=record.marks

                        response.append({'branch':record.branch,'subject':record.subject,'marks':record.marks})
                        # writer.writerow([record.student_uid,record.branch,record.subject,record.marks])
                    # print(ISE1)
                    # print(ISE2)
                    # print(MSE)
                    # print(ESE)
                    print(student_list)
                    student_list.sort()
                    for student in student_list:
                        total=ISE1[student]+ISE2[student]+MSE[student]+ESE[student]
                        writer.writerow([student,ISE1[student],ISE2[student],MSE[student],ESE[student],total])
                        ipfs_file+=student+","+str(ISE1[student])+","+str(ISE2[student])+","+str(MSE[student])+","+str(ESE[student])+","+str(total)+"\n"
                        # ipfs_file+=student,str(ISE1[student])+","+str(ISE2[student])+","+str(MSE[student])+","+str(ESE[student])+","+str(total)
                    files = {"file1": ipfs_file}
                    res= requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
                    print(ipfs_file)
                    p = res.json()
                    hash = p['Hash']
                    print(hash)
                    return JsonResponse({'res':hash}) 


class createClassReport(APIView):
    def get(self,request):

        if request.method == 'GET':
            branch = request.GET.get('branch')
            response=[]
            try:
                student_grade= StudentGrade.objects.filter(branch=branch)
            except:
                return JsonResponse({'res':'False'}) 
            if student_grade:
                    file_path='D:/Users/tanvi/Eighth Semester/Major Project/Educrypto Frontend/csv_files/class_report.csv'
                    file =  open(file_path, 'w',encoding='UTF8', newline='')

                   
                    writer = csv.writer(file)
                    header=['Student UID','OS ISE1 Marks','OS ISE2 Marks','OS MSE Marks','OS ESE Marks','OS Total']
                    writer.writerow(header)
                    ipfs_file="Student UID,"
                    student_marks=defaultdict(list)

                    student_list=[]
                    subject_list=student_grade.values_list('subject', flat=True).distinct()
                    subject_list_count=subject_list.count()
                    
                    for record in student_grade.iterator():
                        if(record.student_uid not in student_list):
                            student_list.append(record.student_uid)
                        student_marks[record.student_uid].append(record.marks)
                        response.append({'branch':record.branch,'subject':record.subject,'marks':record.marks})
                            # writer.writerow([record.student_uid,record.branch,record.subject,record.marks])

                    for subject in subject_list.iterator():
                        ipfs_file+=str(subject+" ISE 1,")
                        ipfs_file+=str(subject+" ISE 2,")
                        ipfs_file+=str(subject+" MSE,")
                        ipfs_file+=str(subject+" ESE,")
                        ipfs_file+=str(subject+" Total,")
                    ipfs_file=ipfs_file[:-1]
                    ipfs_file+="\n"
                    print(student_list)
                    print(ipfs_file)
                    student_list.sort()
                    print(student_marks)
                    
                    for student in student_list:
                        ipfs_file+=student+","
                        c=0
                        total=0
                        for marks in student_marks[student]:
                            writer.writerow([])
                            ipfs_file+=str(marks)+","
                            if(c!=3):
                                total=total+int(marks)
                                print("Added to total",total)
                                c+=1
                            else:
                                total=total+int(marks)
                                ipfs_file+=str(total)+","
                                total=0
                                c=0
                        ipfs_file=ipfs_file[:-1]
                        ipfs_file+="\n"
                    print(ipfs_file)
                    files = {"file1": ipfs_file}
                    res= requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
                    p = res.json()
                    print(p)
                    hash = p['Hash']
                    print(hash)
            return JsonResponse({'res':hash})  