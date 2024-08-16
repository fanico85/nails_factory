from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts import views 


#Add Django site authentication urls (for login, logout, password management)
urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('login/', views.login_requets, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name="accounts/logged_out.html"), name="Logout"),
    path('modificar/', views.editar_usuario, name="Modificar"),
    path('contrasenia/', views.CambiarPassView.as_view(), name="Contrasenia"),
    path('listadocuentas/', views.CuentasListView.as_view(),name= "ListadoCuentas"),
    path('rol/<pk>/modificar', views.RolUpdateView.as_view(),name= "ModificarRol"),      
    
]
