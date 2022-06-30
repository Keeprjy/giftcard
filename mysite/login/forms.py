from django import forms


class UserForm(forms.Form):
    username = forms.EmailField(label="username")
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.EmailField(label="username")
    password1 = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput)
    password2 = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput)
    email = forms.EmailField(label="email", widget=forms.EmailInput)