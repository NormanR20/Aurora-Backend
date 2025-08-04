from decimal import MIN_EMIN
from distutils.cygwinccompiler import Mingw32CCompiler
from email import message
from django.db.models.functions import Concat
from email.policy import HTTP
from django.db.models import Value
from urllib import response
from django.db.models.functions import ExtractYear
import ast
from itertools import chain
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
from django.db.models import CharField, ExpressionWrapper, F,Avg
from .views_calculos_evaluaciones import *
import random
from django.db.models.functions import Cast

class categoria_desempenoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = categoria_desempeno.objects.all()
    serializer_class = categoria_desempenoserializer
    def list(self, request):

        queryset = categoria_desempeno.objects.all()
        serializer_class = categoria_desempenoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')


        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='valor_minimo':
                        filter_kwargs['valor_minimo'] = filter
                    if tipo_busqueda =='valor_maximo':
                        filter_kwargs['valor_maximo'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                    if tipo_busqueda =='filtrado_empresa_y_periodicidad':
                        filtro=json.loads(filter)
                              
                        filter_kwargs['periodicidad_id'] = filtro['periodicidad_id']
                        filter_kwargs['periodicidad__empresa_id'] = filtro['periodicidad__empresa_id']
                    
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad_id'] = filter
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='descripcion':
                            filter_kwargs_2['descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='valor_minimo':
                            filter_kwargs_2['valor_minimo'] = filter_2
                        if tipo_busqueda_2 =='valor_maximo':
                            filter_kwargs_2['valor_maximo'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__date__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_actualizacion':
                            filter_kwargs_2['fecha_actualizacion__icontains'] = filter_2
                        if tipo_busqueda_2 =='filtrado_empresa_y_periodicidad':
                            filtro=json.loads(filter_2)
                                
                            filter_kwargs_2['periodicidad_id'] = filtro['periodicidad_id']
                            filter_kwargs_2['periodicidad__empresa_id'] = filtro['periodicidad__empresa_id']
                        
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad_id'] = filter_2
                            
                    queryset =  categoria_desempeno.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  categoria_desempeno.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = categoria_desempenoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  categoria_desempeno.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  categoria_desempeno.objects.filter(**filter_kwargs).count()
                    serializer = categoria_desempenoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

                queryset =  categoria_desempeno.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  categoria_desempeno.objects.filter(**filter_kwargs).count()
                serializer = categoria_desempenoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='valor_minimo':
                        filter_kwargs['valor_minimo'] = filter
                    if tipo_busqueda =='valor_maximo':
                        filter_kwargs['valor_maximo'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                    if tipo_busqueda =='filtrado_empresa_y_periodicidad':
                        filtro=json.loads(filter)
                              
                        filter_kwargs['periodicidad_id'] = filtro['periodicidad_id']
                        filter_kwargs['periodicidad__empresa_id'] = filtro['periodicidad__empresa_id']
                    
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad_id'] = filter
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='descripcion':
                            filter_kwargs_2['descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='valor_minimo':
                            filter_kwargs_2['valor_minimo'] = filter_2
                        if tipo_busqueda_2 =='valor_maximo':
                            filter_kwargs_2['valor_maximo'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__date__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_actualizacion':
                            filter_kwargs_2['fecha_actualizacion__icontains'] = filter_2
                        if tipo_busqueda_2 =='filtrado_empresa_y_periodicidad':
                            filtro=json.loads(filter_2)
                                
                            filter_kwargs_2['periodicidad_id'] = filtro['periodicidad_id']
                            filter_kwargs_2['periodicidad__empresa_id'] = filtro['periodicidad__empresa_id']
                        
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad_id'] = filter_2
                            
                    queryset =  categoria_desempeno.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  categoria_desempeno.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = categoria_desempenoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  categoria_desempeno.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  categoria_desempeno.objects.filter(**filter_kwargs).count()
                    serializer = categoria_desempenoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
                    

                queryset =  categoria_desempeno.objects.filter(**filter_kwargs).order_by('id')
                conteo =  categoria_desempeno.objects.filter(**filter_kwargs).count()
                serializer = categoria_desempenoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})

    def create(self, request):
        serializer = categoria_desempenoserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= categoria_desempeno.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= categoria_desempenoserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,request, pk):
        # validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(periodicidad=eliminar.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(periodicidad=eliminar.periodicidad.pk) else none
        # validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(periodicidad=eliminar.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(periodicidad=eliminar.periodicidad.pk) else None 
        # #print('435435354354',validacion_periodicidad_competencia)
        # #print('435435354354',validacion_periodicidad_factor)

        
        area = categoria_desempeno.objects.filter(pk=pk).values() if categoria_desempeno.objects.filter(pk=pk) else None

        
        if area:
            categoria = categoria_desempeno.objects.get(pk=pk)
            if categoria.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=categoria.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=categoria.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=categoria.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=categoria.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = categoria_desempeno.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)


        




class evaluacion_frecuenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_frecuencia.objects.all()
    serializer_class = evaluacion_frecuenciaserializer
    def list(self, request):
        queryset = evaluacion_frecuencia.objects.all()
        serializer_class = evaluacion_frecuenciaserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                        
                queryset =  evaluacion_frecuencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_frecuencia.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_frecuenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_frecuencia.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  evaluacion_frecuencia.objects.filter().count()
                serializer = evaluacion_frecuenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter

                        
                queryset =  evaluacion_frecuencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_frecuencia.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_frecuenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_frecuencia.objects.filter().order_by('id')
                conteo =  evaluacion_frecuencia.objects.filter().count()
                serializer = evaluacion_frecuenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = evaluacion_frecuenciaserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_frecuencia.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_frecuenciaserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class evaluacion_tipo_plan_accionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_tipo_plan_accion.objects.all()
    serializer_class = evaluacion_tipo_plan_accionserializer
    def list(self, request):
        queryset = evaluacion_tipo_plan_accion.objects.all()
        serializer_class = evaluacion_tipo_plan_accionserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                        
                queryset =  evaluacion_tipo_plan_accion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_tipo_plan_accion.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_tipo_plan_accionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_tipo_plan_accion.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  evaluacion_tipo_plan_accion.objects.filter().count()
                serializer = evaluacion_tipo_plan_accionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter

                        
                queryset =  evaluacion_tipo_plan_accion.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_tipo_plan_accion.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_tipo_plan_accionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_tipo_plan_accion.objects.filter().order_by('id')
                conteo =  evaluacion_tipo_plan_accion.objects.filter().count()
                serializer = evaluacion_tipo_plan_accionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = evaluacion_tipo_plan_accionserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_tipo_plan_accion.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_tipo_plan_accionserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class evaluacion_tipo_evaluacionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_tipo_evaluacion.objects.all()
    serializer_class = evaluacion_tipo_evaluacionserializer
    def list(self, request):
        queryset = evaluacion_tipo_evaluacion.objects.all()
        serializer_class = evaluacion_tipo_evaluacionserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                        
                queryset =  evaluacion_tipo_evaluacion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_tipo_evaluacion.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_tipo_evaluacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_tipo_evaluacion.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  evaluacion_tipo_evaluacion.objects.filter().count()
                serializer =evaluacion_tipo_evaluacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter

                        
                queryset =  evaluacion_tipo_evaluacion.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_tipo_evaluacion.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_tipo_evaluacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_tipo_evaluacion.objects.filter().order_by('id')
                conteo =  evaluacion_tipo_evaluacion.objects.filter().count()
                serializer = evaluacion_tipo_evaluacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = evaluacion_tipo_evaluacionserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_tipo_evaluacionserializer.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_tipo_evaluacionserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class evaluacion_competenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_competencia.objects.all()
    serializer_class = evaluacion_competenciaserializer
    def list(self, request):
        queryset = evaluacion_competencia.objects.all()
        serializer_class = evaluacion_competenciaserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')

        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='competencia__id':
                        filter_kwargs['competencia__id'] = filter
                    if tipo_busqueda =='competencia__nombre':
                        filter_kwargs['competencia__nombre__icontains'] = filter
                    if tipo_busqueda =='competencia__descripcion':
                        filter_kwargs['competencia__descripcion__icontains'] = filter
                    if tipo_busqueda =='clasificacion_id':
                        filter_kwargs['clasificacion_id'] = filter
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad'] = filter
                        
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='competencia__id':
                            filter_kwargs_2['competencia__id'] = filter_2
                        if tipo_busqueda_2 =='competencia__nombre':
                            filter_kwargs_2['competencia__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='competencia__descripcion':
                            filter_kwargs_2['competencia__descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='clasificacion_id':
                            filter_kwargs_2['clasificacion_id'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad'] = filter_2   

                    queryset =  evaluacion_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_competencia.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})      

                queryset =  evaluacion_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_competencia.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='competencia__id':
                        filter_kwargs['competencia__id'] = filter
                    if tipo_busqueda =='competencia__nombre':
                        filter_kwargs['competencia__nombre__icontains'] = filter
                    if tipo_busqueda =='competencia__descripcion':
                        filter_kwargs['competencia__descripcion__icontains'] = filter
                    if tipo_busqueda =='clasificacion_id':
                        filter_kwargs['clasificacion_id'] = filter
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad'] = filter
                        
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='competencia__id':
                            filter_kwargs_2['competencia__id'] = filter_2
                        if tipo_busqueda_2 =='competencia__nombre':
                            filter_kwargs_2['competencia__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='competencia__descripcion':
                            filter_kwargs_2['competencia__descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='clasificacion_id':
                            filter_kwargs_2['clasificacion_id'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad'] = filter_2   
                            

                    queryset =  evaluacion_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_competencia.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  evaluacion_competencia.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})        

                queryset =  evaluacion_competencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_competencia.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})
        

        # filter=''
        # tipo_busqueda=''
        # if self.request.query_params.get('filter'):
        #         filter = self.request.query_params.get('filter')


        # if self.request.query_params.get('tipo_busqueda'):
        #     tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        # if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
        #     offset=int(self.request.query_params.get('offset'))
        #     limit=int(self.request.query_params.get('limit'))

        #     if filter!='' and tipo_busqueda!='':
        #         filter_kwargs={}
        #         if tipo_busqueda:
        #             if tipo_busqueda =='id':
        #                 filter_kwargs['id'] = filter
        #             if tipo_busqueda =='competencia__id':
        #                 filter_kwargs['competencia__id'] = filter
        #             if tipo_busqueda =='competencia__nombre':
        #                 filter_kwargs['competencia__nombre__icontains'] = filter
        #             if tipo_busqueda =='competencia__descripcion':
        #                 filter_kwargs['competencia__descripcion__icontains'] = filter
        #             if tipo_busqueda =='clasificacion_id':
        #                 filter_kwargs['clasificacion_id'] = filter
                    
                    

                        
        #         queryset =  evaluacion_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
        #         conteo =  evaluacion_competencia.objects.filter(**filter_kwargs).count()
        #         serializer = evaluacion_competenciaserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":conteo}) 
        #     else: 
        #         queryset =  evaluacion_competencia.objects.filter().order_by('id')[offset:offset+limit]
        #         conteo =  evaluacion_competencia.objects.filter().count()
        #         serializer = evaluacion_competenciaserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":conteo})
        # else:
        #     if filter!='' and tipo_busqueda!='':
        #         filter_kwargs={}
        #         if tipo_busqueda:
        #             if tipo_busqueda =='id':
        #                 filter_kwargs['id'] = filter
        #             if tipo_busqueda =='competencia__id':
        #                 filter_kwargs['competencia__id'] = filter
        #             if tipo_busqueda =='competencia__nombre':
        #                 filter_kwargs['competencia__nombre__icontains'] = filter
        #             if tipo_busqueda =='competencia__descripcion':
        #                 filter_kwargs['competencia__descripcion__icontains'] = filter
        #             if tipo_busqueda =='clasificacion_id':
        #                 filter_kwargs['clasificacion_id'] = filter

        #         queryset =  evaluacion_competencia.objects.filter(**filter_kwargs).order_by('id')
        #         conteo =  evaluacion_competencia.objects.filter(**filter_kwargs).count()
        #         serializer = evaluacion_competenciaserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":conteo}) 
        #     else: 
        #         queryset =  evaluacion_competencia.objects.filter().order_by('id')
        #         conteo =  evaluacion_competencia.objects.filter().count()
        #         serializer = evaluacion_competenciaserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = evaluacion_competenciaserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_competencia.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_competenciaserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,request,pk):

        
        area = evaluacion_competencia.objects.filter(pk=pk).values() if evaluacion_competencia.objects.filter(pk=pk) else None

        
        if area:
            competencia= evaluacion_competencia.objects.get(pk=pk)
            if competencia.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=competencia.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=competencia.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=competencia.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=competencia.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_competencia.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)




class evaluacion_metrica_competenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_metrica_competencia.objects.all()
    serializer_class = evaluacion_metrica_competenciaserializer
    def list(self, request):
        queryset = evaluacion_metrica_competencia.objects.all()
        serializer_class = evaluacion_metrica_competenciaserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')


        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='valor_minimo':
                        filter_kwargs['valor_minimo'] = filter
                    if tipo_busqueda =='valor_maximo':
                        filter_kwargs['valor_maximo'] = filter
                    if tipo_busqueda =='valor_porcentual':
                        filter_kwargs['valor_porcentual'] = filter
                    if tipo_busqueda =='grado':
                        filter_kwargs['grado__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__icontains'] = filter
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad'] = filter
                    if tipo_busqueda =='periodicidad_empresa_nombre':
                        filter_kwargs['periodicidad__empresa__nombre'] = filter
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='descripcion':
                            filter_kwargs_2['descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='valor_minimo':
                            filter_kwargs_2['valor_minimo'] = filter_2
                        if tipo_busqueda_2 =='valor_maximo':
                            filter_kwargs_2['valor_maximo'] = filter_2
                        if tipo_busqueda_2 =='valor_porcentual':
                            filter_kwargs_2['valor_porcentual'] = filter_2
                        if tipo_busqueda_2 =='grado':
                            filter_kwargs_2['grado__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre'] = filter_2
                    queryset =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_metrica_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_metrica_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                        
                queryset =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_metrica_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='valor_minimo':
                        filter_kwargs['valor_minimo'] = filter
                    if tipo_busqueda =='valor_maximo':
                        filter_kwargs['valor_maximo'] = filter
                    if tipo_busqueda =='valor_porcentual':
                        filter_kwargs['valor_porcentual'] = filter
                    if tipo_busqueda =='grado':
                        filter_kwargs['grado__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__icontains'] = filter
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad'] = filter
                    if tipo_busqueda =='periodicidad_empresa_nombre':
                        filter_kwargs['periodicidad__empresa__nombre'] = filter
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='descripcion':
                            filter_kwargs_2['descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='valor_minimo':
                            filter_kwargs_2['valor_minimo'] = filter_2
                        if tipo_busqueda_2 =='valor_maximo':
                            filter_kwargs_2['valor_maximo'] = filter_2
                        if tipo_busqueda_2 =='valor_porcentual':
                            filter_kwargs_2['valor_porcentual'] = filter_2
                        if tipo_busqueda_2 =='grado':
                            filter_kwargs_2['grado__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre'] = filter_2
                    queryset =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_metrica_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_metrica_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})                  
                queryset =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_metrica_competencia.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_metrica_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})

    def create(self, request):
        serializer = evaluacion_metrica_competenciaserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_metrica_competencia.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_metrica_competenciaserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,request,pk):
        
        area = evaluacion_metrica_competencia.objects.filter(pk=pk).values() if evaluacion_metrica_competencia.objects.filter(pk=pk) else None

        
        if area:
            metrica_competencia= evaluacion_metrica_competencia.objects.get(pk=pk)
            if metrica_competencia.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=metrica_competencia.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=metrica_competencia.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=metrica_competencia.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=metrica_competencia.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_metrica_competencia.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)






class evaluacion_factorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_factor.objects.all()
    serializer_class = evaluacion_factorserializer
    def list(self, request):
        queryset = evaluacion_factor.objects.all()
        serializer_class = evaluacion_factorserializer(queryset, many=True)
        
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        filter_3=''
        tipo_busqueda_3=''
        if self.request.query_params.get('filter_3'):
            filter_3 = self.request.query_params.get('filter_3')
        
        if self.request.query_params.get('tipo_busqueda_3'):
            tipo_busqueda_3 = self.request.query_params.get('tipo_busqueda_3')

        if self.request.query_params.get('filter_2'):
            filter_2 = self.request.query_params.get('filter_2')
        
        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')
        
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='clasificacion':
                        filter_kwargs['clasificacion'] = filter
                    if tipo_busqueda =='periodicidad':
                        filter_kwargs['periodicidad'] = filter
                    
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='clasificacion':
                            filter_kwargs_2['clasificacion'] = filter_2
                        if tipo_busqueda_2 =='periodicidad':
                            filter_kwargs_2['periodicidad'] = filter_2
                
                        
                    if filter_3!='' and tipo_busqueda_3!='':
                        filter_kwargs_3={}
                        if tipo_busqueda_3:
                            if tipo_busqueda_3 =='id':
                                filter_kwargs_3['id'] = filter_3
                            if tipo_busqueda_3 =='nombre':
                                filter_kwargs_3['nombre__icontains'] = filter_3
                            if tipo_busqueda_3 =='clasificacion':
                                filter_kwargs_3['clasificacion'] = filter_3
                            if tipo_busqueda_3 =='periodicidad':
                                filter_kwargs_3['periodicidad'] = filter_3


                        queryset =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).filter(**filter_kwargs_3).order_by('id')[offset:offset+limit]
                        conteo =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).filter(**filter_kwargs_3).count()
                        serializer = evaluacion_factorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo}) 
                    else:
                        queryset =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                        conteo =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                        serializer = evaluacion_factorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})  
                        

                    queryset =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    # queryset =  evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    # conteo =  evaluacion_factor.objects.filter().count()
                    # serializer = evaluacion_factorserializer(queryset, many=True)
                    # return Response({"data":serializer.data,"count":conteo})
                    return Response({"data":[],"count":0})
                                               
                queryset =  evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_factor.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                # queryset =  evaluacion_factor.objects.filter().order_by('id')[offset:offset+limit]
                # conteo =  evaluacion_factor.objects.filter().count()
                # serializer = evaluacion_factorserializer(queryset, many=True)
                # return Response({"data":serializer.data,"count":conteo})
                return Response({"data":[],"count":0})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='clasificacion':
                        filter_kwargs['clasificacion'] = filter
                    if tipo_busqueda =='periodicidad':
                        filter_kwargs['periodicidad'] = filter

                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='clasificacion':
                            filter_kwargs_2['clasificacion'] = filter_2
                        if tipo_busqueda_2 =='periodicidad':
                            filter_kwargs_2['periodicidad'] = filter_2

                    if filter_3!='' and tipo_busqueda_3!='':
                        filter_kwargs_3={}
                        if tipo_busqueda_3:
                            if tipo_busqueda_3 =='id':
                                filter_kwargs_3['id'] = filter_3
                            if tipo_busqueda_3 =='nombre':
                                filter_kwargs_3['nombre__icontains'] = filter_3
                            if tipo_busqueda_3 =='clasificacion':
                                filter_kwargs_3['clasificacion'] = filter_3
                            if tipo_busqueda_3 =='periodicidad':
                                filter_kwargs_3['periodicidad'] = filter_3


                        queryset =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).filter(**filter_kwargs_3).order_by('id')
                        conteo =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).filter(**filter_kwargs_3).count()
                        serializer = evaluacion_factorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})  
                    else: 
                        queryset =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                        conteo =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                        serializer = evaluacion_factorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})

                        
                    queryset =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    # queryset =  evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')
                    # conteo =  evaluacion_factor.objects.filter().count()
                    # serializer = evaluacion_factorserializer(queryset, many=True)
                    return Response({"data":[],"count":0})
                    # return Response({"El filtro por clasificacion y por periodicidad es obligatorio"},status=status.HTTP_400_BAD_REQUEST)

                queryset =  evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')
                serializer = evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                # queryset =  evaluacion_factor.objects.filter().order_by('id')
                # serializer = evaluacion_factorserializer(queryset, many=True)
                return Response({"data":[],"count":0})

        
        
        
        # filter=''
        # tipo_busqueda=''
        # if self.request.query_params.get('filter'):
        #         filter = self.request.query_params.get('filter')


        # if self.request.query_params.get('tipo_busqueda'):
        #     tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        # #################################################################
        # filter_2=''
        # tipo_busqueda_2=''
        # if self.request.query_params.get('filter_2'):
        #         filter_2 = self.request.query_params.get('filter_2')


        # if self.request.query_params.get('tipo_busqueda_2'):
        #     tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')
        # #################################################################


        # if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
        #     offset=int(self.request.query_params.get('offset'))
        #     limit=int(self.request.query_params.get('limit'))

        #     if filter!='' and tipo_busqueda!='':
        #         filter_kwargs={}
        #         if tipo_busqueda:
        #             if tipo_busqueda =='id':
        #                 filter_kwargs['id'] = filter
        #             if tipo_busqueda =='nombre':
        #                 filter_kwargs['nombre__icontains'] = filter
        #             if tipo_busqueda =='clasificacion':
        #                 filter_kwargs['clasificacion'] = filter
        #             if tipo_busqueda =='periodicidad':
        #                 filter_kwargs['periodicidad'] = filter

        #         if filter_2!='' and tipo_busqueda_2!='':
        #             filter_kwargs_2={}
        #             if tipo_busqueda_2:
        #                 if tipo_busqueda_2 =='id':
        #                     filter_kwargs_2['id'] = filter_2
        #                 if tipo_busqueda_2 =='nombre':
        #                     filter_kwargs_2['nombre__icontains'] = filter_2
        #                 if tipo_busqueda_2 =='clasificacion':
        #                     filter_kwargs_2['clasificacion'] = filter_2
        #                 if tipo_busqueda_2 =='periodicidad':
        #                     filter_kwargs_2['periodicidad'] = filter_2

        #             queryset =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
        #             serializer = evaluacion_factorserializer(queryset, many=True)
        #             conteo =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
        #             return Response({"data":serializer.data,"count":conteo})

        #         queryset =  evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
        #         serializer = evaluacion_factorserializer(queryset, many=True)
        #         conteo =  evaluacion_factor.objects.filter(**filter_kwargs).count()
        #         return Response({"data":serializer.data,"count":conteo}) 
        #     else: 
        #         queryset =  evaluacion_factor.objects.filter().order_by('id')[offset:offset+limit]
        #         conteo =  evaluacion_factor.objects.filter().count()
        #         serializer = evaluacion_factorserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":conteo})
        # else:
        #     if filter!='' and tipo_busqueda!='':
        #         filter_kwargs={}
        #         if tipo_busqueda:
        #             if tipo_busqueda =='id':
        #                 filter_kwargs['id'] = filter
        #             if tipo_busqueda =='nombre':
        #                 filter_kwargs['nombre__icontains'] = filter
        #             if tipo_busqueda =='clasificacion':
        #                 filter_kwargs['clasificacion'] = filter
        #             if tipo_busqueda =='periodicidad':
        #                 filter_kwargs['periodicidad'] = filter
                
        #         if filter_2!='' and tipo_busqueda_2!='':
        #             filter_kwargs_2={}
        #             if tipo_busqueda_2:
        #                 if tipo_busqueda_2 =='id':
        #                     filter_kwargs_2['id'] = filter_2
        #                 if tipo_busqueda_2 =='nombre':
        #                     filter_kwargs_2['nombre__icontains'] = filter_2
        #                 if tipo_busqueda_2 =='clasificacion':
        #                     filter_kwargs_2['clasificacion'] = filter_2
        #                 if tipo_busqueda_2 =='periodicidad':
        #                     filter_kwargs_2['periodicidad'] = filter_2

        #             queryset =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
        #             serializer = evaluacion_factorserializer(queryset, many=True)
        #             conteo =  evaluacion_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
        #             return Response({"data":serializer.data,"count":conteo})

        #         queryset =  evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')
        #         conteo =  evaluacion_factor.objects.filter(**filter_kwargs).count()
        #         serializer = evaluacion_factorserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":conteo}) 
        #     else: 
        #         queryset =  evaluacion_factor.objects.filter().order_by('id')
        #         conteo =  evaluacion_factor.objects.filter().count()
        #         serializer = evaluacion_factorserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = evaluacion_factorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_factor.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_factorserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,request,pk):

        area = evaluacion_factor.objects.filter(pk=pk).values() if evaluacion_factor.objects.filter(pk=pk) else None

        
        if area:
            factor= evaluacion_factor.objects.get(pk=pk)
            if factor.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=factor.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=factor.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=factor.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=factor.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_factor.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)




