from django.shortcuts import render, HttpResponse

# Create your views here.
menu = """
<a href="/">Home</a>
<a href="/formulario">Registrar</a>
<a href="/contacto">Contáctanos</a>

"""
def principal(request):
    return render(request, "inicio/principal.html")

def detalle_recorrido(request):
    return render(request, "inicio/detalle_recorrido.html")

def ejemplo(request):
   return render(request,"inicio/ejemplo.html")

def preinscripcion(request):
    return render(request, "inicio/preinscripcion.html")

def exitoso(request):
    return render(request, "inicio/exitoso.html")