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



class descriptor_perfil_proposito(models.Model):
    descripcion=models.TextField(null=False,blank=False)
    nombre=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class descriptor_perfil_datos_generales(models.Model):
    nombre_posicion=models.CharField(max_length=100,null=False,blank=False)
    descripcion_larga=models.CharField(max_length=1000,null=True,blank=True)
    empresa=models.ForeignKey(Funcional_Organizacion,null=True,blank=True, on_delete=models.CASCADE)
    proposito_general=models.ForeignKey(descriptor_perfil_proposito,null=True,blank=True, on_delete=models.CASCADE)
    division=models.ForeignKey(Funcional_Division,blank=True,null=True, on_delete=models.CASCADE)
    numero_personas_supervisa=models.CharField(max_length=100,null=True,blank=True)
    numero_ocupantes=models.IntegerField(default=0,null=True,blank=True)
    posiciones_sustitutas = models.ManyToManyField(Funcional_Funciones,null=True,blank=True,related_name="substitutas")
    clasificacion_empleado = models.ForeignKey(Funcional_Clasificacion, on_delete=models.CASCADE,null=True,blank=True)
    fecha_creacion=models.DateTimeField(default=timezone.now(),null=True,blank=True)
    fecha_creacion_sinhora=models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    posicion=models.ForeignKey(Funcional_Funciones,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="puesto")
    genero=models.CharField(max_length=100,null=True,blank=True)
    edad_minima=models.IntegerField(default=0,null=True,blank=True)
    edad_maxima=models.IntegerField(default=0,null=True,blank=True)
    necesita_viajar=models.CharField(max_length=100,null=True,blank=True)
    vehiculo=models.CharField(max_length=100,null=True,blank=True)
    unidad_organizativa=models.ForeignKey(Funcional_Unidad_Organizativa,null=True,blank=True,on_delete=models.DO_NOTHING)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="usuario_creo")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="usuario_actualizo")



