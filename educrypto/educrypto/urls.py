"""educrypto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admission.views import login,share,validatethirdparty, facultylogin,getStudentBranch,gradeTest,checkIfGraded,createTestReport,createSubjectReport,createClassReport
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login.as_view(),name='login'),
    path('share/', share.as_view(),name='share'),
    path('validatethirdparty/', validatethirdparty.as_view(),name='validatethirdparty'),
    path('facultylogin/', facultylogin.as_view(),name='facultylogin'),
    path('getstudentbranch/', getStudentBranch.as_view(),name='getstudentbranch'),
    path('gradetest/', gradeTest.as_view(),name='gradetest'),
    path('checkifgraded/', checkIfGraded.as_view(),name='checkifgraded'),
    path('createtestreport/', createTestReport.as_view(),name='createtestreport'),
    path('createsubjectreport/', createSubjectReport.as_view(),name='createsubjectreport'),
    path('createclassreport/', createClassReport.as_view(),name='createclassreport'),



    
]
