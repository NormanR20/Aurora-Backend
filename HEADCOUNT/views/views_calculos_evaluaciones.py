from decimal import MIN_EMIN
from distutils.cygwinccompiler import Mingw32CCompiler
from email import message
from email.policy import HTTP
from urllib import response
from django.db.models.functions import ExtractYear
import ast
from re import sub
from django.contrib.auth.models import User,Group
from django.http.response import Http404
from django.shortcuts import render
from calendar import monthrange
from HEADCOUNT.serializers.serializers_evaluacion import evaluacion_periodicidadserializer, evaluacion_plantilla_competenciaserializer
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from rest_framework import serializers, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from django.contrib.auth.decorators import login_required, user_passes_test,REDIRECT_FIELD_NAME
from django.utils.decorators import method_decorator
from  rest_framework.authtoken.models import Token
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import BadHeaderError, send_mail
from django.db.models import Q,F,Count,Sum,FloatField,ExpressionWrapper, query,Case ,When,IntegerField,Max,Min
from django.utils.crypto import get_random_string
import string
from django.contrib.auth import authenticate
from pyrfc import *
from datetime import date,datetime,timedelta
import json
from ..serializers import *
from ..models import *
from ..models import evaluacion_archivo_plan_accion_gestor
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
import sys
from rest_framework import generics
import io
import string
import csv
sys.setrecursionlimit(100000000)                                                        
from rest_framework import viewsets
import requests
from datetime import datetime
from rest_framework import status
from dateutil.relativedelta import relativedelta
from decimal import Decimal, ROUND_HALF_UP

def calculo_calificacion_factor(encabezado_id):
   preguntas=detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id)
   #llenar datos de configuracion para calculos


   for preg in preguntas:
      if preg.peso is None:
         if preg.evaluacion_plantilla_factor is None:
            preg.peso=preg.factor.peso
            preg.puntos=preg.metrica_factor.puntos
            preg.save()
         else:
            preg.peso=preg.evaluacion_plantilla_factor.factor.peso
            preg.puntos=preg.metrica_factor.puntos
            preg.save()

      else:

         # preg.peso=preg.evaluacion_plantilla_factor.factor.peso
         preg.puntos=preg.metrica_factor.puntos
         preg.save()

   #asignar grado segun metricas. seleccionada  por evaluador, el campo puntos se toma directo de la metrica seleccionada
   for pregunta in preguntas:
      pregunta.grado =pregunta.puntos
      pregunta.save()
   #buscar preguntas por factor
   lista_tipo_factor=[1,2]
   pregunta_x_factor= list(detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id).exclude(factor__tipo_factor__in=lista_tipo_factor).values_list('evaluacion_plantilla_factor__factor_id',flat=True).distinct())
   pregunta_x_facto_sin_plantillar= list(detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id).exclude(factor__tipo_factor=0).values_list('factor_id',flat=True).distinct())
   pregunta_x_factor.extend(pregunta_x_facto_sin_plantillar)
   evaluacion=evaluacion_encabezado.objects.get(id=encabezado_id)
   for factor_evaluado in pregunta_x_factor:
      #se busca el grado de cada respuesta, se acumulan y se obtiene la nota total por factor
      lista_preguntas=list(detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id,factor_id=factor_evaluado).values_list('grado',flat=True))
      #print('lista preguntas',lista_preguntas)
      tot_factor=0
      
      for grado in lista_preguntas:
         tot_factor=tot_factor+ int(grado if grado else 0)

      detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id,factor_id=factor_evaluado).update(valor_total_factor=tot_factor)
      #se cuentan las preguntas por factor y se busca la maxima nota posible al multiplicar estos resultado se obtiene la maxima nota posible por factor
      conteo=detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id,factor_id=factor_evaluado).count()
      maxima_metrica=evaluacion_metrica_factor.objects.filter(periodicidad_id=evaluacion.periodicidad.id).values_list('puntos',flat=True).order_by('-puntos')[0] if evaluacion_metrica_factor.objects.filter(periodicidad_id=evaluacion.periodicidad.id) else 0
      print("maxma metrica",maxima_metrica)
      detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id,factor_id=factor_evaluado).update(maxima_nota_factor=(conteo * maxima_metrica))
      # factor_evaluado.maxima_nota_factor = conteo * maxima_metrica
      # factor_evaluado.save()
   #calculo de maxima nota posbil para la evaluacion
   conteo_preguntas_factor=detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id)
   maxima_metrica_posible=evaluacion_metrica_factor.objects.filter(periodicidad_id=evaluacion.periodicidad.id).order_by('-puntos')[0]
   calculo_nota_maxima=maxima_metrica_posible.puntos*conteo_preguntas_factor.count()
   evaluacion.nota_maxima=calculo_nota_maxima
   evaluacion.save()

   respuestas = detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id)
   for r in respuestas :
      r.nota_total=round((r.valor_total_factor/r.maxima_nota_factor)*100)
      r.save()
      r.nota_total_final=r.peso *(r.nota_total/100)
      r.save()


   #calcular el total obtenido en la evaluacion de factores
   resultados=detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id)
   listado_factores=detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id).values_list('factor_id',flat=True).distinct()
   
   #calcular procentaje por pregunta
   for r in resultados:
      r.porcentaje_pregunta=round((r.puntos/r.maxima_nota_factor)*100)
      r.save()


   resultado_total=0
   encabezado_nota_total_final=0
   for lf in listado_factores:
      nota_por_factor=detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado_id,factor_id=lf)[0]
      print(lf,nota_por_factor.nota_total_final)
      resultado_total=resultado_total + nota_por_factor.valor_total_factor
      encabezado_nota_total_final=encabezado_nota_total_final + nota_por_factor.nota_total_final
   evaluacion.nota_total=resultado_total
   evaluacion.nota_total_porcentaje= round(encabezado_nota_total_final)
   evaluacion.save()
   print("este es el final",encabezado_nota_total_final)
 
   evaluacion.nota_total_porcentaje_sinpeso= round((evaluacion.nota_total/evaluacion.nota_maxima)*100)
   evaluacion.save()

   texto_clasificacion=calcular_clasificacion_factor(evaluacion.nota_total_porcentaje,evaluacion.periodicidad.id,evaluacion.id)
   evaluacion.nivel_resultado=texto_clasificacion
   evaluacion.save()

   calcular_matriz_marcas_evaluacion_factor(evaluacion.id)

   


   return 1


