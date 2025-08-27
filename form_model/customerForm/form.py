from django.forms import ModelForm
from .models import newCustomer

class newcustomerform(ModelForm):
    class Meta:
        model=newCustomer
        fields='__all__'  #to include all form fields
        #fields = {'firstname','lastname'} #to include specific field
