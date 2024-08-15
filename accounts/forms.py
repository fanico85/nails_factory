from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20, label="Usuario")
    first_name = forms.CharField(label='Nombre', max_length=50)
    last_name = forms.CharField(label='Apellido', max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name" , "email", "password1", "password2"]
        help_text = {k: "" for k in fields}

class UserEditForm(UserChangeForm):
    password = None
    username = forms.CharField(max_length=20, label="Usuario: ")
    first_name = forms.CharField(label='Nombre', max_length=50)
    last_name = forms.CharField(label='Apellido', max_length=50)
    email = forms.EmailField()
    imagen = forms.ImageField(label="Avatar",required=False)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name" , "email", "imagen"]
        help_text = {k: "" for k in fields}