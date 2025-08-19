from django.shortcuts import render, redirect
from .models import Recorrido, Inscripcion, Ruta
from django.shortcuts import render, get_object_or_404
from .forms import InscripcionForm
from django.http import HttpResponse
import json



def principal(request):
    proximos = Recorrido.objects.filter(recorrido_realizado=False)[:3]  # Solo 3 próximos
    realizados = Recorrido.objects.filter(recorrido_realizado=True)[:3]  # Solo 3 realizados
    return render(request, 'recorridos/principal.html', {
        'proximos': proximos,        'realizados': realizados,
    })

def detalle_recorrido(request, recorrido_id):
    recorrido = get_object_or_404(Recorrido, id=recorrido_id)
    puntos_recorrido = recorrido.puntos.all()
    puntos_json = json.dumps([[p.latitud, p.longitud] for p in puntos_recorrido])

    # Inscripciones relacionadas a este recorrido
    inscripciones = Inscripcion.objects.filter(recorrido=recorrido)

    return render(request, 'recorridos/detalle.html', {
        'recorrido': recorrido,
        'puntos_json': puntos_json,
        'inscripciones': inscripciones
    })
def preinscripcion(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exitoso')  
    else:
        form = InscripcionForm()
    return render(request, "recorridos/preinscripcion.html", {'form': form})

def exitoso(request):
    return render(request, "recorridos/exitoso.html") 

def MapaRutas(request):
    return render(request, "recorridos/MapaRutas.html") 


def nosotros(request):
    return render(request, "recorridos/nosotros.html") 



def inscribirme(request, recorrido_id):
    recorrido = get_object_or_404(Recorrido, id=recorrido_id)

    # Si el usuario está autenticado, prellenamos los datos
    if request.user.is_authenticated:
        initial_data = {
            'nombre': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        }
        form = InscripcionForm(request.POST or None, initial=initial_data)
    else:
        form = InscripcionForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            inscripcion = form.save(commit=False)
            inscripcion.recorrido = recorrido  # Asignar recorrido
            if request.user.is_authenticated:
                inscripcion.usuario = request.user  # Asignar usuario
            inscripcion.save()
            return redirect('detalle_recorrido', recorrido_id=recorrido.id)

    return render(request, 'recorridos/inscribirme.html', {
        'recorrido': recorrido,
        'form': form
    })

def realizados (request, id):
    recorrido = get_object_or_404(Recorrido, id=id)
    return render(request, 'recorridos/realizados.html', {'recorrido': recorrido})


def mapa(request):
    return render(request, 'mapa.html')

def guardar_ruta(request):
    if request.method == "POST":
        start_lat = request.POST.get("start_lat")
        start_lng = request.POST.get("start_lng")
        end_lat = request.POST.get("end_lat")
        end_lng = request.POST.get("end_lng")

        # Guardar en base de datos
        Ruta.objects.create(
            start_lat=start_lat,
            start_lng=start_lng,
            end_lat=end_lat,
            end_lng=end_lng
        )

        return HttpResponse("Ruta guardada con éxito")

def proximos(request):
    recorridos_proximos = Recorrido.objects.filter(recorrido_realizado=False)
    return render(request, 'recorridos/proximos.html', {'recorridos': recorridos_proximos})

def realizados(request):
    recorridos_realizados = Recorrido.objects.filter(recorrido_realizado=True)
    return render(request, 'recorridos/realizados.html', {'recorridos': recorridos_realizados})