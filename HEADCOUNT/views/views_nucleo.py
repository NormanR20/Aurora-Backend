from django.db.models.functions import ExtractYear

from re import sub
from django.contrib.auth.models import User,Group
from django.http.response import Http404
from django.shortcuts import render
from calendar import monthrange

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
from django.db.models import Q,F,Count,Sum,FloatField,ExpressionWrapper, query
from django.utils.crypto import get_random_string
import string
from django.contrib.auth import authenticate
from pyrfc import *
from datetime import datetime,timedelta
import json
from ..models import *
from ..serializers import *

import sys
sys.setrecursionlimit(100000000)                                                        
from rest_framework import viewsets

class nucleo_modulosViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = nucleo_modulos.objects.all()
    serializer_class = nucleo_modulosserializer
    def list(self,request):
        queryset = nucleo_modulos.objects.all()
        serializer = nucleo_modulosserializer(queryset, many=True)
        queryset = nucleo_modulos.objects.filter(activo=True).order_by('nombre')
        serializer = nucleo_modulosserializer(queryset, many=True)
        return Response({"data":serializer.data})

class nucleo_tipo_mensajeViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = nucleo_tipo_mensaje.objects.all()
    serializer_class = nucleo_tipo_mensajeserializer
    def list(self,request):
        queryset = nucleo_tipo_mensaje.objects.all()
        serializer = nucleo_tipo_mensajeserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if filter != '':
            queryset = nucleo_tipo_mensaje.objects.filter(modulo__activo=True,modulo__nombre__icontains=filter).order_by('nombre')
            serializer = nucleo_tipo_mensajeserializer(queryset, many=True)
            return Response({"data":serializer.data})
        else:
            queryset = nucleo_tipo_mensaje.objects.filter(modulo__activo=True).order_by('nombre')
            serializer = nucleo_tipo_mensajeserializer(queryset, many=True)
            return Response({"data":serializer.data})

class nucleo_configuracion_correosViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = nucleo_configuracion_correos.objects.all()
    serializer_class = nucleo_configuracion_correosserializer
    def list(self,request):
        tipo_mensaje = ''
        filter = ''
        if self.request.query_params.get('tipo_mensaje'):
            tipo_mensaje = self.request.query_params.get('tipo_mensaje')
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if filter!='' or tipo_mensaje!='':
            filter_kwargs={}
            if tipo_mensaje:
                filter_kwargs['tipo_mensaje__nombre__icontains']=tipo_mensaje
            if filter:
                filter_kwargs['descripcion'] = filter

            queryset =  nucleo_configuracion_correos.objects.filter(**filter_kwargs).order_by('descripcion')
            conteo =  nucleo_configuracion_correos.objects.filter(**filter_kwargs).count()
            serializer = nucleo_configuracion_correosserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":conteo})  
        else:
            queryset =  nucleo_configuracion_correos.objects.all().order_by('descripcion')
            conteo =  nucleo_configuracion_correos.objects.all().count()
            serializer = nucleo_configuracion_correosserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":conteo})  

class nucleo_variables_envio_correosViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = nucleo_variables_envio_correos.objects.all()
    serializer_class = nucleo_variables_envio_correosserializer
    def list(self,request):
        tipo_mensaje=''
        modulo=''
        if self.request.query_params.get('tipo_mensaje'):
            tipo_mensaje = self.request.query_params.get('tipo_mensaje')
        if self.request.query_params.get('modulo'):
            modulo = self.request.query_params.get('modulo')
        
        if modulo!='' or tipo_mensaje!='':
            filter_kwargs={}
            if tipo_mensaje:
                filter_kwargs['tipo_mensaje__nombre__icontains']=tipo_mensaje
            if modulo:
                filter_kwargs['tipo_mensaje__modulo__nombre__icontains'] = modulo
                filter_kwargs['tipo_mensaje__modulo__activo']= True
            print (filter_kwargs)
            queryset =  nucleo_variables_envio_correos.objects.filter(**filter_kwargs).order_by('id')
            conteo =  nucleo_variables_envio_correos.objects.filter(**filter_kwargs).count()
            serializer = nucleo_variables_envio_correosserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":conteo})  
        else:
            queryset =  nucleo_variables_envio_correos.objects.all().order_by('id')
            conteo =  nucleo_variables_envio_correos.objects.all().count()
            serializer = nucleo_variables_envio_correosserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":conteo})  

class nucleo_pruebasViewSet(viewsets.ModelViewSet):
    queryset = nucleo_pruebas.objects.all()
    serializer_class = nucleo_pruebasserializer

            


        
