from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from gastos.models import Gasto

# Create your tests here.
class AbmGastosTest(TestCase):
    def setUp(self):
        print("***************************** Comienzo del caso de prueba GASTOS *****************************")
        self.user = User.objects.create_user(username="autoTest", password='A1234567')
        self.client = Client()
        self.client.login(username="autoTest", password='A1234567')
        self.gasto = Gasto.objects.create(
             gas_nombre = "Luz",
            gas_descripcion = "mucha Luz",
            gas_monto = "10000",
            gas_fecha = "2024-05-12"
        )
        print(f"***************************** Gasto generado -> {self.gasto.get_nombre()} *****************************")
        self.url = reverse("BorrarGasto",args=[self.gasto.id])
    
    def test_eliminar_gasto(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"gastos/borrar.html")
        self.client.post(self.url)
        self.assertQuerySetEqual(Gasto.objects.all(),[])
        print("***************************** Fin del caso de prueba GASTOS *****************************\n\n")