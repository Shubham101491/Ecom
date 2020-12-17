from django import forms
from django.contrib.auth.models import User
from pages.models import Register

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder':"Password"}))

    class Meta():
        model = User
        fields = ('username','email','password')

class RegisterForm(forms.ModelForm):
    contact = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Contact"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Address"}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder':"Pincode"}))

    class Meta():
        model = Register
        fields = "__all__"
        
# ('portfolio site','profile pic')