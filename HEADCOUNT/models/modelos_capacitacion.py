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
from .modelos_descriptor_perfil import *
from django.core.validators import MaxValueValidator, MinValueValidator



class capacitacion_tipo_capacitacion(models.Model):
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo_tipo")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo_tipo")


class capacitacion_modalidad(models.Model):
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo_modalidad")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo_modalidad")



class capacitacion_enfoque(models.Model):
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="cap_enfoque_usuario_creo")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="cap_enfoque_usuario_actualizo")


class capacitacion_origen(models.Model):
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo_origen")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo_origen")


class capacitacion_motivo_inasistencia(models.Model):
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="cap_mot_usuario_creo")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="cap_mot_usuario_actualizo")
    #creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo")
    #actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo")

class capacitacion_estado(models.Model):
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    color=models.CharField(max_length=100,null=True,blank=True)
    tipo_estado=models.IntegerField(null=True,blank=True) #1 para campañas, 2 para evaluaciones
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo_estado")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo_estado")

class capacitacion_curso(models.Model):
    codigo_capacitacion=models.CharField(max_length=50,null=True,blank=True)
    nombre_capacitacion=models.CharField(max_length=100,null=True,blank=True)
    descripcion_capacitacion=models.CharField(max_length=1000,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capacur_usuario_creo_estado")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capacur_usuario_actualizo_estado")

class capacitacion_factor_evaluacion(models.Model):
    nombre_factor=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    #creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo")
    #actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo")

class capacitacion_escala_evaluacion_factor(models.Model):
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    porcentaje=models.IntegerField(null=True,blank=True) 
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    #creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo")
    #actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo")

class capacitacion_metrica_evaluacion_factor(models.Model):
    valor_minimo=models.IntegerField(null=True,blank=True) 
    valor_maximo=models.IntegerField(null=True,blank=True) 
    porcentaje = models.IntegerField(null=True,blank=True) 
    color=models.CharField(max_length=100,null=True,blank=True)
    anio=models.IntegerField(null=True,blank=True) 
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo_metrica_factor")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo_metrica_factor")


class capacitacion_matriz_9_cajas(models.Model):
    x=models.IntegerField(null=True,blank=True) 
    y=models.IntegerField(null=True,blank=True) 
    orden=models.IntegerField(null=True,blank=True) 
    encabezado_cuadrante=models.CharField(max_length=100,null=True,blank=True)
    descripcion_cuadrante=models.JSONField(null=True,blank=True)
    anio=models.IntegerField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_matriz9_usuario_creo")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_matriz9_usuario_actualizo")

class capacitacion_metrica_9_cajas(models.Model):
    valor_minimo=models.IntegerField(null=True,blank=True) 
    valor_maximo=models.IntegerField(null=True,blank=True) 
    tipo_criterio=models.IntegerField(null=True,blank=True) #Tipo de criterio (1 para desempeño, 2 para potencial)
    cordenada=models.IntegerField(null=True,blank=True) 
    descripcion=models.CharField(max_length=100,null=True,blank=True)
    anio=models.IntegerField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    #creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo")
    #actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo")

class capacitacion_metrica_educacion_formal(models.Model):
    nombre_metrica=models.CharField(max_length=100,null=True,blank=True)
    porcentaje=models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    anio=models.IntegerField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    #creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo")
    #actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo")

class capacitacion_metrica_experiencia_puesto(models.Model):
    de=models.IntegerField(null=True,blank=True) 
    hasta=models.IntegerField(null=True,blank=True) 
    porcentaje=models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    anio=models.IntegerField(null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo_metrica_experiencia_puesto")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo_metrica_experiencia_puesto")

class capacitacion_archivo_gestor(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)  #nombre del archivo completo
    descripcion=models.CharField(max_length=500,null=True,blank=True) #campo descripcioin que aparece en el gestor
    empresa=models.CharField(max_length=500,null=True,blank=True) #empresa
    division=models.CharField(max_length=500,null=True,blank=True) #division
    codigo_empleado=models.CharField(max_length=500,null=True,blank=True) #codigo_empleado
    id_area = models.IntegerField(null=False,blank=False)
    id_carpeta_encabezado = models.IntegerField(null=False,blank=False)
    tipo_documento = models.CharField(max_length=200,null=True,blank=True) 
    origen = models.CharField(max_length=300,null=True,blank=True)
    extension = models.CharField(max_length=20,null=True,blank=True)
    id_documento = models.IntegerField(default=0,null=False,blank=False)
    llave = models.CharField(max_length=300,null=True,blank=True)  #empresa-division-tipo_documento-descripcion-codigo_empleado-fecha
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion = models.DateField(auto_now=True,null=True,blank=True)
    contentTypeGD = models.CharField(max_length=255,null=True,blank=True)

