from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_mensajes,name="ver_mensajes"),
    path('borrar_mensaje/<int:mensaje_id>',views.borrar_mensaje,name="borrar_mensajes"),
    path('cargar_mensaje/',views.cargar_mensaje.as_view(),name='cargar_mensaje'),
    path('enviado_con_exito/',views.enviado_con_exito,name='enviado_con_exito'),
    path('error_al_enviarlo/',views.error_al_enviarlo,name='error_al_enviarlo'),
   path('ingresar_mensajes/',views.ingresar_mensajes,name='ingresar_mensajes'),
   path("buscar_mensajes/",views.buscar_mensajes,name='buscar_mensajes'),
   path("ver_mensajes_buscados/",views.ver_mensajes_buscados,name='ver_mensajes_buscados'),
    
]
