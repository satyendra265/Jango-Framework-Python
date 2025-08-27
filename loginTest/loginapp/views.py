from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import logout,login,authenticate
from .form import signup
from django.conf import settings
import os
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')

def userReg(request):
    if request.method=="POST":
        # fm=UserCreationForm(request.POST)
        fm=signup(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"User Has Been Registered Successfully")
            return redirect('/index')
        else:
            messages.warning(request,"User Registration Failed")
            return redirect('/userReg')
    else:
        # fm = UserCreationForm()
        fm = signup()
    return render(request,'registration.html',{'form':fm})

def authentication(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                request.session['username'] = uname
                messages.success(request, "Logged In Successfully")
                return redirect('/userDashboard')
            else:
                messages.warning(request, "Login Failed")
                return redirect('/authentication')
        else:
            messages.warning(request, "Login Failed")
            return redirect('/authentication')
    else:
        fm = AuthenticationForm()
        return render(request, 'userLogin.html', {'form': fm})

def userDashboard(request):
    if request.user.is_authenticated :
        return render(request,'UserDashboard.html',{'name':request.user})
    else :
        return redirect('/authentication')

def userLogout(request):
    del request.session['username']
    if request.session.get('username') is not None:
        messages.warning(request,"Unable to Logout")
        return redirect("/userDashboard")
    else :
        logout(request)
        messages.success(request, "Logged out Successfully")
        return redirect('/authentication')