class evaluacion_metrica_factorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_metrica_factor.objects.all()
    serializer_class = evaluacion_metrica_factorserializer
    def list(self, request):
        queryset = evaluacion_metrica_factor.objects.all()
        serializer_class = evaluacion_metrica_factorserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')


        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='factor':
                        filter_kwargs['factor'] = filter
                    if tipo_busqueda =='puntos':
                        filter_kwargs['puntos'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad'] = filter
                    if tipo_busqueda =='periodicidad_empresa_nombre':
                        filter_kwargs['periodicidad__empresa__nombre'] = filter
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='factor':
                            filter_kwargs_2['factor'] = filter_2
                        if tipo_busqueda_2 =='puntos':
                            filter_kwargs_2['puntos'] = filter_2
                        if tipo_busqueda_2 =='descripcion':
                            filter_kwargs_2['descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_actualizacion':
                            filter_kwargs_2['fecha_actualizacion__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre'] = filter_2

                    queryset =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_metrica_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_metrica_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})      

                queryset =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_metrica_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='factor':
                        filter_kwargs['factor'] = filter
                    if tipo_busqueda =='puntos':
                        filter_kwargs['puntos'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='factor':
                            filter_kwargs_2['factor'] = filter_2
                        if tipo_busqueda_2 =='puntos':
                            filter_kwargs_2['puntos'] = filter_2
                        if tipo_busqueda_2 =='descripcion':
                            filter_kwargs_2['descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_actualizacion':
                            filter_kwargs_2['fecha_actualizacion__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre'] = filter_2

                    queryset =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_metrica_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_metrica_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})        

                queryset =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_metrica_factor.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_metrica_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})

    def create(self, request):
        serializer = evaluacion_metrica_factorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_metrica_factor.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_metrica_factorserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,request,pk):
        
        area = evaluacion_metrica_factor.objects.filter(pk=pk).values() if evaluacion_metrica_factor.objects.filter(pk=pk) else None

        
        if area:
            metrica_factor= evaluacion_metrica_factor.objects.get(pk=pk)
            if metrica_factor.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=metrica_factor.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=metrica_factor.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=metrica_factor.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=metrica_factor.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_metrica_factor.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)




class evaluacion_periodicidadViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_periodicidad.objects.all()
    serializer_class = evaluacion_periodicidadserializer
    def list(self, request):
        queryset = evaluacion_periodicidad.objects.all()
        serializer_class = evaluacion_periodicidadserializer(queryset, many=True)
        
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')

        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='empresa__id':
                        filter_kwargs['empresa__id'] = filter
                    if tipo_busqueda =='empresa__codigo':
                        filter_kwargs['empresa__codigo__icontains'] = filter
                    if tipo_busqueda =='empresa__nombre':
                        filter_kwargs['empresa__nombre__icontains'] = filter
                    if tipo_busqueda =='anio':
                        filter_kwargs['anio'] = filter
                    if tipo_busqueda =='frecuencia__id':
                        filter_kwargs['frecuencia__id'] = filter
                    if tipo_busqueda =='frecuencia__nombre':
                        filter_kwargs['frecuencia__nombre__icontains'] = filter
                    if tipo_busqueda =='tipo_evaluacion__id':
                        filter_kwargs['tipo_evaluacion__id'] = filter
                    if tipo_busqueda =='tipo_evaluacion__nombre':
                        filter_kwargs['tipo_evaluacion__nombre__icontains'] = filter
                        
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='empresa__id':
                            filter_kwargs_2['empresa__id'] = filter_2
                        if tipo_busqueda_2 =='empresa__codigo':
                            filter_kwargs_2['empresa__codigo__icontains'] = filter_2
                        if tipo_busqueda_2 =='empresa__nombre':
                            filter_kwargs_2['empresa__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='anio':
                            filter_kwargs_2['anio'] = filter_2
                        if tipo_busqueda_2 =='frecuencia__id':
                            filter_kwargs_2['frecuencia__id'] = filter_2
                        if tipo_busqueda_2 =='frecuencia__nombre':
                            filter_kwargs_2['frecuencia__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='tipo_evaluacion__id':
                            filter_kwargs_2['tipo_evaluacion__id'] = filter_2
                        if tipo_busqueda_2 =='tipo_evaluacion__nombre':
                            filter_kwargs_2['tipo_evaluacion__nombre__icontains'] = filter_2
                            

                    queryset =  evaluacion_periodicidad.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_periodicidad.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_periodicidadserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_periodicidad.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_periodicidad.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_periodicidadserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})      

                queryset =  evaluacion_periodicidad.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_periodicidad.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_periodicidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='empresa__id':
                        filter_kwargs['empresa__id'] = filter
                    if tipo_busqueda =='empresa__codigo':
                        filter_kwargs['empresa__codigo__icontains'] = filter
                    if tipo_busqueda =='empresa__nombre':
                        filter_kwargs['empresa__nombre__icontains'] = filter
                    if tipo_busqueda =='anio':
                        filter_kwargs['anio'] = filter
                    if tipo_busqueda =='frecuencia__id':
                        filter_kwargs['frecuencia__id'] = filter
                    if tipo_busqueda =='frecuencia__nombre':
                        filter_kwargs['frecuencia__nombre__icontains'] = filter
                    if tipo_busqueda =='tipo_evaluacion__id':
                        filter_kwargs['tipo_evaluacion__id'] = filter
                    if tipo_busqueda =='tipo_evaluacion__nombre':
                        filter_kwargs['tipo_evaluacion__nombre__icontains'] = filter
                        
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='empresa__id':
                            filter_kwargs_2['empresa__id'] = filter_2
                        if tipo_busqueda_2 =='empresa__codigo':
                            filter_kwargs_2['empresa__codigo__icontains'] = filter_2
                        if tipo_busqueda_2 =='empresa__nombre':
                            filter_kwargs_2['empresa__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='anio':
                            filter_kwargs_2['anio'] = filter_2
                        if tipo_busqueda_2 =='frecuencia__id':
                            filter_kwargs_2['frecuencia__id'] = filter_2
                        if tipo_busqueda_2 =='frecuencia__nombre':
                            filter_kwargs_2['frecuencia__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='tipo_evaluacion__id':
                            filter_kwargs_2['tipo_evaluacion__id'] = filter_2
                        if tipo_busqueda_2 =='tipo_evaluacion__nombre':
                            filter_kwargs_2['tipo_evaluacion__nombre__icontains'] = filter_2
                            

                    queryset =  evaluacion_periodicidad.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_periodicidad.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_periodicidadserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_periodicidad.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  evaluacion_periodicidad.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_periodicidadserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})        

                queryset =  evaluacion_periodicidad.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_periodicidad.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_periodicidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                lista=[]
                conteo=0
                return Response({"data":lista,"count":conteo})
        
        

    def create(self, request):
        hoy=datetime.now().date()
        serializer = evaluacion_periodicidadserializer(data=request.data)
        # validacion_empresa= evaluacion_periodicidad.objects.filter(empresa=request.data['empresa']).filter(tipo_evaluacion=request.data['tipo_evaluacion']).filter(fecha_fin__gt=hoy) if evaluacion_periodicidad.objects.filter(empresa=request.data['empresa']).filter(tipo_evaluacion=request.data['tipo_evaluacion']).filter(fecha_fin__gt=hoy) else None
        # if validacion_empresa!=None:
        #     return Response({'Ya existe otra periodicidad vigente utilizando esta empresa para este tipo de evaluación '}, status=status.HTTP_400_BAD_REQUEST)


        if serializer.is_valid(): 
            ##print("si es valido")
            serializer.save()
            #print(serializer.data['fecha_fin'])
            # if serializer.data['fecha_creacion']:
            #     resultado= datetime.strptime(serializer.data['fecha_creacion'], '%Y-%m-%d').date()
            #     #print("valor1",resultado)
            #     resultado2 = resultado + relativedelta(months=+12) 
            #     #print("valor2",resultado2)
            #     evaluacion_periodicidad.objects.filter(id=serializer.data['id']).update(fecha_fin=resultado2)

        
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def update(self,requets,pk):
        hoy=datetime.now().date()
        existe= evaluacion_periodicidad.objects.filter(id=pk).count()
        
        if existe!=0:
            put = evaluacion_periodicidad.objects.get(id=pk)
            serializer= evaluacion_periodicidadserializer(put,data=requets.data)
            # validacion_empresa= evaluacion_periodicidad.objects.filter(empresa=self.request.data['empresa']).filter(tipo_evaluacion=self.request.data['tipo_evaluacion']).filter(fecha_fin__gt=hoy) if evaluacion_periodicidad.objects.filter(empresa=self.request.data['empresa']).filter(tipo_evaluacion=self.request.data['tipo_evaluacion']).filter(fecha_fin__gt=hoy) else None
            # if validacion_empresa!=None:
            #     return Response({'Ya existe otra periodicidad vigente utilizando esta empresa para este tipo de evaluación '}, status=status.HTTP_400_BAD_REQUEST)

            if serializer.is_valid():
                serializer.save()
                #print(serializer.data['fecha_fin'])
                # if serializer.data['fecha_creacion']:
                #     resultado= datetime.strptime(serializer.data['fecha_creacion'], '%Y-%m-%d').date()
                #     #print("valor1",resultado)
                #     resultado2 = resultado + relativedelta(months=+12)
                #     #print("valor2",resultado2)
                #     evaluacion_periodicidad.objects.filter(id=serializer.data['id']).update(fecha_fin=resultado2)



                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class evaluacion_configuracion_periodoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_configuracion_periodo.objects.all()
    serializer_class = evaluacion_configuracion_periodoserializer
    def list(self, request):
        queryset = evaluacion_configuracion_periodo.objects.all()
        serializer_class = evaluacion_configuracion_periodoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='tipo_evaluacion__id':
                        filter_kwargs['tipo_evaluacion__id'] = filter
                    if tipo_busqueda =='tipo_evaluacion__nombre':
                        filter_kwargs['tipo_evaluacion__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad__id':
                        filter_kwargs['periodicidad__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__id':
                        filter_kwargs['periodicidad__empresa__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad__empresa__codigo':
                        filter_kwargs['periodicidad__empresa__codigo__icontains'] = filter

                        
                queryset =  evaluacion_configuracion_periodo.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_configuracion_periodo.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_configuracion_periodoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_configuracion_periodo.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  evaluacion_configuracion_periodo.objects.filter().count()
                serializer = evaluacion_configuracion_periodoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='tipo_evaluacion__id':
                        filter_kwargs['tipo_evaluacion__id'] = filter
                    if tipo_busqueda =='tipo_evaluacion__nombre':
                        filter_kwargs['tipo_evaluacion__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad__id':
                        filter_kwargs['periodicidad__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__id':
                        filter_kwargs['periodicidad__empresa__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad__empresa__codigo':
                        filter_kwargs['periodicidad__empresa__codigo__icontains'] = filter
                        
                queryset =  evaluacion_configuracion_periodo.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_configuracion_periodo.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_configuracion_periodoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_configuracion_periodo.objects.filter().order_by('id')
                conteo =  evaluacion_configuracion_periodo.objects.filter().count()
                serializer = evaluacion_configuracion_periodoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = evaluacion_configuracion_periodoserializer(data=request.data)
        # months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        if serializer.is_valid(): 
            serializer.save()
            periodicidad_guardada=serializer.data['periodicidad']
            configuracion_periodo_guardado=serializer.data['id']
            periodo_guardado=serializer.data['periodo']
            fecha_inicio_periodicidad=(evaluacion_periodicidad.objects.filter(id=periodicidad_guardada).values('fecha_inicio'))[0]['fecha_inicio'] if evaluacion_periodicidad.objects.filter(id=periodicidad_guardada).values('fecha_inicio') else None
            if fecha_inicio_periodicidad==None:
                return Response("La fecha de inicio no ha sido registrada en la periodicidad", status=status.HTTP_400_BAD_REQUEST)
            cantidad_periodos= (evaluacion_periodicidad.objects.filter(id=periodicidad_guardada).values('frecuencia__cantidad_meses'))[0]['frecuencia__cantidad_meses'] if evaluacion_periodicidad.objects.filter(id=periodicidad_guardada).values('frecuencia__cantidad_meses') else None
            # print('cantidad_periodos',cantidad_periodos)
            formula_fecha_inicio=(((12/cantidad_periodos)*periodo_guardado)-(12/cantidad_periodos))
            fecha_inicio_periodo=fecha_inicio_periodicidad + relativedelta(months=+formula_fecha_inicio)

            formula_fecha_fin=((12/cantidad_periodos)*periodo_guardado)
            fecha_fin_periodo=(fecha_inicio_periodicidad + relativedelta(months=+formula_fecha_fin)) - timedelta(days=1)

            evaluacion_configuracion_periodo.objects.filter(id=configuracion_periodo_guardado).update(fecha_inicio=fecha_inicio_periodo)
            evaluacion_configuracion_periodo.objects.filter(id=configuracion_periodo_guardado).update(fecha_fin=fecha_fin_periodo)


            # return Response('Hola', status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_configuracion_periodo.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_configuracion_periodoserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,request,pk):


        area = evaluacion_configuracion_periodo.objects.filter(pk=pk).values() if evaluacion_configuracion_periodo.objects.filter(pk=pk) else None

        
        if area:
            configuracion= evaluacion_configuracion_periodo.objects.get(pk=pk)
            if configuracion.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=configuracion.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=configuracion.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=configuracion.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=configuracion.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_configuracion_periodo.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)






class evaluacion_plantilla_competenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_plantilla_competencia.objects.all()
    serializer_class = evaluacion_plantilla_competenciaserializer
    def list(self, request):
       
        queryset = evaluacion_plantilla_competencia.objects.all()
        serializer_class = evaluacion_plantilla_competenciaserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')
        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='posicion_id':
                        filter_kwargs['posicion_id'] = filter
                    if tipo_busqueda =='posicion__codigo':
                        filter_kwargs['posicion__codigo__icontains'] = filter
                    if tipo_busqueda =='posicion__nombre':
                        filter_kwargs['posicion__nombre__icontains'] = filter
                    if tipo_busqueda =='competencia_descriptor__id':
                        filter_kwargs['competencia_descriptor__id'] = filter
                    if tipo_busqueda =='competencia_descriptor__nombre':
                        filter_kwargs['competencia_descriptor__nombre__icontains'] = filter
                    if tipo_busqueda =='competencia_descriptor__descriptor__id':
                        filter_kwargs['competencia_descriptor__descriptor__id'] = filter
                    if tipo_busqueda =='competencia_descriptor__descriptor__nombre_posicion':
                        filter_kwargs['competencia_descriptor__descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='filtrado_competencia_y_periodicidad':
                        filtro=json.loads(filter)
                              
                        filter_kwargs['periodicidad_id'] = filtro['periodicidad_id']
                        filter_kwargs['competencia_id'] = filtro['competencia_id']
                    
                    if tipo_busqueda =='filtrado_competencia_y_encabezado':
                        filtro=json.loads(filter) 
                        filter_kwargs['competencia_plantilla_encabezado__id'] = filtro['competencia_plantilla_encabezado__id']
                        filter_kwargs['competencia_id'] = filtro['competencia_id']


                queryset =  evaluacion_plantilla_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_plantilla_competencia.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_plantilla_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_plantilla_competencia.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  evaluacion_plantilla_competencia.objects.filter().count()
                serializer = evaluacion_plantilla_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='posicion_id':
                        filter_kwargs['posicion_id'] = filter
                    if tipo_busqueda =='posicion__codigo':
                        filter_kwargs['posicion__codigo__icontains'] = filter
                    if tipo_busqueda =='posicion__nombre':
                        filter_kwargs['posicion__nombre__icontains'] = filter
                    if tipo_busqueda =='competencia_descriptor__id':
                        filter_kwargs['competencia_descriptor__id'] = filter
                    if tipo_busqueda =='competencia_descriptor__nombre':
                        filter_kwargs['competencia_descriptor__nombre__icontains'] = filter
                    if tipo_busqueda =='competencia_descriptor__descriptor__id':
                        filter_kwargs['competencia_descriptor__descriptor__id'] = filter
                    if tipo_busqueda =='competencia_descriptor__descriptor__nombre_posicion':
                        filter_kwargs['competencia_descriptor__descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='filtrado_competencia_y_periodicidad':
                        filtro=json.loads(filter)          
                        filter_kwargs['periodicidad_id'] = filtro['periodicidad_id']
                        filter_kwargs['competencia_id'] = filtro['competencia_id']

                    if tipo_busqueda =='filtrado_competencia_y_encabezado':
                        filtro=json.loads(filter) 
                        filter_kwargs['competencia_plantilla_encabezado__id'] = filtro['competencia_plantilla_encabezado__id']
                        filter_kwargs['competencia_id'] = filtro['competencia_id']
                        
                queryset =  evaluacion_plantilla_competencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_plantilla_competencia.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_plantilla_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_plantilla_competencia.objects.filter().order_by('id')
                conteo =  evaluacion_plantilla_competencia.objects.filter().count()
                serializer = evaluacion_plantilla_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = evaluacion_plantilla_competenciaserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_plantilla_competencia.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_plantilla_competenciaserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def destroy(self,request,pk):

        
        area = evaluacion_plantilla_competencia.objects.filter(pk=pk).values() if evaluacion_plantilla_competencia.objects.filter(pk=pk) else None

        
        if area:
            plantilla_competencia= evaluacion_plantilla_competencia.objects.get(pk=pk)
            if plantilla_competencia.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=plantilla_competencia.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=plantilla_competencia.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=plantilla_competencia.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=plantilla_competencia.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_plantilla_competencia.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)



class evaluacion_archivo_plan_accion(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none()
    def post(self,request):
        url =  settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CrearDocumento'
        fecha=''
        hoy=datetime.now().date()
       ###print('entro')
        myobj = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado']}

        x = requests.post(url, data = myobj)
        response_dict = x.json()

        #print('response_dict',response_dict)
        
        if len(response_dict)>0:
           ###print(response_dict)
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CrearDocumento'
            fecha= hoy.strftime("%Y%m%d")
            
            llave = (str(self.request.data['empresa']) +'-'+ str(self.request.data['division'])+'-'+str(self.request.data['tipo_documento'] )+'-'+str(self.request.data['descripcion']) +'-'+str(self.request.data['codigo_empleado']) +'-'+str(fecha) ).upper()
        
            objeto = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado'],'llave':llave,'origen':self.request.data['origen'],'documento':self.request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}
            x = requests.post(enlace, data = objeto)
            # #print("resultado",settings.EMAIL_GESTOR_DOCCUMENTAL)
            
            resultado = x.json()
            if x.status_code==400:
                return Response({"resultado":resultado},status= status.HTTP_404_NOT_FOUND)

            for error in resultado:
                if error['response'].find('creado')==-1:
                    return Response({"resultado":resultado},status= status.HTTP_404_NOT_FOUND)
                    
            for result in resultado:
                indice1=result['response'].index(':')+1
                indice2=result['response'].index(',')
                id_gestor=result['response'][indice1:indice2] if indice1 and indice2 else None


            docx= evaluacion_archivo_plan_accion_gestor.objects.create(id_documento=id_gestor, llave=llave,id_area=self.request.data['id_area'],id_carpeta_encabezado=self.request.data['id_carpeta_encabezado'],empresa=self.request.data['empresa'],tipo_documento=self.request.data['tipo_documento'],origen=self.request.data['origen'],extension=self.request.data['extension'],contentTypeGD=self.request.data['contentTypeGD'],nombre=self.request.data['nombre'],descripcion=self.request.data['descripcion'],division=self.request.data['division'],codigo_empleado=self.request.data['codigo_empleado'])
            # doc= evaluacion_archivo_plan_accion(id_documento=id_gestor, llave=llave,id_area=self.request.data['id_area'],id_carpeta_encabezado=self.request.data['id_carpeta_encabezado'],empresa=self.request.data['empresa'],tipo_documento=self.request.data['tipo_documento'],origen=self.request.data['origen'],extension=self.request.data['extension'],contentTypeGD=self.request.data['contentTypeGD'],nombre=self.request.data['nombre'],descripcion=self.request.data['descripcion'],division=self.request.data['division'],codigo_empleado=self.request.data['codigo_empleado'])
            
            return Response({"resultado": evaluacion_archivo_plan_accion_gestorserializer(docx).data},status= status.HTTP_200_OK)
        else:
            return Response({"resultado":"No se puede verificar el contenido el detalle de la carpeta"},status= status.HTTP_404_NOT_FOUND) 

    def get_object(self, pk):
        try:
            return evaluacion_archivo_plan_accion_gestor.objects.get(pk=pk)
        except evaluacion_archivo_plan_accion_gestor.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        #print(post.id_documento)
        serializer = evaluacion_archivo_plan_accion_gestorserializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/ModificarDocumento'
            objeto = {'id':post.id_documento,'ceid':post.id_carpeta_encabezado,'llave':str(post.llave).upper(),'origen':post.origen,'documento':request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}            
            x = requests.post(enlace, data = objeto)
            resultado = x.json()
            #print('objeto',objeto)
            #print('X',x)
            #print('resultadoresultado',resultado)
            

            # for result in resultado:
            #    ##print('resultado',result)
            #     if result['response'].find('Modificado Correctamente')==-1:
            #         return Response({"resultado":result['response']},status= status.HTTP_404_NOT_FOUND)
            if x.status_code==200:
                return Response(serializer.data)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        existe= evaluacion_archivo_plan_accion_gestor.objects.filter(id=pk).count()
        if existe!=0:
            get = self.get_object(pk)
            #get =  on_off_bording_bienvenida.objects.filter(id=id) if on_off_bording_bienvenida.objects.filter(id=id) else None 
            serializer=evaluacion_archivo_plan_accion_gestorserializer(get)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)



class evaluacion_archivo_plan_accion_gestorViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = evaluacion_archivo_plan_accion_gestor.objects.all()
    serializer_class = evaluacion_archivo_plan_accion_gestorserializer
    def list(self, request):
        queryset = evaluacion_archivo_plan_accion_gestor.objects.all()
        objeto= evaluacion_archivo_plan_accion_gestor.objects.all()
        serializer = evaluacion_archivo_plan_accion_gestorserializer(queryset, many=True)
        tipo_documento=''

        if self.request.query_params.get('tipo_documento'):
            tipo_documento = self.request.query_params.get('tipo_documento')

        if tipo_documento:
            queryset = evaluacion_archivo_plan_accion_gestor.objects.filter(tipo_documento=tipo_documento).order_by('-id')
            serializer = evaluacion_archivo_plan_accion_gestorserializer(queryset, many=True)
            return Response({"data":serializer.data})
        else:
            queryset = evaluacion_archivo_plan_accion_gestor.objects.filter().order_by('-id')
            serializer = evaluacion_archivo_plan_accion_gestorserializer(queryset, many=True)
            return Response({"data":serializer.data})
            
class evaluacion_plantilla_factorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_plantilla_factor.objects.all()
    serializer_class = evaluacion_plantilla_factorserializer
    def list(self, request):
        queryset = evaluacion_plantilla_factor.objects.all()
        serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        filter_3=''
        tipo_busqueda_3=''
        if self.request.query_params.get('filter_3'):
            filter_3 = self.request.query_params.get('filter_3')
        
        if self.request.query_params.get('tipo_busqueda_3'):
            tipo_busqueda_3 = self.request.query_params.get('tipo_busqueda_3')

        if self.request.query_params.get('filter_2'):
            filter_2 = self.request.query_params.get('filter_2')
        
        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')
        
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='posicion':
                        filter_kwargs['posicion'] = filter
                    if tipo_busqueda =='posicion_descripcion':
                        filter_kwargs['posicion__descripcion__icontains'] = filter
                    if tipo_busqueda =='factor':
                        filter_kwargs['factor'] = filter
                    if tipo_busqueda =='factor_nombre':
                        filter_kwargs['factor__nombre__icontains'] = filter
                    if tipo_busqueda =='pregunta':
                        filter_kwargs['pregunta__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad__id'] = filter
                    if tipo_busqueda =='encabezado':
                        filter_kwargs['factor_plantilla_encabezado__id'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='posicion':
                            filter_kwargs_2['posicion'] = filter_2
                        if tipo_busqueda_2 =='posicion_descripcion':
                            filter_kwargs_2['posicion__descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='factor':
                            filter_kwargs_2['factor'] = filter_2
                        if tipo_busqueda_2 =='factor_nombre':
                            filter_kwargs_2['factor__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='pregunta':
                            filter_kwargs_2['pregunta__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__date__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad__id'] = filter_2
                        if tipo_busqueda_2 =='encabezado':
                            filter_kwargs_2['factor_plantilla_encabezado__id'] = filter_2
                        
                    if filter_3!='' and tipo_busqueda_3!='':
                        filter_kwargs_3={}
                        if tipo_busqueda_3:
                            if tipo_busqueda_3 =='posicion':
                                filter_kwargs_3['posicion'] = filter_3
                            if tipo_busqueda_3 =='posicion_descripcion':
                                filter_kwargs_3['posicion__descripcion__icontains'] = filter_3
                            if tipo_busqueda_3 =='factor':
                                filter_kwargs_3['factor'] = filter_3
                            if tipo_busqueda_3 =='factor_nombre':
                                filter_kwargs_3['factor__nombre__icontains'] = filter_3
                            if tipo_busqueda_3 =='pregunta':
                                filter_kwargs_3['pregunta__icontains'] = filter_3
                            if tipo_busqueda_3 =='fecha_creacion':
                                filter_kwargs_3['fecha_creacion__date__icontains'] = filter_3
                            if tipo_busqueda_3 =='periodicidad_id':
                                filter_kwargs_3['periodicidad__id'] = filter_3
                            if tipo_busqueda_3 =='encabezado':
                                filter_kwargs_3['factor_plantilla_encabezado__id'] = filter_3    


                        queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).filter(**filter_kwargs_3).order_by('id')[offset:offset+limit]
                        conteo =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).filter(**filter_kwargs_3).count()
                        serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo}) 
                    else:
                        queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                        conteo =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                        serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})  


                        

                    queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_plantilla_factor.objects.filter().count()
                    serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

                       
                        

                queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  evaluacion_plantilla_factor.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  evaluacion_plantilla_factor.objects.filter().count()
                serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='posicion':
                        filter_kwargs['posicion'] = filter
                    if tipo_busqueda =='posicion_descripcion':
                        filter_kwargs['posicion__descripcion__icontains'] = filter
                    if tipo_busqueda =='factor':
                        filter_kwargs['factor'] = filter
                    if tipo_busqueda =='factor_nombre':
                        filter_kwargs['factor__nombre__icontains'] = filter
                    if tipo_busqueda =='pregunta':
                        filter_kwargs['pregunta__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='periodicidad_id':
                        filter_kwargs['periodicidad__id'] = filter
                    if tipo_busqueda =='encabezado':
                        filter_kwargs['factor_plantilla_encabezado__id'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='posicion':
                            filter_kwargs_2['posicion'] = filter_2
                        if tipo_busqueda_2 =='posicion_descripcion':
                            filter_kwargs_2['posicion__descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='factor':
                            filter_kwargs_2['factor'] = filter_2
                        if tipo_busqueda_2 =='factor_nombre':
                            filter_kwargs_2['factor__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='pregunta':
                            filter_kwargs_2['pregunta__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__date__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_id':
                            filter_kwargs_2['periodicidad__id'] = filter_2
                        if tipo_busqueda_2 =='encabezado':
                            filter_kwargs_2['factor_plantilla_encabezado__id'] = filter_2

                    if filter_3!='' and tipo_busqueda_3!='':
                        filter_kwargs_3={}
                        if tipo_busqueda_3:
                            if tipo_busqueda_3 =='posicion':
                                filter_kwargs_3['posicion'] = filter_3
                            if tipo_busqueda_3 =='posicion_descripcion':
                                filter_kwargs_3['posicion__descripcion__icontains'] = filter_3
                            if tipo_busqueda_3 =='factor':
                                filter_kwargs_3['factor'] = filter_3
                            if tipo_busqueda_3 =='factor_nombre':
                                filter_kwargs_3['factor__nombre__icontains'] = filter_3
                            if tipo_busqueda_3 =='pregunta':
                                filter_kwargs_3['pregunta__icontains'] = filter_3
                            if tipo_busqueda_3 =='fecha_creacion':
                                filter_kwargs_3['fecha_creacion__date__icontains'] = filter_3
                            if tipo_busqueda_3 =='periodicidad_id':
                                filter_kwargs_3['periodicidad__id'] = filter_3
                            if tipo_busqueda_3 =='encabezado':
                                filter_kwargs_3['factor_plantilla_encabezado__id'] = filter_3

                        queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).filter(**filter_kwargs_3).order_by('id')
                        conteo =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).filter(**filter_kwargs_3).count()
                        serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})  
                    else: 
                        queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                        conteo =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                        serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})


                        
                    queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  evaluacion_plantilla_factor.objects.filter().count()
                    serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

                queryset =  evaluacion_plantilla_factor.objects.filter(**filter_kwargs).order_by('id')
                serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  evaluacion_plantilla_factor.objects.filter().order_by('id')
                serializer = evaluacion_plantilla_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        serializer = evaluacion_plantilla_factorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_plantilla_factor.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_plantilla_factorserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    

    def destroy(self,request,pk):


        area = evaluacion_plantilla_factor.objects.filter(pk=pk).values() if evaluacion_plantilla_factor.objects.filter(pk=pk) else None

        
        if area:
            plantilla_factor= evaluacion_plantilla_factor.objects.get(pk=pk)
            if plantilla_factor.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=plantilla_factor.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=plantilla_factor.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=plantilla_factor.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=plantilla_factor.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_plantilla_factor.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)




 

class monitor_colaboradorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = monitor_colaboradoresserializer
    def list(self, request):
        queryset = Funcional_empleado.objects.all()
        serializer_class = monitor_colaboradoresserializer(queryset, many=True)
        filtrado = Funcional_empleado.objects.filter()
        empresa=0
        departamento=0
        unidad_organizativa=0
        empleado=0
        usuario = request.user
        usuario_codigo = request.user.username
        empleados_a_cargo= funcional_get_colaborador([usuario_codigo])
        
        
        
        if self.request.query_params.get('empresa'):
            empresa = json.loads(self.request.query_params.get('empresa'))
            # filter_kwargs['Q(unidad_organizativa__sociedad_financiera__nombre__icontains__in='+empresa+')|Q(unidad_organizativa__sociedad_financiera__codigo__in'+empresa+')'] 
            cod_empleados_empresa=[]
            for x in empresa:
                empleados_empresa= Funcional_empleado.objects.filter(Q(unidad_organizativa__sociedad_financiera__nombre__icontains=x)|Q(unidad_organizativa__sociedad_financiera__codigo=x)).values_list('codigo',flat=True) if Funcional_empleado.objects.filter(Q(unidad_organizativa__sociedad_financiera__nombre__icontains=x)|Q(unidad_organizativa__sociedad_financiera__codigo=x)).values_list('codigo',flat=True) else None
                if empleados_empresa!=None:
                    cod_empleados_empresa.extend(empleados_empresa)
            
            if len(cod_empleados_empresa)!=0:
                #print('filtro')
                filtrado= filtrado.filter(codigo__in=cod_empleados_empresa)

        if self.request.query_params.get('departamento'):
            departamento = json.loads(self.request.query_params.get('departamento'))
            # filter_kwargs['Q(division__descripcion__icontains__in='+departamento+')|Q(division__codigo__in'+departamento+')']
            cod_empleados=[]
            for x in departamento:
                empleados_departamento= Funcional_empleado.objects.filter(Q(division__descripcion__icontains=x)|Q(division__codigo=x)).values_list('codigo',flat=True) if Funcional_empleado.objects.filter(Q(division__descripcion__icontains=x)|Q(division__codigo=x)).values_list('codigo',flat=True) else None
                if empleados_departamento!=None:
                    cod_empleados.extend(empleados_departamento)

            if len(cod_empleados)!=0:
                #print('filtro')
                filtrado= filtrado.filter(codigo__in=cod_empleados)

        if self.request.query_params.get('unidad_organizativa'):
            unidad_organizativa = json.loads(self.request.query_params.get('unidad_organizativa'))
            # filter_kwargs['Q(unidad_organizativa_codigo__in'+unidad_organizativa+')|Q(unidad_organizativa_id__in'+unidad_organizativa+')']
            filtrado= filtrado.filter(Q(unidad_organizativa__codigo__in=unidad_organizativa)|Q(unidad_organizativa__id__in=unidad_organizativa))

            
        if self.request.query_params.get('empleado'):
            empleado = json.loads(self.request.query_params.get('empleado'))
            list_empleados_codigo= []
            for x in empleado:
                query_empleado=  Funcional_empleado.objects.filter(Q(nombre__icontains=x)|Q(codigo=x)).values_list('codigo',flat=True) if Funcional_empleado.objects.filter(Q(nombre__icontains=x)|Q(codigo=x)).values_list('codigo',flat=True) else None
                if query_empleado!=None:
                    list_empleados_codigo.extend(query_empleado)
        
            filtrado = filtrado.filter(codigo__in=list_empleados_codigo)

        grupos = list(usuario.groups.all().values_list('name',flat=True))

        if 'jefe' in grupos:
            filtrado = filtrado.filter(codigo__in=empleados_a_cargo)


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if filtrado:     
                queryset =  filtrado.order_by('id')[offset:offset+limit]
                conteo =  filtrado.count()
                serializer = monitor_colaboradoresserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else:
                return Response({"resultado":"No hay datos"},status= status.HTTP_404_NOT_FOUND)
        else:
            if filtrado:     
                queryset =  filtrado.order_by('id')
                conteo =   filtrado.count()
                serializer = monitor_colaboradoresserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else:
               return Response({"resultado":"No hay datos"},status= status.HTTP_404_NOT_FOUND)
            


def empleados(usuario):
    
    filter=''
    unidad_organizativa=''
    grupos = list(usuario.groups.all().values_list('name',flat=True))
    lista_funciones=[]
    lista_empleados=[]
    
    
    unidad_organizativa = (Funcional_empleado.objects.filter(codigo=usuario).values('unidad_organizativa')[0])['unidad_organizativa']
    
    bandera=None
    listado=[]
    filtros=[unidad_organizativa]
    
    
    while bandera ==None:
        resultado=Funcional_Unidad_Organizativa.objects.filter(id__in=filtros).values_list('unidad_organizativa_jeraquia__id',flat=True)           
        listado.extend(resultado)
        filtros = resultado
        if resultado.count()==0 or resultado==None:
            bandera=0

    
    uni= Funcional_Unidad_Organizativa.objects.filter(id=unidad_organizativa)
    Dirigido_por=uni[0].Dirigido_por
    padre = Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id=unidad_organizativa)
    if padre:
        hijos_list=padre[0].unidad_organizativa_jeraquia.all().values_list('id',flat=True)
        hermanos=Funcional_Unidad_Organizativa.objects.filter(id__in=hijos_list, Dirigido_por=Dirigido_por).exclude(id=unidad_organizativa).values_list('id',flat=True)
        listado.extend(hermanos)
    equipo = Funcional_Unidad_Organizativa.objects.filter(id=unidad_organizativa).values_list('unidad_organizativa_jeraquia__id',flat=True)
    equipo =Funcional_Unidad_Organizativa.objects.filter(id__in=listado)
    
    lista_permiso=list(usuario.groups.all().values_list('name',flat=True))
    

    serializer_unidad = funcional_arbol_padre_serializer(uni[0])
    serializer_padre = funcional_arbol_padre_serializer(padre[0]).data if padre else []
    # #print('serializer_unidad',uni[0].codigo)
    codigo_padre = usuario
    lista_funciones.append(Funcional_empleado.objects.filter(codigo=codigo_padre).values('posicion__id')[0]['posicion__id'])
    serializer_equipo = funcional_arbol_padre_serializer(equipo,many=True).data

    lider = serializer_unidad.data['lider']

    lideres=[]
    if serializer_unidad.data['lider']!=None:
        lideres.append(serializer_unidad.data['lider']['id'])
    
    if 'empleado' in lista_permiso:
        serializer_equipo=[]
        listado=[unidad_organizativa]
        
    else:
        for eq in serializer_equipo:
            if  eq['lider']!=None:
                    lideres.append(eq['lider']['id'])
        listado.append(unidad_organizativa)
        
        
    empleados = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(fecha_baja__lt=datetime.now().date()) else None
    
    if lider!=None:
        empleados = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) else None

    # listado_funciones_empleados = empleados.values_list('posicion',flat=True)
    lista_empleados.extend(empleados.values_list('codigo',flat=True))

    empleados_con_jefe_inmediato= Funcional_empleado.objects.filter(jefe_inmediato=usuario).values_list('codigo',flat=True).exclude(fecha_baja__lt=datetime.now().date())
    lista_empleados.extend(empleados_con_jefe_inmediato)
    # lista_funciones.extend(empleados_con_jefe_inmediato)    
    # lista_funciones.extend(listado_funciones_empleados)
    # #print(lista_empleados)
    return lista_empleados



