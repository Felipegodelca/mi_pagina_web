from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import activate, gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from .models import Articulo
from .forms import ArticuloForm
import requests

class CustomLoginView(LoginView):
    """
    Vista personalizada para manejar el inicio de sesión.
    """
    template_name = 'registration/login.html'  # Cambia este nombre al de tu plantilla
    redirect_authenticated_user = True  # Redirige usuarios autenticados
    next_page = '/'  # Redirige a la página de inicio tras el inicio de sesión

def cambiar_idioma(request, idioma):
    """
    Cambia el idioma de la sesión actual y redirige a la página de inicio.
    """
    activate(idioma)
    request.session['django_language'] = idioma
    messages.success(request, _("Idioma cambiado exitosamente"))
    return redirect('inicio')

def obtener_tipo_cambio():
    """
    Obtiene los tipos de cambio actual y del día anterior, y calcula la variación.
    """
    api_key = 'def72ae572b28e49808fd386b9a0e691'
    base_url = 'https://api.forexrateapi.com/v1'
    monedas = ['MXN', 'BRL', 'CAD']
    tipos_de_cambio = []
    fecha_actual = None

    try:
        # Solicitud para el tipo de cambio actual
        url_actual = f'{base_url}/latest?api_key={api_key}&base=USD&symbols={",".join(monedas)}'
        response_actual = requests.get(url_actual)
        if response_actual.status_code == 200:
            datos_actual = response_actual.json()
            fecha_actual = datos_actual.get('date', None)
            rates_actual = datos_actual.get('rates', {})

        # Solicitud para el tipo de cambio del día anterior
        url_anterior = f'{base_url}/previous?api_key={api_key}&base=USD&symbols={",".join(monedas)}'
        response_anterior = requests.get(url_anterior)
        datos_anterior = response_anterior.json().get('rates', {}) if response_anterior.status_code == 200 else {}

        # Procesar datos
        for moneda in monedas:
            valor_actual = rates_actual.get(moneda, 0)
            valor_anterior = datos_anterior.get(moneda, valor_actual)
            variacion = round(valor_actual - valor_anterior, 4)
            tipos_de_cambio.append({
                'currency': moneda,
                'buy': round(valor_actual, 4),
                'sell': round(valor_actual * 1.02, 4),
                'variation': variacion,
            })
    except Exception as e:
        print(f"Error al obtener los tipos de cambio: {e}")
        tipos_de_cambio = [{'currency': m, 'buy': 0, 'sell': 0, 'variation': 0} for m in monedas]

    return {'tipos_de_cambio': tipos_de_cambio, 'fecha': fecha_actual}

def inicio(request):
    """
    Muestra la página de inicio con los tipos de cambio.
    """
    datos_tipos_cambio = obtener_tipo_cambio()
    tipos_de_cambio = datos_tipos_cambio['tipos_de_cambio']
    fecha = datos_tipos_cambio['fecha']
    return render(request, 'articulos/inicio.html', {'tipos_de_cambio': tipos_de_cambio, 'fecha': fecha})

def lista_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, "articulos/lista_articulos.html", {"articulos": articulos})

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Artículo creado exitosamente"))
            return redirect('lista_articulos')
        else:
            messages.error(request, _("Hubo un error al crear el artículo"))
    else:
        form = ArticuloForm()
    return render(request, 'articulos/crear_articulo.html', {'form': form})

def editar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            messages.success(request, _("Artículo editado exitosamente"))
            return redirect('lista_articulos')
        else:
            messages.error(request, _("Hubo un error al editar el artículo"))
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'articulos/editar_articulo.html', {'form': form})

def eliminar_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        messages.success(request, _("Artículo eliminado exitosamente"))
        return redirect('lista_articulos')
    return render(request, 'articulos/eliminar_articulo.html', {'articulo': articulo})

def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Cuenta creada exitosamente. ¡Ahora puedes iniciar sesión!"))
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'articulos/registro.html', {'form': form})