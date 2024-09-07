from django.db import models

# Create your models here.
class Mensaje(models.Model):
    remitente=models.TextField()
    destinatario=models.TextField()
    contenido_mensaje=models.TextField()
    hora=models.DateTimeField(auto_now=True)

