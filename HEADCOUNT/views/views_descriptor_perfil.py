from decimal import MIN_EMIN
from distutils.cygwinccompiler import Mingw32CCompiler
from email import message
from email.policy import HTTP
from urllib import response
from django.db.models.functions import ExtractYear
from re import sub
from django.contrib.auth.models import User,Group
from django.http.response import Http404
from django.shortcuts import render
from calendar import monthrange
from HEADCOUNT.serializers.serializers_descriptor_perfil import descriptor_perfil_competenciaserializer
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
from datetime import datetime,timedelta
import json
from ..serializers import *
from ..models import *
from django.apps import apps
from datetime import datetime,timedelta
from django.core.exceptions import ObjectDoesNotExist
import sys
from rest_framework import generics
import io
import csv
sys.setrecursionlimit(100000000)                                                        
from rest_framework import viewsets
import requests
from datetime import datetime



class descriptor_perfil_datos_generalesViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_datos_generales.objects.all()
    serializer_class = descriptor_perfil_datos_generalesserializer
    def list(self, request):
        ##print(self.request.query_params.get('filter'))
        queryset = descriptor_perfil_datos_generales.objects.all()
        serializer = descriptor_perfil_datos_generalesserializer(queryset, many=True)
        filter=''
        filter_nombre='' #este filtro se utilizara para hacer una busqueda por and en caso de que se requiera buscar dos parametros

        tipo_busqueda=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('filter_nombre'):
            filter_nombre = self.request.query_params.get('filter_nombre')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                filter_kwargs2={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='posicion_id':
                        filter_kwargs['posicion__id'] = filter

                if filter_nombre !='':
                    filter_kwargs2['nombre_posicion__icontains'] = filter_nombre
                    queryset =  descriptor_perfil_datos_generales.objects.filter(**filter_kwargs2,**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  descriptor_perfil_datos_generales.objects.filter(**filter_kwargs).count()
                    serializer = descriptor_perfil_datos_generalesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})  

                queryset =  descriptor_perfil_datos_generales.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_datos_generales.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_datos_generalesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_datos_generales.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_datos_generales.objects.filter().count()
                serializer = descriptor_perfil_datos_generalesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                filter_kwargs2={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='posicion_id':
                        filter_kwargs['posicion__id'] = filter
                if filter_nombre !='':
                    filter_kwargs2['nombre_posicion__icontains'] = filter_nombre
                    queryset =  descriptor_perfil_datos_generales.objects.filter(**filter_kwargs2,**filter_kwargs).order_by('id')
                    conteo =  descriptor_perfil_datos_generales.objects.filter(**filter_kwargs).count()
                    serializer = descriptor_perfil_datos_generalesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                        
                queryset =  descriptor_perfil_datos_generales.objects.filter(**filter_kwargs).order_by('id')
                serializer = descriptor_perfil_datos_generalesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  descriptor_perfil_datos_generales.objects.filter().order_by('id')
                serializer = descriptor_perfil_datos_generalesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        serializer = descriptor_perfil_datos_generalesserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            descriptor_perfil_datos_generales.objects.filter(id=serializer.data["id"]).update(creado_por=request.user)
            dato= descriptor_perfil_datos_generales.objects.get(id=serializer.data["id"])
            serializer = descriptor_perfil_datos_generalesserializer(dato)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def update(self, request, pk=None):
        
        dg = descriptor_perfil_datos_generales.objects.filter(id=pk) if descriptor_perfil_datos_generales.objects.filter(id=pk) else None

        if dg!=None:
            queryset = descriptor_perfil_datos_generales.objects.get(id=pk)
            serializer = descriptor_perfil_datos_generalesserializer(instance=queryset, data=request.data)
            descriptor=''
            if serializer.is_valid():
                serializer.save()
                descriptor= descriptor_perfil_datos_generales.objects.get(id=pk) if descriptor_perfil_datos_generales.objects.filter(id=pk) else None
                ##################################
                clasificacion=''
                division=''
                if descriptor!=None:
                    if descriptor.clasificacion_empleado:
                        clasificacion=descriptor.clasificacion_empleado.pk

                    if descriptor.division:
                        division= descriptor.division.pk
            
                ###################################
                competencia_descriptor_query=descriptor_perfil_competencia_descriptor.objects.filter(descriptor=pk) if descriptor_perfil_competencia_descriptor.objects.filter(descriptor=pk) else None
                # print('competencia_descriptor_query',competencia_descriptor_query)
                if competencia_descriptor_query!=None:
                    competencia_descriptor_query.update(clasificacion=clasificacion,division=division)
                    # print('competencia_descriptor_query',competencia_descriptor_query) 
                descriptor_perfil_datos_generales.objects.filter(id=serializer.data["id"]).update(actualizado_por=request.user)
                dato= descriptor_perfil_datos_generales.objects.get(id=serializer.data["id"])
                serializer = descriptor_perfil_datos_generalesserializer(dato)
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El proposito no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
       
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class descriptor_perfil_competenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_competencia.objects.all()
    serializer_class = descriptor_perfil_competenciaserializer
    def list(self, request):
        queryset = descriptor_perfil_competencia.objects.all()
        serializer_class = descriptor_perfil_competenciaserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='clasificacion_id':
                        filter_kwargs['clasificacion__id'] = filter
                    if tipo_busqueda =='clasificacion_nombre':
                        filter_kwargs['clasificacion__nombre'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='descripcion':
                            filter_kwargs_2['descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__date__icontains'] = filter_2
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='clasificacion_id':
                            filter_kwargs_2['clasificacion__id'] = filter_2
                        if tipo_busqueda_2 =='clasificacion_nombre':
                            filter_kwargs_2['clasificacion__nombre'] = filter_2


                    queryset =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = descriptor_perfil_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).count()
                    serializer = descriptor_perfil_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})


                queryset =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_competencia.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_competencia.objects.filter().count()
                serializer = descriptor_perfil_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='clasificacion_id':
                        filter_kwargs['clasificacion__id'] = filter
                    if tipo_busqueda =='clasificacion_nombre':
                        filter_kwargs['clasificacion__nombre'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='descripcion':
                            filter_kwargs_2['descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 =='fecha_creacion':
                            filter_kwargs_2['fecha_creacion__date__icontains'] = filter_2
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='clasificacion_id':
                            filter_kwargs_2['clasificacion__id'] = filter_2
                        if tipo_busqueda_2 =='clasificacion_nombre':
                            filter_kwargs_2['clasificacion__nombre'] = filter_2

                    queryset =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = descriptor_perfil_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).count()
                    serializer = descriptor_perfil_competenciaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
                        
                queryset =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_competencia.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 

            else:
                queryset =  descriptor_perfil_competencia.objects.filter().order_by('id')
                conteo =  descriptor_perfil_competencia.objects.filter().count()
                serializer = descriptor_perfil_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        serializer = descriptor_perfil_competenciaserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def update(self, request, pk=None):
        
        cp = descriptor_perfil_competencia.objects.filter(id=pk) if descriptor_perfil_competencia.objects.filter(id=pk) else None
        validacion_peso_existe= descriptor_perfil_competencia.objects.filter(id=pk).values_list('evaluacion_competencia__peso',flat=True)
        if not None in validacion_peso_existe and request.data['clasificacion']:
            return Response({"mensaje":"La clasificación no puede ser editada porque ya esta siendo utilizada en una evaluación "},status=status.HTTP_404_NOT_FOUND)
        

        if cp!=None:
            queryset = descriptor_perfil_competencia.objects.get(id=pk)
            serializer = descriptor_perfil_competenciaserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                competencia = descriptor_perfil_competencia.objects.get(id=pk) if descriptor_perfil_competencia.objects.filter(id=pk) else None
                ##################################
                nombre = ''
                descripcion = ''
                archivo =''
                tipo_competencia =''

                if competencia!=None:
                    if competencia.nombre:
                        nombre=competencia.nombre

                    if competencia.descripcion:
                        descripcion= competencia.descripcion
                    
                    if competencia.archivo:
                        archivo= competencia.archivo
                    
                    if competencia.tipo_competencia:
                        tipo_competencia = competencia.tipo_competencia

                ###########################################
                competencia_query=descriptor_perfil_competencia_descriptor.objects.filter(competencia=pk) if descriptor_perfil_competencia_descriptor.objects.filter(competencia=pk) else None
                # print('competencia_descriptor_query',competencia_descriptor_query)
                if competencia_query!=None:
                    competencia_query.update(nombre=nombre,descripcion=descripcion,archivo=archivo,tipo_competencia=tipo_competencia)
                    # print('competencia_descriptor_query',competencia_descriptor_query)   

                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"La competencia no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class descriptor_perfil_competencia_descriptorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_competencia_descriptor.objects.all()
    serializer_class = descriptor_perfil_competencia_descriptorserializer
    def list(self, request):
        ##print(self.request.query_params.get('filter'))
        queryset = descriptor_perfil_competencia_descriptor.objects.all()
        serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
        filter=''
        segundo_filter=''
        tercer_filter=''
        tipo_busqueda=''
        segundo_tipo_busqueda=''
        tercer_tipo_busqueda=''

        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('segundo_filter'):
            segundo_filter = self.request.query_params.get('segundo_filter')

        if self.request.query_params.get('tercer_filter'):
            tercer_filter = self.request.query_params.get('tercer_filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        if self.request.query_params.get('segundo_tipo_busqueda'):
            segundo_tipo_busqueda = self.request.query_params.get('segundo_tipo_busqueda')
        
        if self.request.query_params.get('tercer_tipo_busqueda'):
            tercer_tipo_busqueda = self.request.query_params.get('tercer_tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='competencia_nombre':
                        filter_kwargs['competencia__nombre__icontains'] = filter
                    if tipo_busqueda =='tipo_competencia_descripcion':
                        filter_kwargs['tipo_competencia__descripcion__icontains'] = filter
                    if tipo_busqueda =='tipo_competencia_id':
                        filter_kwargs['tipo_competencia'] = filter
                    if tipo_busqueda =='area_descripcion':
                        filter_kwargs['area__descripcion__icontains'] = filter

                    if tipo_busqueda =='division_descripcion':
                        filter_kwargs['division__descripcion__icontains'] = filter

                    if tipo_busqueda =='clasificacion_nombre':
                        filter_kwargs['clasificacion__nombre__icontains'] = filter

                if segundo_tipo_busqueda!='' and segundo_filter!='':
                    filter_kwargs_2={}
                    
                    if segundo_tipo_busqueda:
                        if segundo_tipo_busqueda=='clasificacion_nombre':
                            filter_kwargs_2['clasificacion__nombre__icontains']= segundo_filter
                        if segundo_tipo_busqueda=='clasificacion_id':
                            filter_kwargs_2['clasificacion']= segundo_filter
                        if segundo_tipo_busqueda =='descriptor_nombre':
                            filter_kwargs_2['descriptor__nombre_posicion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='descriptor_id':
                            filter_kwargs_2['descriptor'] = segundo_filter
                            
            

                        queryset =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs,**filter_kwargs_2).order_by('id')[offset:offset+limit]
                        serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset.count()})

                queryset =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_competencia_descriptor.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_competencia_descriptor.objects.filter().count()
                serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descriptor_nombre':
                            filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='competencia_nombre':
                        filter_kwargs['competencia__nombre__icontains'] = filter
                    if tipo_busqueda =='tipo_competencia_descripcion':
                        filter_kwargs['tipo_competencia__descripcion__icontains'] = filter
                    if tipo_busqueda =='tipo_competencia_id':
                        filter_kwargs['tipo_competencia'] = filter
                    if tipo_busqueda =='area_descripcion':
                        filter_kwargs['area__descripcion__icontains'] = filter

                    if tipo_busqueda =='division_descripcion':
                        filter_kwargs['division__descripcion__icontains'] = filter

                    if tipo_busqueda =='clasificacion_nombre':
                        filter_kwargs['clasificacion__nombre__icontains'] = filter
            
                if segundo_tipo_busqueda!='' and segundo_filter!='':
                    filter_kwargs_2={}
                    
                    if segundo_tipo_busqueda:
                        if segundo_tipo_busqueda=='clasificacion_nombre':
                            filter_kwargs_2['clasificacion__nombre__icontains']= segundo_filter
                        if segundo_tipo_busqueda=='clasificacion_id':
                            filter_kwargs_2['clasificacion']= segundo_filter
                        if segundo_tipo_busqueda =='descriptor_nombre':
                            filter_kwargs_2['descriptor__nombre_posicion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='descriptor_id':
                            filter_kwargs_2['descriptor'] = segundo_filter
                        

                        queryset =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs,**filter_kwargs_2).order_by('id')
                        queryset2 =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs,**filter_kwargs_2,nivel_desarrollo__gt=0).order_by('id')
                        serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset.count(),"conteo_nivel_desarrollo":queryset2.count()})

                queryset =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs).order_by('id')
                serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  descriptor_perfil_competencia_descriptor.objects.filter().order_by('id')
                serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

    def create(self, request):
        serializer = descriptor_perfil_competencia_descriptorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,requets,id):
        existe= descriptor_perfil_competencia_descriptor.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= descriptor_perfil_competencia_descriptorserializer(put,data=requets.data)
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

