from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from servicios.models import Servicio

# Create your tests here.
class AbmServicioTest(TestCase):
    def setUp(self):
        print("***************************** Comienzo del caso de prueba SERVICIOS *****************************")
        self.user = User.objects.create_user(username="autoTest", password='A1234567')
        self.client = Client()
        self.client.login(username="autoTest", password='A1234567')
        self.servicio = Servicio.objects.create(
            ser_nombre = "Esmaltado semipermanente",
            ser_descripcion = "Esmlatado unia por unia",
            ser_duracion = "60"
        )
        print(f"***************************** Servicio generado -> {self.servicio.get_nombre()} *****************************")
        self.url = reverse("BorrarServicio",args=[self.servicio.id])
    
    def test_eliminar_servicio(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"servicios/borrar.html")
        self.client.post(self.url)
        self.assertQuerySetEqual(Servicio.objects.all(),[])
        print("***************************** Fin del caso de prueba SERVICIOS *****************************\n\n")
