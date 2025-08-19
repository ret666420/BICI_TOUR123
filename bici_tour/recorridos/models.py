from django.db import models
from django.contrib.auth.models import User  


class Recorrido(models.Model):
    # 1. Información general
    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre del recorrido",
        default="Recorrido sin nombre"
    )  

    TIPO_CHOICES = [
        ("proximo", "Próximo"),
        ("realizado", "Realizado"),
    ]
    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES,
        default="proximo",
        verbose_name="Tipo de recorrido"
    )
    
    fecha = models.DateField(verbose_name="Fecha del recorrido")
    hora_inicio = models.TimeField(
        verbose_name="Hora de inicio",
        default="08:00"
    )

    # 2. Ubicación
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    estado = models.CharField(max_length=100, verbose_name="Estado / Región")
    punto_inicio = models.CharField(max_length=200, verbose_name="Punto de inicio")
    punto_final = models.CharField(max_length=200, verbose_name="Punto final")

    # 3. Detalles del recorrido
    kilometros = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Kilómetros"
    )
    tiempo_estimado = models.CharField(max_length=100, verbose_name="Tiempo estimado")  
    costo = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Costo")
    descripcion = models.TextField(verbose_name="Descripción")
    fotografia = models.ImageField(
        upload_to="recorridos/",
        blank=True,
        null=True,
        verbose_name="Fotografía / Imagen"
    )

    recorrido_realizado = models.BooleanField(
        default=False,
        verbose_name="¿Recorrido realizado?"
    )

    def __str__(self):
        return f"{self.nombre} ({self.ciudad}, {self.estado})"

    class Meta:
        verbose_name = "Recorrido"
        verbose_name_plural = "Recorridos"
        ordering = ["fecha", "hora_inicio"]


class EstadoRecorrido(models.Model):
    """Renombrado: antes era 'Recorridos' (confuso con Recorrido)."""
    estado = models.CharField(max_length=100, verbose_name="Estado del Recorrido")

    def __str__(self):
        return self.estado

    class Meta:
        verbose_name = "Estado del Recorrido"
        verbose_name_plural = "Estados de los Recorridos"


class Preinscripcion(models.Model):
    recorrido = models.ForeignKey(
        Recorrido,
        on_delete=models.CASCADE,
        verbose_name="Recorrido",
        related_name="preinscripciones"  # <- para diferenciar de inscripciones
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    ciudad = models.CharField(max_length=50, verbose_name="Ciudad")
    estado = models.CharField(max_length=50, verbose_name="Estado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    
    class Meta:
        verbose_name = "Preinscripción"
        verbose_name_plural = "Preinscripciones"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.nombre} - {self.recorrido.nombre}"


class Ruta(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Ruta")

    def __str__(self):
        return self.nombre


class PuntosMapa(models.Model):
    recorrido = models.ForeignKey(Recorrido, on_delete=models.CASCADE, related_name="puntos")
    latitud = models.FloatField()
    longitud = models.FloatField()

    def _str_(self):
        return f"{self.latitud}, {self.longitud}"



class Inscripcion(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Usuario"
    )
    recorrido = models.ForeignKey(
        Recorrido,
        on_delete=models.CASCADE,
        related_name="inscripciones",
        verbose_name="Recorrido"
    )
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    fecha_inscripcion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inscripción")

    def __str__(self):
        return f"{self.nombre} inscrito en {self.recorrido.nombre} ({self.recorrido.fecha})"

    class Meta:
        verbose_name = "Inscripción"
        verbose_name_plural = "Inscripciones"
        ordering = ["-fecha_inscripcion"]
