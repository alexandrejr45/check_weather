from django import forms


class CreateUserForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    login = forms.CharField(max_length=30)
    password = forms.CharField(max_length=40, widget=forms.PasswordInput())
    password_check = forms.CharField(max_length=40, widget=forms.PasswordInput())