class capacitacion_campania(models.Model):
    estado=models.ForeignKey(capacitacion_estado,null=True,blank=True,on_delete=models.DO_NOTHING)
    codigo_campania=models.CharField(max_length=100,null=True,blank=True)
    nombre_campania=models.CharField(max_length=100,null=True,blank=True)
    duracion_horas=models.IntegerField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    fecha_fin=models.DateField(null=True,blank=True)
    fecha_inicio= models.DateField(null=True,blank=True)

    
class capacitacion_evento_capacitacion(models.Model):
    campania=models.ForeignKey(capacitacion_campania,null=True,blank=True,on_delete=models.DO_NOTHING)
    capacitacion=models.ForeignKey(capacitacion_curso,null=True,blank=True,on_delete=models.DO_NOTHING)
    responsable=models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.DO_NOTHING)
    tipo_capacitacion=models.ForeignKey(capacitacion_tipo_capacitacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    enfoque=models.ForeignKey(capacitacion_enfoque,null=True,blank=True,on_delete=models.DO_NOTHING)
    origen=models.ForeignKey(capacitacion_origen,null=True,blank=True,on_delete=models.DO_NOTHING)
    nivel_formacion=models.ForeignKey(Funcional_Instituto,null=True,blank=True,on_delete=models.DO_NOTHING)
    formacion=models.ForeignKey(Funcional_Formacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    titulo=models.ForeignKey(Funcional_Titulo,null=True,blank=True,on_delete=models.DO_NOTHING)
    especialidad=models.ForeignKey(Funcional_Especialidad,null=True,blank=True,on_delete=models.DO_NOTHING)
    modalidad=models.ForeignKey(capacitacion_modalidad,null=True,blank=True,on_delete=models.DO_NOTHING)
    #archivo_evaluacion=models.ForeignKey(     ,null=True,blank=True,on_delete=models.DO_NOTHING)
    fecha_inicio= models.DateField(null=True,blank=True)
    estado=models.ForeignKey(capacitacion_estado,null=True,blank=True,on_delete=models.DO_NOTHING)
    fecha_fin=models.DateField(null=True,blank=True)
    duracion_horas=models.IntegerField(null=True,blank=True)
    impartido_por=models.CharField(max_length=100,null=True,blank=True)
    facilitador=models.CharField(max_length=100,null=True,blank=True)
    horas_cumplidas=models.IntegerField(null=True,blank=True)
    meta_horas=models.IntegerField(null=True,blank=True)
    costo_capacitacion=models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    costo_empleado=models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    numero_empleados_recibir=models.IntegerField(null=True,blank=True)
    dias_evaluacion=models.IntegerField(null=True,blank=True)
    nota_evaluacion=models.IntegerField(null=True,blank=True)
    porcentaje_asistencia=models.IntegerField(null=True,blank=True) 
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_creo_evento_capacitacion")
    nota_aprovatoria=models.IntegerField(null=True,blank=True)
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_usuario_actualizo_evento_capacitacion")
    es_evaluacion=models.BooleanField(null=True,blank=True,default=True)
    hora_capacitacion=models.CharField(max_length=100,null=True,blank=True)
    nombre_evento_capacitacion=models.CharField(max_length=100,null=True,blank=True)


class capacitacion_asistencia(models.Model):
    empleado = models.ForeignKey(Funcional_empleado,blank=True,null=True,on_delete=models.DO_NOTHING ,related_name='empleado_capacitacion_asistencia')
    evento_capacitacion = models.ForeignKey(capacitacion_evento_capacitacion,blank=True,null=True,on_delete=models.DO_NOTHING)
    motivo_inasistencia=models.ForeignKey(capacitacion_motivo_inasistencia,blank=True,null=True,on_delete=models.DO_NOTHING)
    asistio=models.BooleanField(null=True,blank=True,default=True)
    nota_evaluacion=models.DecimalField(max_digits=20, decimal_places=2,null=True,blank=True)
    estado=models.ForeignKey(capacitacion_estado,null=True,blank=True,on_delete=models.DO_NOTHING)
    archivo=models.ForeignKey(capacitacion_archivo_gestor,null=True,blank=True,on_delete=models.DO_NOTHING)
    recibidas=models.IntegerField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_asistencia_usuario_creo")
    actualizado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.DO_NOTHING,related_name="capa_asistencia_usuario_actualizo")





