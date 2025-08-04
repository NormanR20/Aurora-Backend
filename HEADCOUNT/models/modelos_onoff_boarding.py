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


class on_off_bording_workflow_plantilla(models.Model):
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    fecha_inicio = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_fin = models.DateField(default=datetime.now().date(),null=True,blank=True)
    estado=models.BooleanField(default=False)
    creador = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING)
    tipo_workflow = models.IntegerField(blank=True,null=True,default=0)



class on_off_bording_bloque_plantilla(models.Model):
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    fecha_inicio = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_fin = models.DateField(default=datetime.now().date(),null=True,blank=True)
    estado=models.BooleanField(default=False)
    posicion=models.IntegerField()
    workflow=models.ForeignKey(on_off_bording_workflow_plantilla,on_delete=models.CASCADE)

class on_off_bording_tarea_plantilla(models.Model):
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    fecha_inicio = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_fin = models.DateField(default=datetime.now().date(),null=True,blank=True)
    evaluable=models.BooleanField(default=False)
    calificacion=models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)
    posicion=models.IntegerField()
    estado=models.BooleanField(default=False)
    archivo_subir=models.FileField(upload_to='media/on_offboarding',null=True,blank=True)
    archivo_bajar=models.FileField(upload_to='media/on_offboarding',null=True,blank=True)
    subir_archivo = models.BooleanField(default=False,null=True,blank=True)
    enlace_evaluacion=models.CharField( max_length=500,blank=True,null=True)
    bloque=models.ForeignKey(on_off_bording_bloque_plantilla,on_delete=models.CASCADE)
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.DO_NOTHING)



class on_off_bording_workflow(models.Model):
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    fecha_inicio = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_fin = models.DateField(default=datetime.now().date(),null=True,blank=True)
    estado=models.BooleanField(default=False)
    empleado = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING)
    responsable = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING ,related_name='responsable')
    tipo_workflow = models.IntegerField(blank=True,null=True,default=0)
    fecha_conclusion = models.DateTimeField(default=timezone.now(),null=True,blank=True)
        
class on_off_bording_bloque(models.Model):
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    fecha_inicio = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_fin = models.DateField(default=datetime.now().date(),null=True,blank=True)
    estado=models.BooleanField(default=False)
    posicion=models.IntegerField()
    workflow=models.ForeignKey(on_off_bording_workflow,on_delete=models.CASCADE)
    fecha_conclusion = models.DateTimeField(default=timezone.now(),null=True,blank=True)

class on_off_bording_tarea(models.Model):
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    fecha_inicio = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_fin = models.DateField(default=datetime.now().date(),null=True,blank=True)
    evaluable=models.BooleanField(default=False)
    calificacion=models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)
    posicion=models.IntegerField()
    estado=models.BooleanField(default=False)
    archivo_subir =models.FileField(upload_to='media/on_offboarding',null=True,blank=True)
    archivo_bajar=models.FileField(upload_to='media/on_offboarding',null=True,blank=True)
    subir_archivo = models.BooleanField(default=False,null=True,blank=True)
    enlace_evaluacion=models.CharField( max_length=500,blank=True,null=True)
    bloque=models.ForeignKey(on_off_bording_bloque,on_delete=models.CASCADE)
    compa_guia = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING)
    fecha_conclusion = models.DateTimeField(default=timezone.now(),null=True,blank=True)
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.DO_NOTHING)

class on_off_bording_bienvenida(models.Model):
    texto_json = models.JSONField()

#forzar actualizacion