class archivos_gestor_competenciaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = archivos_gestor_competencia.objects.all()
    serializer_class = archivos_gestor_competenciaserializer
    def list(self, request):
        queryset = archivos_gestor_competencia.objects.all()
        objeto= archivos_gestor_competencia.objects.all()
        serializer = archivos_gestor_competenciaserializer(queryset, many=True)
        tipo_documento=''

        if self.request.query_params.get('tipo_documento'):
            tipo_documento = self.request.query_params.get('tipo_documento')

        if tipo_documento:
            queryset = archivos_gestor_competencia.objects.filter(tipo_documento=tipo_documento).order_by('-id')
            serializer = archivos_gestor_competenciaserializer(queryset, many=True)
            return Response({"data":serializer.data})
        else:
            queryset = archivos_gestor_competencia.objects.filter().order_by('-id')
            serializer = archivos_gestor_competenciaserializer(queryset, many=True)
            return Response({"data":serializer.data})

class archivos_gestor_competencia_postViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none() 
    def post(self,request):
        url =  settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CarpetaDetalle'
       ##print('entro')
        myobj = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado']}

        x = requests.post(url, data = myobj)
        response_dict = x.json()
        

        if len(response_dict)>0:
           ##print(response_dict)
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CrearDocumento'


            llave = str(self.request.data['subnivel1']) +'-'+ str(self.request.data['subnivel2']) 

            #llave = str(self.request.data['descripcion']) 
            
            objeto = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado'],'llave':llave,'origen':self.request.data['origen'],'documento':self.request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}
            x = requests.post(enlace, data = objeto)
            resultado = x.json()
           ##print(resultado)
            if x.status_code==400:
                return Response({"resultado":resultado},status= status.HTTP_404_NOT_FOUND)

            for error in resultado:
                if error['response'].find('creado')==-1:
                    return Response({"resultado":resultado},status= status.HTTP_404_NOT_FOUND)
                    
            for result in resultado:
                indice1=result['response'].index(':')+1
                indice2=result['response'].index(',')
                id_gestor=result['response'][indice1:indice2] if indice1 and indice2 else None


            doc=archivos_gestor_competencia.objects.create(id_documento=id_gestor, llave=llave,id_area=self.request.data['id_area'],id_carpeta_encabezado=self.request.data['id_carpeta_encabezado'],medidas_disciplinarias=self.request.data['medidas_disciplinarias'],tipo_documento=self.request.data['tipo_documento'],origen=self.request.data['origen'],extension=self.request.data['extension'],contentTypeGD=self.request.data['contentTypeGD'],nombre=self.request.data['nombre'],descripcion=self.request.data['descripcion'],subnivel1=self.request.data['subnivel1'],subnivel2=self.request.data['subnivel2'])
            return Response({"resultado": archivos_gestor_competenciaserializer(doc).data},status= status.HTTP_200_OK)
        else:
            return Response({"resultado":"No se puede verificar el contenido el detalle de la carpeta"},status= status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return archivos_gestor_competencia.objects.get(pk=pk)
        except archivos_gestor_competencia.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = archivos_gestor_competenciaserializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/ModificarDocumento'
            objeto = {'id':post.id_documento,'ceid':post.id_carpeta_encabezado,'llave':post.llave,'origen':post.origen,'documento':request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}
            ##print('objeto',objeto)
            x = requests.post(enlace, data = objeto)
            resultado = x.json()
            for result in resultado:
               ##print('resultado',result)
                if result['response'].find('Correctamente')==-1:
                        return Response({"resultado":result['response']},status= status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk):
        existe= archivos_gestor_competencia.objects.filter(id=pk).count()
        if existe!=0:
            get = self.get_object(pk)
            #get =  on_off_bording_bienvenida.objects.filter(id=id) if on_off_bording_bienvenida.objects.filter(id=id) else None 
            serializer=archivos_gestor_competenciaserializer(get)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


# class descriptor_perfil_competencia_descriptor_archivoViewSet(viewsets.ModelViewSet):
#     authentication_classes=[TokenAuthentication]
#     permission_classes=[DjangoModelPermissions]
#     queryset = descriptor_perfil_competencia_descriptor_archivo.objects.all()
#     serializer_class = descriptor_perfil_competencia_descriptor_archivoserializer
#     def list(self, request):
#         ##print(self.request.query_params.get('filter'))
#         queryset = descriptor_perfil_competencia_descriptor_archivo.objects.all()
#         serializer = descriptor_perfil_competencia_descriptor_archivoserializer(queryset, many=True)
#         filter=''
#         tipo_busqueda=''
#         if self.request.query_params.get('filter'):
#             filter = self.request.query_params.get('filter')

#         if self.request.query_params.get('tipo_busqueda'):
#             tipo_busqueda = self.request.query_params.get('tipo_busqueda')

#         if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
#             offset=int(self.request.query_params.get('offset'))
#             limit=int(self.request.query_params.get('limit'))

#             if filter!='' and tipo_busqueda!='':
#                 filter_kwargs={}
#                 if tipo_busqueda:
#                     if tipo_busqueda =='nombre':
#                         filter_kwargs['nombre__icontains'] = filter
#                     if tipo_busqueda =='descripcion':
#                         filter_kwargs['descripcion__icontains'] = filter
#                     if tipo_busqueda =='descriptor':
#                         filter_kwargs['competencia_descriptor__id'] = filter






#                 queryset =  descriptor_perfil_competencia_descriptor_archivo.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
#                 conteo =  descriptor_perfil_competencia_descriptor_archivo.objects.filter(**filter_kwargs).count()
#                 serializer = descriptor_perfil_competencia_descriptor_archivoserializer(queryset, many=True)
#                 return Response({"data":serializer.data,"count":conteo})  
#             else: 
#                 queryset =  descriptor_perfil_competencia_descriptor_archivo.objects.filter().order_by('id')[offset:offset+limit]
#                 conteo =  descriptor_perfil_competencia_descriptor_archivo.objects.filter().count()
#                 serializer = descriptor_perfil_competencia_descriptor_archivoserializer(queryset, many=True)
#                 return Response({"data":serializer.data,"count":conteo})
#         else:
#             if filter!='' and tipo_busqueda!='':
#                 filter_kwargs={}
#                 if tipo_busqueda:
#                     if tipo_busqueda =='nombre':
#                         filter_kwargs['nombre__icontains'] = filter
#                     if tipo_busqueda =='descripcion':
#                         filter_kwargs['descripcion__icontains'] = filter
#                     if tipo_busqueda =='descriptor':
#                         filter_kwargs['competencia_descriptor__id'] = filter

                        
#                 queryset =  descriptor_perfil_competencia_descriptor_archivo.objects.filter(**filter_kwargs).order_by('id')
#                 serializer = descriptor_perfil_competencia_descriptor_archivoserializer(queryset, many=True)
#                 return Response({"data":serializer.data,"count":queryset.count()})
#             else:
#                 queryset =  descriptor_perfil_competencia_descriptor_archivo.objects.filter().order_by('id')
#                 serializer = descriptor_perfil_competencia_descriptor_archivoserializer(queryset, many=True)
#                 return Response({"data":serializer.data,"count":queryset.count()})


#     def create(self, request):
#         serializer = descriptor_perfil_competencia_descriptor_archivoserializer(data=request.data)
#         if serializer.is_valid(): 
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         else:       
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     def put(self,requets,id):
#         existe= descriptor_perfil_competencia_descriptor_archivo.objects.filter(id=id).count()
#         if existe!=0:
#             put = self.get_object(id)
#             serializer= descriptor_perfil_competencia_descriptor_archivoserializer(put,data=requets.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data,status=status.HTTP_200_OK)
#             else:
#                 return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)

#     def delete(self,request,id):
#         eliminar = self.get_object(id)
#         eliminar.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class descriptor_perfil_tipo_competenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_tipo_competencia.objects.all()
    serializer_class = descriptor_perfil_tipo_competenciaserializer
    def list(self, request):
        queryset = descriptor_perfil_tipo_competencia.objects.all()
        serializer_class = descriptor_perfil_tipo_competenciaserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_tipo_competencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_tipo_competencia.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_tipo_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_tipo_competencia.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_tipo_competencia.objects.filter().count()
                serializer = descriptor_perfil_tipo_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_tipo_competencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_tipo_competencia.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_tipo_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_tipo_competencia.objects.filter().order_by('id')
                conteo =  descriptor_perfil_tipo_competencia.objects.filter().count()
                serializer = descriptor_perfil_tipo_competenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
  
    def create(self, request):
        # do your thing here
        serializer = descriptor_perfil_tipo_competenciaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # #print(serializer.data)
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El tipo de competencia no ha sido creado"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        tipo_competencia = descriptor_perfil_tipo_competencia.objects.filter(id=pk) if descriptor_perfil_tipo_competencia.objects.filter(id=pk) else None

        if tipo_competencia!=None:
            queryset = descriptor_perfil_tipo_competencia.objects.get(id=pk)
            serializer = descriptor_perfil_tipo_competenciaserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El tipo de competencia no ha sido encontrada"},status=status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_tipo_competencia_id'):
            id = self.request.query_params.get('descriptor_perfil_tipo_competencia_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto "},status=status.HTTP_400_BAD_REQUEST)

        
        area = descriptor_perfil_tipo_competencia.objects.filter(id=id).values() if descriptor_perfil_tipo_competencia.objects.filter(id=id) else None

        
        if area:
            queryset = descriptor_perfil_tipo_competencia.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"Tipo de competencia no existe"},status=status.HTTP_404_NOT_FOUND)
        

