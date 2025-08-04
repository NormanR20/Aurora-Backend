from pyexpat import model
from re import T
from django.db import models
from django.db.models import base
from django.db.models.deletion import CASCADE
from django.db.models.functions.datetime import TruncHour
from django.utils.timezone import now
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User, Group
from .modelos_head_clima import *
from .modelos_onoff_boarding import *

class nucleo_modulos(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=False,blank=True,null=True)

class nucleo_tipo_mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    modulo = models.ForeignKey(nucleo_modulos,on_delete=models.CASCADE)

class nucleo_configuracion_correos(models.Model):
    descripcion = models.CharField(max_length=255,null=True,blank=True)
    asunto = models.CharField(max_length=130)
    mensaje = models.TextField()
    creador = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_creacion = models.DateField(default=datetime.now().date(),null=True,blank=True)
    tipo_mensaje = models.ForeignKey(nucleo_tipo_mensaje,on_delete=models.CASCADE)

class nucleo_variables_envio_correos(models.Model):
    variable = models.CharField(max_length=50)
    app = models.CharField(max_length=50)
    modelos = models.CharField(max_length=255)
    valores = models.CharField(max_length=255)
    tipo_mensaje = models.ForeignKey(nucleo_tipo_mensaje,on_delete=models.CASCADE)
    
class nucleo_pruebas(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion = models.DateField(auto_now=True,null=True,blank=True)
    fecha_creaciontime = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizaciontime = models.DateTimeField(auto_now=True,null=True,blank=True)
