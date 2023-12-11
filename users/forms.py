from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class": "form-control"}))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    contact = forms.CharField(max_length=10, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class": "form-control"}))