class descriptor_perfil_datos_unidad_medidaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_datos_unidad_medida.objects.all()
    serializer_class = descriptor_perfil_datos_unidad_medidaserializer
    def list(self, request):
        queryset = descriptor_perfil_datos_unidad_medida.objects.all()
        serializer_class = descriptor_perfil_datos_unidad_medidaserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_datos_unidad_medida.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_datos_unidad_medida.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_datos_unidad_medidaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_datos_unidad_medida.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_datos_unidad_medida.objects.filter().count()
                serializer = descriptor_perfil_datos_unidad_medidaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_datos_unidad_medida.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_datos_unidad_medida.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_datos_unidad_medidaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_datos_unidad_medida.objects.filter().order_by('id')
                conteo =  descriptor_perfil_datos_unidad_medida.objects.filter().count()
                serializer = descriptor_perfil_datos_unidad_medidaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        serializer = descriptor_perfil_datos_unidad_medidaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # #print(serializer.data)
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La unidad de medida no ha sido creada"}, status=status.HTTP_400_BAD_REQUEST)
   
    def update(self, request, pk=None):
        
        unidad_medida = descriptor_perfil_datos_unidad_medida.objects.filter(id=pk) if descriptor_perfil_datos_unidad_medida.objects.filter(id=pk) else None

        if unidad_medida!=None:
            queryset = descriptor_perfil_datos_unidad_medida.objects.get(id=pk)
            serializer = descriptor_perfil_datos_unidad_medidaserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"La unidad de medida no ha sido encontrada"},status=status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('unidad_medida_id'):
            id = self.request.query_params.get('unidad_medida_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        unidad_medida = descriptor_perfil_datos_unidad_medida.objects.filter(id=id).values() if descriptor_perfil_datos_unidad_medida.objects.filter(id=id) else None

        
        if unidad_medida:
            queryset = descriptor_perfil_datos_unidad_medida.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La unidad de medida no existe"},status=status.HTTP_404_NOT_FOUND)


class descriptor_perfil_areaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_area.objects.all()
    serializer_class = descriptor_perfil_areaserializer
    def list(self, request):
        queryset = descriptor_perfil_area.objects.all()
        serializer_class = descriptor_perfil_areaserializer(queryset, many=True)
        filter=''
        
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        
                    
                


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_area.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_area.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_areaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_area.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_area.objects.filter().count()
                serializer = descriptor_perfil_areaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_area.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_area.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_areaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_area.objects.filter().order_by('id')
                conteo =  descriptor_perfil_area.objects.filter().count()
                serializer = descriptor_perfil_areaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        serializer = descriptor_perfil_areaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # #print(serializer.data)
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La area no ha sido creada"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        area = descriptor_perfil_area.objects.filter(id=pk) if descriptor_perfil_area.objects.filter(id=pk) else None

        if area!=None:
            queryset = descriptor_perfil_area.objects.get(id=pk)
            serializer = descriptor_perfil_areaserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"La area no ha sido encontrada"},status=status.HTTP_404_NOT_FOUND)
        
    
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_area_id'):
            id = self.request.query_params.get('descriptor_perfil_area_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        area = descriptor_perfil_area.objects.filter(id=id).values() if descriptor_perfil_area.objects.filter(id=id) else None

        
        if area:
            queryset = descriptor_perfil_area.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La area no existe"},status=status.HTTP_404_NOT_FOUND)


class descriptor_perfil_propositoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_proposito.objects.all()
    serializer_class = descriptor_perfil_propositoserializer
    def list(self, request):
        queryset = descriptor_perfil_proposito.objects.all()
        serializer_class = descriptor_perfil_propositoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_proposito.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_proposito.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_propositoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_proposito.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_proposito.objects.filter().count()
                serializer = descriptor_perfil_propositoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_proposito.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_proposito.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_propositoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_proposito.objects.filter().order_by('id')
                conteo =  descriptor_perfil_proposito.objects.filter().count()
                serializer = descriptor_perfil_propositoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        serializer = descriptor_perfil_propositoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # #print(serializer.data)
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El propósito no ha sido creado "}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        proposito = descriptor_perfil_proposito.objects.filter(id=pk) if descriptor_perfil_proposito.objects.filter(id=pk) else None

        if proposito!=None:
            queryset = descriptor_perfil_proposito.objects.get(id=pk)
            serializer = descriptor_perfil_propositoserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El proposito no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_proposito_id'):
            id = self.request.query_params.get('descriptor_perfil_proposito_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        area = descriptor_perfil_proposito.objects.filter(id=id).values() if descriptor_perfil_proposito.objects.filter(id=id) else None

        
        if area:
            queryset = descriptor_perfil_proposito.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El propósito no existe"},status=status.HTTP_404_NOT_FOUND)
   
   


class descriptor_perfil_formacion_area_conocimientoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_formacion_area_conocimiento.objects.all()
    serializer_class = descriptor_perfil_formacion_area_conocimientoserializer

    def list(self, request):
        queryset = descriptor_perfil_formacion_area_conocimiento.objects.all()
        serializer_class = descriptor_perfil_formacion_area_conocimientoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_formacion_area_conocimiento.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_formacion_area_conocimiento.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_formacion_area_conocimientoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_formacion_area_conocimiento.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_formacion_area_conocimiento.objects.filter().count()
                serializer = descriptor_perfil_formacion_area_conocimientoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_formacion_area_conocimiento.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_formacion_area_conocimiento.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_formacion_area_conocimientoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_formacion_area_conocimiento.objects.filter().order_by('id')
                conteo =  descriptor_perfil_formacion_area_conocimiento.objects.filter().count()
                serializer = descriptor_perfil_formacion_area_conocimientoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        nombre=''
        if "nombre" in request.data:
            nombre=request.data['nombre']

        serializer = descriptor_perfil_formacion_area_conocimientoserializer(data=request.data)
        # #print(request.data['nombre'])
        if serializer.is_valid() and nombre!='':
            serializer.save()
            # #print(serializer.data)
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"El área de conocimientos no ha sido creada, parámetro incorrecto "}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        nombre=''
        if "nombre" in request.data:
            nombre=request.data['nombre']

        area_conocimiento = descriptor_perfil_formacion_area_conocimiento.objects.filter(id=pk) if descriptor_perfil_formacion_area_conocimiento.objects.filter(id=pk) else None

        if area_conocimiento!=None:
            queryset = descriptor_perfil_formacion_area_conocimiento.objects.get(id=pk)
            serializer = descriptor_perfil_formacion_area_conocimientoserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid() and nombre!='':
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada, parámetro incorrecto"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"mensaje":"El área de conocimientos no ha sido encontrada"},status=status.HTTP_404_NOT_FOUND)
   
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_formacion_area_conocimiento_id'):
            id = self.request.query_params.get('descriptor_perfil_formacion_area_conocimiento_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        area_conocimiento = descriptor_perfil_formacion_area_conocimiento.objects.filter(id=id).values() if descriptor_perfil_formacion_area_conocimiento.objects.filter(id=id) else None

        
        if area_conocimiento:
            queryset = descriptor_perfil_formacion_area_conocimiento.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El área de conocimientos no existe"},status=status.HTTP_404_NOT_FOUND)



class descriptor_perfil_politicas_procedimientosViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_politicas_procedimientos.objects.all()
    serializer_class = descriptor_perfil_politicas_procedimientosserializer

    def list(self, request):
        ##print(self.request.query_params.get('filter'))
        queryset = descriptor_perfil_politicas_procedimientos.objects.all()
        serializer = descriptor_perfil_politicas_procedimientosserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter

                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    

                queryset =  descriptor_perfil_politicas_procedimientos.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_politicas_procedimientos.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_politicas_procedimientosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_politicas_procedimientos.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_politicas_procedimientos.objects.filter().count()
                serializer = descriptor_perfil_politicas_procedimientosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter

                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter


                queryset =  descriptor_perfil_politicas_procedimientos.objects.filter(**filter_kwargs).order_by('id')
                serializer = descriptor_perfil_politicas_procedimientosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  descriptor_perfil_politicas_procedimientos.objects.filter().order_by('id')
                serializer = descriptor_perfil_politicas_procedimientosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        serializer = descriptor_perfil_politicas_procedimientosserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= descriptor_perfil_politicas_procedimientos.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= descriptor_perfil_politicas_procedimientosserializer(put,data=requets.data)
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


class descriptor_perfil_indicadorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_indicador.objects.all()
    serializer_class = descriptor_perfil_indicadorserializer
    def list(self, request):
        ##print(self.request.query_params.get('filter'))
        queryset = descriptor_perfil_indicador.objects.all()
        serializer = descriptor_perfil_indicadorserializer(queryset, many=True)
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
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='objetivo':
                        filter_kwargs['objetivo__icontains'] = filter

                queryset =  descriptor_perfil_indicador.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_indicador.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_indicadorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_indicador.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_indicador.objects.filter().count()
                serializer = descriptor_perfil_indicadorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='objetivo':
                        filter_kwargs['objetivo__icontains'] = filter


                queryset =  descriptor_perfil_indicador.objects.filter(**filter_kwargs).order_by('id')
                serializer = descriptor_perfil_indicadorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  descriptor_perfil_indicador.objects.filter().order_by('id')
                serializer = descriptor_perfil_indicadorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        serializer = descriptor_perfil_indicadorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= descriptor_perfil_indicador.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= descriptor_perfil_indicadorserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,request,pk):

        validacion_registro=''
        dpf = descriptor_perfil_indicador.objects.filter(pk=pk).values() if descriptor_perfil_indicador.objects.filter(pk=pk) else None

        
        if dpf!=None:
            validacion_registro= detalle_evaluacion_factor.objects.filter(factor__tipo_factor=2).filter(respuesta_pregunta=pk) if detalle_evaluacion_factor.objects.filter(factor__tipo_factor=2).filter(respuesta_pregunta=pk) else None
            
            if validacion_registro!=None:
                return Response({"mensaje":"El parámetro no puede ser eliminado porque está siendo utilizado en las evaluaciones del desempeño."}, status=status.HTTP_400_BAD_REQUEST)

            descriptor_perfil_indicador.objects.filter(pk=pk).delete()
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El registro no existe"},status=status.HTTP_404_NOT_FOUND)


class descriptor_perfil_indicador_descriptorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_indicador_descriptor.objects.all()
    serializer_class = descriptor_perfil_indicador_descriptorserializer
    def list(self, request):
        ##print(self.request.query_params.get('filter'))
        queryset = descriptor_perfil_indicador_descriptor.objects.all()
        serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
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
                    if tipo_busqueda =='indicador_id':
                        filter_kwargs['indicador__id'] = filter
                    if tipo_busqueda =='indicador_nombre':
                        filter_kwargs['indicador__nombre__icontains'] = filter
                    if tipo_busqueda =='objetivo':
                        filter_kwargs['indicador__objetivo__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='descriptor__nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='indicador':
                            filter_kwargs_2['indicador__id'] = filter_2
                        if tipo_busqueda_2 =='indicador_nombre':
                            filter_kwargs_2['indicador__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='objetivo':
                            filter_kwargs_2['indicador__objetivo__icontains'] = filter_2
                        if tipo_busqueda_2 =='descriptor':
                            filter_kwargs_2['descriptor__id'] = filter_2
                        if tipo_busqueda_2 =='descriptor__nombre':
                            filter_kwargs_2['descriptor__nombre_posicion__icontains'] = filter_2


                    queryset =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  descriptor_perfil_indicador_descriptor.objects.filter().count()
                    serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})


                        
                        

                queryset =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_indicador_descriptor.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_indicador_descriptor.objects.filter().count()
                serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='indicador_id':
                        filter_kwargs['indicador__id'] = filter
                    if tipo_busqueda =='indicador_nombre':
                        filter_kwargs['indicador__nombre__icontains'] = filter
                    if tipo_busqueda =='objetivo':
                        filter_kwargs['indicador__objetivo__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='descriptor__nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='indicador':
                            filter_kwargs_2['indicador__id'] = filter_2
                        if tipo_busqueda_2 =='indicador_nombre':
                            filter_kwargs_2['indicador__nombre__icontains'] = filter_2
                        if tipo_busqueda_2 =='objetivo':
                            filter_kwargs_2['indicador__objetivo__icontains'] = filter_2
                        if tipo_busqueda_2 =='descriptor':
                            filter_kwargs_2['descriptor__id'] = filter_2
                        if tipo_busqueda_2 =='descriptor__nombre':
                            filter_kwargs_2['descriptor__nombre_posicion__icontains'] = filter_2
                    queryset =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                    conteo =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  
                else: 
                    queryset =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  descriptor_perfil_indicador_descriptor.objects.filter().count()
                    serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

                queryset =  descriptor_perfil_indicador_descriptor.objects.filter(**filter_kwargs).order_by('id')
                serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  descriptor_perfil_indicador_descriptor.objects.filter().order_by('id')
                serializer = descriptor_perfil_indicador_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        serializer = descriptor_perfil_indicador_descriptorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= descriptor_perfil_indicador_descriptor.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= descriptor_perfil_indicador_descriptorserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self,request,pk):

        validacion_registro=''
        dpf = descriptor_perfil_indicador_descriptor.objects.filter(pk=pk).values() if descriptor_perfil_indicador_descriptor.objects.filter(pk=pk) else None

        if dpf!=None:
            indicador_id=  (descriptor_perfil_indicador_descriptor.objects.filter(pk=pk).values('indicador'))[0]['indicador'] if descriptor_perfil_indicador_descriptor.objects.filter(pk=pk).values('indicador') else None
            
            if indicador_id!=None:
                validacion_registro= detalle_evaluacion_factor.objects.filter(factor__tipo_factor=2).filter(respuesta_pregunta=indicador_id) if detalle_evaluacion_factor.objects.filter(factor__tipo_factor=2).filter(respuesta_pregunta=indicador_id) else None
            else:
                validacion_registro=None
                
            if validacion_registro!=None:
                return Response({"mensaje":"El parámetro no puede ser eliminado porque está siendo utilizado en las evaluaciones del desempeño."}, status=status.HTTP_400_BAD_REQUEST)

            descriptor_perfil_indicador_descriptor.objects.filter(pk=pk).delete()
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El registro no existe"},status=status.HTTP_404_NOT_FOUND)



class descriptor_perfil_preparacionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_preparacion.objects.all()
    serializer_class = descriptor_perfil_preparacionserializer
    def list(self, request):
        ##print(self.request.query_params.get('filter'))
        queryset = descriptor_perfil_preparacion.objects.all()
        serializer = descriptor_perfil_preparacionserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='curso__id':
                        filter_kwargs['curso__id'] = filter                        
                    


                queryset =  descriptor_perfil_preparacion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_preparacion.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_preparacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_preparacion.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_preparacion.objects.filter().count()
                serializer = descriptor_perfil_preparacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='curso__id':
                        filter_kwargs['curso__id'] = filter                        

                        
                queryset =  descriptor_perfil_preparacion.objects.filter(**filter_kwargs).order_by('id')
                serializer = descriptor_perfil_preparacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  descriptor_perfil_preparacion.objects.filter().order_by('id')
                serializer = descriptor_perfil_preparacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        serializer = descriptor_perfil_preparacionserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= descriptor_perfil_preparacion.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= descriptor_perfil_preparacionserializer(put,data=requets.data)
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





class descriptor_perfil_formacion_nivel_educativoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_formacion_nivel_educativo.objects.all()
    serializer_class = descriptor_perfil_formacion_nivel_educativoserializer
    def list(self, request):
        queryset = descriptor_perfil_formacion_nivel_educativo.objects.all()
        serializer_class = descriptor_perfil_formacion_nivel_educativoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_formacion_nivel_educativo.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_formacion_nivel_educativo.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_formacion_nivel_educativoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_formacion_nivel_educativo.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_formacion_nivel_educativo.objects.filter().count()
                serializer = descriptor_perfil_formacion_nivel_educativoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_formacion_nivel_educativo.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_formacion_nivel_educativo.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_formacion_nivel_educativoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_formacion_nivel_educativo.objects.filter().order_by('id')
                conteo =  descriptor_perfil_formacion_nivel_educativo.objects.filter().count()
                serializer = descriptor_perfil_formacion_nivel_educativoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        nombre=''
        if "nombre" in request.data:
            nombre=request.data['nombre']

        serializer = descriptor_perfil_formacion_nivel_educativoserializer(data=request.data)
        # #print(request.data['nombre'])
        if serializer.is_valid() and nombre!='':
            serializer.save()
            # #print(serializer.data)
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"El nivel educativo no ha sido creado, parámetro incorrecto "}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        nombre=''
        if "nombre" in request.data:
            nombre=request.data['nombre']

        nive_educacion = descriptor_perfil_formacion_nivel_educativo.objects.filter(id=pk) if descriptor_perfil_formacion_nivel_educativo.objects.filter(id=pk) else None

        if nive_educacion!=None:
            queryset = descriptor_perfil_formacion_nivel_educativo.objects.get(id=pk)
            serializer = descriptor_perfil_formacion_nivel_educativoserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid() and nombre!='':
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada, parámetro incorrecto"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"mensaje":"El nivel de educativo no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_formacion_nivel_educativo_id'):
            id = self.request.query_params.get('descriptor_perfil_formacion_nivel_educativo_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        nivel_educacion = descriptor_perfil_formacion_nivel_educativo.objects.filter(id=id).values() if descriptor_perfil_formacion_nivel_educativo.objects.filter(id=id) else None

        
        if nivel_educacion:
            queryset = descriptor_perfil_formacion_nivel_educativo.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El nivel educativo no existe"},status=status.HTTP_404_NOT_FOUND)



class descriptor_perfil_tituloViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_titulo.objects.all()
    serializer_class = descriptor_perfil_tituloserializer
    def list(self, request):
        queryset = descriptor_perfil_titulo.objects.all()
        serializer_class = descriptor_perfil_tituloserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nivel_academico':
                        filter_kwargs['nivel_academico_id__nombre__icontains'] = filter
                    if tipo_busqueda =='titulo':
                        filter_kwargs['titulo__icontains'] = filter
                    if tipo_busqueda =='area_conocimiento':
                        filter_kwargs['area_conocimiento_id__nombre__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_titulo.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_titulo.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_titulo.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_titulo.objects.filter().count()
                serializer = descriptor_perfil_tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nivel_academico':
                        filter_kwargs['nivel_academico_id__nombre__icontains'] = filter
                    if tipo_busqueda =='titulo':
                        filter_kwargs['titulo__icontains'] = filter
                    if tipo_busqueda =='area_conocimiento':
                        filter_kwargs['area_conocimiento_id__nombre__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_titulo.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_titulo.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_titulo.objects.filter().order_by('id')
                conteo =  descriptor_perfil_titulo.objects.filter().count()
                serializer = descriptor_perfil_tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
  
    def create(self, request):
        serializer = descriptor_perfil_tituloserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Título no ha sido creado, parámetro incorrecto "}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        tipo_competencia = descriptor_perfil_titulo.objects.filter(id=pk) if descriptor_perfil_titulo.objects.filter(id=pk) else None

        if tipo_competencia!=None:
            queryset = descriptor_perfil_titulo.objects.get(id=pk)
            serializer = descriptor_perfil_tituloserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El título no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
     
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_titulo_id'):
            id = self.request.query_params.get('descriptor_perfil_titulo_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        titulo = descriptor_perfil_titulo.objects.filter(id=id).values() if descriptor_perfil_titulo.objects.filter(id=id) else None

        
        if titulo:
            queryset = descriptor_perfil_titulo.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El título no existe"},status=status.HTTP_404_NOT_FOUND)



class descriptor_perfil_conocimiento_tecnicoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_conocimiento_tecnico.objects.all()
    serializer_class = descriptor_perfil_conocimiento_tecnicoserializer
    def list(self, request):
        queryset = descriptor_perfil_conocimiento_tecnico.objects.all()
        serializer_class = descriptor_perfil_conocimiento_tecnicoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_conocimiento_tecnico.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_conocimiento_tecnico.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_conocimiento_tecnicoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_conocimiento_tecnico.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_conocimiento_tecnico.objects.filter().count()
                serializer = descriptor_perfil_conocimiento_tecnicoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_conocimiento_tecnico.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_conocimiento_tecnico.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_conocimiento_tecnicoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_conocimiento_tecnico.objects.filter().order_by('id')
                conteo =  descriptor_perfil_conocimiento_tecnico.objects.filter().count()
                serializer = descriptor_perfil_conocimiento_tecnicoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        nombre=''
        if "nombre" in request.data:
            nombre=request.data['nombre']

        serializer = descriptor_perfil_conocimiento_tecnicoserializer(data=request.data)
        # #print(request.data['nombre'])
        if serializer.is_valid() and nombre!='':
            serializer.save()
            # #print(serializer.data)
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"El conocimiento técnico no ha sido creado, parámetro incorrecto "}, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk=None):
        nombre=''
        if "nombre" in request.data:
            nombre=request.data['nombre']

        area_conocimiento = descriptor_perfil_conocimiento_tecnico.objects.filter(id=pk) if descriptor_perfil_conocimiento_tecnico.objects.filter(id=pk) else None

        if area_conocimiento!=None:
            queryset = descriptor_perfil_conocimiento_tecnico.objects.get(id=pk)
            serializer = descriptor_perfil_conocimiento_tecnicoserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid() and nombre!='':
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada, parámetro incorrecto"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"mensaje":"El conocimiento técnico no ha sido encontrada"},status=status.HTTP_404_NOT_FOUND)
 
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_conocimiento_tecnico_id'):
            id = self.request.query_params.get('descriptor_perfil_conocimiento_tecnico_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        conocimiento = descriptor_perfil_conocimiento_tecnico.objects.filter(id=id).values() if descriptor_perfil_conocimiento_tecnico.objects.filter(id=id) else None

        
        if conocimiento:
            queryset = descriptor_perfil_conocimiento_tecnico.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El conocimiento técnico no existe"},status=status.HTTP_404_NOT_FOUND)

##############################################################################
class descriptor_perfil_formacionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_formacion.objects.all()
    serializer_class = descriptor_perfil_formacionserializer
    def list(self, request):
        queryset = descriptor_perfil_formacion.objects.all()
        serializer_class = descriptor_perfil_formacionserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='formacion':
                        filter_kwargs['formacion_id__titulo__icontains'] = filter
                    if tipo_busqueda =='indispensable':
                        filter_kwargs['indispensable__icontains'] = filter
                        
                        
                queryset =  descriptor_perfil_formacion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_formacion.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_formacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_formacion.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_formacion.objects.filter().count()
                serializer = descriptor_perfil_formacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='formacion':
                        filter_kwargs['formacion_id__titulo__icontains'] = filter
                    if tipo_busqueda =='indispensable':
                        filter_kwargs['indispensable__icontains'] = filter
                        
                queryset =  descriptor_perfil_formacion.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_formacion.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_formacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_formacion.objects.filter().order_by('id')
                conteo =  descriptor_perfil_formacion.objects.filter().count()
                serializer = descriptor_perfil_formacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = descriptor_perfil_formacionserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La formación no ha sido creada"}, status=status.HTTP_400_BAD_REQUEST)
   
    def update(self, request, pk=None):
        
        formacion = descriptor_perfil_formacion.objects.filter(id=pk) if descriptor_perfil_formacion.objects.filter(id=pk) else None

        if formacion!=None:
            queryset = descriptor_perfil_formacion.objects.get(id=pk)
            serializer = descriptor_perfil_formacionserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"La formación no ha sido encontrada"},status=status.HTTP_404_NOT_FOUND)
  
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_formacion_id'):
            id = self.request.query_params.get('descriptor_perfil_formacion_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        formacion = descriptor_perfil_formacion.objects.filter(id=id).values() if descriptor_perfil_formacion.objects.filter(id=id) else None

        
        if formacion:
            queryset = descriptor_perfil_formacion.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La formación no existe"},status=status.HTTP_404_NOT_FOUND)



class descriptor_perfil_conocimiento_tecnico_adquiridoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_conocimiento_tecnico_adquirido.objects.all()
    serializer_class = descriptor_perfil_conocimiento_tecnico_adquiridoserializer
    def list(self, request):
        queryset = descriptor_perfil_conocimiento_tecnico_adquirido.objects.all()
        serializer_class = descriptor_perfil_conocimiento_tecnico_adquiridoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor_id__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor_id'] = filter
                    if tipo_busqueda =='indispensable':
                        filter_kwargs['indispensable__icontains'] = filter
                   
                        
                        
                queryset =  descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_conocimiento_tecnico_adquiridoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter().count()
                serializer = descriptor_perfil_conocimiento_tecnico_adquiridoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='indispensable':
                        filter_kwargs['indispensable__icontains'] = filter
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor_id__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor_id'] = filter
                        
                queryset =  descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_conocimiento_tecnico_adquiridoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter().order_by('id')
                conteo =  descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter().count()
                serializer = descriptor_perfil_conocimiento_tecnico_adquiridoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = descriptor_perfil_conocimiento_tecnico_adquiridoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El conocimiento técnico adquirido no ha sido creada"}, status=status.HTTP_400_BAD_REQUEST)
  
    def update(self, request, pk=None):
        
        conocimiento = descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter(id=pk) if descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter(id=pk) else None

        if conocimiento!=None:
            queryset = descriptor_perfil_conocimiento_tecnico_adquirido.objects.get(id=pk)
            serializer = descriptor_perfil_conocimiento_tecnico_adquiridoserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El conocimiento técnico adquirido no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
  
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('descriptor_perfil_conocimiento_tecnico_adquirido_id'):
            id = self.request.query_params.get('descriptor_perfil_conocimiento_tecnico_adquirido_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        conocimiento = descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter(id=id).values() if descriptor_perfil_conocimiento_tecnico_adquirido.objects.filter(id=id) else None

        
        if conocimiento:
            queryset = descriptor_perfil_conocimiento_tecnico_adquirido.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El conocimiento técnico adquirido no existe"},status=status.HTTP_404_NOT_FOUND)



class descriptor_perfil_funcionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_funcion.objects.all()
    serializer_class = descriptor_perfil_funcionserializer
    def list(self, request):
        queryset = descriptor_perfil_funcion.objects.all()
        serializer_class = descriptor_perfil_funcionserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='perioricidad':
                        filter_kwargs['perioricidad'] = filter
                    if tipo_busqueda =='unidad_medida':
                        filter_kwargs['unidad_medida_id'] = filter
                    if tipo_busqueda =='descriptor':
                        filter_kwargs['descriptor_id'] = filter
                   
                        
                        
                queryset =  descriptor_perfil_funcion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_funcion.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_funcionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()}) 
            else: 
                queryset =  descriptor_perfil_funcion.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_funcion.objects.filter().count()
                serializer = descriptor_perfil_funcionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='perioricidad':
                        filter_kwargs['perioricidad'] = filter
                    if tipo_busqueda =='unidad_medida':
                        filter_kwargs['unidad_medida_id'] = filter
                    if tipo_busqueda =='descriptor':
                        filter_kwargs['descriptor_id'] = filter
                        
                queryset =  descriptor_perfil_funcion.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_funcion.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_funcionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()}) 
            else: 
                queryset =  descriptor_perfil_funcion.objects.filter().order_by('id')
                conteo =  descriptor_perfil_funcion.objects.filter().count()
                serializer = descriptor_perfil_funcionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

    def create(self, request):
        serializer = descriptor_perfil_funcionserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La función no ha sido creada"}, status=status.HTTP_400_BAD_REQUEST)
  
    def update(self, request, pk=None):
        validacion_registro=''
        funcion = descriptor_perfil_funcion.objects.filter(id=pk) if descriptor_perfil_funcion.objects.filter(id=pk) else None
        
        

        if funcion!=None:
            if 'fundamental' in request.data:
                validacion_registro= detalle_evaluacion_factor.objects.filter(factor__tipo_factor=1).filter(respuesta_pregunta=pk) if detalle_evaluacion_factor.objects.filter(factor__tipo_factor=1).filter(respuesta_pregunta=pk) else None
            
            if validacion_registro!=None:
                return Response({"mensaje":"El parámetro fundamental no puede ser modificado porque está siendo utilizado en las evaluaciones del desempeño."}, status=status.HTTP_400_BAD_REQUEST)
            #################################################################################################
            queryset = descriptor_perfil_funcion.objects.get(id=pk)
            serializer = descriptor_perfil_funcionserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"La función no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
  
    def destroy(self,request,pk):

        validacion_registro=''
        dpf = descriptor_perfil_funcion.objects.filter(pk=pk).values() if descriptor_perfil_funcion.objects.filter(pk=pk) else None

        
        if dpf!=None:
            validacion_registro= detalle_evaluacion_factor.objects.filter(factor__tipo_factor=1).filter(respuesta_pregunta=pk) if detalle_evaluacion_factor.objects.filter(factor__tipo_factor=1).filter(respuesta_pregunta=pk) else None
            
            if validacion_registro!=None:
                return Response({"mensaje":"El parámetro no puede ser eliminado porque está siendo utilizado en las evaluaciones del desempeño."}, status=status.HTTP_400_BAD_REQUEST)

            descriptor_perfil_funcion.objects.filter(pk=pk).delete()
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El registro no existe"},status=status.HTTP_404_NOT_FOUND)


