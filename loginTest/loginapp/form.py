from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class signup(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']