def calcular_nota_competencia(nota,periodocidad):


   clasificacion=evaluacion_metrica_competencia.objects.filter(periodicidad_id=periodocidad)
   valor=0
   for c in clasificacion:
      if  nota >= c.valor_minimo and nota<= c.valor_maximo:
         valor=c.valor_porcentual
   return valor



def calculo_calificacion_competencia(encabezado_id):
   #promediar puntos de respuetas por competencia

   pregunta_x_competencia= list(detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id).values_list('evaluacion_plantilla_competencia__competencia__id').distinct())
   preguntas=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id)
   #llenar datos de configuracion para calculos
   #print(preguntas.values())
   for preg in preguntas:
    
      
      #print(preg)
      if preg.peso is None:
         #print("entro")
         preg.peso=preg.evaluacion_plantilla_competencia.competencia.peso
         preg.puntos=preg.metrica_competencia.valor_porcentual
         preg.grado=preg.metrica_competencia.grado
         preg.save()
      else:
         preg.puntos=preg.metrica_competencia.valor_porcentual
         preg.grado=preg.metrica_competencia.grado
         preg.save()

      if preg.desempeno_esperado is None:
         preg.desempeno_esperado=preg.evaluacion_plantilla_competencia.competencia.desempeno_esperado
         preg.save()

   for x in pregunta_x_competencia:
     #calculo media por competencia en campo resultado
      respuestas=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id,evaluacion_plantilla_competencia__competencia_id=x)
      resultado=0
      for y in respuestas:
         resultado=y.puntos + resultado
      #rt=round(resultado/respuestas.count())
      rt=Decimal(resultado/respuestas.count()).quantize(0, ROUND_HALF_UP)

      detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id,evaluacion_plantilla_competencia__competencia_id=x).update(resultado=rt)
      #calculo calificaicon final por competencia segun peso
   for y in pregunta_x_competencia:
      respuestas_por_competencias=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id,evaluacion_plantilla_competencia__competencia_id=y)
      nota_competencia=0
      for x in respuestas_por_competencias:
         nota_competencia=x.resultado + nota_competencia
      #nota_competencia=round(nota_competencia/respuestas_por_competencias.count())
      nota_competencia=Decimal(nota_competencia/respuestas_por_competencias.count()).quantize(0, ROUND_HALF_UP)
      detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id,evaluacion_plantilla_competencia__competencia_id=y).update(nota_competencia=nota_competencia)   
      
   preguntas=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id)
   for preg in preguntas:

      print('preg',preg)
      print('preg.peso',preg.peso)
      print('preg.resultado',preg.resultado)
      nivel=calcular_nota_competencia(preg.resultado,preg.evaluacion_plantilla_competencia.periodicidad.id)
      pregunta1=nivel/100
      print('nivel',pregunta1)
      pregunta2=preg.peso*pregunta1
      print('puntos segun peso',pregunta2)
      #preg.nota_total_competencia=round(pregunta2)
      preg.nota_total_competencia=Decimal(pregunta2).quantize(0, ROUND_HALF_UP)
      preg.save()
   
   # for preg in preguntas:
   #    preg.nota_total_competencia=round(preg.peso*(preg.resultado/100))
   #    preg.save()

   nota_por_preguntas= detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id).values("evaluacion_plantilla_competencia__competencia_id","nota_competencia","nota_total_competencia").distinct()
   nota_evaluacion=0
   for f in nota_por_preguntas:
      nota_evaluacion=nota_evaluacion+f["nota_competencia"]
      print(nota_evaluacion)
   nota_evaluacion
   nota_evaluacion=nota_evaluacion/nota_por_preguntas.count()
     
   encabezado=evaluacion_encabezado.objects.get(id=encabezado_id)
   
   clasificacion=evaluacion_metrica_competencia.objects.filter(periodicidad_id=encabezado.periodicidad.id)
   nota_total_porcentaje=0
   for f in nota_por_preguntas:
      nota_total_porcentaje=nota_total_porcentaje+f["nota_total_competencia"]


   
   texto_clasificacion=''
   for c in clasificacion:
      print('nota_evaluacion',nota_evaluacion)
      print('c.valor_minimo',c.valor_minimo)
      print('c.valor_maximo',c.valor_maximo)
      if nota_total_porcentaje >= c.valor_minimo and nota_total_porcentaje<= c.valor_maximo: # si n está en el rango 5 - 10*
         print('c.descripcionc.descripcion',c.descripcion)
         texto_clasificacion=c.descripcion
         print('texto_clasificacion21',texto_clasificacion)

   print('texto_clasificacion12',texto_clasificacion)
   evaluacion_encabezado.objects.filter(id=encabezado_id).update(nota_total=nota_evaluacion,nota_maxima=100,nota_total_porcentaje=nota_total_porcentaje,nivel_resultado=texto_clasificacion)
  

  #inicio prorateo
   evaluacion_prorateo=evaluacion_encabezado.objects.get(id=encabezado_id)
   td=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id)
   td_competencias=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id).values('peso','evaluacion_plantilla_competencia__competencia__competencia__id').distinct()
   total_evaluacion_competencias=0
   for x in td_competencias:
      print(x)
      total_evaluacion_competencias=total_evaluacion_competencias+x['peso']
   
      print(x['peso'])
   print('nota final final',total_evaluacion_competencias)   
   print('evaluacion',evaluacion_prorateo.nota_total_porcentaje)
   nota_evaluacion_real=(evaluacion_prorateo.nota_total_porcentaje/total_evaluacion_competencias)*100
   print('nueva nota',round(nota_evaluacion_real,1))

   for preguntax in td :
      nuevo_peso=(preguntax.nota_total_competencia/evaluacion_prorateo.nota_total_porcentaje)*100
 
      print('nuevo_peso',nuevo_peso)
      print('viejo_peso',preguntax.peso)
      relacion_porcentual_nota_competencia=preguntax.nota_total_competencia/preguntax.peso
      print('relacion_procentual',relacion_porcentual_nota_competencia)
      nueva_nota_competencia=nuevo_peso*relacion_porcentual_nota_competencia
      preguntax.nota_total_competencia_prorateada_decimal=round(nueva_nota_competencia,1)
      preguntax.nota_total_competencia_prorateada_decimal=round(nueva_nota_competencia,1)
      preguntax.peso_prorateado=Decimal(nuevo_peso).quantize(0, ROUND_HALF_UP)
      preguntax.peso_prorateado_decimal=round(nuevo_peso,1)
      preguntax.save()
      print('viejo:'+str(preguntax.nota_total_competencia),'nuevo:'+str(nueva_nota_competencia))

   td_competencias=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id).values('nota_total_competencia_prorateada_decimal','evaluacion_plantilla_competencia__competencia__competencia__id').distinct()
   nuevo_resultado=0
   for x in td_competencias:
      print(x)
      nuevo_resultado=nuevo_resultado + x['nota_total_competencia_prorateada_decimal']

   evaluacion_prorateo.nota_total_porcentaje_prorateo_decimal=nuevo_resultado
   evaluacion_prorateo.nota_total_porcentaje_prorateo=Decimal(nuevo_resultado).quantize(0,ROUND_HALF_UP)
   evaluacion_prorateo.save()
   texto_clasificacion=''
   for c in clasificacion:
      print('nota_evaluacion',nota_evaluacion)
      print('c.valor_minimo',c.valor_minimo)
      print('c.valor_maximo',c.valor_maximo)
      if nuevo_resultado >= c.valor_minimo and nuevo_resultado<= c.valor_maximo: # si n está en el rango 5 - 10*
         print('c.descripcionc.descripcion',c.descripcion)
         texto_clasificacion=c.descripcion
         print('texto_clasificacion21',texto_clasificacion)
   evaluacion_prorateo.nivel_resultado=texto_clasificacion
   evaluacion_prorateo.save()
   
   preguntas=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_id)
   for preg in preguntas:


      nivel=calcular_nota_competencia(preg.resultado,preg.evaluacion_plantilla_competencia.periodicidad.id)
      pregunta1=nivel/100
      pregunta2=preg.peso_prorateado_decimal*Decimal(pregunta1)
      print('puntos segun peso',pregunta2)
      #preg.nota_total_competencia=round(pregunta2)
      preg.nota_total_competencia_prorateada_decimal=round(pregunta2,1)
      preg.nota_total_competencia_prorateada=Decimal(pregunta2).quantize(0, ROUND_HALF_UP)
      preg.nota_competencia_prorateada_decimal=Decimal((preg.nota_total_competencia_prorateada_decimal/preg.peso_prorateado_decimal)*100).quantize(0, ROUND_HALF_UP)
      preg.save()




   return 1





