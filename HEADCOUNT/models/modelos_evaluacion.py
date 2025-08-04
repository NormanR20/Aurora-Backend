from enum import Flag
from pyexpat import model
from re import T
#from symbol import factor
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




class evaluacion_frecuencia(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    descripcion=models.CharField(max_length=500,null=False,blank=False)
    cantidad_meses=models.IntegerField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)

class evaluacion_tipo_plan_accion(models.Model):
    descripcion=models.CharField(max_length=500,null=False,blank=False)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)


class evaluacion_archivo_plan_accion_gestor(models.Model):
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



class evaluacion_tipo_evaluacion(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    descripcion=models.CharField(max_length=500,null=False,blank=False)
    requerido=models.BooleanField(null=True,blank=True,default=False)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)




class evaluacion_periodicidad(models.Model):
    empresa=models.ForeignKey(Funcional_Organizacion,null=True,blank=True, on_delete=models.CASCADE)
    anio=models.IntegerField(null=True,blank=True)
    frecuencia = models.ForeignKey(evaluacion_frecuencia,null=True,blank=True, on_delete=models.CASCADE)
    # tipo_evaluacion=models.ForeignKey(evaluacion_tipo_evaluacion,null=True,blank=True, on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_inicio= models.DateField(null=True,blank=True)
    fecha_fin=models.DateField(null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)  


class categoria_desempeno(models.Model):
    descripcion=models.CharField(max_length=500,null=True,blank=True)
    valor_minimo=models.IntegerField(null=True,blank=True)
    valor_maximo=models.IntegerField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)



class evaluacion_configuracion_periodo(models.Model):
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)
    periodo=models.IntegerField(null=True,blank=True)
    tipo_evaluacion=models.ForeignKey(evaluacion_tipo_evaluacion,null=True,blank=True, on_delete=models.CASCADE)
    fecha_fin=models.DateField(null=True,blank=True)
    fecha_inicio= models.DateField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)


class evaluacion_metrica_competencia(models.Model):
    nombre=models.CharField(max_length=50,null=True,blank=True)
    valor_minimo = models.IntegerField(null=True,blank=True)
    valor_maximo = models.IntegerField(null=True,blank=True)
    valor_porcentual=models.IntegerField(null=True,blank=True)
    grado=models.IntegerField(null=True,blank=True)
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)

    

class evaluacion_factor(models.Model):
    nombre=models.CharField(max_length=50,null=True,blank=True)
    peso = models.IntegerField(null=True,blank=True)
    #desempeno_esperado=models.IntegerField(null=True,blank=True)
    tipo_factor=models.IntegerField(null=True,blank=True,default=0)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    clasificacion=models.ForeignKey(Funcional_Clasificacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True,on_delete=models.CASCADE)



class evaluacion_competencia(models.Model):
    competencia=models.ForeignKey(descriptor_perfil_competencia,null=True,blank=True,on_delete=models.CASCADE)
    peso = models.IntegerField(null=True,blank=True)
    desempeno_esperado=models.IntegerField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    clasificacion=models.ForeignKey(Funcional_Clasificacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)

    
class evaluacion_metrica_factor(models.Model):
    nombre=models.CharField(max_length=50,null=True,blank=True)
    factor=models.ForeignKey(evaluacion_factor,null=True,blank=True,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500,null=True,blank=True)
    puntos=models.IntegerField(null=True,blank=True)        
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)  
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)


class evaluacion_factor_plantilla_encabezado(models.Model):
    nombre=models.CharField(max_length=50,null=True,blank=True)
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)

class evaluacion_competencia_plantilla_encabezado(models.Model):
    nombre=models.CharField(max_length=50,null=True,blank=True)
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)  

class evaluacion_plantilla_competencia(models.Model):
    posicion=models.ForeignKey(Funcional_Funciones,null=True,blank=True,on_delete=models.DO_NOTHING)
    competencia_descriptor =models.ForeignKey(descriptor_perfil_competencia_descriptor,null=True,blank=True,on_delete=models.DO_NOTHING)
    competencia=models.ForeignKey(evaluacion_competencia,null=True,blank=True,on_delete=models.CASCADE)
    clasificacion=models.ForeignKey(Funcional_Clasificacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    pregunta=models.CharField(max_length=500,null=True,blank=True)
    competencia_plantilla_encabezado=models.ForeignKey(evaluacion_competencia_plantilla_encabezado,null=True,blank=True, on_delete=models.CASCADE)
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True) 


