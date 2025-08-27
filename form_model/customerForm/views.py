from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

from .form import newcustomerform
from .models import newCustomer
# def newCustomerForm(request):
#     form=newcustomerform()
#     return render(request,'newCustomerForm.html',{'form':form})

def newCustomerForm(request):
    form=newcustomerform()
    if request.method=='POST':
        form=newcustomerform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'newCustomerForm.html',{'form':form})