from django.shortcuts import render,HttpResponse,redirect
from .models import student
# Create your views here.

def index(request):
    return render(request,"index.html")

def registration(request):
    return render(request,"Student_Register.html")

def Register(request):
    if request.method == "POST":
        fname=request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["pass"]
        app=student(fname=fname,lname=lname,email=email,password=password)
        app.save()
        return redirect('/ShowStudentData')

def ShowStudentData(request):
    #data=student.objects.all()
    data = student.objects.filter(id=1)  # to select specific data from table
    return render(request,"ShowStudentData.html",{'data':data})