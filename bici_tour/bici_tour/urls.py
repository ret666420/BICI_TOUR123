from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from recorridos import views as recorridos_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', recorridos_views.principal, name='principal'),
    path('detalle_recorrido/', views.detalle_recorrido, name='detalle_recorrido'),
    path('realizados/<int:id>/', recorridos_views.realizados, name='realizados'),
    path('realizados/', recorridos_views.realizados, name='realizados'), 
    path('exitoso/', recorridos_views.exitoso, name='exitoso'),  
    path('mapa/', recorridos_views.mapa, name='mapa'),  
    path('nosotros/', recorridos_views.nosotros, name='nosotros'),  
    path('proximos/', recorridos_views.proximos, name='proximos'),

    path('MapaRutas/', recorridos_views.MapaRutas, name='MapaRutas'),  
    path('<int:recorrido_id>/', recorridos_views.detalle_recorrido, name='detalle_recorrido'),
    path('<int:recorrido_id>/inscribirme/', recorridos_views.inscribirme, name='inscribirme'),

    path('<int:recorrido_id>/', recorridos_views.detalle_recorrido, name='detalle_recorrido'),
    path('<int:recorrido_id>/inscribirme/', recorridos_views.inscribirme, name='inscribirme'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

