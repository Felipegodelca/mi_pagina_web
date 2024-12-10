import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import activate, gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import JsonResponse
from .models import Articulo
from .forms import ArticuloForm

class CustomLoginView(LoginView):
    """
    Vista personalizada para manejar el inicio de sesión.
    """
    template_name = 'articulos/login.html'  # Plantilla para iniciar sesión
    redirect_authenticated_user = True
    next_page = '/'  # Redirige a la página de inicio tras el inicio de sesión


# Configurar LogoutView con plantilla personalizada
logout_view = LogoutView.as_view(template_name='articulos/logout.html')


def debug_headers(request):
    """
    Devuelve los encabezados HTTP enviados por el cliente para depuración.
    """
    headers = {
        key: value
        for key, value in request.META.items()
        if key.startswith('HTTP_') or key in ['REMOTE_ADDR', 'SERVER_NAME']
    }
    return JsonResponse(headers)


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
    api_key = 'ec6bcbf2e0f378756d693ba1'  # Tu clave de API
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    monedas = ['MXN', 'BRL', 'CAD']
    tipos_de_cambio = []
    fecha_actual = None

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data.get('result') == 'success':
            fecha_actual = data.get('time_last_update_utc', 'No disponible')
            rates_actual = data.get('conversion_rates', {})

            for moneda in monedas:
                valor_actual = rates_actual.get(moneda, 0)
                variacion = round(valor_actual - 1, 4)
                tipos_de_cambio.append({
                    'currency': moneda,
                    'buy': round(valor_actual, 4),
                    'sell': round(valor_actual * 1.02, 4),  # Agregamos un 2% para "venta"
                    'variation': variacion,
                })
        else:
            raise ValueError("Error al obtener los datos de la API")

    except Exception as e:
        print(f"Error al obtener los tipos de cambio: {e}")
        tipos_de_cambio = [{'currency': m, 'buy': 0, 'sell': 0, 'variation': 0} for m in monedas]

    return {'tipos_de_cambio': tipos_de_cambio, 'fecha': fecha_actual}


def inicio(request):
    """
    Muestra la página de inicio con los tipos de cambio.
    """
    datos_tipos_cambio = obtener_tipo_cambio()
    return render(request, 'articulos/inicio.html', datos_tipos_cambio)


def lista_articulos(request):
    """
    Muestra una lista de artículos.
    """
    articulos = Articulo.objects.all()
    return render(request, "articulos/lista_articulos.html", {"articulos": articulos})


def crear_articulo(request):
    """
    Permite crear un artículo.
    """
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Artículo creado exitosamente"))
            return redirect('articulos:lista_articulos')
    else:
        form = ArticuloForm()
    return render(request, 'articulos/crear_articulo.html', {'form': form})


def editar_articulo(request, pk):
    """
    Permite editar un artículo existente.
    """
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            messages.success(request, _("Artículo editado exitosamente"))
            return redirect('articulos:lista_articulos')
    else:
        form = ArticuloForm(instance=articulo)
    return render(request, 'articulos/editar_articulo.html', {'form': form})


def eliminar_articulo(request, pk):
    """
    Permite eliminar un artículo existente.
    """
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == 'POST':
        articulo.delete()
        messages.success(request, _("Artículo eliminado exitosamente"))
        return redirect('articulos:lista_articulos')
    return render(request, 'articulos/eliminar_articulo.html', {'articulo': articulo})


def detalle_articulo(request, pk):
    """
    Muestra los detalles de un artículo.
    """
    articulo = get_object_or_404(Articulo, pk=pk)
    return render(request, 'articulos/detalle_articulo.html', {'articulo': articulo})


def registro(request):
    """
    Permite registrar un nuevo usuario.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Cuenta creada exitosamente. ¡Ahora puedes iniciar sesión!"))
            return redirect('articulos:login')
    else:
        form = UserCreationForm()
    return render(request, 'articulos/registro.html', {'form': form})


def tipos_cambio(request):
    """
    Muestra una página con información sobre los tipos de cambio.
    """
    datos_tipos_cambio = obtener_tipo_cambio()
    return render(request, 'articulos/tipos_cambio.html', datos_tipos_cambio)