class evaluacion_encabezadoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezadoserializer
    def list(self, request):
        queryset = evaluacion_encabezado.objects.all()
        serializer_class = evaluacion_encabezadoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='evaluado_id':
                        filter_kwargs['evaluado_id'] = filter
                    if tipo_busqueda =='evaluado_nombre':
                        filter_kwargs['evaluado_nombre__icontains'] = filter
                    if tipo_busqueda =='evaluado_codigo':
                        filter_kwargs['evaluado_codigo__icontains'] = filter  
                    if tipo_busqueda =='responsable_directo_id':
                        filter_kwargs['responsable_directo__id'] = filter
                    if tipo_busqueda =='responsable_directo_nombre':
                        filter_kwargs['responsable_directo__icontains'] = filter
                    if tipo_busqueda =='responsable_directo_codigo':
                        filter_kwargs['responsable_directo__icontains'] = filter
                    if tipo_busqueda =='evaluador_id':
                        filter_kwargs['evaluador_id'] = filter
                    if tipo_busqueda =='evaluador_nombre':
                        filter_kwargs['evaluador_nombre__icontains'] = filter
                    if tipo_busqueda =='evaluador_codigo':
                        filter_kwargs['evaluador_codigo__icontains'] = filter
                    if tipo_busqueda =='tipo_evaluacion_id':
                        filter_kwargs['tipo_evaluacion__id'] = filter
                    if tipo_busqueda =='tipo_evaluacion_nombre':
                        filter_kwargs['tipo_evaluacion__nombre__icontains'] = filter

                    if tipo_busqueda =='periodicidad__id':
                        filter_kwargs['periodicidad__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__id':
                        filter_kwargs['periodicidad__empresa__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter  
                    if tipo_busqueda =='periodicidad__empresa__codigo':
                        filter_kwargs['periodicidad__empresa__codigo__icontains'] = filter   
                    if tipo_busqueda =='periodicidad__anio':
                        filter_kwargs['periodicidad__anio'] = filter 

                    if tipo_busqueda =='periodicidad__frecuencia__id':
                        filter_kwargs['periodicidad__frecuencia__id'] = filter 
                    if tipo_busqueda =='periodicidad__frecuencia__nombre':
                        filter_kwargs['periodicidad__frecuencia__nombre__icontains'] = filter                                          
                    if tipo_busqueda =='periodo':
                        filter_kwargs['periodo'] = filter 
                    if tipo_busqueda =='estado':
                        filter_kwargs['estado'] = filter  


                        
                queryset =  evaluacion_encabezado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_encabezado.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_encabezado.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  evaluacion_encabezado.objects.filter().count()
                serializer = evaluacion_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='evaluado_id':
                        filter_kwargs['evaluado_id'] = filter
                    if tipo_busqueda =='evaluado_nombre':
                        filter_kwargs['evaluado_nombre__icontains'] = filter
                    if tipo_busqueda =='evaluado_codigo':
                        filter_kwargs['evaluado_codigo__icontains'] = filter  
                    if tipo_busqueda =='responsable_directo_id':
                        filter_kwargs['responsable_directo__id'] = filter
                    if tipo_busqueda =='responsable_directo_nombre':
                        filter_kwargs['responsable_directo__icontains'] = filter
                    if tipo_busqueda =='responsable_directo_codigo':
                        filter_kwargs['responsable_directo__icontains'] = filter
                    if tipo_busqueda =='evaluador_id':
                        filter_kwargs['evaluador_id'] = filter
                    if tipo_busqueda =='evaluador_nombre':
                        filter_kwargs['evaluador_nombre__icontains'] = filter
                    if tipo_busqueda =='evaluador_codigo':
                        filter_kwargs['evaluador_codigo__icontains'] = filter
                    if tipo_busqueda =='tipo_evaluacion_id':
                        filter_kwargs['tipo_evaluacion__id'] = filter
                    if tipo_busqueda =='tipo_evaluacion_nombre':
                        filter_kwargs['tipo_evaluacion__nombre__icontains'] = filter

                    if tipo_busqueda =='periodicidad__id':
                        filter_kwargs['periodicidad__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__id':
                        filter_kwargs['periodicidad__empresa__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter  
                    if tipo_busqueda =='periodicidad__empresa__codigo':
                        filter_kwargs['periodicidad__empresa__codigo__icontains'] = filter   
                    if tipo_busqueda =='periodicidad__anio':
                        filter_kwargs['periodicidad__anio'] = filter 

                    if tipo_busqueda =='periodicidad__frecuencia__id':
                        filter_kwargs['periodicidad__frecuencia__id'] = filter 
                    if tipo_busqueda =='periodicidad__frecuencia__nombre':
                        filter_kwargs['periodicidad__frecuencia__nombre__icontains'] = filter                                          
                    if tipo_busqueda =='periodo':
                        filter_kwargs['periodo'] = filter 
                    if tipo_busqueda =='estado':
                        filter_kwargs['estado'] = filter  

                        
                queryset =  evaluacion_encabezado.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_encabezado.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_encabezado.objects.filter().order_by('id')
                conteo =  evaluacion_encabezado.objects.filter().count()
                serializer = evaluacion_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = evaluacion_encabezadoserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= evaluacion_encabezado.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= evaluacion_encabezadoserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def destroy(self,request,pk):

        area = evaluacion_encabezado.objects.filter(pk=pk).values() if evaluacion_encabezado.objects.filter(pk=pk) else None

        
        if area:
            encabezado= evaluacion_encabezado.objects.get(pk=pk)
            if encabezado.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=encabezado.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=encabezado.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=encabezado.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=encabezado.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_encabezado.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)


      


class Monitor_evaluacionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezadoserializer
    def list(self, request):
        queryset = evaluacion_encabezado.objects.all()
        serializer_class = evaluacion_encabezadoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        evaluaciones_actuales=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        ################################################################
        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')


        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')
        
        if self.request.query_params.get('evaluaciones_actuales'):
            evaluaciones_actuales = self.request.query_params.get('evaluaciones_actuales')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                filter_kwargs['tipo_evaluacion_encabezado'] = 2
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='evaluado_id':
                        filter_kwargs['evaluado_id'] = filter
                    if tipo_busqueda =='evaluado_nombre':
                        filter_kwargs['evaluado_nombre__icontains'] = filter
                    if tipo_busqueda =='evaluado_codigo':
                        filter_kwargs['evaluado_codigo__icontains'] = filter  
                    if tipo_busqueda =='responsable_directo_id':
                        filter_kwargs['responsable_directo__id'] = filter
                    if tipo_busqueda =='responsable_directo_nombre':
                        filter_kwargs['responsable_directo__icontains'] = filter
                    if tipo_busqueda =='responsable_directo_codigo':
                        filter_kwargs['responsable_directo__icontains'] = filter
                    if tipo_busqueda =='evaluador_id':
                        filter_kwargs['evaluador_id'] = filter
                    if tipo_busqueda =='evaluador_nombre':
                        filter_kwargs['evaluador_nombre__icontains'] = filter
                    if tipo_busqueda =='evaluador_codigo':
                        filter_kwargs['evaluador_codigo__icontains'] = filter
                    if tipo_busqueda =='tipo_evaluacion_id':
                        filter_kwargs['tipo_evaluacion__id'] = filter
                    if tipo_busqueda =='tipo_evaluacion_nombre':
                        filter_kwargs['tipo_evaluacion__nombre__icontains'] = filter

                    if tipo_busqueda =='periodicidad__id':
                        filter_kwargs['periodicidad__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__id':
                        filter_kwargs['periodicidad__empresa__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter  
                    if tipo_busqueda =='periodicidad__empresa__codigo':
                        filter_kwargs['periodicidad__empresa__codigo__icontains'] = filter   
                    if tipo_busqueda =='periodicidad__anio':
                        filter_kwargs['periodicidad__anio'] = filter 

                    if tipo_busqueda =='periodicidad__frecuencia__id':
                        filter_kwargs['periodicidad__frecuencia__id'] = filter 
                    if tipo_busqueda =='periodicidad__frecuencia__nombre':
                        filter_kwargs['periodicidad__frecuencia__nombre__icontains'] = filter                                          
                    if tipo_busqueda =='periodo':
                        filter_kwargs['periodo'] = filter 
                    if tipo_busqueda =='estado':
                        filter_kwargs['estado'] = filter
                

                if evaluaciones_actuales!='':
                    filter_kwargs['periodicidad_id'] = evaluaciones_actuales

                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='evaluado_id':
                            filter_kwargs_2['evaluado_id'] = filter_2
                        if tipo_busqueda_2 =='evaluado_nombre':
                            filter_kwargs_2['evaluado_nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='evaluado_codigo':
                            filter_kwargs_2['evaluado_codigo__icontains'] = filter_2  
                        if tipo_busqueda_2 =='responsable_directo_id':
                            filter_kwargs_2['responsable_directo__id'] = filter_2
                        if tipo_busqueda_2 =='responsable_directo_nombre':
                            filter_kwargs_2['responsable_directo__icontains'] = filter_2
                        if tipo_busqueda_2 =='responsable_directo_codigo':
                            filter_kwargs_2['responsable_directo__icontains'] = filter_2
                        if tipo_busqueda_2 =='evaluador_id':
                            filter_kwargs_2['evaluador_id'] = filter_2
                        if tipo_busqueda_2 =='evaluador_nombre':
                            filter_kwargs_2['evaluador_nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='evaluador_codigo':
                            filter_kwargs_2['evaluador_codigo__icontains'] = filter_2
                        if tipo_busqueda_2 =='tipo_evaluacion_id':
                            filter_kwargs_2['tipo_evaluacion__id'] = filter_2
                        if tipo_busqueda_2 =='tipo_evaluacion_nombre':
                            filter_kwargs_2['tipo_evaluacion__nombre__icontains'] = filter_2

                        if tipo_busqueda_2 =='periodicidad__id':
                            filter_kwargs_2['periodicidad__id'] = filter_2
                        if tipo_busqueda_2 =='periodicidad__empresa__id':
                            filter_kwargs_2['periodicidad__empresa__id'] = filter_2
                        if tipo_busqueda_2 =='periodicidad__empresa__nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre__icontains'] = filter_2  
                        if tipo_busqueda_2 =='periodicidad__empresa__codigo':
                            filter_kwargs_2['periodicidad__empresa__codigo__icontains'] = filter_2   
                        if tipo_busqueda_2 =='periodicidad__anio':
                            filter_kwargs_2['periodicidad__anio'] = filter_2 

                        if tipo_busqueda_2 =='periodicidad__frecuencia__id':
                            filter_kwargs_2['periodicidad__frecuencia__id'] = filter_2 
                        if tipo_busqueda_2 =='periodicidad__frecuencia__nombre':
                            filter_kwargs_2['periodicidad__frecuencia__nombre__icontains'] = filter_2                                          
                        if tipo_busqueda_2 =='periodo':
                            filter_kwargs_2['periodo'] = filter_2 
                        if tipo_busqueda_2 =='estado':
                            filter_kwargs_2['estado'] = filter_2

                    queryset =  evaluacion_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_encabezadoserializer(queryset, many=True)
                    
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_encabezado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_encabezado.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 

                queryset =  evaluacion_encabezado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_encabezado.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_encabezadoserializer(queryset, many=True)
                
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_encabezado.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  evaluacion_encabezado.objects.filter().count()
                serializer = evaluacion_encabezadoserializer(queryset, many=True)
                serializer.data['asdasdasdasd']='asdadasdasdasdasdasdasd'
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='evaluado_id':
                        filter_kwargs['evaluado_id'] = filter
                    if tipo_busqueda =='evaluado_nombre':
                        filter_kwargs['evaluado_nombre__icontains'] = filter
                    if tipo_busqueda =='evaluado_codigo':
                        filter_kwargs['evaluado_codigo__icontains'] = filter  
                    if tipo_busqueda =='responsable_directo_id':
                        filter_kwargs['responsable_directo__id'] = filter
                    if tipo_busqueda =='responsable_directo_nombre':
                        filter_kwargs['responsable_directo__icontains'] = filter
                    if tipo_busqueda =='responsable_directo_codigo':
                        filter_kwargs['responsable_directo__icontains'] = filter
                    if tipo_busqueda =='evaluador_id':
                        filter_kwargs['evaluador_id'] = filter
                    if tipo_busqueda =='evaluador_nombre':
                        filter_kwargs['evaluador_nombre__icontains'] = filter
                    if tipo_busqueda =='evaluador_codigo':
                        filter_kwargs['evaluador_codigo__icontains'] = filter
                    if tipo_busqueda =='tipo_evaluacion_id':
                        filter_kwargs['tipo_evaluacion__id'] = filter
                    if tipo_busqueda =='tipo_evaluacion_nombre':
                        filter_kwargs['tipo_evaluacion__nombre__icontains'] = filter

                    if tipo_busqueda =='periodicidad__id':
                        filter_kwargs['periodicidad__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__id':
                        filter_kwargs['periodicidad__empresa__id'] = filter
                    if tipo_busqueda =='periodicidad__empresa__nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter  
                    if tipo_busqueda =='periodicidad__empresa__codigo':
                        filter_kwargs['periodicidad__empresa__codigo__icontains'] = filter   
                    if tipo_busqueda =='periodicidad__anio':
                        filter_kwargs['periodicidad__anio'] = filter 

                    if tipo_busqueda =='periodicidad__frecuencia__id':
                        filter_kwargs['periodicidad__frecuencia__id'] = filter 
                    if tipo_busqueda =='periodicidad__frecuencia__nombre':
                        filter_kwargs['periodicidad__frecuencia__nombre__icontains'] = filter                                          
                    if tipo_busqueda =='periodo':
                        filter_kwargs['periodo'] = filter 
                    if tipo_busqueda =='estado':
                        filter_kwargs['estado'] = filter  
                if evaluaciones_actuales!='':
                    filter_kwargs['periodicidad_id'] = evaluaciones_actuales
                    
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='evaluado_id':
                            filter_kwargs_2['evaluado_id'] = filter_2
                        if tipo_busqueda_2 =='evaluado_nombre':
                            filter_kwargs_2['evaluado_nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='evaluado_codigo':
                            filter_kwargs_2['evaluado_codigo__icontains'] = filter_2  
                        if tipo_busqueda_2 =='responsable_directo_id':
                            filter_kwargs_2['responsable_directo__id'] = filter_2
                        if tipo_busqueda_2 =='responsable_directo_nombre':
                            filter_kwargs_2['responsable_directo__icontains'] = filter_2
                        if tipo_busqueda_2 =='responsable_directo_codigo':
                            filter_kwargs_2['responsable_directo__icontains'] = filter_2
                        if tipo_busqueda_2 =='evaluador_id':
                            filter_kwargs_2['evaluador_id'] = filter_2
                        if tipo_busqueda_2 =='evaluador_nombre':
                            filter_kwargs_2['evaluador_nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='evaluador_codigo':
                            filter_kwargs_2['evaluador_codigo__icontains'] = filter_2
                        if tipo_busqueda_2 =='tipo_evaluacion_id':
                            filter_kwargs_2['tipo_evaluacion__id'] = filter_2
                        if tipo_busqueda_2 =='tipo_evaluacion_nombre':
                            filter_kwargs_2['tipo_evaluacion__nombre__icontains'] = filter_2

                        if tipo_busqueda_2 =='periodicidad__id':
                            filter_kwargs_2['periodicidad__id'] = filter_2
                        if tipo_busqueda_2 =='periodicidad__empresa__id':
                            filter_kwargs_2['periodicidad__empresa__id'] = filter_2
                        if tipo_busqueda_2 =='periodicidad__empresa__nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre__icontains'] = filter_2  
                        if tipo_busqueda_2 =='periodicidad__empresa__codigo':
                            filter_kwargs_2['periodicidad__empresa__codigo__icontains'] = filter_2   
                        if tipo_busqueda_2 =='periodicidad__anio':
                            filter_kwargs_2['periodicidad__anio'] = filter_2 

                        if tipo_busqueda_2 =='periodicidad__frecuencia__id':
                            filter_kwargs_2['periodicidad__frecuencia__id'] = filter_2 
                        if tipo_busqueda_2 =='periodicidad__frecuencia__nombre':
                            filter_kwargs_2['periodicidad__frecuencia__nombre__icontains'] = filter_2                                          
                        if tipo_busqueda_2 =='periodo':
                            filter_kwargs_2['periodo'] = filter_2 
                        if tipo_busqueda_2 =='estado':
                            filter_kwargs_2['estado'] = filter_2
                    queryset =  evaluacion_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  evaluacion_encabezado.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  evaluacion_encabezado.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

                queryset =  evaluacion_encabezado.objects.filter(**filter_kwargs).order_by('id')
                conteo =  evaluacion_encabezado.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  evaluacion_encabezado.objects.filter().order_by('id')
                conteo =  evaluacion_encabezado.objects.filter().count()
                serializer = evaluacion_encabezadoserializer(queryset, many=True)
                
                
                return Response({"data":serializer.data,"count":conteo})

    def update(self,requets,pk):
        existe= evaluacion_encabezado.objects.filter(id=pk).count()
        tipo_evaluacion_encabezado_e=(evaluacion_encabezado.objects.filter(id=pk).values('tipo_evaluacion_encabezado'))[0]['tipo_evaluacion_encabezado'] if evaluacion_encabezado.objects.filter(id=pk).values('tipo_evaluacion_encabezado') else None
        validacion_prueba_completa=None
        comentario_evaluado=''
        if "comentario_evaluado" in requets.data:
            comentario_evaluado= requets.data['comentario_evaluado']
        ###################################################################################
        if existe > 0 and  comentario_evaluado!='' and tipo_evaluacion_encabezado_e==2:
            # print('entro al if')
            validacion_evaluacion_llenada=validacion_evaluacion_factor(pk)
            
            encabezado= evaluacion_encabezado.objects.get(id=pk) if evaluacion_encabezado.objects.filter(id=pk) else None
            if encabezado!=None:#este codigo lleva la fecha de la evaluacion
                encabezado_evaluado= (evaluacion_encabezado.objects.filter(id=pk).values('evaluado'))[0]['evaluado'] if evaluacion_encabezado.objects.filter(id=pk).values('evaluado') else None
                encabezado_periodicidad=  (evaluacion_encabezado.objects.filter(id=pk).values('periodicidad'))[0]['periodicidad'] if evaluacion_encabezado.objects.filter(id=pk).values('periodicidad') else None
                encabezado_periodo =  (evaluacion_encabezado.objects.filter(id=pk).values('periodo'))[0]['periodo'] if evaluacion_encabezado.objects.filter(id=pk).values('periodo') else None
                encabezado_tipo_evaluacion =  (evaluacion_encabezado.objects.filter(id=pk).values('tipo_evaluacion__id'))[0]['tipo_evaluacion__id'] if evaluacion_encabezado.objects.filter(id=pk).values('tipo_evaluacion__id') else None
                #########################################################################################################################
                encabezado_competencia_id=(evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=1).values('id'))[0]['id'] if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=1) else None
                validacion_encabezado_competencia_1=validacion_evaluacion_competencia(encabezado_competencia_id)
                tipo_e=(evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=1).values('tipo_evaluacion__nombre'))[0]['tipo_evaluacion__nombre'] if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=1) else None
                # print('validacion_evaluacion_llenada',validacion_evaluacion_llenada)
                # print('validacion_encabezado_competencia_1',validacion_encabezado_competencia_1)
                # print('encabezado_competencia_id',encabezado_competencia_id)
                if validacion_evaluacion_llenada== True and validacion_encabezado_competencia_1==True:
                    # print('entro a la validacion de los true')
                    if existe!=0:
                        put = evaluacion_encabezado.objects.get(id=pk)
                        serializer= evaluacion_encabezadoserializer(put,data=requets.data)
                        if serializer.is_valid():
                            serializer.save()

                            return Response(serializer.data,status=status.HTTP_200_OK)
                        else:
                            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response ('Las evaluaciones aún no han sido terminadas',status=status.HTTP_400_BAD_REQUEST)
        else:
            # print('entro al else')
        ###################################################################################
            if existe!=0:
                put = evaluacion_encabezado.objects.get(id=pk)
                serializer= evaluacion_encabezadoserializer(put,data=requets.data)
                if serializer.is_valid():
                    serializer.save()

                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
    

class detalle_evaluacion_factorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = detalle_evaluacion_factor.objects.all()
    serializer_class = detalle_evaluacion_factorserializer
    def list(self, request):
        queryset = detalle_evaluacion_factor.objects.all()
        serializer_class = detalle_evaluacion_factorserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='encabezado':
                        filter_kwargs['encabezado'] = filter
                    if tipo_busqueda =='metrica_factor':
                        filter_kwargs['metrica_factor'] = filter
                    if tipo_busqueda =='evaluacion_plantilla_competencia':
                        filter_kwargs['evaluacion_plantilla_competencia'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                        
                queryset =  detalle_evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  detalle_evaluacion_factor.objects.filter(**filter_kwargs).count()
                serializer = detalle_evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  detalle_evaluacion_factor.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  detalle_evaluacion_factor.objects.filter().count()
                serializer = detalle_evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='encabezado':
                        filter_kwargs['encabezado'] = filter
                    if tipo_busqueda =='metrica_factor':
                        filter_kwargs['metrica_factor'] = filter
                    if tipo_busqueda =='evaluacion_plantilla_competencia':
                        filter_kwargs['evaluacion_plantilla_competencia'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                        
                queryset =  detalle_evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')
                conteo =  detalle_evaluacion_factor.objects.filter(**filter_kwargs).count()
                serializer = detalle_evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  detalle_evaluacion_factor.objects.filter().order_by('id')
                conteo =  detalle_evaluacion_factor.objects.filter().count()
                serializer = detalle_evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = detalle_evaluacion_factorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= detalle_evaluacion_factor.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= detalle_evaluacion_factorserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class detalle_evaluacion_factor_indicadorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = detalle_evaluacion_factor_indicador.objects.all()
    serializer_class = detalle_evaluacion_factor_indicadorserializer
    def list(self, request):
        queryset = detalle_evaluacion_factor_indicador.objects.all()
        serializer_class = detalle_evaluacion_factor_indicadorserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='encabezado':
                        filter_kwargs['encabezado'] = filter
                    if tipo_busqueda =='factor':
                        filter_kwargs['factor'] = filter
                    if tipo_busqueda =='metrica_factor':
                        filter_kwargs['metrica_factor'] = filter
                    if tipo_busqueda =='evaluacion_plantilla_competencia':
                        filter_kwargs['evaluacion_plantilla_competencia'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                        
                queryset =  detalle_evaluacion_factor_indicador.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  detalle_evaluacion_factor_indicador.objects.filter(**filter_kwargs).count()
                serializer = detalle_evaluacion_factor_indicadorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  detalle_evaluacion_factor_indicador.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  detalle_evaluacion_factor_indicador.objects.filter().count()
                serializer = detalle_evaluacion_factor_indicadorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='encabezado':
                        filter_kwargs['encabezado'] = filter
                    if tipo_busqueda =='factor':
                        filter_kwargs['factor'] = filter
                    if tipo_busqueda =='metrica_factor':
                        filter_kwargs['metrica_factor'] = filter
                    if tipo_busqueda =='evaluacion_plantilla_competencia':
                        filter_kwargs['evaluacion_plantilla_competencia'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                        
                queryset =  detalle_evaluacion_factor_indicador.objects.filter(**filter_kwargs).order_by('id')
                conteo =  detalle_evaluacion_factor_indicador.objects.filter(**filter_kwargs).count()
                serializer = detalle_evaluacion_factor_indicadorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  detalle_evaluacion_factor_indicador.objects.filter().order_by('id')
                conteo =  detalle_evaluacion_factor_indicador.objects.filter().count()
                serializer = detalle_evaluacion_factor_indicadorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = detalle_evaluacion_factor_indicadorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= detalle_evaluacion_factor_indicador.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= detalle_evaluacion_factor_indicadorserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class evaluacion_despliegue_preguntas_competenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezado_preguntasserializer
    ##print(queryset)
    def list(self, request):
        queryset = evaluacion_encabezado.objects.all()
        serializer_class = evaluacion_encabezado_preguntasserializer(queryset, many=True)
        id=''
        clasificacion=''
        periodicidad=''
        pregunta=[]
        #competencias=[]
        estado_evaluacion=''
        nota_competencia_f=''
        categoria_desempenio_f=''
        tipo_evaluacion_encabezado=''
        if self.request.query_params.get('id'):
            id = self.request.query_params.get('id')
        
        if id!='':
            codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
            id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
            posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
            descriptor_encabezado = (evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado'))[0]['descriptor_empleado'] if evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado') else None
            if descriptor_encabezado==None:
                return Response({"Descriptor no encontrado en el encabezado"},status= status.HTTP_404_NOT_FOUND)
            
            descriptor= descriptor_perfil_datos_generales.objects.get(id=descriptor_encabezado) if descriptor_perfil_datos_generales.objects.filter(id=descriptor_encabezado) else None
            if descriptor==None:
                return Response({"Descriptor no existe"},status= status.HTTP_404_NOT_FOUND)


            clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
            #clasificacion=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id'))[0]['evaluado__clasificacion_empleado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id') else None
            #competencias=evaluacion_competencia.objects.filter(clasificacion_id=clasificacion).values_list('id', flat=True)          
            periodicidad=(evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id'))[0]['periodicidad__id'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id') else None          
            tipo_evaluacion_encabezado=(evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion_encabezado'))[0]['tipo_evaluacion_encabezado'] if evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion_encabezado') else None
            estado_evaluacion=(evaluacion_encabezado.objects.filter(id=id).values('estado'))[0]['estado'] if evaluacion_encabezado.objects.filter(id=id).values('estado') else None
            competencia_perfil_descriptor=descriptor_perfil_competencia_descriptor.objects.filter(descriptor_id=descriptor.id).values_list('id', flat=True)
            competencia_descriptor=evaluacion_competencia.objects.filter(periodicidad__id=periodicidad).filter(competencia__descriptor_perfil_competencia_descriptor__id__in=competencia_perfil_descriptor).distinct().values_list('id', flat=True)
            nota_competencia_f=(evaluacion_encabezado.objects.filter(id=id).values('nota_total_porcentaje_prorateo'))[0]['nota_total_porcentaje_prorateo'] if evaluacion_encabezado.objects.filter(id=id).values('nota_total_porcentaje_prorateo') else None
            if nota_competencia_f!='' and nota_competencia_f!=None:
                categoria_desempenio_f= (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=nota_competencia_f, valor_maximo__gte=nota_competencia_f).values('descripcion'))[0]['descripcion'] if (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=nota_competencia_f, valor_maximo__gte=nota_competencia_f).values('descripcion')) else 'Sin categorizaciòn'
        # print(periodicidad)
        # nueva_competencias=[]

        # if competencias==None:
        #     return Response({"Competencias no encontradas"},status= status.HTTP_404_NOT_FOUND)
        # else:
        #     if len(competencias)!=0:
        #         for item in competencias:
        #             if item not in nueva_competencias:
        #                 if item!=None:
        #                     nueva_competencias.append(item)

        data={}
       
        if tipo_evaluacion_encabezado==1:    
            if clasificacion!=None:
                if periodicidad!=None:
                    for competencia in competencia_descriptor:
                        # print("codigo_empleado",codigo_empleado)
                        # print("competencia",competencia)
                        # print('############## clasficiacion',clasificacion)
                        # print('############## descriptor',descriptor)
                        # print('############## competencia_perfil_descriptor',competencia_perfil_descriptor)
                        # print('############## descriptor_competencia',competencia_descriptor)
                        listado_pregunta_competencia=list(evaluacion_plantilla_competencia.objects.filter(competencia__clasificacion=clasificacion).filter(competencia__id=competencia).filter(periodicidad__id=periodicidad).values('pregunta',idCompetencia=F('competencia__competencia__id'),nombreCompetencia=F('competencia__competencia__nombre'),descripcionCompetencia=F('competencia__competencia__descripcion'),idClasificacion=F('competencia__clasificacion'),idPlantilla=F('id')))
                        #listado_competencia_descriptor=list(evaluacion_plantilla_competencia.objects.filter(clasificacion_id=clasificacion).values(idCompetencia=F('competencia__competencia__id')))
                        # print(('############## listado_pregunta_competencia',listado_pregunta_competencia))
                        for lista in listado_pregunta_competencia:
                            metrica_competencia_id_x= detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia=lista['idPlantilla']).filter(encabezado=id).values('metrica_competencia','metrica_competencia__grado')
                            if metrica_competencia_id_x:
                                lista['idMetrica']=metrica_competencia_id_x[0]['metrica_competencia']
                                lista['grado']=metrica_competencia_id_x[0]['metrica_competencia__grado']
                            else:
                                lista['idMetrica']=None
                                lista['grado']=None

                        pregunta.append(listado_pregunta_competencia)
                    if pregunta==None:
                        return Response({"Preguntas no encontradas"},status= status.HTTP_404_NOT_FOUND)
                    else:
                        data['data']= pregunta
                        data['estado_evaluacion']= estado_evaluacion
                        data['nota_competencia']= nota_competencia_f
                        data['categoria_desempenio']= categoria_desempenio_f
                        
                        return Response(data,status= status.HTTP_200_OK)
                else:
                    return Response({"Periodicidad no encontrada"},status= status.HTTP_404_NOT_FOUND)
            else:
                return Response({"Clasificacion no encontrada"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"El encabezado ingresado, no posee competencias, ya que es de tipo factor"},status= status.HTTP_404_NOT_FOUND)
        




    def update(self,requets,pk):
        #print(self)
        #print(requets)
        datax=[]
        obj=self.get_object()
        existe= evaluacion_encabezado.objects.filter(id=obj.id).count()
        if existe!=0:
            respuestas=''
            respuestas=self.request.data["respuesta_competencia"]
            put = self.get_object()
            for datos in respuestas:
                #print(datos)       
                serializer= evaluacion_encabezado_preguntasserializer(put,data=datos)
                if serializer.is_valid():
                    #serializer.save()
                    obj, created = detalle_evaluacion_competencia.objects.update_or_create(
                    encabezado_id=datos["encabezado"],
                    evaluacion_plantilla_competencia_id=datos["evaluacion_plantilla_competencia"],
                    defaults={
                        "metrica_competencia_id":datos["metrica_competencia"],
                    }
                )                    
                else:
                    return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        validacion_evaluacion_completada=validacion_evaluacion_competencia(pk)
        if validacion_evaluacion_completada==True:
            try:
                calculo_calificacion_competencia(pk)
                encabezado= evaluacion_encabezado.objects.get(id=pk) if evaluacion_encabezado.objects.filter(id=pk) else None
                if encabezado!=None:#este codigo lleva la fecha de la evaluacion
                    encabezado_evaluado= (evaluacion_encabezado.objects.filter(id=pk).values('evaluado'))[0]['evaluado'] if evaluacion_encabezado.objects.filter(id=pk).values('evaluado') else None
                    encabezado_periodicidad=  (evaluacion_encabezado.objects.filter(id=pk).values('periodicidad'))[0]['periodicidad'] if evaluacion_encabezado.objects.filter(id=pk).values('periodicidad') else None
                    encabezado_periodo =  (evaluacion_encabezado.objects.filter(id=pk).values('periodo'))[0]['periodo'] if evaluacion_encabezado.objects.filter(id=pk).values('periodo') else None
                    encabezado_tipo_evaluacion =  (evaluacion_encabezado.objects.filter(id=pk).values('tipo_evaluacion__id'))[0]['tipo_evaluacion__id'] if evaluacion_encabezado.objects.filter(id=pk).values('tipo_evaluacion__id') else None
                    #########################################################################################################################
                    fecha_evalua=evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=2).update(fecha_evaluacion=datetime.now().date()) if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=2) else None
                    encabezado_factor_id=(evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=2).values('id'))[0]['id'] if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=2) else None
                    validacion_encabezado_factor=validacion_evaluacion_factor(encabezado_factor_id)
                    tipo_e=(evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=2).values('tipo_evaluacion__nombre'))[0]['tipo_evaluacion__nombre'] if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=2) else None
                    #print('validacion_evaluacion_completada',validacion_evaluacion_completada)
                    #print('validacion_encabezado_factor',validacion_encabezado_factor)
                    #print('tipo_e',tipo_e)
                    #print('encabezado_factor_id',encabezado_factor_id)
                    if validacion_encabezado_factor== True and validacion_evaluacion_completada==True and tipo_e=='0°':
                        funcion_correo_evaluacion(encabezado_factor_id,'Jefe: Colaborador realizo su autoevaluación') 
            except BadHeaderError:
                raise Http404  
              

        
        id=pk
        clasificacion=''
        periodicidad=''
        pregunta=[]
        #competencias=[]
        estado_evaluacion=''
        nota_competencia_f=''
        categoria_desempenio_f=''
        tipo_evaluacion_encabezado=''
        if self.request.query_params.get('id'):
            id = self.request.query_params.get('id')
        
        if id!='':
            codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
            id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
            posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
            descriptor_encabezado = (evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado'))[0]['descriptor_empleado'] if evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado') else None
            if descriptor_encabezado==None:
                return Response({"Descriptor no encontrado en el encabezado"},status= status.HTTP_404_NOT_FOUND)
            
            descriptor= descriptor_perfil_datos_generales.objects.get(id=descriptor_encabezado) if descriptor_perfil_datos_generales.objects.filter(id=descriptor_encabezado) else None
            if descriptor==None:
                return Response({"Descriptor no existe"},status= status.HTTP_404_NOT_FOUND)
            
            clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
            #clasificacion=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id'))[0]['evaluado__clasificacion_empleado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id') else None
            #competencias=evaluacion_competencia.objects.filter(clasificacion_id=clasificacion).values_list('id', flat=True)          
            periodicidad=(evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id'))[0]['periodicidad__id'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id') else None          
            tipo_evaluacion_encabezado=(evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion_encabezado'))[0]['tipo_evaluacion_encabezado'] if evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion_encabezado') else None
            estado_evaluacion=(evaluacion_encabezado.objects.filter(id=id).values('estado'))[0]['estado'] if evaluacion_encabezado.objects.filter(id=id).values('estado') else None
            competencia_perfil_descriptor=descriptor_perfil_competencia_descriptor.objects.filter(descriptor_id=descriptor.id).values_list('id', flat=True)
            competencia_descriptor=evaluacion_competencia.objects.filter(periodicidad__id=periodicidad).filter(competencia__descriptor_perfil_competencia_descriptor__id__in=competencia_perfil_descriptor).distinct().values_list('id', flat=True)
            nota_competencia_f=(evaluacion_encabezado.objects.filter(id=id).values('nota_total_porcentaje_prorateo'))[0]['nota_total_porcentaje_prorateo'] if evaluacion_encabezado.objects.filter(id=id).values('nota_total_porcentaje_prorateo') else None
            if nota_competencia_f!='' and nota_competencia_f!=None:
                categoria_desempenio_f= (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=nota_competencia_f, valor_maximo__gte=nota_competencia_f).values('descripcion'))[0]['descripcion'] if (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=nota_competencia_f, valor_maximo__gte=nota_competencia_f).values('descripcion')) else 'Sin categorizaciòn'
        # print(periodicidad)
        # nueva_competencias=[]

        # if competencias==None:
        #     return Response({"Competencias no encontradas"},status= status.HTTP_404_NOT_FOUND)
        # else:
        #     if len(competencias)!=0:
        #         for item in competencias:
        #             if item not in nueva_competencias:
        #                 if item!=None:
        #                     nueva_competencias.append(item)

        data={}
       
        if tipo_evaluacion_encabezado==1:    
            if clasificacion!=None:
                if periodicidad!=None:
                    for competencia in competencia_descriptor:
                        # print("codigo_empleado",codigo_empleado)
                        # print("competencia",competencia)
                        # print('############## clasficiacion',clasificacion)
                        # print('############## descriptor',descriptor)
                        # print('############## competencia_perfil_descriptor',competencia_perfil_descriptor)
                        # print('############## descriptor_competencia',competencia_descriptor)
                        listado_pregunta_competencia=list(evaluacion_plantilla_competencia.objects.filter(competencia__clasificacion=clasificacion).filter(competencia__id=competencia).filter(periodicidad__id=periodicidad).values('pregunta',idCompetencia=F('competencia__competencia__id'),nombreCompetencia=F('competencia__competencia__nombre'),descripcionCompetencia=F('competencia__competencia__descripcion'),idClasificacion=F('competencia__clasificacion'),idPlantilla=F('id')))
                        #listado_competencia_descriptor=list(evaluacion_plantilla_competencia.objects.filter(clasificacion_id=clasificacion).values(idCompetencia=F('competencia__competencia__id')))
                        # print(('############## listado_pregunta_competencia',listado_pregunta_competencia))
                        for lista in listado_pregunta_competencia:
                            metrica_competencia_id_x= detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia=lista['idPlantilla']).filter(encabezado=id).values('metrica_competencia','metrica_competencia__grado')
                            if metrica_competencia_id_x:
                                lista['idMetrica']=metrica_competencia_id_x[0]['metrica_competencia']
                                lista['grado']=metrica_competencia_id_x[0]['metrica_competencia__grado']
                            else:
                                lista['idMetrica']=None
                                lista['grado']=None

                        pregunta.append(listado_pregunta_competencia)
                    if pregunta==None:
                        return Response({"Preguntas no encontradas"},status= status.HTTP_404_NOT_FOUND)
                    else:
                        data['data']= pregunta
                        data['estado_evaluacion']= estado_evaluacion
                        data['nota_competencia']= nota_competencia_f
                        data['categoria_desempenio']= categoria_desempenio_f
                        

                        return Response(data,status= status.HTTP_200_OK)
                else:
                    return Response({"Periodicidad no encontrada"},status= status.HTTP_404_NOT_FOUND)
            else:
                return Response({"Clasificacion no encontrada"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"El encabezado ingresado, no posee competencias, ya que es de tipo factor"},status= status.HTTP_404_NOT_FOUND)
                


           
