from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from accounts.forms import UserRegisterForm, UserEditForm
from django.views.generic.edit import UpdateView
from accounts.models import Avatar
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import ListView
from django.urls import reverse_lazy

# Create your views here.
def login_requets(request):
    msg_login =""
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username = usuario, password = contrasenia)

            if user is not None:
                login(request, user)                
                return render(request, "core/index.html")
        
        msg_login = "Usuario o contrasenia incorrectos"

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form":form, "msg_login": msg_login})

def register(request):
    msg_register = ""

    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return render(request,"core/index.html")
        
        msg_register = "Error en los datos ingresados"

    else:
        form = UserRegisterForm()
        
    return render(request,"accounts/registro.html",{"form":form, "msg_register":msg_register})

@login_required
def editar_usuario(request):
    usuario = request.user

    if request.method == 'POST':
        mi_form = UserEditForm(request.POST, request.FILES,instance=usuario)
        if mi_form.is_valid():
            if mi_form.cleaned_data.get("imagen"):
                avatar = Avatar(user=usuario, imagen = mi_form.cleaned_data.get("imagen"))                
                avatar.save()
            mi_form.save()
            return render(request, "core/index.html")
    else:
        mi_form = UserEditForm(instance = usuario)
    
    return render(request,"accounts/modificar.html",{"form":mi_form}) 

class CambiarPassView(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/password.html"
    success_url = reverse_lazy("Modificar")

class CuentasListView(LoginRequiredMixin,ListView):
    model = User
    context_object_name = "usuarios"
    template_name = "accounts/listado.html"

class RolUpdateView(LoginRequiredMixin,UpdateView):
    model = User
    template_name = "accounts/rol.html"
    success_url = reverse_lazy('ListadoCuentas')
    fields = ['groups']