def calcular_clasificacion_factor(nota,periodicidad,encabezado):

   conteo_preguntas = detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado)


   metricas=evaluacion_metrica_factor.objects.filter(periodicidad=periodicidad).order_by('puntos')
   rangos=[]
   conteo=0
   for metrica in metricas:
      if conteo==0:
         minimo=0
         maximo=((metrica.puntos*conteo_preguntas.count())+1)
         rangos.append({'id':metrica.id,'puntos':metrica.puntos,'minimo':minimo,"maximo":maximo})
         conteo+=1
      else:
         minimo=(((metrica.puntos-1)*conteo_preguntas.count())+1)
         maximo=((metrica.puntos*conteo_preguntas.count())+1)
         rangos.append({'id':metrica.id,'puntos':metrica.puntos,'minimo':minimo,"maximo":maximo})

   categoria=""
   for rango in rangos:
      if nota in range(rango['minimo'],rango['maximo'])  :
         cat=evaluacion_metrica_factor.objects.get(id=rango['id'])
         categoria=cat.descripcion
   return categoria


def calcular_clasificacion_competencia(nota,periodocidad):


   clasificacion=evaluacion_metrica_competencia.objects.filter(periodicidad_id=periodocidad)
   texto_clasificacion=''
   for c in clasificacion:
      if nota in range(c.valor_minimo, c.valor_maximo): # si n está en el rango 5 - 10*
         texto_clasificacion=c.descripcion
   return texto_clasificacion