class evaluacion_factor_plantilla_encabezadoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_factor_plantilla_encabezado.objects.all()
    serializer_class = evaluacion_factor_plantilla_encabezadoserializer
    def list(self, request):
        queryset = evaluacion_factor_plantilla_encabezado.objects.all()
        serializer = evaluacion_factor_plantilla_encabezadoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        
        if self.request.query_params.get('filter_2'):
            filter_2 = self.request.query_params.get('filter_2')

        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')
        
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_empresa_nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_empresa_id':
                        filter_kwargs['periodicidad__empresa'] = filter
                    if tipo_busqueda =='frecuencia_nombre':
                        filter_kwargs['periodicidad__frecuencia__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_fecha_fin':
                        filter_kwargs['periodicidad__fecha_fin__icontains'] = filter
                    if tipo_busqueda =='periodicidad_fecha_creacion':
                        filter_kwargs['periodicidad__fecha_creacion__icontains'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_id':
                            filter_kwargs_2['periodicidad__empresa'] = filter_2
                        if tipo_busqueda_2 =='frecuencia_nombre':
                            filter_kwargs_2['periodicidad__frecuencia__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_fecha_fin':
                            filter_kwargs_2['periodicidad__fecha_fin__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_fecha_creacion':
                            filter_kwargs_2['periodicidad__fecha_creacion__icontains'] = filter_2   
                    
                    queryset =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_factor_plantilla_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_factor_plantilla_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

                queryset =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_factor_plantilla_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else:
                data=[]
                c=0 
                return Response({"data":data,"count":c})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_empresa_nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_empresa_id':
                        filter_kwargs['periodicidad__empresa'] = filter
                    if tipo_busqueda =='frecuencia_nombre':
                        filter_kwargs['periodicidad__frecuencia__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_fecha_fin':
                        filter_kwargs['periodicidad__fecha_fin__icontains'] = filter
                    if tipo_busqueda =='periodicidad_fecha_creacion':
                        filter_kwargs['periodicidad__fecha_creacion__icontains'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_id':
                            filter_kwargs_2['periodicidad__empresa'] = filter_2
                        if tipo_busqueda_2 =='frecuencia_nombre':
                            filter_kwargs_2['periodicidad__frecuencia__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_fecha_fin':
                            filter_kwargs_2['periodicidad__fecha_fin__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_fecha_creacion':
                            filter_kwargs_2['periodicidad__fecha_creacion__icontains'] = filter_2 
                    queryset =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_factor_plantilla_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_factor_plantilla_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

               
                queryset =  evaluacion_factor_plantilla_encabezado.objects.filter(**filter_kwargs).order_by('id') 
                serializer = evaluacion_factor_plantilla_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                data=[]
                c=0 
                return Response({"data":data,"count":c})

    def create(self, request):
        hoy=datetime.now().date()
        año= hoy.year
        
        validacion_empresa = evaluacion_factor_plantilla_encabezado.objects.filter(periodicidad=self.request.data['periodicidad']) if evaluacion_factor_plantilla_encabezado.objects.filter(periodicidad=self.request.data['periodicidad']) else None
        if validacion_empresa!=None:
            return Response({'Esta periodicidad ya está siendo utilizada en otro encabezado de plantilla vigente'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = evaluacion_factor_plantilla_encabezadoserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self,request,pk):

        
        area = evaluacion_factor_plantilla_encabezado.objects.filter(pk=pk).values() if evaluacion_factor_plantilla_encabezado.objects.filter(pk=pk) else None

        
        if area:
            plantilla_encabezado= evaluacion_factor_plantilla_encabezado.objects.get(pk=pk)
            if plantilla_encabezado.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=plantilla_encabezado.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=plantilla_encabezado.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=plantilla_encabezado.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=plantilla_encabezado.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_factor_plantilla_encabezado.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)



 
class evaluacion_competencia_plantilla_encabezadoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_competencia_plantilla_encabezado.objects.all()
    serializer_class = evaluacion_competencia_plantilla_encabezadoserializer
    def list(self, request):
        queryset = evaluacion_competencia_plantilla_encabezado.objects.all()
        serializer = evaluacion_competencia_plantilla_encabezadoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''
        tipo_busqueda_2=''
        
        if self.request.query_params.get('filter_2'):
            filter_2 = self.request.query_params.get('filter_2')

        if self.request.query_params.get('tipo_busqueda_2'):
            tipo_busqueda_2 = self.request.query_params.get('tipo_busqueda_2')
        
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_empresa_nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_empresa_id':
                        filter_kwargs['periodicidad__empresa'] = filter
                    if tipo_busqueda =='frecuencia_nombre':
                        filter_kwargs['periodicidad__frecuencia__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_fecha_fin':
                        filter_kwargs['periodicidad__fecha_fin__icontains'] = filter
                    if tipo_busqueda =='periodicidad_fecha_creacion':
                        filter_kwargs['periodicidad__fecha_creacion__icontains'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_id':
                            filter_kwargs_2['periodicidad__empresa'] = filter_2
                        if tipo_busqueda_2 =='frecuencia_nombre':
                            filter_kwargs_2['periodicidad__frecuencia__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_fecha_fin':
                            filter_kwargs_2['periodicidad__fecha_fin__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_fecha_creacion':
                            filter_kwargs_2['periodicidad__fecha_creacion__icontains'] = filter_2   
                    
                    queryset =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_competencia_plantilla_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_competencia_plantilla_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

                queryset =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).count()
                serializer = evaluacion_competencia_plantilla_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                data=[]
                c=0 
                return Response({"data":data,"count":c})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_empresa_nombre':
                        filter_kwargs['periodicidad__empresa__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_empresa_id':
                        filter_kwargs['periodicidad__empresa'] = filter
                    if tipo_busqueda =='frecuencia_nombre':
                        filter_kwargs['periodicidad__frecuencia__nombre__icontains'] = filter
                    if tipo_busqueda =='periodicidad_fecha_fin':
                        filter_kwargs['periodicidad__fecha_fin__icontains'] = filter
                    if tipo_busqueda =='periodicidad_fecha_creacion':
                        filter_kwargs['periodicidad__fecha_creacion__icontains'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_nombre':
                            filter_kwargs_2['periodicidad__empresa__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_empresa_id':
                            filter_kwargs_2['periodicidad__empresa'] = filter_2
                        if tipo_busqueda_2 =='frecuencia_nombre':
                            filter_kwargs_2['periodicidad__frecuencia__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_fecha_fin':
                            filter_kwargs_2['periodicidad__fecha_fin__icontains'] = filter_2
                        if tipo_busqueda_2 =='periodicidad_fecha_creacion':
                            filter_kwargs_2['periodicidad__fecha_creacion__icontains'] = filter_2 
                    queryset =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = evaluacion_competencia_plantilla_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).count()
                    serializer = evaluacion_competencia_plantilla_encabezadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

               
                queryset =  evaluacion_competencia_plantilla_encabezado.objects.filter(**filter_kwargs).order_by('id') 
                serializer = evaluacion_competencia_plantilla_encabezadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                data=[]
                c=0 
                return Response({"data":data,"count":c})

    
    def create(self, request):
        hoy=datetime.now().date()
        año= hoy.year
        
        validacion_empresa = evaluacion_competencia_plantilla_encabezado.objects.filter(periodicidad=self.request.data['periodicidad']) if evaluacion_competencia_plantilla_encabezado.objects.filter(periodicidad=self.request.data['periodicidad']) else None
        if validacion_empresa!=None:
            return Response({'Esta periodicidad ya está siendo utilizada en otro encabezado de plantilla vigente'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = evaluacion_competencia_plantilla_encabezadoserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):

        area = evaluacion_competencia_plantilla_encabezado.objects.filter(pk=pk).values() if evaluacion_competencia_plantilla_encabezado.objects.filter(pk=pk) else None

        
        if area:
            plantilla_encabezado= evaluacion_competencia_plantilla_encabezado.objects.get(pk=pk)
            if plantilla_encabezado.periodicidad!=None:
                validacion_periodicidad_competencia=detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=plantilla_encabezado.periodicidad.pk) if detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__periodicidad_id=plantilla_encabezado.periodicidad.pk) else None
                validacion_periodicidad_factor=detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=plantilla_encabezado.periodicidad.pk) if detalle_evaluacion_factor.objects.filter(evaluacion_plantilla_factor__periodicidad_id=plantilla_encabezado.periodicidad.pk) else None 
                if validacion_periodicidad_competencia!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                if validacion_periodicidad_factor!=None:
                    return Response({"La periodicidad esta siendo utilizada"}, status=status.HTTP_400_BAD_REQUEST)

                

            queryset = evaluacion_competencia_plantilla_encabezado.objects.get(pk=pk).delete()
            #print('se elimino')
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El area no existe"},status=status.HTTP_404_NOT_FOUND)



class copiado_evaluacion_plantilla_competencia(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none()
    def post(self,request):
        id =''
        hoy=datetime.now().date()
        if self.request.data['id']:
            id = self.request.data['id']

        encabezado_seleccionado=evaluacion_competencia_plantilla_encabezado.objects.get(id=id) if evaluacion_competencia_plantilla_encabezado.objects.filter(id=id) else None 
        if encabezado_seleccionado==None:
            return Response({"Resultado":"Este id no pertenece a ningun encabezado"},status= status.HTTP_404_NOT_FOUND)
        #print('easdasdasdas',encabezado_seleccionado.periodicidad.fecha_fin)
        
        # validacion para ver si existen las preguntas
        plantillas= evaluacion_plantilla_competencia.objects.filter(competencia_plantilla_encabezado=id).values_list('id',flat=True) if evaluacion_plantilla_competencia.objects.filter(competencia_plantilla_encabezado=id) else None
        if plantillas==None:
            return Response({"Resultado":"Este encabezado no tiene preguntas para utilizar"},status= status.HTTP_404_NOT_FOUND)

        #busca una periodicidad actual para ese tipo de empresa, tipo de evaluacion y que se encuentre vigente
        periodicidad_actual= evaluacion_periodicidad.objects.filter(empresa=encabezado_seleccionado.periodicidad.empresa.id).filter(fecha_fin__gt=hoy).values('id') if evaluacion_periodicidad.objects.filter(empresa=encabezado_seleccionado.periodicidad.empresa.id).filter(fecha_fin__gt=hoy) else None
        #print('periodicidad actual',periodicidad_actual_id)
        if periodicidad_actual==None:
            return Response({"Resultado":"No se encontró una periodicidad vigente para esta empresa y tipo de evaluación "},status= status.HTTP_404_NOT_FOUND)
        
        periodicidad_actual_id=int(periodicidad_actual[0]['id'])
        instancia_periodicidad= evaluacion_periodicidad.objects.get(id=periodicidad_actual_id) if evaluacion_periodicidad.objects.filter(id=periodicidad_actual_id) else None 
        #verificacion para ver si la periodicidad_actual encontrada anteriormente no esta siendo utilizada ya en un competencia_plantilla_encabezado
        verificacion_periodicidad_encabezado=evaluacion_competencia_plantilla_encabezado.objects.filter(periodicidad=(periodicidad_actual_id)) if evaluacion_competencia_plantilla_encabezado.objects.filter(periodicidad=periodicidad_actual_id) else None
        # #print('verificacion_periodicidad_encabezado',verificacion_periodicidad_encabezado)
        if verificacion_periodicidad_encabezado!=None:
            return Response({"Resultado":"Ya existe un encabezado de plantilla almacenando preguntas para esta empresa y tipo de evaluación"},status= status.HTTP_404_NOT_FOUND)



        nombre_enzabezado= encabezado_seleccionado.nombre
        nuevo_encabezado= evaluacion_competencia_plantilla_encabezado.objects.create(nombre=nombre_enzabezado,periodicidad=instancia_periodicidad)
        for plantilla_id in plantillas:
            plantilla = evaluacion_plantilla_competencia.objects.get(id=plantilla_id) if evaluacion_plantilla_competencia.objects.filter(id=plantilla_id) else None

            nueva_plantilla = evaluacion_plantilla_competencia.objects.create(periodicidad=instancia_periodicidad,pregunta=plantilla.pregunta,competencia=plantilla.competencia,competencia_plantilla_encabezado=nuevo_encabezado,clasificacion=plantilla.clasificacion,posicion=plantilla.posicion,competencia_descriptor=plantilla.competencia_descriptor)
        
        nombre_enzabezado_creado= evaluacion_competencia_plantilla_encabezado.objects.filter(id=nuevo_encabezado.pk)
        serializer = evaluacion_competencia_plantilla_encabezadoserializer(nombre_enzabezado_creado, many=True)
        return Response(serializer.data,status= status.HTTP_200_OK)
        # return Response({'sadf'},status= status.HTTP_200_OK)

class copiado_evaluacion_plantilla_factor(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none()
    def post(self,request):
        id =''
        hoy=datetime.now().date()
        if self.request.data['id']:
            id = self.request.data['id']

        encabezado_seleccionado=evaluacion_factor_plantilla_encabezado.objects.get(id=id) if evaluacion_factor_plantilla_encabezado.objects.filter(id=id) else None 
        if encabezado_seleccionado==None:
            return Response({"Resultado":"Este id no pertenece a ningun encabezado"},status= status.HTTP_404_NOT_FOUND)
        
        
        # validacion para ver si existen las preguntas
        plantillas= evaluacion_plantilla_factor.objects.filter(factor_plantilla_encabezado=id).values_list('id',flat=True) if evaluacion_plantilla_factor.objects.filter(factor_plantilla_encabezado=id) else None
        if plantillas==None:
            return Response({"Resultado":"Este encabezado no tiene preguntas para utilizar"},status= status.HTTP_404_NOT_FOUND)

        #busca una periodicidad actual para ese tipo de empresa, tipo de evaluacion y que se encuentre vigente
        periodicidad_actual= evaluacion_periodicidad.objects.filter(empresa=encabezado_seleccionado.periodicidad.empresa.id).filter(fecha_fin__gt=hoy).values('id') if evaluacion_periodicidad.objects.filter(empresa=encabezado_seleccionado.periodicidad.empresa.id).filter(fecha_fin__gt=hoy) else None
        if periodicidad_actual==None:
            return Response({"Resultado":"No se encontró una periodicidad vigente para esta empresa y tipo de evaluación "},status= status.HTTP_404_NOT_FOUND)
        
        periodicidad_actual_id=int(periodicidad_actual[0]['id'])
        instancia_periodicidad= evaluacion_periodicidad.objects.get(id=periodicidad_actual_id) if evaluacion_periodicidad.objects.filter(id=periodicidad_actual_id) else None 
        
        #verificacion para ver si la periodicidad_actual encontrada anteriormente no esta siendo utilizada ya en un competencia_plantilla_encabezado
        verificacion_periodicidad_encabezado=evaluacion_factor_plantilla_encabezado.objects.filter(periodicidad=periodicidad_actual_id) if evaluacion_factor_plantilla_encabezado.objects.filter(periodicidad=periodicidad_actual_id) else None
        
        if verificacion_periodicidad_encabezado!=None:
            return Response({"Resultado":"Ya existe un encabezado de plantilla almacenando preguntas para esta empresa y tipo de evaluación"},status= status.HTTP_404_NOT_FOUND)



        nombre_enzabezado= encabezado_seleccionado.nombre
        nuevo_encabezado= evaluacion_factor_plantilla_encabezado.objects.create(nombre=nombre_enzabezado,periodicidad=instancia_periodicidad)
        for plantilla_id in plantillas:
            plantilla = evaluacion_plantilla_factor.objects.get(id=plantilla_id) if evaluacion_plantilla_factor.objects.filter(id=plantilla_id) else None

            nueva_plantilla = evaluacion_plantilla_factor.objects.create(periodicidad=instancia_periodicidad,pregunta=plantilla.pregunta,factor=plantilla.factor,factor_plantilla_encabezado=nuevo_encabezado,clasificacion=plantilla.clasificacion,posicion=plantilla.posicion)
        
        nombre_enzabezado_creado= evaluacion_factor_plantilla_encabezado.objects.filter(id=nuevo_encabezado.pk)
        serializer = evaluacion_factor_plantilla_encabezadoserializer(nombre_enzabezado_creado, many=True)
        return Response(serializer.data,status= status.HTTP_200_OK)
        

class resumen_general_evaluacionesViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezadoserializer
    def list(self, request):
        hoy=datetime.now().date()
        filter_anio=''
        año= hoy.year
        
        id=''
        if self.request.query_params.get('id'):
            id = self.request.query_params.get('id')

        

        empresa =( evaluacion_encabezado.objects.filter(id=id).values('evaluado__unidad_organizativa__sociedad_financiera__nombre'))[0]['evaluado__unidad_organizativa__sociedad_financiera__nombre'] if  evaluacion_encabezado.objects.filter(id=id).values('evaluado__unidad_organizativa__sociedad_financiera__nombre') else None
        frecuencia= ( evaluacion_encabezado.objects.filter(id=id).values('periodicidad__frecuencia__nombre'))[0]['periodicidad__frecuencia__nombre'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__frecuencia__nombre') else None
        periodicidad= ( evaluacion_encabezado.objects.filter(id=id).values('periodicidad'))[0]['periodicidad'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad') else None
        tipo_evaluacion= ( evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion__nombre'))[0]['tipo_evaluacion__nombre'] if evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion__nombre') else None
        tipo_evaluacion_id= ( evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion__id'))[0]['tipo_evaluacion__id'] if evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion__id') else None
        # #print('tipo_evaluacion_id',tipo_evaluacion_id)
        #cambiar la fecha de evaluacion de fecha_creacion a fecha_inicio
        fecha_evaluacion=(evaluacion_encabezado.objects.filter(id=id).values('fecha_evaluacion'))[0]['fecha_evaluacion'] if evaluacion_encabezado.objects.filter(id=id).values('fecha_evaluacion') else None
        periodo= (evaluacion_encabezado.objects.filter(id=id).values('periodo'))[0]['periodo'] if evaluacion_encabezado.objects.filter(id=id).values('periodo') else None
        nombre_evaluado= (evaluacion_encabezado.objects.filter(id=id).values('evaluado__nombre'))[0]['evaluado__nombre'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__nombre') else None 
        funcion = (evaluacion_encabezado.objects.filter(id=id).values('evaluado__posicion__descripcion'))[0]['evaluado__posicion__descripcion'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__posicion__descripcion') else None
        departamento = (evaluacion_encabezado.objects.filter(id=id).values('evaluado__division__descripcion'))[0]['evaluado__division__descripcion'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__division__descripcion') else None
        evaluado= (evaluacion_encabezado.objects.filter(id=id).values('evaluado__id'))[0]['evaluado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__id') else None 
        archivo_id_documento= (evaluacion_encabezado.objects.filter(id=id).values('evaluacion_archivo_plan_accion_gestor__id_documento'))[0]['evaluacion_archivo_plan_accion_gestor__id_documento'] if evaluacion_encabezado.objects.filter(id=id).values('evaluacion_archivo_plan_accion_gestor__id_documento') else None 
        archivo_llave= (evaluacion_encabezado.objects.filter(id=id).values('evaluacion_archivo_plan_accion_gestor__llave'))[0]['evaluacion_archivo_plan_accion_gestor__llave'] if evaluacion_encabezado.objects.filter(id=id).values('evaluacion_archivo_plan_accion_gestor__llave') else None 
        archivo_origen= (evaluacion_encabezado.objects.filter(id=id).values('evaluacion_archivo_plan_accion_gestor__origen'))[0]['evaluacion_archivo_plan_accion_gestor__origen'] if evaluacion_encabezado.objects.filter(id=id).values('evaluacion_archivo_plan_accion_gestor__origen') else None 
        archivo_contentTypeGD= (evaluacion_encabezado.objects.filter(id=id).values('evaluacion_archivo_plan_accion_gestor__contentTypeGD'))[0]['evaluacion_archivo_plan_accion_gestor__contentTypeGD'] if evaluacion_encabezado.objects.filter(id=id).values('evaluacion_archivo_plan_accion_gestor__contentTypeGD') else None 
        tipo_plan_accion_id=(evaluacion_encabezado.objects.filter(id=id).values('tipo_plan_accion'))[0]['tipo_plan_accion'] if evaluacion_encabezado.objects.filter(id=id).values('tipo_plan_accion') else None 
        tipo_plan_accion_obj=evaluacion_tipo_plan_accion.objects.filter(id=tipo_plan_accion_id).values() if evaluacion_tipo_plan_accion.objects.filter(id=tipo_plan_accion_id) else None
        #######
        configuracion_periodo_id=(evaluacion_encabezado.objects.filter(id=id,periodicidad__evaluacion_configuracion_periodo__tipo_evaluacion=tipo_evaluacion_id).values('periodicidad__evaluacion_configuracion_periodo__id'))[0]['periodicidad__evaluacion_configuracion_periodo__id']
        evaluadores = (evaluacion_encabezado.objects.filter(evaluado=evaluado,periodicidad=periodicidad,periodicidad__evaluacion_configuracion_periodo=configuracion_periodo_id,tipo_evaluacion__id=tipo_evaluacion_id).values_list('evaluador__codigo',flat=True).distinct())
        #######
        jefe_evaluado_codigo_f=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__jefe_inmediato'))[0]['evaluado__jefe_inmediato'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__jefe_inmediato') else None 
        jefe_evaluado_nombre=(Funcional_empleado.objects.filter(codigo=jefe_evaluado_codigo_f).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=jefe_evaluado_codigo_f).values('nombre') else None
        tipo_evaluacion_nombre= ( evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion__nombre'))[0]['tipo_evaluacion__nombre'] if evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion__nombre') else None
        metricas_factor = evaluacion_metrica_factor.objects.filter(periodicidad=periodicidad).order_by('id').values_list('descripcion',flat=True) if evaluacion_metrica_factor.objects.filter(periodicidad=periodicidad).order_by('id').values_list('descripcion',flat=True) else None
        # #print('nombrenombre',tipo_evaluacion_nombre)
        comentario_evaluado= ''
        comentario_evaluador=''
        listado_evaluadores=[]
        for evaluador in evaluadores:
            if tipo_evaluacion_nombre=='0°':
                nombre = (Funcional_empleado.objects.filter(id=evaluado).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(id=evaluado).values('nombre') else None
                Funcion_evaluador = (Funcional_empleado.objects.filter(id=evaluado).values('posicion__descripcion'))[0]['posicion__descripcion'] if Funcional_empleado.objects.filter(id=evaluado).values('posicion__descripcion') else None  
                listado_evaluadores_obj={'Evaluador':nombre,"Relación":"Autoevaluación","Función":Funcion_evaluador}
                listado_evaluadores.append(listado_evaluadores_obj)
            
            elif tipo_evaluacion_nombre=='90°':
                codigo_jefe = (Funcional_empleado.objects.filter(id=evaluado).values('jefe_inmediato'))[0]['jefe_inmediato'] if Funcional_empleado.objects.filter(id=evaluado).values('jefe_inmediato') else None 
                nombre = (Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None 
                Funcion_evaluador= (Funcional_empleado.objects.filter(codigo=codigo_jefe).values('posicion__descripcion'))[0]['posicion__descripcion'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('posicion__descripcion') else None 
                listado_evaluadores_obj={'Evaluador':nombre,"Relación":"Jefe inmediato","Función":Funcion_evaluador}
                listado_evaluadores.append(listado_evaluadores_obj)

        # calculo de nota competencia
        nota_total_competencia=''
        nota_total_competencia_desempeno=''
        nota_total_factor=''
        nota_total_factor_desempenio=''
        total_desempenio=''
        desempenio=''
        matriz_marcas_factor=''
        encabezado_competencia_id=''
        lista_competencias_puntajes_y_esperado=''
        # #print('periodicidad',periodicidad)
        resultados_evaluaciones=list(evaluacion_encabezado.objects.filter(evaluado=evaluado,periodicidad=periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=periodo,tipo_evaluacion__id=tipo_evaluacion_id).values('id','tipo_evaluacion_encabezado')) if evaluacion_encabezado.objects.filter(evaluado=evaluado,periodicidad=periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=periodo,tipo_evaluacion__id=tipo_evaluacion_id).values('id','tipo_evaluacion_encabezado') else None
        if  resultados_evaluaciones!=None:
            for x in resultados_evaluaciones:
                id_encabezado = x['id']
                id_tipo_evaluacion=x['tipo_evaluacion_encabezado']
                
                if id_tipo_evaluacion==1:
                    # #print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                    # #print('id_encabezado',id_encabezado)
                    # #print('id_tipo_evaluacion',id_tipo_evaluacion)
                    nota_competencia= evaluacion_encabezado.objects.filter(id=id_encabezado).values('nota_total_porcentaje_prorateo','nivel_resultado')
                    nota_total_competencia =nota_competencia[0]['nota_total_porcentaje_prorateo']
                    nota_total_competencia_desempeno=nota_competencia[0]['nivel_resultado']
                    encabezado_competencia_id=id_encabezado


                if id_tipo_evaluacion==2:
                    # #print('##################################')
                    # #print('id_encabezado',id_encabezado)
                    # #print('id_tipo_evaluacion',id_tipo_evaluacion)
                    nota_factor= evaluacion_encabezado.objects.filter(id=id_encabezado).values('nota_total_porcentaje','nivel_resultado')
                    nota_total_factor = nota_factor[0]['nota_total_porcentaje']
                    nota_total_factor_desempenio = nota_factor[0]['nivel_resultado']
                    matriz_marcas_factor= calcular_matriz_marcas_evaluacion_factor(id_encabezado)
                    comentario_evaluado= (evaluacion_encabezado.objects.filter(id=id_encabezado).values('comentario_evaluado'))[0]['comentario_evaluado'] if evaluacion_encabezado.objects.filter(id=id_encabezado).values('comentario_evaluado') else None
                    comentario_evaluador= evaluacion_encabezado.objects.filter(id=id_encabezado).values('comentario_evaluador')[0]['comentario_evaluador'] if evaluacion_encabezado.objects.filter(id=id_encabezado).values('comentario_evaluador') else None 

            if nota_total_competencia!=None and nota_total_factor!=None:
                total_desempenio= (int(nota_total_competencia)+int(nota_total_factor))/2
                desempenio = (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=total_desempenio, valor_maximo__gte=total_desempenio).values('descripcion'))[0]['descripcion'] if (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=total_desempenio, valor_maximo__gte=total_desempenio).values('descripcion')) else 'Sin categorizaciòn'
            else:
                total_desempenio='Aun faltan evaluaciones'
                desempenio='Aun faltan evaluaciones'
                
            lista_competencias_puntajes_y_esperado = detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_competencia_id).values_list('evaluacion_plantilla_competencia__competencia__competencia__id', flat=True).order_by('evaluacion_plantilla_competencia__competencia__competencia__nombre').distinct()
            

        data={}
        datasets=[]
        datasets.extend([
            {   'empresa': empresa,
                'frecuencia':frecuencia,
                'periodicidad':periodicidad,
                'tipo_evaluacion':tipo_evaluacion_nombre,
                'fecha_evaluacion':fecha_evaluacion,
                'periodo':periodo,
                'evaluado':evaluado,
                'nombre':nombre_evaluado,
                'funcion':funcion,
                'departamento':departamento,
                'evaluadores':listado_evaluadores,
                'nota_total_competencia':nota_total_competencia if nota_total_competencia!=None else 'Aun no hay una nota total para competencias' ,
                'nota_total_competencia_desempeno':nota_total_competencia_desempeno if nota_total_competencia_desempeno!=None else 'Aun no existe una categorización' ,
                'nota_total_factor':nota_total_factor if nota_total_factor!=None else 'Aun no hay una nota total para factor',
                'nota_total_factor_desempenio':nota_total_factor_desempenio if nota_total_factor_desempenio!=None else  'Aun no existe una categorización' ,
                'total_desempenio':total_desempenio if total_desempenio!=None else 'Aun no hay una nota total',
                'desempenio':desempenio if desempenio!=None else 'Aun no existe una categorización',
                'comentario_evaluado':comentario_evaluado,
                'comentario_evaluador':comentario_evaluador,
                'archivo_id_documento':archivo_id_documento,
                'archivo_llave':archivo_llave,
                'archivo_contentTypeGD':archivo_contentTypeGD,
                'archivo_origen':archivo_origen,
                'tipo_plan_accion_obj':tipo_plan_accion_obj,
                'jefe_evaluado_nombre':jefe_evaluado_nombre
                


                
            },
        ])
        data['data']=datasets
    
        
        ###################################################################################################
        lista_nombre_competencia=[]
        lista_nota_obtenida=[]
        lista_nota_esperada=[]
        matriz_de_competencia=[]
        for descriptor_perfil_competencia_id in lista_competencias_puntajes_y_esperado:
            # #print('descriptor_perfil_competencia_id',descriptor_perfil_competencia_id)
            puntaje_obtenido=0
            acumulador_puntaje_obtenido=0
            puntaje_esperado=0
            nombre_competencia=''

            puntaje_obtenido=(detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_competencia_id,evaluacion_plantilla_competencia__competencia__competencia__id=descriptor_perfil_competencia_id).values('nota_competencia_prorateada_decimal'))[0]['nota_competencia_prorateada_decimal'] if detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_competencia_id,evaluacion_plantilla_competencia__competencia__competencia__id=descriptor_perfil_competencia_id).values('nota_competencia_prorateada_decimal') else None
            # #print('puntopuntopuntopuntopuntopunto',puntos)
            conteo_puntaje_obtenido=0
            # if not None in puntos:
            #     for punto in puntos:
                    
            #         acumulador_puntaje_obtenido+=punto
            #         conteo_puntaje_obtenido+=1
            #     puntaje_obtenido= round(acumulador_puntaje_obtenido/conteo_puntaje_obtenido)
            # else:
            #     puntaje_obtenido=None
            ############################################################################################
            esperado=detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_competencia_id,evaluacion_plantilla_competencia__competencia__competencia__id=descriptor_perfil_competencia_id).values_list('evaluacion_plantilla_competencia__competencia__desempeno_esperado',flat=True).distinct() 
            for nota in esperado:
                puntaje_esperado=nota

            #################################################################################################

            nombre=(detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_competencia_id,evaluacion_plantilla_competencia__competencia__competencia__id=descriptor_perfil_competencia_id).values('evaluacion_plantilla_competencia__competencia__competencia__nombre'))[0]['evaluacion_plantilla_competencia__competencia__competencia__nombre'] if detalle_evaluacion_competencia.objects.filter(encabezado_id=encabezado_competencia_id,evaluacion_plantilla_competencia__competencia__competencia__id=descriptor_perfil_competencia_id).values('evaluacion_plantilla_competencia__competencia__competencia__nombre') else None
            nombre_competencia= nombre

            semaforo=0
            if puntaje_obtenido!=None:
                if puntaje_obtenido>=puntaje_esperado:
                    semaforo=0
                else:
                    semaforo=1
            else:
                semaforo='Aun no evaluado'
            data_matriz={"puntaje_obtenido":puntaje_obtenido,"puntaje_esperado":puntaje_esperado,"nombre_competencia":nombre_competencia,"semaforo":semaforo}
            matriz_de_competencia.append(data_matriz)
            lista_nombre_competencia.append(nombre_competencia)
            lista_nota_obtenida.append(puntaje_obtenido)
            lista_nota_esperada.append(puntaje_esperado)


            #print('###################################################')

        

        data_2={
            'labels':lista_nombre_competencia ,
            'datasets': [
            {
                'label': "Puntaje",
                'backgroundColor': "rgba(4, 127, 243)",
                'borderColor': "rgb(14, 127, 243)",
                'data': lista_nota_obtenida,
            },
            {
                'label': "Esperado",
                'backgroundColor': "rgba(243, 87, 4)",
                'borderColor': "rgb(243, 87, 4)",
                'data':lista_nota_esperada,
            },
            ],
        }

        for marcas in matriz_marcas_factor:
            marcas['puntuaciones']=[marcas['INF'],marcas['INT'],marcas['TM'],marcas['STM'],marcas['SUP']]

        return Response({'informacion':data,'matriz_marcas_factor':matriz_marcas_factor,'matriz_competencia':matriz_de_competencia,'dashboard':data_2,"metricas_factor":metricas_factor},status= status.HTTP_200_OK) 
        
class calculo_calificaciones(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none()
    def post(self,request):
        

        competencia_encabezado_id=int(request.data["competencia_encabezado_id"])
        factor_encabezado_id=int(request.data["factor_encabezado_id"])
        calculo_calificacion_competencia(competencia_encabezado_id)
        calculo_calificacion_factor(factor_encabezado_id)

        return Response(request.data,status= status.HTTP_200_OK)


class correo_evaluaciones(APIView):
    authentication_classes=[TokenAuthentication]

    def post(self,request):
        notificaciones = self.request.data['data']
        modulo='EVALUACION_DESEMPENIO'
        id=''
        tipo_mensaje=''
        fun=''
        
        
        for variable in notificaciones:
            
            
            if "id" in variable:
                id = variable['id']
            
            if "tipo_mensaje" in variable:
                tipo_mensaje = variable['tipo_mensaje']
                
            if id!='' and tipo_mensaje!='':
                fun = funcion_correo_evaluacion(id,tipo_mensaje)

            else:
                return Response({"mensaje":"No hemos recibido los valores completos"},status= status.HTTP_404_NOT_FOUND)

         
   
        return Response ({"mensaje":fun},status= status.HTTP_200_OK)


def funcion_correo_evaluacion(id,tipo_mensaje):
    modulo='EVALUACION_DESEMPENIO'
    #print('1')
    correo_jefe=''
    correo_responsable=''
    if tipo_mensaje == 'colaborador: Jefe realizo su evaluacion':
        encabezado = evaluacion_encabezado.objects.get(id=id) if evaluacion_encabezado.objects.get(id=id) else None
        
       
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            #print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    modelo_tb= apps.get_model(app,modelos)
                    if variable=='@@jefe_empleado':
                        #print('entro a variable jefe empleado')
                        codigo_empleado =  (evaluacion_encabezado.objects.filter(id=encabezado.id).values('evaluado__codigo'))[0]['evaluado__codigo']
                        #print('3')
                        if codigo_empleado:
                            codigo_jefe= (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato']
                            #print('x')
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    valor_a_sustituir=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre']
                                    #print('4')
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    return 'codigo de jefe no encontrado'
                            else:        
                                return 'Jefe no encontrado'             
                        else:
                            return 'no se encontro el empleado'
                    elif variable=='@@funcion_jefe':
                        #print('5')
                        codigo_empleado =  encabezado.evaluado.codigo
                        if codigo_empleado:
                            codigo_jefe= (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato']
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    #print('6')
                                    valor_a_sustituir=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('posicion__nombre'))[0]['posicion__nombre']
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    return Response({"mensaje":"Jefe no encontrado"},status= status.HTTP_404_NOT_FOUND)                
                            else:
                                return 'Jefe no encontrado'
                        else:
                            return 'Empleado no encontrado'
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_colaborador = encabezado.evaluado.correo_empresarial
                #print('correo',correo_colaborador)
                if correo_colaborador:
                    correo_a_enviar=correo_colaborador
                    #print('llego')
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            notificacion=notificacion_aurora.objects.create(destinatario=encabezado.evaluado,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'jefe: Colaborador acepto evaluación':
        encabezado = evaluacion_encabezado.objects.get(id=id) if evaluacion_encabezado.objects.get(id=id) else None
        correo_j=''
       
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            #print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    modelo_tb= apps.get_model(app,modelos)
                    if variable=='@@Jefe':
                        #print('entro a variable jefe empleado')
                        codigo_empleado =  (evaluacion_encabezado.objects.filter(id=encabezado.id).values('evaluado__codigo'))[0]['evaluado__codigo']
                        #print('3')
                        if codigo_empleado:
                            codigo_jefe= (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato']
                            
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    correo_j=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial') else None
                                    valor_a_sustituir=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre']
                                    #print('4')
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    return 'codigo de jefe no encontrado'
                            else:        
                                return 'Jefe no encontrado'             
                        else:
                            return 'no se encontro el empleado'
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_colaborador = correo_j
                #print('correo',correo_colaborador)
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    #print('llego')
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            id_jefe=(Funcional_empleado.objects.filter(codigo=encabezado.evaluado.jefe_inmediato).values('id'))[0]['id'] if Funcional_empleado.objects.filter(codigo=encabezado.evaluado.jefe_inmediato) else None
                            destinatario= Funcional_empleado.objects.get(id=id_jefe)
                            notificacion=notificacion_aurora.objects.create(destinatario=destinatario,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Responsable: Colaborador acepto evaluación':
        encabezado = evaluacion_encabezado.objects.get(id=id) if evaluacion_encabezado.objects.get(id=id) else None

        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Evaluacion').values_list('username',flat=True)
        #print('usuarios_reponsablesusuarios_reponsablesusuarios_reponsables',usuarios_reponsables)
        for usuario_responable in usuarios_reponsables:
            configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
            if configuracion_correo:
                #print('2')
                asunto=configuracion_correo[0]['asunto']
                mensaje=configuracion_correo[0]['mensaje']
                variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            
                #print('usuario_responableX',usuario_responable)
                id_responsable=''
                if variables_envio_correo:
                    #print('variables_envio_correo')
                    for vec in variables_envio_correo:
                        variable= vec.variable
                        app= vec.app
                        modelos= vec.modelos
                        valores= vec.valores
                        modelo_tb= apps.get_model(app,modelos)
                        if variable=='@@jefe':
                            #print('entro a variable jefe empleado')
                            codigo_empleado =  (evaluacion_encabezado.objects.filter(id=encabezado.id).values('evaluado__codigo'))[0]['evaluado__codigo']
                            #print('3')
                            if codigo_empleado:
                                codigo_jefe= (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato']
                                #print('x')
                                if codigo_jefe:    
                                    if codigo_jefe!= "00000000":
                                        valor_a_sustituir=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre']
                                        #print('4')
                                        if valor_a_sustituir:
                                            valor_a_sustituir_str = valor_a_sustituir
                                            mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                            asunto= asunto.replace(variable,str(valor_a_sustituir))
                                        else:
                                            valor_a_sustituir_str =''
                                            mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                            asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        return 'codigo de jefe no encontrado'
                                else:        
                                    return 'Jefe no encontrado'             
                            else:
                                return 'no se encontro el empleado'
                        elif variable=='@@Responsable':
                                responsable_evaluacion=''
                                responsable_evaluacion= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                                #print('responsable_evaluacionresponsable_evaluacion',responsable_evaluacion)
                                if usuario_responable:
                                    id_responsable=Funcional_empleado.objects.get(codigo=usuario_responable) if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                                correo_responsable = (Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                                ##print('correo responsable',correo_responsable)
                                valor_a_sustituir = responsable_evaluacion[0]['nombre'] 
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    #print('mensajemensaje',valor_a_sustituir)
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir_str))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir_str)) 
                        else:
                            valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                    
                    
                    if correo_responsable and correo_responsable!=None :
                        correo_a_enviar=correo_responsable
                        #print('llego',correo_responsable)
                        if correo_a_enviar:
                            from_email_jefe= settings.EMAIL_HOST_USER
                            try:
                                msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                                msg_jefe.send()
                                notificacion=notificacion_aurora.objects.create(destinatario=id_responsable,asunto=asunto,mensaje=mensaje)
                            except BadHeaderError:
                                return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Jefe: Recordatorio':
        encabezado = evaluacion_encabezado.objects.get(id=id) if evaluacion_encabezado.objects.get(id=id) else None
        correo_j=''
       
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            #print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    modelo_tb= apps.get_model(app,modelos)
                    if variable=='@@jefe':
                        #print('entro a variable jefe empleado')
                        codigo_empleado =  (evaluacion_encabezado.objects.filter(id=encabezado.id).values('evaluado__codigo'))[0]['evaluado__codigo']
                        #print('3')
                        if codigo_empleado:
                            codigo_jefe= (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato']
                            #print('x')
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    correo_j=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial') else None
                                    valor_a_sustituir=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre']
                                    #print('4')
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    return 'codigo de jefe no encontrado'
                            else:        
                                return 'Jefe no encontrado'             
                        else:
                            return 'no se encontro el empleado'
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_colaborador = correo_j
                #print('correo',correo_colaborador)
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    #print('llego')
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            id_jefe=(Funcional_empleado.objects.filter(codigo=encabezado.evaluado.jefe_inmediato).values('id'))[0]['id'] if Funcional_empleado.objects.filter(codigo=encabezado.evaluado.jefe_inmediato) else None
                            destinatario= Funcional_empleado.objects.get(id=id_jefe)
                            notificacion=notificacion_aurora.objects.create(destinatario=destinatario,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Jefe: Colaborador realizo su autoevaluación':
        encabezado = evaluacion_encabezado.objects.get(id=id) if evaluacion_encabezado.objects.get(id=id) else None
        correo_j=''
       
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            #print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    modelo_tb= apps.get_model(app,modelos)
                    if variable=='@@jefe':
                        #print('entro a variable jefe empleado')
                        codigo_empleado =  (evaluacion_encabezado.objects.filter(id=encabezado.id).values('evaluado__codigo'))[0]['evaluado__codigo']
                        #print('3')
                        if codigo_empleado:
                            codigo_jefe= (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato']
                            #print('x')
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    correo_j=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial') else None
                                    valor_a_sustituir=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre']
                                    #print('4')
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    return 'codigo de jefe no encontrado'
                            else:        
                                return 'Jefe no encontrado'             
                        else:
                            return 'no se encontro el empleado'
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_colaborador = correo_j
                #print('correo',correo_colaborador)
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    #print('llego')
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            id_jefe=(Funcional_empleado.objects.filter(codigo=encabezado.evaluado.jefe_inmediato).values('id'))[0]['id'] if Funcional_empleado.objects.filter(codigo=encabezado.evaluado.jefe_inmediato) else None
                            destinatario= Funcional_empleado.objects.get(id=id_jefe)
                            notificacion=notificacion_aurora.objects.create(destinatario=destinatario,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    
    return 'Proceso Exitoso'

class evaluacion_despliegue_preguntas_factorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezado_preguntas_factorserializer
    ##print(queryset)
    def list(self, request):
        queryset = evaluacion_encabezado.objects.all()
        serializer_class = evaluacion_encabezado_preguntas_factorserializer(queryset, many=True)
        id=''
        factores=[]
        periodicidad=''
        clasificacion=''
        preguntas=[]
        lista_factores=[]
        preguntas_tipo_0=[]
        preguntas_tipo_2=[]
        funcion=''
        listado=[]
        tipo_factores=[]
        estado_evaluacion=''
        nota_factor_f=''
        categoria_desempenio_f=''
        data_factor={}
        if self.request.query_params.get('id'):
            id = self.request.query_params.get('id')

        

        if id!='':
            ######################################################
            metricas_vacias= detalle_evaluacion_factor.objects.filter(encabezado__id=id).filter(metrica_factor=None) if detalle_evaluacion_factor.objects.filter(encabezado__id=id).filter(metrica_factor=None) else None
            if metricas_vacias!=None:
                detalle_evaluacion_factor.objects.filter(encabezado__id=id).filter(metrica_factor=None).delete()
            #####################################################
            codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
            id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
            posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
            
            descriptor_encabezado = (evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado'))[0]['descriptor_empleado'] if evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado') else None
            if descriptor_encabezado==None:
                return Response({"Descriptor no encontrado en el encabezado"},status= status.HTTP_404_NOT_FOUND)
            
            descriptor= descriptor_perfil_datos_generales.objects.get(id=descriptor_encabezado) if descriptor_perfil_datos_generales.objects.filter(id=descriptor_encabezado) else None
            if descriptor==None:
                return Response({"Descriptor no existe"},status= status.HTTP_404_NOT_FOUND)

            #clasificacion=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id'))[0]['evaluado__clasificacion_empleado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id') else None
            clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
            periodicidad=(evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id'))[0]['periodicidad__id'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id') else None
            factores.extend(evaluacion_factor.objects.filter(clasificacion_id=clasificacion,periodicidad=periodicidad).values_list('id', flat=True))
            estado_evaluacion=(evaluacion_encabezado.objects.filter(id=id).values('estado'))[0]['estado'] if evaluacion_encabezado.objects.filter(id=id).values('estado') else None
            nota_factor_f=(evaluacion_encabezado.objects.filter(id=id).values('nota_total_porcentaje'))[0]['nota_total_porcentaje'] if evaluacion_encabezado.objects.filter(id=id).values('nota_total_porcentaje') else None
            if nota_factor_f!='' and nota_factor_f!=None:
                categoria_desempenio_f= (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=nota_factor_f, valor_maximo__gte=nota_factor_f).values('descripcion'))[0]['descripcion'] if (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=nota_factor_f, valor_maximo__gte=nota_factor_f).values('descripcion')) else 'Sin categorizaciòn'
        #print(tipo_factores)
        #print('hfdjhfdkfdkf',factores)
     
        if not None in factores:
            for factor in factores:
                objeto_encabezado=evaluacion_encabezado.objects.get(id=id)
                objeto_factor=evaluacion_factor.objects.get(id=factor)

                if objeto_factor.tipo_factor!=None:
                    if objeto_factor.tipo_factor==0:
                        respuesta_peso_encontrado=None
                        preguntas_tipo_factor=evaluacion_plantilla_factor.objects.filter(factor=factor,factor__tipo_factor=0, periodicidad=objeto_factor.periodicidad).values_list('pregunta','id')
                        preguntas_tipo_factor_0=[]
                        for pregunta, id_origen_pregunta in preguntas_tipo_factor:
                            
                            metrica= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=0,factor=factor,encabezado=id).values('metrica_factor'))[0]['metrica_factor'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=0,factor=factor,encabezado=id).values('metrica_factor') else None
                            id_detalle_evaluacion_factor= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=0,factor=factor,encabezado=id).values('id'))[0]['id'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=0,factor=factor,encabezado=id).values('id') else None
                            
                            respuesta_peso= detalle_evaluacion_factor.objects.filter(factor_id=factor,evaluacion_plantilla_factor=id_origen_pregunta,encabezado=id).values('peso') if detalle_evaluacion_factor.objects.filter(factor_id=factor,evaluacion_plantilla_factor=id_origen_pregunta,encabezado=id).values('metrica_factor') else None
                            pregunta_data_0={}
                            pregunta_data_0['id_origen_pregunta']= id_origen_pregunta
                            
                            pregunta_data_0['pregunta']= pregunta
                            pregunta_data_0['metrica_id']= metrica
                            pregunta_data_0['id_detalle_evaluacion_factor']=id_detalle_evaluacion_factor
                            preguntas_tipo_factor_0.append(pregunta_data_0)
                            
                            if respuesta_peso!=None:
                                respuesta_peso_encontrado=respuesta_peso[0]['peso']
                            else:
                                respuesta_peso_encontrado=None
                        
                        data={
                                "encabezado_id":id,
                                "periodicidad":objeto_factor.periodicidad.id,
                                "id_factor":factor,
                                "tipo_factor":objeto_factor.tipo_factor,
                                "nombre_factor":objeto_factor.nombre,
                                "peso":objeto_factor.peso if respuesta_peso_encontrado is None else respuesta_peso_encontrado,
                                "preguntas":preguntas_tipo_factor_0
                        }
                        
                        lista_factores.append(data)
                    if objeto_factor.tipo_factor==1:
                        codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                        id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
                        e=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
                        descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=e).order_by('-id').first()
                        
                        
                        
                        preg=descriptor_perfil_funcion.objects.filter(descriptor_id=descriptor.id,fundamental=True).values_list('id','descripcion')
                        peso_factor_tipo_1=''
                        contador_pregunta=0
                        for id_origen_pregunta, pregunta in preg:
                            contador_pregunta+=1
                            metrica= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('metrica_factor'))[0]['metrica_factor'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('metrica_factor') else None
                            id_detalle_evaluacion_factor= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('id'))[0]['id'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('id') else None
                            pesos= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('peso'))[0]['peso'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('metrica_factor') else None
                            peso_factor_tipo_1=pesos
                            pregunta_data_2={}
                            pregunta_data_2['id_origen_pregunta']= id_origen_pregunta
                            #print('pla',pregunta_data_2)
                            pregunta_data_2['pregunta']= pregunta
                            pregunta_data_2['metrica_id']= metrica
                            pregunta_data_2['id_detalle_evaluacion_factor']=id_detalle_evaluacion_factor
                            pregunta_data_2['indice_pregunta']= contador_pregunta
                            preguntas.append(pregunta_data_2)
                        
                        data={
                                "encabezado_id":id,
                                "periodicidad":objeto_factor.periodicidad.id,
                                "id_factor":factor,
                                "tipo_factor":objeto_factor.tipo_factor,
                                "nombre_factor":objeto_factor.nombre,
                                "peso":objeto_factor.peso if peso_factor_tipo_1==None else peso_factor_tipo_1,
                                "preguntas":preguntas
                        }
                        lista_factores.append(data)
                    
                    if objeto_factor.tipo_factor==2:
                        lista_preguntas_factor2=[]
                        codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                        id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
                        e=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)
                        descriptor = descriptor_perfil_datos_generales.objects.filter(posicion__in=e).order_by('-id').first()
                        
                        
                        
                        preg=descriptor_perfil_indicador_descriptor.objects.filter(descriptor_id=descriptor.id).values_list('indicador','indicador__objetivo')
                        peso_factor_tipo_2=''
                        contador_pregunta_factor_2=0
                        for id_origen_pregunta, pregunta in preg:
                            contador_pregunta_factor_2+=1
                            metrica= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('metrica_factor'))[0]['metrica_factor'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('metrica_factor') else None
                            id_detalle_evaluacion_factor= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('id'))[0]['id'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('id') else None
                            pesos= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('peso'))[0]['peso'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('metrica_factor') else None
                            peso_factor_tipo_2=pesos
                            pregunta_data_2={}
                            pregunta_data_2['id_origen_pregunta']= id_origen_pregunta
                            #print('pla',pregunta_data_2)
                            pregunta_data_2['pregunta']= pregunta
                            pregunta_data_2['metrica_id']= metrica
                            pregunta_data_2['id_detalle_evaluacion_factor']=id_detalle_evaluacion_factor
                            pregunta_data_2['indice_pregunta'] =contador_pregunta_factor_2
                            lista_preguntas_factor2.append(pregunta_data_2)
                        
                        data={
                                "encabezado_id":id,
                                "periodicidad":objeto_factor.periodicidad.id,
                                "id_factor":factor,
                                "tipo_factor":objeto_factor.tipo_factor,
                                "nombre_factor":objeto_factor.nombre,
                                "peso":objeto_factor.peso if peso_factor_tipo_2==None else peso_factor_tipo_2,
                                "preguntas":lista_preguntas_factor2
                        }
                        lista_factores.append(data)    
                else:
                    return Response({"Tipo de factor no definido"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Factores no encontrados"},status= status.HTTP_404_NOT_FOUND)
              
        return Response({"factores":lista_factores,"estado_evaluacion":estado_evaluacion,"nota_factor":nota_factor_f,"categoria_desempenio":categoria_desempenio_f},status= status.HTTP_200_OK)


    def update(self,requets,pk):
        #print(self)
        #print(requets)
        datax=[]
        obj=self.get_object()
        existe= evaluacion_encabezado.objects.filter(id=obj.id).count()
        if existe!=0:
            respuestas=''
            respuestas=self.request.data["respuesta_factor"]
            put = self.get_object()
            for datos in respuestas:
                #print(datos)       
                serializer= evaluacion_encabezadoserializer(put,data=datos)
                if serializer.is_valid():
                    #serializer.save()
                    #print('**********************')
                    if datos["tipo_factor"]==0:
                        obj, created = detalle_evaluacion_factor.objects.update_or_create(
                            encabezado_id=datos["encabezado_id"],
                            evaluacion_plantilla_factor_id=datos["id_origen_pregunta"],
                            respuesta_pregunta=datos["id_origen_pregunta"],
                            factor_id=datos["id_factor"],
                            factor__tipo_factor=datos["tipo_factor"],
                            defaults={    
                                "metrica_factor_id":datos["metrica_factor"]
                                }
                                )                  
                        #print('*************ASD*********')

                    if datos["tipo_factor"]==1:
                        obj, created = detalle_evaluacion_factor.objects.update_or_create(
                            encabezado_id=datos["encabezado_id"],
                            respuesta_pregunta=datos["id_origen_pregunta"],
                            factor_id=datos["id_factor"],
                            factor__tipo_factor=datos["tipo_factor"],
                            defaults={    
                                "metrica_factor_id":datos["metrica_factor"]
                                }
                                )                  
                        #print('*************474*********')

                    if datos["tipo_factor"]==2:
                        obj, created = detalle_evaluacion_factor.objects.update_or_create(
                            encabezado_id=datos["encabezado_id"],
                            respuesta_pregunta=datos["id_origen_pregunta"],
                            factor_id=datos["id_factor"],
                            factor__tipo_factor=datos["tipo_factor"],
                            defaults={    
                                "metrica_factor_id":datos["metrica_factor"]
                                }
                                )                  
                        #print('*************48384343434*********')
                else:
                    return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)       
        else:
            return Response({'DASD'},status=status.HTTP_204_NO_CONTENT)
        
        #return Response({'RETURN DE PRUEBA'},status=status.HTTP_204_NO_CONTENT)
        metricas_vacias= detalle_evaluacion_factor.objects.filter(encabezado__id=pk).filter(metrica_factor=None) if detalle_evaluacion_factor.objects.filter(encabezado__id=pk).filter(metrica_factor=None) else None
        if metricas_vacias!=None:
            detalle_evaluacion_factor.objects.filter(encabezado__id=pk).filter(metrica_factor=None).delete()
        validacion_evaluacion_llenada=validacion_evaluacion_factor(pk)
        print('validacion_evaluacion_llenada',validacion_evaluacion_llenada)
        
        if validacion_evaluacion_llenada==True:
            try:
                calculo_calificacion_factor(pk)
                encabezado_N=evaluacion_encabezado.objects.filter(id=pk).update(fecha_evaluacion=datetime.now().date())
                encabezado= evaluacion_encabezado.objects.get(id=pk) if evaluacion_encabezado.objects.filter(id=pk) else None
                if encabezado!=None:#este codigo lleva la fecha de la evaluacion
                    encabezado_evaluado= (evaluacion_encabezado.objects.filter(id=pk).values('evaluado'))[0]['evaluado'] if evaluacion_encabezado.objects.filter(id=pk).values('evaluado') else None
                    encabezado_periodicidad=  (evaluacion_encabezado.objects.filter(id=pk).values('periodicidad'))[0]['periodicidad'] if evaluacion_encabezado.objects.filter(id=pk).values('periodicidad') else None
                    encabezado_periodo =  (evaluacion_encabezado.objects.filter(id=pk).values('periodo'))[0]['periodo'] if evaluacion_encabezado.objects.filter(id=pk).values('periodo') else None
                    encabezado_tipo_evaluacion =  (evaluacion_encabezado.objects.filter(id=pk).values('tipo_evaluacion__id'))[0]['tipo_evaluacion__id'] if evaluacion_encabezado.objects.filter(id=pk).values('tipo_evaluacion__id') else None
                    #########################################################################################################################
                    # fecha_evalua=evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=2).update(fecha_evaluacion=datetime.now().date()) if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=2) else None
                    encabezado_competencia_id=(evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=1).values('id'))[0]['id'] if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=1) else None
                    validacion_encabezado_competencia_1=validacion_evaluacion_competencia(encabezado_competencia_id)
                    tipo_e=(evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=1).values('tipo_evaluacion__nombre'))[0]['tipo_evaluacion__nombre'] if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion,tipo_evaluacion_encabezado=1) else None
                    # print('validacion_evaluacion_llenada',validacion_evaluacion_llenada)
                    # print('validacion_encabezado_competencia_1',validacion_encabezado_competencia_1)
                    # print('tipo_e',tipo_e)
                    # print('encabezado_competencia_id',encabezado_competencia_id)
                    if validacion_evaluacion_llenada== True and validacion_encabezado_competencia_1==True and tipo_e=='0°':
                        funcion_correo_evaluacion(pk,'Jefe: Colaborador realizo su autoevaluación')
            except BadHeaderError:
                raise Http404

        # metricas_vacias= detalle_evaluacion_factor.objects.filter(encabezado__id=pk).filter(metrica_factor=None) if detalle_evaluacion_factor.objects.filter(encabezado__id=pk).filter(metrica_factor=None) else None
        # if metricas_vacias!=None:
        #     detalle_evaluacion_factor.objects.filter(encabezado__id=pk).filter(metrica_factor=None).delete()
        
        id=pk
        factores=[]
        periodicidad=''
        clasificacion=''
        preguntas=[]
        lista_factores=[]
        funcion=''
        listado=[]
        tipo_factores=[]
        estado_evaluacion=''
        nota_factor_f=''
        categoria_desempenio_f=''
        data_factor={}
        
        if id!='':
            codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
            id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
            posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
            descriptor_encabezado = (evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado'))[0]['descriptor_empleado'] if evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado') else None
            if descriptor_encabezado==None:
                return Response({"Descriptor no encontrado en el encabezado"},status= status.HTTP_404_NOT_FOUND)
            
            descriptor= descriptor_perfil_datos_generales.objects.get(id=descriptor_encabezado) if descriptor_perfil_datos_generales.objects.filter(id=descriptor_encabezado) else None
            if descriptor==None:
                return Response({"Descriptor no existe"},status= status.HTTP_404_NOT_FOUND)

            #clasificacion=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id'))[0]['evaluado__clasificacion_empleado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id') else None
            clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
            periodicidad=(evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id'))[0]['periodicidad__id'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id') else None
            factores.extend(evaluacion_factor.objects.filter(clasificacion_id=clasificacion,periodicidad=periodicidad).values_list('id', flat=True))
            estado_evaluacion=(evaluacion_encabezado.objects.filter(id=id).values('estado'))[0]['estado'] if evaluacion_encabezado.objects.filter(id=id).values('estado') else None
            nota_factor_f=(evaluacion_encabezado.objects.filter(id=id).values('nota_total_porcentaje'))[0]['nota_total_porcentaje'] if evaluacion_encabezado.objects.filter(id=id).values('nota_total_porcentaje') else None
            if nota_factor_f!='' and nota_factor_f!=None:
                categoria_desempenio_f= (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=nota_factor_f, valor_maximo__gte=nota_factor_f).values('descripcion'))[0]['descripcion'] if (categoria_desempeno.objects.filter(periodicidad=periodicidad,valor_minimo__lte=nota_factor_f, valor_maximo__gte=nota_factor_f).values('descripcion')) else 'Sin categorizaciòn'
        #print(tipo_factores)
        #print('hfdjhfdkfdkf',factores)
     
        if not None in factores:
            for factor in factores:
                objeto_encabezado=evaluacion_encabezado.objects.get(id=id)
                objeto_factor=evaluacion_factor.objects.get(id=factor)
                #print(factor)
                #print("ttttttttttttttttt",objeto_factor.periodicidad)
                if objeto_factor.tipo_factor!=None:
                    if objeto_factor.tipo_factor==0:
                        respuesta_peso_encontrado=None
                        preguntas_tipo_factor=evaluacion_plantilla_factor.objects.filter(factor=factor,factor__tipo_factor=0, periodicidad=objeto_factor.periodicidad).values_list('pregunta','id')
                        preguntas_tipo_factor_0=[]
                        for pregunta, id_origen_pregunta in preguntas_tipo_factor:
                            
                            metrica= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=0,factor=factor,encabezado=id).values('metrica_factor'))[0]['metrica_factor'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=0,factor=factor,encabezado=id).values('metrica_factor') else None
                            id_detalle_evaluacion_factor= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=0,factor=factor,encabezado=id).values('id'))[0]['id'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=0,factor=factor,encabezado=id).values('id') else None
                            
                            respuesta_peso= detalle_evaluacion_factor.objects.filter(factor_id=factor,evaluacion_plantilla_factor=id_origen_pregunta,encabezado=id).values('peso') if detalle_evaluacion_factor.objects.filter(factor_id=factor,evaluacion_plantilla_factor=id_origen_pregunta,encabezado=id).values('metrica_factor') else None
                            pregunta_data_0={}
                            pregunta_data_0['id_origen_pregunta']= id_origen_pregunta
                            
                            pregunta_data_0['pregunta']= pregunta
                            pregunta_data_0['metrica_id']= metrica
                            pregunta_data_0['id_detalle_evaluacion_factor']=id_detalle_evaluacion_factor
                            preguntas_tipo_factor_0.append(pregunta_data_0)
                            
                            if respuesta_peso!=None:
                                respuesta_peso_encontrado=respuesta_peso[0]['peso']
                            else:
                                respuesta_peso_encontrado=None
                        
                        data={
                                "encabezado_id":id,
                                "periodicidad":objeto_factor.periodicidad.id,
                                "id_factor":factor,
                                "tipo_factor":objeto_factor.tipo_factor,
                                "nombre_factor":objeto_factor.nombre,
                                "peso":objeto_factor.peso if respuesta_peso_encontrado is None else respuesta_peso_encontrado,
                                "preguntas":preguntas_tipo_factor_0
                        }
                        
                        lista_factores.append(data)
                    if objeto_factor.tipo_factor==1:
                        codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                        id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
                        e=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
                        descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=e).order_by('-id').first()
                        
                        
                        
                        preg=descriptor_perfil_funcion.objects.filter(descriptor_id=descriptor.id,fundamental=True).values_list('id','descripcion')
                        peso_factor_tipo_1=''
                        contador_pregunta=0
                        for id_origen_pregunta, pregunta in preg:
                            contador_pregunta+=1
                            metrica= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('metrica_factor'))[0]['metrica_factor'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('metrica_factor') else None
                            id_detalle_evaluacion_factor = (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('id'))[0]['id'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('id') else None
                            pesos= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('peso'))[0]['peso'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=1,factor=factor,encabezado=id).values('metrica_factor') else None
                            peso_factor_tipo_1=pesos
                            pregunta_data_2={}
                            pregunta_data_2['id_origen_pregunta']= id_origen_pregunta
                            #print('pla',pregunta_data_2)
                            pregunta_data_2['pregunta']= pregunta
                            pregunta_data_2['metrica_id']= metrica
                            pregunta_data_2['id_detalle_evaluacion_factor']=id_detalle_evaluacion_factor
                            pregunta_data_2['indice_pregunta']= contador_pregunta
                            preguntas.append(pregunta_data_2)
                        
                        data={
                                "encabezado_id":id,
                                "periodicidad":objeto_factor.periodicidad.id,
                                "id_factor":factor,
                                "tipo_factor":objeto_factor.tipo_factor,
                                "nombre_factor":objeto_factor.nombre,
                                "peso":objeto_factor.peso if peso_factor_tipo_1==None else peso_factor_tipo_1,
                                "preguntas":preguntas
                        }
                        lista_factores.append(data)
                    
                    if objeto_factor.tipo_factor==2:
                        lista_preguntas_factor2=[]
                        codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                        id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
                        e=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)
                        descriptor = descriptor_perfil_datos_generales.objects.filter(posicion__in=e).order_by('-id').first()
                        
                        
                        
                        preg=descriptor_perfil_indicador_descriptor.objects.filter(descriptor_id=descriptor.id).values_list('indicador','indicador__objetivo')
                        peso_factor_tipo_2=''
                        contador_pregunta_factor_2=0
                        for id_origen_pregunta, pregunta in preg:
                            contador_pregunta_factor_2+=1
                            metrica= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('metrica_factor'))[0]['metrica_factor'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('metrica_factor') else None
                            id_detalle_evaluacion_factor  = (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('id'))[0]['id'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('id') else None
                            pesos= (detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('peso'))[0]['peso'] if detalle_evaluacion_factor.objects.filter(respuesta_pregunta=id_origen_pregunta,factor__tipo_factor=2,factor=factor,encabezado=id).values('metrica_factor') else None
                            peso_factor_tipo_2=pesos
                            pregunta_data_2={}
                            pregunta_data_2['id_origen_pregunta']= id_origen_pregunta
                            #print('pla',pregunta_data_2)
                            pregunta_data_2['pregunta']= pregunta
                            pregunta_data_2['metrica_id']= metrica
                            pregunta_data_2['id_detalle_evaluacion_factor']=id_detalle_evaluacion_factor
                            pregunta_data_2['indice_pregunta'] =contador_pregunta_factor_2
                            lista_preguntas_factor2.append(pregunta_data_2)
                        
                        data={
                                "encabezado_id":id,
                                "periodicidad":objeto_factor.periodicidad.id,
                                "id_factor":factor,
                                "tipo_factor":objeto_factor.tipo_factor,
                                "nombre_factor":objeto_factor.nombre,
                                "peso":objeto_factor.peso if peso_factor_tipo_2==None else peso_factor_tipo_2,
                                "preguntas":lista_preguntas_factor2
                        }
                        lista_factores.append(data)    
                else:
                    return Response({"Tipo de factor no definido"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Factores no encontrados"},status= status.HTTP_404_NOT_FOUND)
              
        return Response({"factores":lista_factores,"estado_evaluacion":estado_evaluacion,"nota_factor":nota_factor_f,"categoria_desempenio":categoria_desempenio_f},status= status.HTTP_200_OK)




class evaluacion_cambio_pesos_factorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = detalle_evaluacion_factor.objects.all()
    serializer_class = detalle_evaluacion_factorserializer
    def update(self,request,pk):
        
       
        respuestas=''
        respuestas=self.request.data["cambio_pesos"]
        for datos in respuestas:     
            detalle_evaluacion_factor.objects.filter(encabezado_id=datos["encabezado"],factor_id=datos['id_factor']).update(peso=datos["peso"])                    
        
        validacion_evaluacion_llenada=validacion_evaluacion_factor(pk)
        
        if validacion_evaluacion_llenada==True:
            try:
                calculo_calificacion_factor(pk)
            except BadHeaderError:
                raise Http404
          
        return Response({"actualizacion exitosa"},status= status.HTTP_200_OK)


def validacion_evaluacion_factor(id):
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezado_preguntas_factorserializer(queryset, many=True)
 
    factores=[]
    periodicidad=''
    clasificacion=''
    preguntas=[]
    lista_factores=[]
    preguntas_tipo_0=[]
    preguntas_tipo_2=[]
    funcion=''
    listado=[]
    tipo_factores=[]
    data_factor={}
    contador_preguntas=0

    respuestas_factor_totales=0

    
    if id!='':
        codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
        id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
        posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
        descriptor_encabezado = (evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado'))[0]['descriptor_empleado'] if evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado') else None
        if descriptor_encabezado==None:
            return Response({"Descriptor no encontrado en el encabezado"},status= status.HTTP_404_NOT_FOUND)
        
        descriptor= descriptor_perfil_datos_generales.objects.get(id=descriptor_encabezado) if descriptor_perfil_datos_generales.objects.filter(id=descriptor_encabezado) else None
        if descriptor==None:
            return Response({"Descriptor no existe"},status= status.HTTP_404_NOT_FOUND)

        #clasificacion=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id'))[0]['evaluado__clasificacion_empleado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id') else None
        clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
        periodicidad=(evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id'))[0]['periodicidad__id'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id') else None
        factores.extend(evaluacion_factor.objects.filter(clasificacion_id=clasificacion,periodicidad=periodicidad).values_list('id', flat=True))
        
    
    if not None in factores:
        #print('encontro factores')
        for factor in factores:
            #print('id de factor iterando',factor)
            objeto_encabezado=evaluacion_encabezado.objects.get(id=id)
            objeto_factor=evaluacion_factor.objects.get(id=factor)

            if objeto_factor.tipo_factor!=None:
                if objeto_factor.tipo_factor==0:
                    respuesta_peso_encontrado=''
                    preguntas_tipo_factor=evaluacion_plantilla_factor.objects.filter(factor=factor,factor__tipo_factor=0, periodicidad=objeto_factor.periodicidad).values('pregunta',id_origen_pregunta=F('id'))
                    respuesta= detalle_evaluacion_factor.objects.filter(factor=factor,factor__tipo_factor=0, encabezado=id).values('id')
                    contador_preguntas+=preguntas_tipo_factor.count()
                    respuestas_factor_totales+=respuesta.count()
                    #print('RESPUESTA_preguntas-contador_preguntas__0',respuestas_factor_totales)
                    #print('contador_preguntas-contador_preguntas__0',contador_preguntas)
                    #print('#########################################################')





                if objeto_factor.tipo_factor==1:
                    codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                    id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
                    e=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
                    descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=e).order_by('-id').first()
                    
                    
                    
                    preg=descriptor_perfil_funcion.objects.filter(descriptor_id=descriptor.id,fundamental=True).values('id','descripcion')
                    if preg.count()<=3:
                        contador_preguntas+=preg.count()
                    else:
                        contador_preguntas+=3
                    respuesta= detalle_evaluacion_factor.objects.filter(factor=factor,factor__tipo_factor=1, encabezado=id).values()
                    respuestas_factor_totales+=respuesta.count()
                    #print('RESPUESTA_preguntas-contador_preguntas__0',respuestas_factor_totales)
                    #print('contador_preguntas-contador_preguntas',contador_preguntas)
                    #print('#########################################################')

                if objeto_factor.tipo_factor==2:
                    lista_preguntas_factor2=[]
                    codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                    id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
                    e=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)
                    descriptor = descriptor_perfil_datos_generales.objects.filter(posicion__in=e).order_by('-id').first()
                    
                    
                    
                    preg=descriptor_perfil_indicador_descriptor.objects.filter(descriptor_id=descriptor.id).values_list('indicador','indicador__objetivo')
                    if preg.count()<=3:
                        contador_preguntas+=preg.count()
                    else:
                        contador_preguntas+=3
                    respuesta= detalle_evaluacion_factor.objects.filter(factor=factor,factor__tipo_factor=2, encabezado=id).values()
                    respuestas_factor_totales+=respuesta.count()
                    #print('RESPUESTA_preguntas-contador_preguntas__0',respuestas_factor_totales)
                    #print('contador_preguntas-contador_preguntas',contador_preguntas)
                    #print('#########################################################')
            else:
                return "Tipo de factor no definido"

    else:
        return "Factores no encontrados"

    if respuestas_factor_totales == contador_preguntas:
        return True
    if respuestas_factor_totales > contador_preguntas:
        return 'Se encontro un problema, hay mas respuestas que preguntas en el sistema'
    
    if respuestas_factor_totales < contador_preguntas:
        return False


class validacion(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none()

    def get(self,request,pk):
        funcion_validadcion=validacion_evaluacion_factor(pk)

    
        return Response({"actualizacion exitosa":funcion_validadcion},status= status.HTTP_200_OK)


def validacion_evaluacion_competencia(id):
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezado_preguntas_factorserializer(queryset, many=True)
        
    clasificacion=''
    periodicidad=''
    pregunta=[]
    #competencias=[]
    estado_evaluacion=''
    tipo_evaluacion_encabezado=''
    contador_respuestas=0
    almacenamiento_cantidad_preguntas=0
   
    if id!='':
        codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
        id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
        posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
        descriptor_encabezado = (evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado'))[0]['descriptor_empleado'] if evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado') else None
        if descriptor_encabezado==None:
            return Response({"Descriptor no encontrado en el encabezado"},status= status.HTTP_404_NOT_FOUND)
        
        descriptor= descriptor_perfil_datos_generales.objects.get(id=descriptor_encabezado) if descriptor_perfil_datos_generales.objects.filter(id=descriptor_encabezado) else None
        if descriptor==None:
            return Response({"Descriptor no existe"},status= status.HTTP_404_NOT_FOUND)
        
        clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
        #clasificacion=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id'))[0]['evaluado__clasificacion_empleado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id') else None
        #competencias=evaluacion_competencia.objects.filter(clasificacion_id=clasificacion).values_list('id', flat=True)          
        periodicidad=(evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id'))[0]['periodicidad__id'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id') else None          
        tipo_evaluacion_encabezado=(evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion_encabezado'))[0]['tipo_evaluacion_encabezado'] if evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion_encabezado') else None
        estado_evaluacion=(evaluacion_encabezado.objects.filter(id=id).values('estado'))[0]['estado'] if evaluacion_encabezado.objects.filter(id=id).values('estado') else None
        competencia_perfil_descriptor=descriptor_perfil_competencia_descriptor.objects.filter(descriptor_id=descriptor.id).values_list('id', flat=True)
        competencia_descriptor=evaluacion_competencia.objects.filter(periodicidad__id=periodicidad).filter(competencia__descriptor_perfil_competencia_descriptor__id__in=competencia_perfil_descriptor).distinct().values_list('id', flat=True)

    # print(competencias)
    # nueva_competencias=[]

    # if competencias==None:
    #     return Response({"Competencias no encontradas"},status= status.HTTP_404_NOT_FOUND)
    # else:
    #     if len(competencias)!=0:
    #         for item in competencias:
    #             if item not in nueva_competencias:
    #                 if item!=None:
    #                     nueva_competencias.append(item)

    data={}
    
    if clasificacion!=None:
        if periodicidad!=None:
            for competencia in competencia_descriptor:
                #print(competencia)
                
                listado_pregunta_competencia=list(evaluacion_plantilla_competencia.objects.filter(competencia__clasificacion=clasificacion).filter(competencia__id=competencia).filter(periodicidad__id=periodicidad).values('pregunta',idCompetencia=F('competencia__competencia__id'),nombreCompetencia=F('competencia__competencia__nombre'),descripcionCompetencia=F('competencia__competencia__descripcion'),idClasificacion=F('competencia__clasificacion'),idPlantilla=F('id')))
                conteo_preguntas=evaluacion_plantilla_competencia.objects.filter(competencia__clasificacion=clasificacion).filter(competencia__id=competencia).filter(periodicidad__id=periodicidad).values('pregunta',idCompetencia=F('competencia__competencia__id'),nombreCompetencia=F('competencia__competencia__nombre'),descripcionCompetencia=F('competencia__competencia__descripcion'),idClasificacion=F('competencia__clasificacion'),idPlantilla=F('id')).count()
                
                almacenamiento_cantidad_preguntas+=conteo_preguntas
                
                for lista in listado_pregunta_competencia:
                    metrica_competencia_id_x= detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia=lista['idPlantilla']).filter(encabezado=id).values('metrica_competencia','metrica_competencia__grado')
                    contador_respuestas+=metrica_competencia_id_x.count()

    if almacenamiento_cantidad_preguntas==contador_respuestas:
        return True
    if almacenamiento_cantidad_preguntas>contador_respuestas:
        return False

    if almacenamiento_cantidad_preguntas<contador_respuestas:
        return 'Algo salio mal, hay mas respuestas que preguntas en el sistema'


class dashboard_evaluaciones_jefe(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none()
    def get(self,request):
        empleado_bajo_mando=[]
        usuario = request.user
        hoy=datetime.now().date()
        año= hoy.year
        empleado_bajo_mando=funcional_get_colaborador([usuario.username])
        ###print(empleado_bajo_mando)
        empleado=''
        filter_año=''
        conjunto_filtros={}

        ###################################
        nota_total_competencia=''
        nota_total_competencia_desempeno=''
        nota_total_factor=''
        nota_total_factor_desempenio=''
        total_desempenio=''
        desempenio=''
        matriz_marcas_factor=''
        encabezado_competencia_id=''
        lista_competencias_puntajes_y_esperado=''
        ###################################
        
        # if self.request.query_params.get('codigo_empleado'):
        #     conjunto_filtros['codigo'] = self.request.query_params.get('codigo_empleado')
        
        # if self.request.query_params.get('nombre_empleado'):
        #     conjunto_filtros['nombre'] = self.request.query_params.get('nombre_empleado')
        
        # if self.request.query_params.get('nombre_empleado'):
        #     conjunto_filtros['nombre'] = self.request.query_params.get('nombre_empleado')
        
        # if self.request.query_params.get('codigo_funcion'):
        #     conjunto_filtros['posicion__codigo'] = self.request.query_params.get('codigo_funcion')
        
        # if self.request.query_params.get('nombre_funcion'):
        #     conjunto_filtros['posicion__nombre'] = self.request.query_params.get('nombre_funcion')
        ###############################################################################################
        tipo_busqueda=''
        filter=''
        listado_empleados_filtros_aplicados=''
        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
            
        if tipo_busqueda!='' and filter!='':
            if tipo_busqueda=='codigo_empleado':
                listado_empleados_filtros_aplicados = Funcional_empleado.objects.filter(codigo__in=empleado_bajo_mando).filter(codigo=filter).values_list('codigo',flat=True)
            if tipo_busqueda=='nombre_empleado':
                listado_empleados_filtros_aplicados = Funcional_empleado.objects.filter(codigo__in=empleado_bajo_mando).filter(nombre__icontains=filter).values_list('codigo',flat=True)
            if tipo_busqueda=='division':
                listado_empleados_filtros_aplicados = Funcional_empleado.objects.filter(codigo__in=empleado_bajo_mando).filter(division__descripcion__icontains=filter).values_list('codigo',flat=True)    
            if tipo_busqueda=='codigo_funcion':
                listado_empleados_filtros_aplicados = Funcional_empleado.objects.filter(codigo__in=empleado_bajo_mando).filter(posicion__codigo=filter).values_list('codigo',flat=True)
            if tipo_busqueda=='nombre_funcion':
                listado_empleados_filtros_aplicados = Funcional_empleado.objects.filter(codigo__in=empleado_bajo_mando).filter(posicion__nombre__icontains=filter).values_list('codigo',flat=True)
        
        else:
            listado_empleados_filtros_aplicados = Funcional_empleado.objects.filter(codigo__in=empleado_bajo_mando).values_list('codigo',flat=True)
        ############################################################################################



        # listado_empleados_filtros_aplicados = Funcional_empleado.objects.filter(codigo__in=empleado_bajo_mando).filter(**conjunto_filtros).values_list('codigo',flat=True)    
        print('listado_empleados_filtros_aplicados',listado_empleados_filtros_aplicados)
        print('listado_empleados_filtros_aplicados count ',len(listado_empleados_filtros_aplicados))
        encabezados={}
        periodicidad_vigente=''
        jefe_empresa= (Funcional_empleado.objects.filter(codigo=usuario.username).values('unidad_organizativa__sociedad_financiera__id'))[0]['unidad_organizativa__sociedad_financiera__id'] if Funcional_empleado.objects.filter(codigo=usuario.username).values('unidad_organizativa__sociedad_financiera__id') else None
        if jefe_empresa!=None:
            ###print('ENTRO1')
            ###print('EMPRESA',jefe_empresa)
            periodicidad_vigente= (evaluacion_periodicidad.objects.filter(fecha_inicio__lte=hoy).filter(fecha_fin__gte=hoy).filter(empresa=jefe_empresa).values('id'))[0]['id'] if evaluacion_periodicidad.objects.filter(fecha_inicio__lte=hoy).filter(fecha_fin__gte=hoy).filter(empresa=jefe_empresa).values('id') else None


        if len(listado_empleados_filtros_aplicados)>0:
            for empleado in listado_empleados_filtros_aplicados:
                listado_encabezados_por_persona=evaluacion_encabezado.objects.filter(evaluado__codigo=empleado,tipo_evaluacion_encabezado=1).values_list('id',flat=True)  
                encabezados[empleado]=listado_encabezados_por_persona

        
        colaboradores={}
        # for encabezados_por_persona in encabezados:
        #     acumulador_total=0
        #     contador_total=0
        #     ###print('encabezados_por_persona'+' '+encabezados_por_persona ,encabezados[encabezados_por_persona])
        #     if len(encabezados[encabezados_por_persona])>0:
        #         ###print('================================>',encabezados[encabezados_por_persona])
        #         for recorrido in encabezados[encabezados_por_persona]:
        #             ###print('.............................',recorrido)
        #             nota=calculo_nota_puntuacion_total(recorrido)
        #             ###print('notaaaaaaaaaaaaaaaaa',nota) 
        #             if nota!=False:
        #                 acumulador_total+=nota
        #                 contador_total+=1
                    


        #     ###print('acumulador_totalacumulador_total',acumulador_total)
        #     ###print('contador_totalcontador_total',contador_total)    
        #     if acumulador_total!=0 and contador_total!=0:
        lista_colaboradores_notas= evaluacion_encabezado.objects.annotate(
        nota_total_porcentaje_c=Case(
            When(tipo_evaluacion_encabezado=1, then=Cast('nota_total_porcentaje_prorateo',IntegerField())),
            When(tipo_evaluacion_encabezado=2, then=Cast('nota_total_porcentaje',IntegerField())),
            default=Value(0),
            )
        ).filter(periodicidad=periodicidad_vigente,evaluado__codigo__in=listado_empleados_filtros_aplicados).values_list('evaluado__codigo').annotate(Avg('nota_total_porcentaje_c'))        
        print('lista_colaboradores_notasasdasdasdasdasdasdasasdasddasdas',lista_colaboradores_notas)
        for colaborador, nota in lista_colaboradores_notas:
            if nota!=None:
                colaboradores[colaborador]= round(nota)


        listado_distribucion_media=[0,0,0,0,0,0,0,0,0,0]
        print('colaboradorescolaboradorescolaboradores',colaboradores)
        for nota in colaboradores:
            if colaboradores[nota]>=0 and colaboradores[nota]<=9:
                listado_distribucion_media[0]+=1
            if colaboradores[nota]>=10 and colaboradores[nota]<=19:
                listado_distribucion_media[1]+=1
            if colaboradores[nota]>=20 and colaboradores[nota]<=29:
                listado_distribucion_media[2]+=1
            if colaboradores[nota]>=30 and colaboradores[nota]<=39:
                listado_distribucion_media[3]+=1
            if colaboradores[nota]>=40 and colaboradores[nota]<=49:
                listado_distribucion_media[4]+=1
            if colaboradores[nota]>=50 and colaboradores[nota]<=59:
                listado_distribucion_media[5]+=1
            if colaboradores[nota]>=60 and colaboradores[nota]<=69:
                listado_distribucion_media[6]+=1
            if colaboradores[nota]>=70 and colaboradores[nota]<=79:
                listado_distribucion_media[7]+=1
            if colaboradores[nota]>=80 and colaboradores[nota]<=89:
                listado_distribucion_media[8]+=1
            if colaboradores[nota]>=90 and colaboradores[nota]<=99:
                listado_distribucion_media[9]+=1

        print('listado_distribucion_medialistado_distribucion_media',listado_distribucion_media)
        distribucion_m=[
          
                {
                    "Puntuacion_Media": "20", 
                    "Personas": listado_distribucion_media[2], 
                    "Distribucion_Normal": 0, 
                },
                {
                    "Puntuacion_Media": "30",
                    "Personas": listado_distribucion_media[3],
                    "Distribucion_Normal": 0,
                },
                {
                    "Puntuacion_Media": "40",
                    "Personas": listado_distribucion_media[4],
                    "Distribucion_Normal": 0,
                },
                {
                    "Puntuacion_Media": "50",
                    "Personas": listado_distribucion_media[5],
                    "Distribucion_Normal": 0,
                },
                {
                    "Puntuacion_Media": "60",
                    "Personas": listado_distribucion_media[6],
                    "Distribucion_Normal": 0,
                },
                {
                    "Puntuacion_Media": "70",
                    "Personas": listado_distribucion_media[7],
                    "Distribucion_Normal": 0,
                },
                {
                    "Puntuacion_Media": "80",
                    "Personas": listado_distribucion_media[8],
                    "Distribucion_Normal": 0,
                },
                {
                    "Puntuacion_Media": "90",
                    "Personas": listado_distribucion_media[9],
                    "Distribucion_Normal": 0,
                },
                ]



        if self.request.query_params.get('filter_año'):
                filter_año = self.request.query_params.get('filter_año')
        else:
            filter_año=año
        ###
        listado_nombre_competencia=[]
        listado_puntaje_obtenido=[]
        listado_puntaje_esperado=[]
        ###print('usuario.username',usuario.username)
        periodicidad_vigente=''
        jefe_empresa= (Funcional_empleado.objects.filter(codigo=usuario.username).values('unidad_organizativa__sociedad_financiera__id'))[0]['unidad_organizativa__sociedad_financiera__id'] if Funcional_empleado.objects.filter(codigo=usuario.username).values('unidad_organizativa__sociedad_financiera__id') else None
        if jefe_empresa!=None:
            ###print('ENTRO1')
            ###print('EMPRESA',jefe_empresa)
            periodicidad_vigente= (evaluacion_periodicidad.objects.filter(fecha_inicio__lte=hoy).filter(fecha_fin__gte=hoy).filter(empresa=jefe_empresa).values('id'))[0]['id'] if evaluacion_periodicidad.objects.filter(fecha_inicio__lte=hoy).filter(fecha_fin__gte=hoy).filter(empresa=jefe_empresa).values('id') else None
            ###print('periodicidad_vigente',periodicidad_vigente)
            if periodicidad_vigente!=None:
                ###print('ENTRO2')
                c=detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__id=periodicidad_vigente).values_list('evaluacion_plantilla_competencia__competencia__competencia_id',flat=True).distinct() if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__id=periodicidad_vigente).values_list('evaluacion_plantilla_competencia__competencia__competencia_id',flat=True).distinct() else None
                if c !=None:
                    ###print('ENTRO3')
                    resultadoss = detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia__competencia__competencia_id__in=c).filter(encabezado__evaluado__codigo__in=listado_empleados_filtros_aplicados).values_list('evaluacion_plantilla_competencia__competencia__competencia_id','evaluacion_plantilla_competencia__competencia__competencia__nombre','evaluacion_plantilla_competencia__competencia__desempeno_esperado').order_by('evaluacion_plantilla_competencia__competencia__competencia__nombre').annotate(Avg('nota_competencia_prorateada_decimal'))
                    for id ,nombre, esperado, obtenido in resultadoss:
                        
                        ###print('nombre',nombre)
                        ###print('esperado',esperado)
                        ###print('obtenidoi',obtenido)
                        ###print('#####################')
                        listado_nombre_competencia.append(nombre)
                        if obtenido==None:
                            return Response({"tiene evaluaciones pendientes"},status= status.HTTP_404_NOT_FOUND)
                        listado_puntaje_obtenido.append(round(obtenido))
                        listado_puntaje_esperado.append(esperado)

        data_competencia ={
            "labels": listado_nombre_competencia,
            "datasets": [
                    {
                        "label": "Puntaje",
                        "backgroundColor": "rgba(4, 127, 243)",
                        "borderColor": "rgb(14, 127, 243)",
                        "data": listado_puntaje_obtenido,
                    },
                    {
                        "label": "Esperado",
                        "backgroundColor": "rgba(243, 87, 4)",
                        "borderColor": "rgb(243, 87, 4)",
                        "data": listado_puntaje_esperado,
                    }
                ]
        }
        ##############################PROMEDIO#########################################
   
        # conteo_general=0
        # acumulador_general=0
        # total_genetal=0
        # for colaborador in colaboradores:
        #     acumulador_general+=colaboradores[colaborador]
        #     conteo_general+=1
            
        # total = acumulador_general/conteo_general
        total=0
        consulta_total_nota_general=evaluacion_encabezado.objects.annotate(
        nota_total_porcentaje_c=Case(
            When(tipo_evaluacion_encabezado=1, then=Cast('nota_total_porcentaje_prorateo',IntegerField())),
            When(tipo_evaluacion_encabezado=2, then=Cast('nota_total_porcentaje',IntegerField())),
            default=Value(0),
            )
        ).filter(periodicidad=periodicidad_vigente).filter(evaluado__codigo__in=listado_empleados_filtros_aplicados).values_list('periodicidad').annotate(Avg('nota_total_porcentaje_c')) 

        for periodicidad,nota in consulta_total_nota_general:
            if nota!=None:
                total= round(nota)
            else:
                total=0
        desempenio = (categoria_desempeno.objects.filter(periodicidad=periodicidad_vigente,valor_minimo__lte=total, valor_maximo__gte=total).values('descripcion'))[0]['descripcion'] if (categoria_desempeno.objects.filter(periodicidad=periodicidad_vigente,valor_minimo__lte=total, valor_maximo__gte=total).values('descripcion')) else 'Sin categorizaciòn'  
     #########################ALTO/BAJO DESEMPENIO##################################################
                ##############90 - 100    "Mejor Desempeño"###############
                ##############61 - 89      "Aceptable Desempeño""###############
                ##############0 - 60        "Bajo Desempeño"###############
        mejores_puntajes={}
        puntajes_intermedios={}
        peores_puntajes={}
        peores_puntajes_list=[]
        puntajes_intermedios_list=[]
        mejores_puntajes_list=[]

        for colaborador in colaboradores:
            if colaboradores[colaborador]>=90 and colaboradores[colaborador]<=100:
                mejores_puntajes[colaborador]=colaboradores[colaborador]

            if colaboradores[colaborador]>=61 and colaboradores[colaborador]<=89:
                puntajes_intermedios[colaborador]=colaboradores[colaborador]

            if colaboradores[colaborador]>=0 and colaboradores[colaborador]<=60:
                peores_puntajes[colaborador]=colaboradores[colaborador]
                
        
        
        mejor_puntaje_colaborador=''
        mejor_puntaje_puntaje=''
        if len(mejores_puntajes)>0:
            codigo=max(mejores_puntajes,key=mejores_puntajes.get)
            mejor_puntaje_puntaje=mejores_puntajes.get(codigo)
            mejor_puntaje_colaborador=(Funcional_empleado.objects.filter(codigo=codigo).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo).values('nombre') else None
        mejor_en_mejores_puntajes=[{

                    "empleado":mejor_puntaje_colaborador,
                    "puntaje":mejor_puntaje_puntaje
                }]
        #######################################
        medio_puntaje_colaborador=''
        medio_puntaje_puntaje=''
        if len(puntajes_intermedios)>0:
            codigo=max(puntajes_intermedios,key=puntajes_intermedios.get)
            medio_puntaje_puntaje=puntajes_intermedios.get(codigo)
            medio_puntaje_colaborador=(Funcional_empleado.objects.filter(codigo=codigo).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo).values('nombre') else None
        mejor_en_puntajes_intermedios=[{

                    "empleado":medio_puntaje_colaborador,
                    "puntaje":medio_puntaje_puntaje
                }]
        #######################################
        peor_puntaje_colaborador=''
        peor_puntaje_puntaje=''
        ##print('peores_puntajes',peores_puntajes)
        if len(peores_puntajes)>0:
            codigo=min(peores_puntajes,key=peores_puntajes.get)
            ##print('codigo',codigo)
            peor_puntaje_puntaje=peores_puntajes.get(codigo)
            ##print('peor_puntaje_puntaje',peor_puntaje_puntaje)
            peor_puntaje_colaborador=(Funcional_empleado.objects.filter(codigo=codigo).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo).values('nombre') else None
        peor_en_peores_puntajes=[{

                    "empleado":peor_puntaje_colaborador,
                    "puntaje":peor_puntaje_puntaje
                }]
        #######################################
        
        
        
       # data_peores={

                #     "puntaje":colaboradores[colaborador],
                #     "empleado":nombre
                # }


        listado_empledo_desempenio={}
        
        listado_empledo_desempenio['mejores_puntajes']=mejor_en_mejores_puntajes
        listado_empledo_desempenio['puntajes_intermedios']=mejor_en_puntajes_intermedios
        listado_empledo_desempenio['peores_puntajes']=peor_en_peores_puntajes
        
        #############################Comparación entre Empleados######################################
        datasets_1=[]
        for col in colaboradores:
            
            color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
            nombre=(Funcional_empleado.objects.filter(codigo=col).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=col).values('nombre') else None
            data={
            "label": nombre,
            "data": [colaboradores[col]],
            "backgroundColor": color,
            }
            datasets_1.append(data)

        # ###print('datasets',datasets_1)

        comparacion_empleados={
                            "labels": [""],
                            "datasets": datasets_1
                            }
        

        # empleado_mejor_rendimiento=max(colaboradores)
        # empleado_peor_rendimiento=min(colaboradores)
        # mejor_puntaje=colaboradores.get(empleado_mejor_rendimiento)
        # peor_puntaje=colaboradores.get(empleado_peor_rendimiento)
        # nombre_mejor_empleado= Funcional_empleado.objects.get(codigo=empleado_mejor_rendimiento) if Funcional_empleado.objects.filter(codigo=empleado_mejor_rendimiento) else None
        # nombre_peor_empleado= Funcional_empleado.objects.get(codigo=empleado_peor_rendimiento) if Funcional_empleado.objects.filter(codigo=empleado_peor_rendimiento) else None
        # mejor_peor_empleado={}
        # mejor_peor_empleado["Mejor_empleado_nombre"]=nombre_mejor_empleado.nombre
        # mejor_peor_empleado["puntaje_mejor_empleado"]=mejor_puntaje
        # mejor_peor_empleado["Peor_empleado_nombre"]= nombre_peor_empleado.nombre
        # mejor_peor_empleado["puntaje_peor_empleado"]=peor_puntaje

        #PUNTUACION TRIMESTRAL PROMEDIO
        periodos = evaluacion_encabezado.objects.annotate(
        nota_total_porcentaje_c=Case(
            When(tipo_evaluacion_encabezado=1, then=Cast('nota_total_porcentaje_prorateo',IntegerField())),
            When(tipo_evaluacion_encabezado=2, then=Cast('nota_total_porcentaje',IntegerField())),
            default=Value(0),
            )
        ).filter(periodicidad=periodicidad_vigente).filter(evaluado__codigo__in=listado_empleados_filtros_aplicados).values_list('periodicidad__evaluacion_configuracion_periodo__periodo','periodicidad__fecha_inicio__month').annotate(Avg('nota_total_porcentaje_c'))
        meses=[]
        nota_mes=[]
        meses_obj={'1':'Enero',
               '2':'Febrero',
               '3':'Marzo',
               '4':'Abril',
               '5':'Mayo',
               '6':'Junio',
               '7':'Julio',
               '8':'Agosto',
               '9':'Septiembre',
               '10':'Octubre',
               '11':'Noviembre',
               '12':'Diciembre'   
            }
        for periodo,mes,nota in periodos:
            #print('mes de esta onda',mes)
            m= meses_obj.get(str(mes))
            #print('aquiiiiiiiiiiiiiiiiiiii',m)
            meses.append(m)
            nota_mes.append(round(nota))






        
        
        ptp={
            'labels': meses,
            'datasets': [
                {
                'data': nota_mes,
                'borderColor': "rgb(216, 216, 216)",
                },
            ],
            }

        #####// Distribución de resultados de evaluación en número deempleados
        listado_rangos=[20,30,40,50,60,70,80,90,100]
        


        return Response({"listado_empledo_desempenio":listado_empledo_desempenio,"total":total,'desempenio_total':desempenio,'comparacion_empleados':comparacion_empleados,'Dasboard_competencias':data_competencia,'puntuacion_trimestral_promedio':ptp,"distribucion_m":distribucion_m})
 
class notificacion_auroraViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = notificacion_aurora.objects.all()
    serializer_class = notificacion_auroraserializer


    def list(self, request):
        queryset = notificacion_aurora.objects.all()
        serializer_class = notificacion_auroraserializer(queryset, many=True)
        id_destinatario=''
        leido=None
        filter_kwargs={}
        
        if self.request.query_params.get('leido'):
            leido = self.request.query_params.get('leido')
        
        if self.request.query_params.get('id_destinatario'):
            id_destinatario = self.request.query_params.get('id_destinatario')

        if id_destinatario!='':
            filter_kwargs['destinatario_id']= id_destinatario

        if leido!=None:
            if leido=='1':
                estado=True
                filter_kwargs['leido']= estado
            if leido=='0':
                estado=False
                filter_kwargs['leido']= estado
                
                
        


        #print('filter_kwargs',filter_kwargs)
    
        if id_destinatario!='':
            queryset =  notificacion_aurora.objects.filter(**filter_kwargs).order_by('id')
            #print('queryset',queryset)
            conteo =  notificacion_aurora.objects.filter(destinatario_id=id_destinatario).count()
            serializer = notificacion_auroraserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":conteo})
        else:
            return Response({"Destinatario no encontrado"},status= status.HTTP_404_NOT_FOUND)


    def put(self,requets,id):
        existe= notificacion_aurora.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= notificacion_auroraserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
 
def calculo_nota_puntuacion_total(encabezado_id):
    encabezado_evaluado= (evaluacion_encabezado.objects.filter(id=encabezado_id).values('evaluado'))[0]['evaluado'] if evaluacion_encabezado.objects.filter(id=encabezado_id).values('evaluado') else None
    encabezado_periodicidad=  (evaluacion_encabezado.objects.filter(id=encabezado_id).values('periodicidad'))[0]['periodicidad'] if evaluacion_encabezado.objects.filter(id=encabezado_id).values('periodicidad') else None
    encabezado_periodo =  (evaluacion_encabezado.objects.filter(id=encabezado_id).values('periodicidad__evaluacion_configuracion_periodo__periodo'))[0]['periodicidad__evaluacion_configuracion_periodo__periodo'] if evaluacion_encabezado.objects.filter(id=encabezado_id).values('periodicidad__evaluacion_configuracion_periodo__periodo') else None
    encabezado_tipo_evaluacion =  (evaluacion_encabezado.objects.filter(id=encabezado_id).values('tipo_evaluacion__id'))[0]['tipo_evaluacion__id'] if evaluacion_encabezado.objects.filter(id=encabezado_id).values('tipo_evaluacion__id') else None
    #########################################################################################################################
    resultados_evaluaciones=list(evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion).values('id','tipo_evaluacion_encabezado')) if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion).values('id','tipo_evaluacion_encabezado') else None
    if  resultados_evaluaciones!=None:
            for x in resultados_evaluaciones:
                id_encabezado = x['id']
                id_tipo_evaluacion=x['tipo_evaluacion_encabezado']
                
                if id_tipo_evaluacion==1:
                    #print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                    #print('id_encabezado',id_encabezado)
                    #print('id_tipo_evaluacion',id_tipo_evaluacion)
                    nota_competencia= evaluacion_encabezado.objects.filter(id=id_encabezado).values('nota_total_porcentaje_prorateo','nivel_resultado')
                    nota_total_competencia =nota_competencia[0]['nota_total_porcentaje_prorateo']
                    nota_total_competencia_desempeno=nota_competencia[0]['nivel_resultado']
                    encabezado_competencia_id=id_encabezado


                if id_tipo_evaluacion==2:
                    #print('##################################')
                    #print('id_encabezado',id_encabezado)
                    #print('id_tipo_evaluacion',id_tipo_evaluacion)
                    nota_factor= evaluacion_encabezado.objects.filter(id=id_encabezado).values('nota_total_porcentaje','nivel_resultado')
                    nota_total_factor = nota_factor[0]['nota_total_porcentaje']
                    nota_total_factor_desempenio = nota_factor[0]['nivel_resultado']
                    

            if nota_total_competencia!=None and nota_total_factor!=None:
                total_desempenio= (int(nota_total_competencia)+int(nota_total_factor))/2
            else:
                return False 
            
            
    return total_desempenio


