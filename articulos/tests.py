from django.test import TestCase
from django.urls import reverse
from .models import Articulo
from django.utils.translation import activate
from django.contrib.auth.models import User


class ArticuloTests(TestCase):
    def setUp(self):
        # Activa el idioma predeterminado para las pruebas
        activate('es')
        
        # Crea un usuario de prueba para interactuar con las vistas que requieren autenticación
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Crea un artículo de prueba asociado al usuario
        self.articulo = Articulo.objects.create(
            titulo="Artículo de Prueba",
            contenido="Contenido de prueba para el artículo.",
            tema="FIL",
            etiquetas="prueba,artículo",
            autor=self.user  # Asociamos un autor al artículo
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
        # Aseguramos que el usuario esté autenticado antes de crear el artículo
        self.client.login(username='testuser', password='12345')

        response = self.client.post(reverse('crear_articulo'), {
            'titulo': 'Nuevo Artículo',
            'contenido': 'Contenido del nuevo artículo.',
            'tema': 'PSI',
            'etiquetas': 'nuevo,artículo',
            'autor': self.user.id,  # Aseguramos que el artículo esté asociado al usuario
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de crear
        nuevo_articulo = Articulo.objects.last()
        self.assertEqual(nuevo_articulo.titulo, 'Nuevo Artículo')
        self.assertEqual(nuevo_articulo.tema, 'PSI')
        self.assertEqual(nuevo_articulo.autor, self.user)  # Verificamos que el autor esté asociado correctamente

    def test_editar_articulo_view(self):
        # Aseguramos que el usuario esté autenticado antes de editar
        self.client.login(username='testuser', password='12345')

        response = self.client.post(reverse('editar_articulo', args=[self.articulo.id]), {
            'titulo': 'Artículo Editado',
            'contenido': 'Contenido editado del artículo.',
            'tema': 'NEG',
            'etiquetas': 'editado,prueba',
            'autor': self.user.id,  # Mantenemos el autor al editar
        })
        self.assertEqual(response.status_code, 302)  # Redirige después de editar
        self.articulo.refresh_from_db()
        self.assertEqual(self.articulo.titulo, 'Artículo Editado')
        self.assertEqual(self.articulo.tema, 'NEG')
        self.assertEqual(self.articulo.autor, self.user)  # Verificamos que el autor se mantenga

    def test_eliminar_articulo_view(self):
        # Aseguramos que el usuario esté autenticado antes de eliminar
        self.client.login(username='testuser', password='12345')

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

    def test_unauthorized_access_to_create_article(self):
        # Verifica que un usuario no autenticado no pueda acceder a la vista de crear artículo
        response = self.client.get(reverse('crear_articulo'))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('crear_articulo'))

    def test_unauthorized_access_to_edit_article(self):
        # Verifica que un usuario no autenticado no pueda acceder a la vista de editar artículo
        response = self.client.get(reverse('editar_articulo', args=[self.articulo.id]))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('editar_articulo', args=[self.articulo.id]))

    def test_unauthorized_access_to_delete_article(self):
        # Verifica que un usuario no autenticado no pueda acceder a la vista de eliminar artículo
        response = self.client.get(reverse('eliminar_articulo', args=[self.articulo.id]))
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('eliminar_articulo', args=[self.articulo.id]))