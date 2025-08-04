from enum import Flag
from pyexpat import model
from re import T
from unicodedata import category
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
from django.core.validators import MaxValueValidator, MinValueValidator


class seleccion_contratacion_motivo(models.Model):
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class seleccion_contratacion_pais(models.Model):
    nombre_pais=models.CharField(max_length=500,null=True,blank=True)
    codigo_pais=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class seleccion_contratacion_estado(models.Model):
    nombre_estado=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    color_mostrar = models.CharField(max_length=500,null=True,blank=True)
    tipo_estado=models.IntegerField(default=2,null=True,blank=True)


class seleccion_contratacion_solicitud_plaza_vacante(models.Model):
    posicion =  models.ForeignKey(Funcional_Puesto,null=True,blank=True,on_delete=models.CASCADE)
    motivo = models.ForeignKey(seleccion_contratacion_motivo,null=True,blank=True,on_delete=models.CASCADE)
    numero_posiciones = models.IntegerField(default=0,null=True,blank=True)
    fecha_solicitud = models.DateField(auto_now_add=True,null=True,blank=True)
    pais = models.ForeignKey(seleccion_contratacion_pais,null=True,blank=True,on_delete=models.CASCADE)
    funcion=models.ForeignKey(Funcional_Funciones,null=True,blank=True,on_delete=models.CASCADE)
    estado=models.ForeignKey(seleccion_contratacion_estado,null=True,blank=True,on_delete=models.CASCADE)
    creador_plaza = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='creador_solicitud_plaza')
    responsable_seguimiento_plaza = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='responsable_seleccion')
    finalizador_plaza = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='finalizador_seleccion_contratacion')
    plan_induccion = models.FileField(upload_to='media/seleccion_contratacion/plan_induccion',null=True,blank=True)
    nombre_plan_induccion = models.CharField(max_length=500,null=True,blank=True)
    departamento = models.ForeignKey(Funcional_Division,blank=True,null=True, on_delete=models.CASCADE)
    fecha_inicio_proceso = models.DateField(null=True,blank=True)
    fecha_actualizacion = models.DateField(auto_now=True,null=True,blank=True)

class seleccion_contratacion_postulante_plaza(models.Model):
    profesion= models.ForeignKey(descriptor_perfil_titulo,blank=True,null=True,on_delete=models.CASCADE)
    nombre_postulante=models.CharField(max_length=500,null=True,blank=True)
    estado = models.ForeignKey(seleccion_contratacion_estado,blank=True,null=True,on_delete=models.CASCADE)
    plaza = models.ForeignKey(seleccion_contratacion_solicitud_plaza_vacante,blank=True,null=True,on_delete=models.CASCADE)
    archivo_cv = models.FileField(upload_to='media/seleccion_contratacion/postulantes',null=True,blank=True)
    nombre_archivo_cv=models.CharField(max_length=500,null=True,blank=True)
    calificacion = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0,null=True,blank=True)
    descripcion_calificacion=models.CharField(max_length=1000,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion = models.DateField(auto_now=True,null=True,blank=True)

class seleccion_contratacion_puestos_vacante(models.Model):
    codigo=models.CharField(max_length=500,null=True,blank=True)
    descripcion= models.CharField(max_length=500,null=True,blank=True)
    descripcion_larga = models.CharField(max_length=500,null=True,blank=True)
    funcional_empleado_codigo = models.CharField(max_length=500,null=True,blank=True)
    funcional_empleado_nombre = models.CharField(max_length=500,null=True,blank=True)
    unidad_organizativa_nombre = models.CharField(max_length=500,null=True,blank=True)
    unidad_organizativa_codigo = models.CharField(max_length=500,null=True,blank=True)
    estado_puesto = models.CharField(max_length=500,null=True,blank=True)