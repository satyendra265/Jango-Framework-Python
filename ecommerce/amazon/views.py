from django.shortcuts import render,HttpResponse,redirect
from .models import student,employee
from .models import calculator
from django.conf import settings
import os
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"About_us.html")
def form(request):
    return render(request,"form_test.html")
def Addition(request):
    return render(request, "Addition.html")
def Calculator(request):
    return render(request, "Calculator.html")

def Cal1(request):
    if request.method=="POST":
        num1=eval(request.POST["num1"])
        num2=eval(request.POST["num2"])
        result=num1+num2
        data={'num1':num1,'num2':num2,'output':result}
#    return HttpResponse("Successfully posted")
        return render(request,"Addition.html",data)

def Cal(request):
    if request.method=="POST":
        num1=eval(request.POST["num1"])
        num2=eval(request.POST["num2"])
        op=request.POST["op"]
        if op=='Add':
            result=num1+num2
        elif op=='Sub':
            result=num1-num2
        elif op=='Mul':
            result=num1*num2
        elif op=='Div':
            result=num1/num2
        data={'num1':num1,'num2':num2,'op':op,'output':result}
        app=calculator(num1=num1,num2=num2,op=op,result=result)
        app.save()
#    return HttpResponse("Successfully posted")
        return render(request,"Calculator.html",data)

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
    data=student.objects.all()
    #data = student.objects.filter(id=5)  # to select specific data from table
    return render(request,"ShowStudentData.html",{'data':data})

from itertools import chain
def filterStud(request):
    data=student.objects.all()
    if request.method=="POST":
        st=request.POST['searchname']
        if st!=None:
            data1 = student.objects.filter(fname__icontains=st)
            data2 = student.objects.filter(lname__icontains=st)
            data = list(set(list(chain(data1,data2))))
            # data=[]
            # for i in data1 :
            #     if i not in data2:
            #         data+=[i]
            # data+=data2
            # data= list(data.distinct())
            # data = student.objects.filter(fname__icontains=st) or student.objects.filter(lname__icontains=st)

    return render(request,'showFilteredStudData.html',{'data':data})
def delete_stud(request):
    id=request.GET["id"]
    student.objects.filter(id=id).delete()
    return redirect("/ShowStudentData")

def edit_stud(request):
    id = request.GET["id"]
    data=student.objects.all().filter(id=id)
    return render(request,"editStud.html",{'data':data})


def updateStud(request):
    if request.method=="POST":
        id=request.POST["id"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["pass"]
        student.objects.filter(id=id).update(fname=fname,lname=lname,email=email,password=password)
    return redirect("/ShowStudentData")

def del_editStud(request):
    sb=request.POST["searchBy"]
    spid=request.POST["id"]

def regiEmp(request):
    return render(request,'upload_photo.html')

def uploadPhoto(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        photo=request.FILES['photo']
        app=employee(fname=fname,lname=lname,photo=photo)
        app.save()
        return HttpResponse("Photo And details saved successfully")
    else:
        return HttpResponse("Failed")

def ShowEmpData(request):
    data=employee.objects.all()
    return render(request,"ShowEmpData.html",{'data':data})

def photo_view(request, photo_name):
    photo_path = os.path.join(settings.MEDIA_ROOT, 'media/photo/'+photo_name)
    if os.path.exists(photo_path):
        with open(photo_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')  # Adjust content type as per your image format
    else:
        return HttpResponse(photo_path)

def delete_emp(request):
    id=request.GET["id"]
    employee.objects.filter(id=id).delete()
    return redirect("/ShowEmpData")

def edit_emp(request):
    id = request.GET["id"]
    data=employee.objects.all().filter(id=id)
    return render(request,"editEmp.html",{'data':data})


# def updateEmp(request):
#     if request.method == "POST":
#         id = request.POST["id"]
#         fname = request.POST["fname"]
#         lname = request.POST["lname"]
#         photo = request.FILES.get('photo')  # Use get method to avoid KeyError if photo is not present
#         employee.objects.filter(id=id).update(fname=fname, lname=lname, photo=photo)
#     return redirect("/ShowEmpData")


def updateEmp(request):
    if request.method == "POST":
        id = request.POST["id"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        photo = request.FILES.get('photo')  # Use get method to avoid KeyError if photo is not present
        if photo:  # Check if photo is provided in the form
            employee_obj = employee.objects.get(id=id)
            os.remove(employee_obj.photo.name)
            employee_obj.photo = photo  # Update the photo field directly with the new photo object
            employee_obj.save()
        employee.objects.filter(id=id).update(fname=fname, lname=lname)
    return redirect("/ShowEmpData")

# def updateEmp(request):
#     if request.method=="POST":
#         id=request.POST["id"]
#         fname = request.POST["fname"]
#         lname = request.POST["lname"]
#         photo = request.FILES.get['photo']
#         employee.objects.filter(id=id).update(fname=fname,lname=lname,photo=photo)
#     return redirect("/ShowEmpData")


def studLogin(request):
    return render(request,'studLogin.html')

def studLoginCheck(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["pass"]
        data=student.objects.all().filter(email=email,password=password)
        if data:
            request.session['username']=email
            messages.success(request,"login Successfully")
            return redirect("/studDashboard")
        else:
            messages.warning(request,"login Failed In-Correct Username or Password")
            return redirect("/studLogin")

def studDashboard(request):
    if request.session.get('username') is not None:
        return render(request,'studDashboard.html')
    else :
        return redirect('/studLogin')

    #return render(request,"studDashboard.html")
def studLogout(request):
    del request.session['username']
    if request.session.get('username') is not None:
        messages.warning(request,"Unable to Logout")
        return redirect("/studDashboard")
    else :
        messages.warning(request,"Logged Out Successfully")
        return redirect('/studLogin')

# def index(request):
#     return HttpResponse("JALDI WAHA SE HATO")