def  calcular_matriz_marcas_evaluacion_factor(encabezado):


   matriz=[]
   matriz_resultado=[]
   encabezado=evaluacion_encabezado.objects.get(id=encabezado)
   metricas=evaluacion_metrica_factor.objects.filter(periodicidad_id=encabezado.periodicidad.id).order_by("puntos")
   for x in metricas:
      matriz.append({"nombre":x.nombre,"puntos":x.puntos,"id":x.id})
   factores=detalle_evaluacion_factor.objects.filter(encabezado_id=encabezado.id).values_list("factor_id",flat=True)
   factores_lista=evaluacion_factor.objects.filter(periodicidad_id=encabezado.periodicidad.id,id__in=factores)
   metrica=evaluacion_metrica_factor.objects.filter(periodicidad_id=encabezado.periodicidad.id)
   #print(factores_lista.values('id','peso','tipo_factor','periodicidad'))
   #print(metrica.values('id','nombre','valor_minimo','valor_maximo','valor_porcentual','grado'))
   for f in factores_lista:
      objeto={}
      objeto["factor"]=f.nombre
      for m in metrica:
         respuesta=detalle_evaluacion_factor.objects.filter(factor_id=f.id,encabezado_id=encabezado.id,metrica_factor_id=m.id)
         objeto[m.nombre]=respuesta.count() if respuesta else 0
      
      matriz_resultado.append(objeto)
 
   

   return matriz_resultado