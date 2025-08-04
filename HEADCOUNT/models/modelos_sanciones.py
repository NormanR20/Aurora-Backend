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

class sanciones_categoria_desvinculacion(models.Model):
    nombre = models.CharField(max_length=200,null=True,blank=True)
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)

class sanciones_motivo_accion_disciplinaria(models.Model):
    nombre = models.CharField(max_length=200,null=True,blank=True)
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)

class sanciones_tipo_accion_disciplinaria(models.Model):
    nombre = models.CharField(max_length=200,null=True,blank=True)
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    mostrar_jefe = models.BooleanField(default=False,null=True,blank=True)

class sanciones_medidas_disciplinarias(models.Model):
    nombre = models.CharField(max_length=200,null=True,blank=True)
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    mostrar_jefe = models.BooleanField(default=False,null=True,blank=True)

class sanciones_tipo_falta(models.Model):
    nombre = models.CharField(max_length=200,null=True,blank=True)
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    mostrar_jefe = models.BooleanField(default=False,null=True,blank=True)


class sanciones_estatus(models.Model):
    nombre = models.CharField(max_length=200,null=True,blank=True) 
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    color_a_mostrar = models.CharField(max_length=200,null=True,blank=True)

class sanciones_casos_disciplinarios(models.Model):
    caso_disciplinario = models.CharField(max_length=200,null=True,blank=True)
    id_accion_disciplinaria = models.ForeignKey(sanciones_tipo_accion_disciplinaria,on_delete=models.CASCADE)
    id_motivo = models.ForeignKey(sanciones_motivo_accion_disciplinaria,on_delete=models.CASCADE)
    id_encargado = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    id_tipo_falta = models.ForeignKey(sanciones_tipo_falta,on_delete=models.CASCADE)
    codigo_empleado = models.ForeignKey(Funcional_empleado,blank=True,null=True,on_delete=models.CASCADE ,related_name='codigo_empleado')
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE ,related_name='creado_por')
    fecha_vencimiento = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    estatus = models.ForeignKey(sanciones_estatus,on_delete=models.CASCADE)
    numero_ticket = models.IntegerField(default=0,null=True,blank=True)
    off_bording=models.ForeignKey(on_off_bording_workflow,null=True,blank=True,on_delete=models.CASCADE)
    categoria_desvinculacion=models.ForeignKey(sanciones_categoria_desvinculacion,null=True,blank=True,on_delete=models.CASCADE)
    fecha_cierre = models.DateField(null=True,blank=True)




class sanciones_plantilla_formatos_oficiales(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    archivo = models.ForeignKey(archivos_gestor_formatos_oficiales,on_delete=models.CASCADE)
    creado_por = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_actualizacion = models.DateField(auto_now=True,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)



class sanciones_accion_disciplinaria(models.Model):
    caso_disciplinario=models.ForeignKey(sanciones_casos_disciplinarios,null=True,blank=True,on_delete=models.CASCADE)
    medida_disciplinaria=models.ForeignKey(sanciones_medidas_disciplinarias,null=True,blank=True,on_delete=models.CASCADE)
    off_bording=models.ForeignKey(on_off_bording_workflow,null=True,blank=True,on_delete=models.CASCADE)
    categoria_desvinculacion=models.ForeignKey(sanciones_categoria_desvinculacion,null=True,blank=True,on_delete=models.CASCADE)
    observacion=models.CharField(max_length=500,null=True,blank=True)
    archivo_evidencia=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE,related_name='archivo_evidencia')
    aplicada_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_vencimiento=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    archivo_autorizacion=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE,related_name='archivo_autorizacion')
    autorizado_por = models.CharField(max_length=500,null=True,blank=True)
    calculo_prestaciones= models.CharField(max_length=500,null=True,blank=True)


class sanciones_accion_disciplinaria_correos(models.Model):
    accion_disciplinaria=models.ForeignKey(sanciones_accion_disciplinaria,null=True,blank=True,on_delete=models.CASCADE)
    correo=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)