class descriptor_perfil_proposito_descriptorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_proposito_descriptor.objects.all()
    serializer_class = descriptor_perfil_proposito_descriptorserializer
    #print(queryset)
    def list(self, request):
        queryset = descriptor_perfil_proposito_descriptor.objects.all()
        serializer_class = descriptor_perfil_proposito_descriptorserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                   
                        
                        
                queryset =  descriptor_perfil_proposito_descriptor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_proposito_descriptor.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_proposito_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_proposito_descriptor.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_proposito_descriptor.objects.filter().count()
                serializer = descriptor_perfil_proposito_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='perioricidad':
                        filter_kwargs['perioricidad'] = filter
                    if tipo_busqueda =='unidad_medida':
                        filter_kwargs['unidad_medida_id'] = filter
                        
                queryset =  descriptor_perfil_proposito_descriptor.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_proposito_descriptor.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_proposito_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_proposito_descriptor.objects.filter().order_by('id')
                conteo =  descriptor_perfil_proposito_descriptor.objects.filter().count()
                serializer = descriptor_perfil_proposito_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = descriptor_perfil_proposito_descriptorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"Descriptor no ha sido creado"}, status=status.HTTP_400_BAD_REQUEST)
  
    def update(self, request, pk=None):
        
        descriptor = descriptor_perfil_proposito_descriptor.objects.filter(id=pk) if descriptor_perfil_proposito_descriptor.objects.filter(id=pk) else None

        if descriptor!=None:
            queryset = descriptor_perfil_proposito_descriptor.objects.get(id=pk)
            serializer = descriptor_perfil_proposito_descriptorserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"La función no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
  
    def delete(self, request):
        id =''
        if self.request.query_params.get('descriptor_perfil_proposito_descriptor_id'):
            id = self.request.query_params.get('descriptor_perfil_proposito_descriptor_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)
        funcion = descriptor_perfil_proposito_descriptor.objects.filter(id=id).values() if descriptor_perfil_proposito_descriptor.objects.filter(id=id) else None     
        if funcion:
            queryset = descriptor_perfil_proposito_descriptor.objects.get(id=id).delete()
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La función no existe"},status=status.HTTP_404_NOT_FOUND)



class descriptor_perfil_experienciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_experiencia.objects.all()
    serializer_class = descriptor_perfil_experienciaserializer

    def list(self, request):
        queryset = descriptor_perfil_experiencia.objects.all()
        serializer_class = descriptor_perfil_experienciaserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #print(filter)
            #print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='detalle':
                        filter_kwargs['detalle__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor'] = filter
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                   
                        
                        
                queryset =  descriptor_perfil_experiencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_experiencia.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_experienciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_experiencia.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_experiencia.objects.filter().count()
                serializer = descriptor_perfil_experienciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='detalle':
                        filter_kwargs['detalle__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor'] = filter
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                
                        
                queryset =  descriptor_perfil_experiencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_experiencia.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_experienciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_experiencia.objects.filter().order_by('id')
                conteo =  descriptor_perfil_experiencia.objects.filter().count()
                serializer = descriptor_perfil_experienciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        serializer = descriptor_perfil_experienciaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # #print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"Experiencia no ha sido Registrada"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        experiencia = descriptor_perfil_experiencia.objects.filter(id=pk) if descriptor_perfil_experiencia.objects.filter(id=pk) else None

        if experiencia!=None:
            queryset = descriptor_perfil_experiencia.objects.get(id=pk)
            serializer = descriptor_perfil_experienciaserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"La experiencia no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
  
    def delete(self, request):
        id =''
        if self.request.query_params.get('descriptor_perfil_experiencia_id'):
            id = self.request.query_params.get('descriptor_perfil_experiencia_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)
        funcion = descriptor_perfil_experiencia.objects.filter(id=id).values() if descriptor_perfil_experiencia.objects.filter(id=id) else None     
        if funcion:
            queryset = descriptor_perfil_experiencia.objects.get(id=id).delete()
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La experiencia no existe"},status=status.HTTP_404_NOT_FOUND)

# APIVIEW DE NOTIFICACIONES
class descriptor_perfil_envio_correoViewSet(APIView):
    authentication_classes=[TokenAuthentication]

    def post(self,request):
        notificaciones = self.request.data['data']
        modulo='DESCRIPTOR_PERFIL'
        usuario=''
        tipo_mensaje = ''
        usuario=request.user
        #print('asdasdasdsadsadsadasgdffg',usuario)
        funcion_descriptor=''
        for variable in notificaciones:
            
            
            if "funcion_descriptor" in variable:
                funcion_descriptor = variable['funcion_descriptor']
            
            if "tipo_mensaje" in variable:
                tipo_mensaje = variable['tipo_mensaje']
            
            if funcion_descriptor!='' and tipo_mensaje!='' and usuario!='':
                descriptor_perfil_correo(funcion_descriptor,tipo_mensaje,usuario)
                
            else:
                return Response({"mensaje":"No hemos recibido los valores completos"},status= status.HTTP_404_NOT_FOUND)

         
   
        return Response ({"mensaje":"Proceso exitoso"},status= status.HTTP_200_OK)



def descriptor_perfil_correo(funcion_descriptor,tipo_mensaje,usuario):
    modulo='DESCRIPTOR_PERFIL'
    if tipo_mensaje == 'Jefe actualiza descriptor':
        codigo_jefe=''
        codigo_empleado=''
        correo_responsable=''
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Descriptores_Perfiles').values_list('username',flat=True)
        #print('usuarios_reponsables',usuarios_reponsables)
        for usuario_responable in usuarios_reponsables:
            configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
            if configuracion_correo:

                asunto=configuracion_correo[0]['asunto']
                mensaje=configuracion_correo[0]['mensaje']
                variables_envio_correo= nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
                if variables_envio_correo:
                    for vec in variables_envio_correo:
                        variable= vec.variable
                        app= vec.app
                        modelos= vec.modelos
                        valores= vec.valores
                        modelo_tb= apps.get_model(app,modelos)
                        if variable=='@@ResponsableDescriptoresPerfiles':
                            responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                            correo_responsable = Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                            #print('correo responsable',correo_responsable)
                            valor_a_sustituir = responsable[0]['nombre'] 
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))                                      
                        elif variable=='@@JefeSolicitaPlaza':
                            jefe = Funcional_empleado.objects.filter(codigo=usuario).values("nombre")
                            if jefe:
                                valor_a_sustituir=jefe[0]['nombre']
                                
                                
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                
                                return Response({"mensaje":"No se encontro codigo de jefe"},status= status.HTTP_404_NOT_FOUND)
                        elif variable=='@@codigo':
                            codigo = usuario
                            if codigo:
                                valor_a_sustituir=codigo
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                
                                return Response({"mensaje":"No se encontro codigo de jefe"},status= status.HTTP_404_NOT_FOUND)
                        elif variable=='@@Funcion':
                            codigo = usuario
                            funcion = Funcional_empleado.objects.filter(codigo=usuario).values('puesto__descripcion')
                            funcion_nombre =funcion[0]['puesto__descripcion']
                            if funcion_nombre:
                                valor_a_sustituir=funcion_nombre
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                
                                return Response({"mensaje":"No se encontro codigo de jefe"},status= status.HTTP_404_NOT_FOUND)
                        elif variable=='@@NuevaFuncionDescriptor':
                            funcion_busqueda=Funcional_Funciones.objects.filter(id=funcion_descriptor).values('descripcion')
                            funcion_des = funcion_busqueda[0]['descripcion']
                            if funcion_des:
                                valor_a_sustituir=funcion_des
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                
                                return Response({"mensaje":"No se encontro codigo de jefe"},status= status.HTTP_404_NOT_FOUND)
                        elif variable=='@@Fechamodificacion':
                            fecha =datetime.today().strftime('%d/%m/%y')
                            if fecha:
                                valor_a_sustituir=fecha
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                
                                return Response({"mensaje":"No se encontro codigo de jefe"},status= status.HTTP_404_NOT_FOUND)
                        
                        
                          
            if correo_responsable:
                correo_a_enviar= correo_responsable[0]['correo_empresarial']
                if correo_a_enviar:
                    from_email_jefe= settings.EMAIL_HOST_USER
                    try:
                        msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                        msg_jefe.send()
                    except BadHeaderError:
                        return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
    
        
        
    return 1