class evaluacion_plantilla_factor(models.Model):
    periodicidad=models.ForeignKey(evaluacion_periodicidad,null=True,blank=True, on_delete=models.CASCADE)
    posicion=models.ForeignKey(Funcional_Funciones,null=True,blank=True,on_delete=models.DO_NOTHING)
    factor = models.ForeignKey(evaluacion_factor,null=True,blank=True,on_delete=models.DO_NOTHING)
    pregunta=models.CharField(max_length=500,null=True,blank=True)
    clasificacion=models.ForeignKey(Funcional_Clasificacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    factor_plantilla_encabezado=models.ForeignKey(evaluacion_factor_plantilla_encabezado,null=True,blank=True, on_delete=models.CASCADE)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)





class evaluacion_encabezado(models.Model):
    evaluado=models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.DO_NOTHING)
    responsable_directo=models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='responsable_directo')
    evaluador=models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.DO_NOTHING,related_name='evaluador')
    tipo_evaluacion=models.ForeignKey(evaluacion_tipo_evaluacion,null=True,blank=True,on_delete=models.DO_NOTHING)
    periodicidad = models.ForeignKey(evaluacion_periodicidad,null=True,blank=True,on_delete=models.DO_NOTHING)
    periodo = models.IntegerField(null=True,blank=True)        
    tipo_evaluacion_encabezado=models.IntegerField(null=True,blank=True) #1 para competencia y 2 para factor
    estado=models.BooleanField(null=True,blank=True,default=True)
    nota_total=models.IntegerField(null=True,blank=True)        
    nota_maxima=models.IntegerField(null=True,blank=True)
    nota_total_porcentaje=models.IntegerField(null=True,blank=True)
    nota_total_porcentaje_prorateo=models.IntegerField(null=True,blank=True)
    nota_total_porcentaje_prorateo_decimal=models.DecimalField(null=True,blank=True,max_digits=20, decimal_places=2)#resultado por el peso para la competencia prorateado
    nota_total_porcentaje_sinpeso=models.IntegerField(null=True,blank=True)
    nivel_resultado=models.CharField(max_length=500,null=True,blank=True)
    comentario_evaluador=models.CharField(max_length=500,null=True,blank=True)
    comentario_evaluado=models.CharField(max_length=500,null=True,blank=True)
    tipo_plan_accion=models.ForeignKey(evaluacion_tipo_plan_accion,null=True,blank=True,on_delete=models.DO_NOTHING)
    evaluacion_archivo_plan_accion_gestor=models.ForeignKey(evaluacion_archivo_plan_accion_gestor,null=True,blank=True,on_delete=models.DO_NOTHING)
    fecha_evaluacion= models.DateField(null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    fecha_comentario_evaluado= models.DateField(null=True,blank=True)
    descriptor_empleado=models.ForeignKey(descriptor_perfil_datos_generales,null=True,blank=True,on_delete=models.DO_NOTHING) 
     



class detalle_evaluacion_competencia(models.Model):
    encabezado= models.ForeignKey(evaluacion_encabezado,null=True,blank=True,on_delete=models.DO_NOTHING)
    metrica_competencia= models.ForeignKey(evaluacion_metrica_competencia,null=True,blank=True,on_delete=models.DO_NOTHING)
    evaluacion_plantilla_competencia = models.ForeignKey(evaluacion_plantilla_competencia,null=True,blank=True,on_delete=models.DO_NOTHING)
    nota_competencia=models.IntegerField(null=True,blank=True)
    nota_competencia_prorateada_decimal=models.IntegerField(null=True,blank=True)
    nota_competencia_prorateada=models.DecimalField(null=True,blank=True,max_digits=20, decimal_places=2)#resultado por el peso para la competencia prorateado
    desempeno_esperado=models.IntegerField(null=True,blank=True)
    peso=models.IntegerField(null=True,blank=True)#peso asignado a la competencia de la pregunta
    grado=models.IntegerField(null=True,blank=True) #vvalor de metrica asignado a la respuesta
    puntos=models.IntegerField(null=True,blank=True) #valor de metrica asignada a la respuesta en porcentaje
    resultado=models.IntegerField(null=True,blank=True) #promedio de valores metrica porcentaje, por competencia evaluada 
    nota_total_competencia=models.IntegerField(null=True,blank=True)#resultado por el peso para la competencia
    nota_total_competencia_prorateada=models.IntegerField(null=True,blank=True)#resultado por el peso para la competencia prorateado
    nota_total_competencia_prorateada_decimal=models.DecimalField(null=True,blank=True,max_digits=20, decimal_places=2)#resultado por el peso para la competencia prorateado
    peso_prorateado=models.IntegerField(null=True,blank=True)#peso prorateado asignado a la competencia de la pregunta
    peso_prorateado_decimal=models.DecimalField(null=True,blank=True,max_digits=20, decimal_places=2)#peso prorateado asignado a la competencia de la pregunta
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True) 