class validar_envio_evaluacion_colaborador(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none()
    def post(self,request):
        competencia=''
        factor=''
        comentario=None
        competencia_encabezado_id=int(request.data["competencia_encabezado_id"])
        factor_encabezado_id=int(request.data["factor_encabezado_id"])
        competencia=validacion_evaluacion_competencia(competencia_encabezado_id)
        factor=validacion_evaluacion_factor(factor_encabezado_id)
        comentario_evaluador = (evaluacion_encabezado.objects.filter(id=factor_encabezado_id).values('comentario_evaluador'))[0]['comentario_evaluador'] if evaluacion_encabezado.objects.filter(id=factor_encabezado_id).values('comentario_evaluador') else None 
        comentario_evaluado = (evaluacion_encabezado.objects.filter(id=factor_encabezado_id).values('comentario_evaluado'))[0]['comentario_evaluado'] if evaluacion_encabezado.objects.filter(id=factor_encabezado_id).values('comentario_evaluador') else None
        
        if competencia==True and factor==True and comentario_evaluador!=None:
            funcion_correo_evaluacion(factor_encabezado_id,'colaborador: Jefe realizo su evaluacion')

        else:
            return Response({'La evaluacion aun no esta completa'},status=status.HTTP_400_BAD_REQUEST)

        return Response('notificacion_enviada',status= status.HTTP_200_OK)

def funcional_get_colaborador(empleado_codigo):
    hoy=datetime.now().date()
    if not empleado_codigo:
        return []
    empleado = list(Funcional_empleado.objects.filter(jefe_inmediato__in=empleado_codigo).filter(Q(fecha_baja__gt=hoy)|Q(fecha_baja=None)).exclude(codigo__in=empleado_codigo).values_list("codigo",flat=True))
    result=[]
    # result = funcional_get_colaborador(empleado)
    result.extend(empleado)    

    return result



def validacion_descriptor_clasificacion(codigo_empleado):
    id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado) if Funcional_empleado.objects.filter(codigo=codigo_empleado) else None
    if id_funcion==None:
        return False
    posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0] if id_funcion.posicion.all() else None 
    if posicion==None:
        return False
    descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=posicion).order_by('-id').first() if descriptor_perfil_datos_generales.objects.filter(posicion=posicion) else None
    if descriptor==None:
        return False

    clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
    if clasificacion==None:
        return False
    
    funciones=descriptor_perfil_funcion.objects.filter(descriptor_id=descriptor.id,fundamental=True).values('descripcion') if descriptor_perfil_funcion.objects.filter(descriptor_id=descriptor.id,fundamental=True).values('descripcion') else None
    if funciones==None:
        return False

    indicadores=descriptor_perfil_indicador_descriptor.objects.filter(descriptor_id=descriptor.id).values('indicador__objetivo') if descriptor_perfil_indicador_descriptor.objects.filter(descriptor_id=descriptor.id).values('indicador__objetivo') else None
    if indicadores==True:
        return False


    return True



class validacion_decriptor_colaborador(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none()

    def get(self,request):
        codigo=''
        validacion=''
        
        if self.request.query_params.get('codigo_empleado'):
            codigo=self.request.query_params.get('codigo_empleado')
        
        if codigo!='':
            validacion=validacion_descriptor_clasificacion(codigo)
        else:
            validacion=False
    
        return Response({"Resultado":validacion},status= status.HTTP_200_OK)