class descriptor_perfil_competencia_totalViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_competencia_total.objects.all()
    serializer_class = descriptor_perfil_competencia_totalserializer
    def list(self, request):
        queryset = descriptor_perfil_competencia_total.objects.all()
        serializer_class = descriptor_perfil_competencia_totalserializer(queryset, many=True)
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
                    if tipo_busqueda =='total':
                        filter_kwargs['total'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_competencia_total.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_competencia_total.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_competencia_totalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_competencia_total.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_competencia_total.objects.filter().count()
                serializer = descriptor_perfil_competencia_totalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='total':
                        filter_kwargs['total'] = filter
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                queryset =  descriptor_perfil_competencia_total.objects.filter(**filter_kwargs).order_by('id')
                conteo =  descriptor_perfil_competencia_total.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_competencia_totalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  descriptor_perfil_competencia_total.objects.filter().order_by('id')
                conteo =  descriptor_perfil_competencia_total.objects.filter().count()
                serializer = descriptor_perfil_competencia_totalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = descriptor_perfil_competencia_totalserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class descriptor_perfil_colaborador_FuncionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_datos_generales.objects.all()
    serializer_class = descriptor_perfil_datos_generalesserializer
    #print(queryset)
    def list(self, request):
        queryset = Funcional_empleado.objects.all()
        serializer_class = Funcional_empleadoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        codigo_empleado=''
        if self.request.query_params.get('codigo_empleado'):
            codigo_empleado = self.request.query_params.get('codigo_empleado')
        
        empleado = Funcional_empleado.objects.filter(codigo=codigo_empleado) if Funcional_empleado.objects.filter(codigo=codigo_empleado) else None
        
        if empleado!=None:
             serializer = Funcional_empleadoserializer(empleado, many=True)
             return Response({"data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"Empleado no encontrado"},status= status.HTTP_404_NOT_FOUND)



class descriptor_perfil_competencia_descriptor_correccionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_competencia_descriptor.objects.all()
    serializer_class = descriptor_perfil_competencia_descriptorserializer
    def list(self, request):
        ##print(self.request.query_params.get('filter'))
        queryset = descriptor_perfil_competencia_descriptor.objects.all()
        serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
        filter=''
        segundo_filter=''
        tercer_filter=''
        tipo_busqueda=''
        segundo_tipo_busqueda=''
        tercer_tipo_busqueda=''

        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('segundo_filter'):
            segundo_filter = self.request.query_params.get('segundo_filter')

        if self.request.query_params.get('tercer_filter'):
            tercer_filter = self.request.query_params.get('tercer_filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        if self.request.query_params.get('segundo_tipo_busqueda'):
            segundo_tipo_busqueda = self.request.query_params.get('segundo_tipo_busqueda')
        
        if self.request.query_params.get('tercer_tipo_busqueda'):
            tercer_tipo_busqueda = self.request.query_params.get('tercer_tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='competencia_nombre':
                        filter_kwargs['competencia__nombre__icontains'] = filter
                    if tipo_busqueda =='tipo_competencia_descripcion':
                        filter_kwargs['competencia__tipo_competencia__descripcion__icontains'] = filter
                    if tipo_busqueda =='tipo_competencia_id':
                        filter_kwargs['competencia__tipo_competencia'] = filter
                    if tipo_busqueda =='area_descripcion':
                        filter_kwargs['area__descripcion__icontains'] = filter
                    if tipo_busqueda =='division_descripcion':
                        filter_kwargs['division__descripcion__icontains'] = filter
                    if tipo_busqueda =='clasificacion_nombre':
                        filter_kwargs['clasificacion__nombre__icontains'] = filter

                if segundo_tipo_busqueda!='' and segundo_filter!='':
                    filter_kwargs_2={}
                    
                    if segundo_tipo_busqueda:
                        if segundo_tipo_busqueda =='descriptor_nombre':
                            filter_kwargs_2['descriptor__nombre_posicion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='descriptor_id':
                            filter_kwargs_2['descriptor__id'] = segundo_filter
                        if segundo_tipo_busqueda =='competencia_nombre':
                            filter_kwargs_2['competencia__nombre__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='tipo_competencia_descripcion':
                            filter_kwargs_2['competencia__tipo_competencia__descripcion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='tipo_competencia_id':
                            filter_kwargs_2['competencia__tipo_competencia'] = segundo_filter
                        if segundo_tipo_busqueda =='area_descripcion':
                            filter_kwargs_2['area__descripcion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='division_descripcion':
                            filter_kwargs_2['division__descripcion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='clasificacion_nombre':
                            filter_kwargs_2['clasificacion__nombre__icontains'] = segundo_filter
                            
            

                        queryset =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs,**filter_kwargs_2).order_by('id')[offset:offset+limit]
                        serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset.count()})

                queryset =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_competencia_descriptor.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_competencia_descriptor.objects.filter().count()
                serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descriptor_nombre':
                        filter_kwargs['descriptor__nombre_posicion__icontains'] = filter
                    if tipo_busqueda =='descriptor_id':
                        filter_kwargs['descriptor__id'] = filter
                    if tipo_busqueda =='competencia_nombre':
                        filter_kwargs['competencia__nombre__icontains'] = filter
                    if tipo_busqueda =='tipo_competencia_descripcion':
                        filter_kwargs['competencia__tipo_competencia__descripcion__icontains'] = filter
                    if tipo_busqueda =='tipo_competencia_id':
                        filter_kwargs['competencia__tipo_competencia'] = filter
                    if tipo_busqueda =='area_descripcion':
                        filter_kwargs['area__descripcion__icontains'] = filter
                    if tipo_busqueda =='division_descripcion':
                        filter_kwargs['division__descripcion__icontains'] = filter
                    if tipo_busqueda =='clasificacion_nombre':
                        filter_kwargs['clasificacion__nombre__icontains'] = filter
            
                if segundo_tipo_busqueda!='' and segundo_filter!='':
                    filter_kwargs_2={}
                    
                    if segundo_tipo_busqueda:
                        if segundo_tipo_busqueda =='descriptor_nombre':
                            filter_kwargs_2['descriptor__nombre_posicion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='descriptor_id':
                            filter_kwargs_2['descriptor__id'] = segundo_filter
                        if segundo_tipo_busqueda =='competencia_nombre':
                            filter_kwargs_2['competencia__nombre__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='tipo_competencia_descripcion':
                            filter_kwargs_2['competencia__tipo_competencia__descripcion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='tipo_competencia_id':
                            filter_kwargs_2['competencia__tipo_competencia'] = segundo_filter
                        if segundo_tipo_busqueda =='area_descripcion':
                            filter_kwargs_2['area__descripcion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='division_descripcion':
                            filter_kwargs_2['division__descripcion__icontains'] = segundo_filter
                        if segundo_tipo_busqueda =='clasificacion_nombre':
                            filter_kwargs_2['clasificacion__nombre__icontains'] = segundo_filter
                        

                        queryset =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs,**filter_kwargs_2).order_by('id')
                        queryset2 =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs,**filter_kwargs_2,nivel_desarrollo__gt=0).order_by('id')
                        serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset.count(),"conteo_nivel_desarrollo":queryset2.count()})

                queryset =  descriptor_perfil_competencia_descriptor.objects.filter(**filter_kwargs).order_by('id')
                serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  descriptor_perfil_competencia_descriptor.objects.filter().order_by('id')
                serializer = descriptor_perfil_competencia_descriptorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        
        descriptor=''
        competencia=''
        nivel_desarrollo=''

        if 'descriptor' in request.data:
            descriptor=self.request.data['descriptor']
        
        if 'competencia' in request.data:
            competencia=self.request.data['competencia']
            print()

        if 'area' in request.data:
            area=self.request.data['area']

        descriptor_perfil_query=''
        competencia_query=''
        nombre_competencia=''
        descripcion_competencia=''
        archivo=''
        tipo_competencia=''
        division=''
        clasificacion=''
        #descriptor
        descriptor_perfil_query= descriptor_perfil_datos_generales.objects.get(id=descriptor) if descriptor_perfil_datos_generales.objects.filter(id=descriptor) else None
        
        if descriptor_perfil_query!=None:
            if descriptor_perfil_query.clasificacion_empleado:
                clasificacion=descriptor_perfil_query.clasificacion_empleado.pk

            if descriptor_perfil_query.division:
                division= descriptor_perfil_query.division.pk
                # print('division',division)

        
        #competencia
        competencia_query=descriptor_perfil_competencia.objects.get(id=competencia) if descriptor_perfil_competencia.objects.filter(id=competencia) else None
        
        
        if competencia_query!=None:
            if competencia_query.nombre:
                nombre_competencia= competencia_query.nombre
            
            if competencia_query.descripcion:
                descripcion_competencia= competencia_query.descripcion

            if competencia_query.archivo:
                archivo= competencia_query.archivo.pk
            
            if competencia_query.tipo_competencia:
                tipo_competencia= competencia_query.tipo_competencia.pk
                # print('tipo_competencia',tipo_competencia)

            
            
        data ={
            
            "nombre": nombre_competencia,
            "descripcion": descripcion_competencia,
            "competencia": competencia,
            "archivo": archivo,
            "tipo_competencia": tipo_competencia,
               
            "descriptor": descriptor,
            "clasificacion": clasificacion,
            "division": division,

            "area": area
        }
    
        serializer = descriptor_perfil_competencia_descriptorserializer(data=data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,requets,id):
        existe= descriptor_perfil_competencia_descriptor.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= descriptor_perfil_competencia_descriptorserializer(put,data=requets.data)
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