class detalle_evaluacion_factor(models.Model):
    encabezado= models.ForeignKey(evaluacion_encabezado,null=True,blank=True,on_delete=models.DO_NOTHING)
    metrica_factor= models.ForeignKey(evaluacion_metrica_factor,null=True,blank=True,on_delete=models.DO_NOTHING)
    evaluacion_plantilla_factor = models.ForeignKey(evaluacion_plantilla_factor ,null=True,blank=True,on_delete=models.DO_NOTHING)
    factor = models.ForeignKey(evaluacion_factor,null=True,blank=True,on_delete=models.DO_NOTHING,related_name="factor_detalle")
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    #evaluacion_factor= models.ForeignKey(evaluacion_factor,null=True,blank=True,on_delete=models.DO_NOTHING) 
    peso=models.IntegerField(null=True,blank=True)#peso asignado al momento de evaluar
    puntos=models.IntegerField(null=True,blank=True) #valor metrica asignado por evaluador
    maxima_nota_factor=models.IntegerField(null=True,blank=True)#maximo valor posible por factor que puede asignarse
    grado=models.IntegerField(null=True,blank=True) #valor final asignado a la respuesta
    porcentaje_pregunta=models.IntegerField(null=True,blank=True)#valor porcentual que tiene la pregunta con respecto al valor total del factor
    valor_total_factor=models.IntegerField(null=True,blank=True) #suma de los grados multiplicados por su metrica correspondiente 
    nota_total=models.IntegerField(null=True,blank=True)
    nota_total_final=models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=7)
    pregunta_descriptor=models.CharField(max_length=500,null=True,blank=True) #esta pregunta se llena con los factores de tipo 1 y 2 con el texto que se extrae de 
    respuesta_pregunta=models.IntegerField(null=True,blank=True)#id_origin_pregunta(este id se obtiene de la tabla descriptor_perfil_funcion(tipo_factor1),descriptor_perfil_indicador(tipo_factor2))



class detalle_evaluacion_factor_indicador(models.Model):
    encabezado= models.ForeignKey(evaluacion_encabezado,null=True,blank=True,on_delete=models.DO_NOTHING)
    factor = models.ForeignKey(evaluacion_factor,null=True,blank=True,on_delete=models.DO_NOTHING)
    metrica_factor= models.ForeignKey(evaluacion_metrica_factor,null=True,blank=True,on_delete=models.DO_NOTHING)
    evaluacion_plantilla_competencia = models.ForeignKey(evaluacion_plantilla_competencia,null=True,blank=True,on_delete=models.DO_NOTHING)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)      
    metrica=models.IntegerField(null=True,blank=True)  
    peso=models.IntegerField(null=True,blank=True) 
    maxima_nota=models.IntegerField(null=True,blank=True)   
    grado=models.IntegerField(null=True,blank=True)
    porcentaje_pregunta=models.IntegerField(null=True,blank=True)
    valor_total=models.IntegerField(null=True,blank=True)
    nota_totall=models.IntegerField(null=True,blank=True)



########NOTIFICACIONES EN AURORA########################################################################

class notificacion_aurora(models.Model):    
    destinatario=models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.DO_NOTHING)
    asunto=models.CharField(max_length=200,null=True,blank=True)
    mensaje=models.TextField(null=True,blank=True)
    leido=models.BooleanField(null=True,blank=True,default=False)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion=models.DateField(auto_now=True,null=True,blank=True)
    enlace=models.CharField(max_length=500,null=True,blank=True)
