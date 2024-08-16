from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from insumos.models import Marca, Insumo

# Create your tests here.
class AbmInsumosTest(TestCase):
    def setUp(self):
        print("***************************** Comienzo del caso de prueba INSUMOS *****************************")
        self.user = User.objects.create_user(username="autoTest", password='A1234567')
        self.client = Client()
        self.client.login(username="autoTest", password='A1234567')
        self.marca = Marca.objects.create(
            mar_nombre = "IBD",
            mar_descripcion = "Marca reconocida de Esmaltes",
            mar_fecha_alta = "2024-05-12"
        )
        print(f"***************************** Marca generada -> {self.marca.get_nombre()} *****************************")
        self.insumo = Insumo.objects.create(
            ins_nombre = "esmalte",
            ins_marca = self.marca,
            ins_descripcion = "2024-05-12",
            ins_stock_actual = "1",
            ins_stock_minimo = "1", 
            ins_stock_maximo = "2", 
            ins_unidad_medida = "lt",
            ins_contenido = "10"
        )
        print(f"***************************** Insumo generado -> {self.insumo.get_nombre()} *****************************")
        self.url = reverse("BorrarInsumo",args=[self.insumo.pk])   

    def test_eliminar_insumo(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"insumos/borrar.html")
        self.client.post(self.url)
        self.assertQuerySetEqual(Insumo.objects.all(),[])
        print("***************************** Fin del caso de prueba INSUMOS *****************************\n\n")

