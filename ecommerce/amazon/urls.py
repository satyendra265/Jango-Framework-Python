"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.index,name='index'),
   path('index',views.index,name='index'),
   path('form',views.form,name='form'),
   path('about',views.about,name='about'),
   path('Addition', views.Addition, name='Addition'),
   path('Calculator',views.Calculator,name='Calculator'),
   path('Cal', views.Cal, name='Cal'),
   path('Cal1', views.Cal1, name='Cal1'),
   path('registration', views.registration, name='registraion'),
   path('Register', views.Register, name='Register'),
   path('ShowStudentData', views.ShowStudentData, name='ShowStudentData'),
   path('delete_stud', views.delete_stud, name='delete_stud'),
   path('edit_stud', views.edit_stud, name='edit_stud'),
   path('updateStud', views.updateStud, name='updateStud'),
   path('regiEmp', views.regiEmp, name='regiEmp'),
   path('uploadPhoto',views.uploadPhoto, name='uploadPhoto'),
   path('ShowEmpData',views.ShowEmpData, name='ShowEmpData'),
   path('media/photo/<str:photo_name>/', views.photo_view, name='photo_view'),
   path('edit_emp', views.edit_emp, name='edit_emp'),
   path('updateEmp', views.updateEmp, name='updateEmp'),
   path('delete_emp', views.delete_emp, name='delete_emp'),
   path('studLogin', views.studLogin, name='studLogin'),
   path('studLoginCheck', views.studLoginCheck, name='studLoginCheck'),
   path('studDashboard', views.studDashboard, name='studDashboard'),
   path('studLogout', views.studLogout, name='studLogout'),
   path('filterStud', views.filterStud, name='filterStud'),
   path('manageMenu', views.)
]