class descriptor_perfil_proposito_descriptor(models.Model):
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    proposito = models.ForeignKey(descriptor_perfil_proposito,null=True,blank=True,on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    descriptor = models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
class archivos_gestor_competencia(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    subnivel1=models.CharField(max_length=500,null=True,blank=True)
    subnivel2=models.CharField(max_length=500,null=True,blank=True)
    id_area = models.IntegerField(null=False,blank=False)
    id_carpeta_encabezado = models.IntegerField(null=False,blank=False)
    medidas_disciplinarias = models.CharField(max_length=200,null=True,blank=True)
    tipo_documento = models.CharField(max_length=200,null=True,blank=True) 
    origen = models.CharField(max_length=300,null=True,blank=True)
    extension = models.CharField(max_length=20,null=True,blank=True)
    id_documento = models.IntegerField(default=0,null=False,blank=False)
    llave = models.CharField(max_length=300,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion = models.DateField(auto_now=True,null=True,blank=True)
    contentTypeGD = models.CharField(max_length=255,null=True,blank=True)  



class descriptor_perfil_tipo_competencia(models.Model):
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    numero_competencia=models.IntegerField(null=True,blank=True)
    competencia_indispensable=models.BooleanField(default=False)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)



class descriptor_perfil_competencia(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    nombre_gestor_documental=models.CharField(max_length=500,null=True,blank=True)
    descripcion_gestor_documental=models.CharField(max_length=500,null=True,blank=True)
    clasificacion=models.ForeignKey(Funcional_Clasificacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    archivo=models.ForeignKey(archivos_gestor_competencia,null=True,blank=True,on_delete=models.DO_NOTHING)
    tipo_competencia=models.ForeignKey(descriptor_perfil_tipo_competencia,null=True,blank=True,on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    
class descriptor_perfil_competencia_total(models.Model):
    total = models.IntegerField(null=True,blank=True)

class descriptor_perfil_area(models.Model):
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    



class descriptor_perfil_competencia_descriptor(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    descriptor = models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
    competencia=models.ForeignKey(descriptor_perfil_competencia,null=True,blank=True,on_delete=models.CASCADE)
    archivo=models.ForeignKey(archivos_gestor_competencia,null=True,blank=True,on_delete=models.DO_NOTHING)
    tipo_competencia=models.ForeignKey(descriptor_perfil_tipo_competencia,null=True,blank=True,on_delete=models.CASCADE)
    area = models.ForeignKey(descriptor_perfil_area,null=True,blank=True,on_delete=models.CASCADE)
    division=models.ForeignKey(Funcional_Division,null=True,blank=True,on_delete=models.CASCADE)
    nivel_desarrollo = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)],default=0,null=True,blank=True)
    clasificacion=models.ForeignKey(Funcional_Clasificacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)

  

# class descriptor_perfil_competencia_descriptor_archivo(models.Model):
#     nombre=models.CharField(max_length=500,null=True,blank=True)
#     descripcion=models.CharField(max_length=500,null=True,blank=True)
#     competencia_descriptor=models.ForeignKey(descriptor_perfil_competencia_descriptor,null=True,blank=True,on_delete=models.CASCADE)
#     archivo= models.ForeignKey(archivos_gestor_competencia,null=True,blank=True,on_delete=models.CASCADE)
#     fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
#     fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)

class descriptor_perfil_politicas_procedimientos(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    descriptor = models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
    archivo= models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.DO_NOTHING)
    url = models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)


class descriptor_perfil_indicador(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    objetivo=models.CharField(max_length=500,null=True,blank=True)
    formula_calculo=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)


class descriptor_perfil_indicador_descriptor(models.Model):
    indicador= models.ForeignKey(descriptor_perfil_indicador,null=True,blank=True,on_delete=models.CASCADE)
    descriptor = models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
    meta=models.CharField(max_length=500,null=True,blank=True)
    unidad_medida=models.ForeignKey(descriptor_perfil_datos_unidad_medida,null=True,blank=True,on_delete=models.CASCADE)
    fuente_verificacion = models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)

class descriptor_perfil_funcion(models.Model):
    descripcion=models.CharField(max_length=500,null=False,blank=False)
    perioricidad=models.IntegerField(default=0,null=False,blank=False)
    concecuencias_error= models.IntegerField(default=0,null=False,blank=False)
    complejidad = models.IntegerField(default=0,null=False,blank=False)
    unidad_medida = models.ForeignKey(descriptor_perfil_datos_unidad_medida,null=True,blank=True,on_delete=models.CASCADE)
    descriptor = models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
    meta =models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    fundamental = models.BooleanField(default=False,null=True,blank=True)



class descriptor_perfil_experiencia(models.Model):
    descriptor=models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
    tiempo=models.DecimalField(max_digits=20, decimal_places=2)
    tiempo_2=models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    institucion=models.CharField(max_length=500,null=True,blank=True)
    detalle=models.CharField(max_length=500,null=True,blank=True)
    experiencia_tipo_institucion=models.BooleanField(default=False)
    experiencia_tipo_institucion_detalle = models.TextField(null=True,blank=True)
    experiencia_tipo_cargo=models.BooleanField(default=False)
    experiencia_tipo_cargo_detalle=models.TextField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)

class descriptor_perfil_formacion(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    descriptor=models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
    formacion=models.ForeignKey(descriptor_perfil_titulo,null=True,blank=True,on_delete=models.CASCADE)
    indispensable = models.BooleanField(default=False)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)
    

class descriptor_perfil_preparacion(models.Model):
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    descriptor=models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
    curso=models.ForeignKey(descriptor_perfil_cursos_diplomados_seminario_pasantia,null=True,blank=True,on_delete=models.CASCADE)
    indispensable = models.BooleanField(default=False)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)


class descriptor_perfil_conocimiento_tecnico_adquirido(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    descriptor=models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.CASCADE)
    conocimiento=models.ForeignKey(descriptor_perfil_conocimiento_tecnico,null=True,blank=True,on_delete=models.CASCADE)
    indispensable = models.BooleanField(default=False)
    nivel_profundidad = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],default=1,null=True,blank=True)
    descripcion=models.CharField(max_length=1000,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)

