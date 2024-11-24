from django.test import TestCase
from django.urls import reverse
from .models import Articulo
from django.utils.translation import activate


class ArticuloTests(TestCase):
    def setUp(self):
        # Activa el idioma predeterminado para las pruebas
        activate('es')
        # Crea un artículo de prueba
        self.articulo = Articulo.objects.create(
            titulo="Artículo de Prueba",
            contenido="Contenido de prueba para el artículo.",
            tema="FIL",
            etiquetas="prueba,artículo",
        )

    def test_lista_articulos_view(self):
        response = self.client.get(reverse('lista_articulos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articulos/lista_articulos.html')
        self.assertContains(response, self.articulo.titulo)

    def test_detalle_articulo_view(self):
        response = self.client.get(reverse('detalle_articulo', args=[self.articulo.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articulos/detalle_articulo.html')
        self.assertContains(response, self.articulo.contenido)

    def test_crear_articulo_view(self):
        response = self.client.post(reverse('crear_articulo'), {
            'titulo': 'Nuevo Artículo',
            'contenido': 'Contenido del nuevo artículo.',
            'tema': 'PSI',
            'etiquetas': 'nuevo,artículo',
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de crear
        nuevo_articulo = Articulo.objects.last()
        self.assertEqual(nuevo_articulo.titulo, 'Nuevo Artículo')
        self.assertEqual(nuevo_articulo.tema, 'PSI')

    def test_editar_articulo_view(self):
        response = self.client.post(reverse('editar_articulo', args=[self.articulo.id]), {
            'titulo': 'Artículo Editado',
            'contenido': 'Contenido editado del artículo.',
            'tema': 'NEG',
            'etiquetas': 'editado,prueba',
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de editar
        self.articulo.refresh_from_db()
        self.assertEqual(self.articulo.titulo, 'Artículo Editado')
        self.assertEqual(self.articulo.tema, 'NEG')

    def test_eliminar_articulo_view(self):
        response = self.client.post(reverse('eliminar_articulo', args=[self.articulo.id]))
        self.assertEqual(response.status_code, 302)  # Redirige después de eliminar
        self.assertFalse(Articulo.objects.filter(id=self.articulo.id).exists())

    def test_cambiar_idioma_view(self):
        response = self.client.get(reverse('cambiar_idioma', args=['en']))
        self.assertEqual(response.status_code, 302)  # Redirige después de cambiar idioma
        self.assertEqual(self.client.session['django_language'], 'en')

    def test_obtener_tipo_cambio(self):
        # Asegúrate de que la función devuelve datos válidos
        from articulos.views import obtener_tipo_cambio
        tipos_de_cambio = obtener_tipo_cambio()
        self.assertIsInstance(tipos_de_cambio, list)
        self.assertTrue(all('currency' in cambio for cambio in tipos_de_cambio))