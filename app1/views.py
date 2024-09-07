from django.shortcuts import render,redirect
from django.views import View
from .models import Mensaje
from django.http import HttpResponse
# Create your views here.
def ver_mensajes(request):
    mensaje=Mensaje.objects.all()
    contexto = {
        'mensajes': mensaje
    }
    return render(request,'ver_mensajes.html',contexto)

def borrar_mensaje(request,mensaje_id):

    mensaje=Mensaje.objects.get(id=mensaje_id)
    mensaje.delete()
    return redirect('ver_mensajes')

class cargar_mensaje(View):
    def post(self,request):
        remitente=request.POST.get("remitente")
        destinatario=request.POST.get("destinatario")
        contenido=request.POST.get("mensaje")
        if(remitente != "" and destinatario != "" and contenido != "" ):
            nuevo_mensaje=Mensaje(destinatario=destinatario,remitente=remitente,contenido_mensaje=contenido)
            nuevo_mensaje.save()
            return redirect('enviado_con_exito')   
        else:
           return redirect('error_al_enviarlo ')
         
def enviado_con_exito(request):
    return render(request,'mensaje_enviado.html')

def error_al_enviarlo(request):
    return render(request,'mensaje_error.html') 
def ingresar_mensajes(request):
    return render(request,'ingresar_mensajes.html')        