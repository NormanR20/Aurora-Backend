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
from django.db.models import Q,F,Count,Sum,FloatField,ExpressionWrapper, query,Case ,When,IntegerField,Max,Min,Avg
from django.utils.crypto import get_random_string
import string
from django.contrib.auth import authenticate
from pyrfc import *
from datetime import date,datetime,timedelta
import json
from ..serializers import *
from ..models import *
from django.apps import apps
from datetime import datetime,timedelta
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
from base64 import b64decode
from django.core.files.base import ContentFile
import base64
from django.db.models import Value
from dateutil.relativedelta import relativedelta
from django.db.models.functions import Cast
from .views_capacitacion import *
from decimal import Decimal, ROUND_HALF_UP
from .views_generar_archivo import *


class capacitacion_tipo_capacitacionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_tipo_capacitacion.objects.all()
    serializer_class = capacitacion_tipo_capacitacionserializer
    def list(self, request):
        queryset = capacitacion_tipo_capacitacion.objects.all()
        serializer_class = capacitacion_tipo_capacitacionserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  capacitacion_tipo_capacitacion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_tipo_capacitacion.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_tipo_capacitacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_tipo_capacitacion.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_tipo_capacitacion.objects.filter().count()
                serializer = capacitacion_tipo_capacitacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_tipo_capacitacion.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_tipo_capacitacion.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_tipo_capacitacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_tipo_capacitacion.objects.filter().order_by('id')
                conteo =  capacitacion_tipo_capacitacion.objects.filter().count()
                serializer = capacitacion_tipo_capacitacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = capacitacion_tipo_capacitacionserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_tipo_capacitacion.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_tipo_capacitacionserializer(put,data=requets.data)
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


class capacitacion_modalidadViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_modalidad.objects.all()
    serializer_class = capacitacion_modalidadserializer
    def list(self, request):
        queryset = capacitacion_modalidad.objects.all()
        serializer_class = capacitacion_modalidadserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  capacitacion_modalidad.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_modalidad.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_modalidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_modalidad.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_modalidad.objects.filter().count()
                serializer = capacitacion_modalidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_modalidad.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_modalidad.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_modalidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_modalidad.objects.filter().order_by('id')
                conteo =  capacitacion_modalidad.objects.filter().count()
                serializer = capacitacion_modalidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = capacitacion_modalidadserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_modalidad.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_modalidadserializer(put,data=requets.data)
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



class capacitacion_enfoqueViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_enfoque.objects.all()
    serializer_class = capacitacion_enfoqueserializer
    def list(self, request):
        queryset = capacitacion_enfoque.objects.all()
        serializer_class = capacitacion_enfoqueserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  capacitacion_enfoque.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_enfoque.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_enfoqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_enfoque.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_enfoque.objects.filter().count()
                serializer = capacitacion_enfoqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_enfoque.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_enfoque.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_enfoqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_enfoque.objects.filter().order_by('id')
                conteo =  capacitacion_enfoque.objects.filter().count()
                serializer = capacitacion_enfoqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        request.data["creado_por"]=request.user.id
        serializer = capacitacion_enfoqueserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            capacitacion_enfoque.objects.filter(id=serializer.data["id"]).update(creado_por=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_enfoque.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            request.data["creado_por"]=request.user.id
            serializer= capacitacion_enfoqueserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                capacitacion_enfoque.objects.filter(id=serializer.data["id"]).update(actualizado_por=request.user)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class capacitacion_motivo_inasistenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_motivo_inasistencia.objects.all()
    serializer_class = capacitacion_motivo_inasistenciaserializer
    def list(self, request):
        queryset = capacitacion_motivo_inasistencia.objects.all()
        serializer_class = capacitacion_motivo_inasistenciaserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  capacitacion_motivo_inasistencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_motivo_inasistencia.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_motivo_inasistenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_motivo_inasistencia.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_motivo_inasistencia.objects.filter().count()
                serializer = capacitacion_motivo_inasistenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_motivo_inasistencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_motivo_inasistencia.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_motivo_inasistenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_motivo_inasistencia.objects.filter().order_by('id')
                conteo =  capacitacion_motivo_inasistencia.objects.filter().count()
                serializer = capacitacion_motivo_inasistenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        request.data["creado_por"]=request.user.id
        
        serializer = capacitacion_motivo_inasistenciaserializer(data=request.data)
        
        if serializer.is_valid(): 
            serializer.save()
            
            #capacitacion_motivo_inasistencia.objects.filter(id=serializer.data["id"]).update(creado_por=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_motivo_inasistencia.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            request.data["actualizado_por"]=request.user.id

            serializer= capacitacion_motivo_inasistenciaserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                #capacitacion_motivo_inasistencia.objects.filter(id=serializer.data["id"]).update(actualizado_por=request.user)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def delete(self,request,id):
        eliminar = self.get_object(id)
        eliminar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class capacitacion_origenViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_origen.objects.all()
    serializer_class = capacitacion_origenserializer
    def list(self, request):
        queryset = capacitacion_origen.objects.all()
        serializer_class = capacitacion_origenserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  capacitacion_origen.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_origen.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_origenserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_origen.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_origen.objects.filter().count()
                serializer = capacitacion_origenserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_origen.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_origen.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_origenserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_origen.objects.filter().order_by('id')
                conteo =  capacitacion_origen.objects.filter().count()
                serializer = capacitacion_origenserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = capacitacion_origenserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_origen.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_origenserializer(put,data=requets.data)
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


class capacitacion_estadoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_estado.objects.all()
    serializer_class = capacitacion_estadoserializer
    def list(self, request):
        queryset = capacitacion_estado.objects.all()
        serializer_class = capacitacion_estadoserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='color':
                        filter_kwargs['color__icontains'] = filter
                    if tipo_busqueda =='tipo_estado':
                        filter_kwargs['tipo_estado'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  capacitacion_estado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_estado.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_estadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_estado.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_estado.objects.filter().count()
                serializer = capacitacion_estadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='color':
                        filter_kwargs['color__icontains'] = filter
                    if tipo_busqueda =='tipo_estado':
                        filter_kwargs['tipo_estado'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_estado.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_estado.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_estadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_estado.objects.filter().order_by('id')
                conteo =  capacitacion_estado.objects.filter().count()
                serializer = capacitacion_estadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = capacitacion_estadoserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_estado.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_estadoserializer(put,data=requets.data)
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


class capacitacion_cursoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_curso.objects.all()
    serializer_class = capacitacion_cursoserializer
    def list(self, request):
        queryset = capacitacion_curso.objects.all()
        serializer_class = capacitacion_cursoserializer(queryset, many=True)
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
                    if tipo_busqueda =='descripcion_capacitacion':
                        filter_kwargs['descripcion_capacitacion__icontains'] = filter
                    if tipo_busqueda =='codigo_capacitacion':
                        filter_kwargs['codigo_capacitacion__icontains'] = filter
                    if tipo_busqueda =='nombre_capacitacion':
                        filter_kwargs['nombre_capacitacion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  capacitacion_curso.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_curso.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_cursoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_curso.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_curso.objects.filter().count()
                serializer = capacitacion_cursoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion_capacitacion':
                        filter_kwargs['descripcion_capacitacion__icontains'] = filter
                    if tipo_busqueda =='codigo_capacitacion':
                        filter_kwargs['codigo_capacitacion__icontains'] = filter
                    if tipo_busqueda =='nombre_capacitacion':
                        filter_kwargs['nombre_capacitacion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_curso.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_curso.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_cursoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_curso.objects.filter().order_by('id')
                conteo =  capacitacion_curso.objects.filter().count()
                serializer = capacitacion_cursoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        request.data["creado_por"]=request.user.id
        
        serializer = capacitacion_cursoserializer(data=request.data)
        
        if serializer.is_valid(): 
            serializer.save()
            
            #capacitacion_motivo_inasistencia.objects.filter(id=serializer.data["id"]).update(creado_por=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_curso.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            request.data["actualizado_por"]=request.user.id

            serializer= capacitacion_cursoserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                #capacitacion_motivo_inasistencia.objects.filter(id=serializer.data["id"]).update(actualizado_por=request.user)
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"La información enviada no es valida"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        try:
            instance = self.get_object()
            evento = capacitacion_evento_capacitacion.objects.filter(capacitacion_id=instance.id) if capacitacion_evento_capacitacion.objects.filter(capacitacion_id=instance.id) else None 
            if evento:
                return Response ({"respuesta":"No se puede borrar el curso debido a que existe un evento ligado a el."},status=status.HTTP_400_BAD_REQUEST)
            else:
                self.perform_destroy(instance)
            
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)

class capacitacion_metrica_evaluacion_factorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_metrica_evaluacion_factor.objects.all()
    serializer_class = capacitacion_metrica_evaluacion_factorserializer
    def list(self, request):
        queryset = capacitacion_metrica_evaluacion_factor.objects.all()
        serializer_class = capacitacion_metrica_evaluacion_factorserializer(queryset, many=True)
        filter=''
        filter_2=''
        tipo_busqueda=''
        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')

        filter_kwargs={}
        if filter_2!='':
            filter_kwargs['anio']= filter_2

        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
     
                    if tipo_busqueda =='valor_minimo':
                        filter_kwargs['valor_minimo'] = filter
                        
                    if tipo_busqueda =='valor_maximo':
                        filter_kwargs['valor_maximo'] = filter
                        
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                        
                    if tipo_busqueda =='color':
                        filter_kwargs['color__icontains'] = filter
                        
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                        
                queryset =  capacitacion_metrica_evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_metrica_evaluacion_factor.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_metrica_evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_metrica_evaluacion_factor.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
     
                    if tipo_busqueda =='valor_minimo':
                        filter_kwargs['valor_minimo'] = filter
                        
                    if tipo_busqueda =='valor_maximo':
                        filter_kwargs['valor_maximo'] = filter
                        
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                        
                    if tipo_busqueda =='color':
                        filter_kwargs['color__icontains'] = filter
                        
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_metrica_evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_metrica_evaluacion_factor.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_metrica_evaluacion_factor.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_metrica_evaluacion_factor.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_evaluacion_factorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 

                #sadsasd


    def create(self, request):
        serializer = capacitacion_metrica_evaluacion_factorserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_metrica_evaluacion_factor.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_metrica_evaluacion_factorserializer(put,data=requets.data)
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


class capacitacion_metrica_experiencia_puestoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_metrica_experiencia_puesto.objects.all()
    serializer_class = capacitacion_metrica_experiencia_puestoserializer
    def list(self, request):
        queryset = capacitacion_metrica_experiencia_puesto.objects.all()
        serializer_class = capacitacion_metrica_experiencia_puestoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        filter_2=''

        if self.request.query_params.get('filter_2'):
            filter_2 = self.request.query_params.get('filter_2')

        filter_kwargs={}
        if filter_2!='':
            filter_kwargs['anio']= filter_2

        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                    if tipo_busqueda =='de':
                        filter_kwargs['de'] = filter
                        
                    if tipo_busqueda =='hasta':
                        filter_kwargs['hasta'] = filter
                        
                    if tipo_busqueda =='porcentaje':
                        filter_kwargs['porcentaje__icontains'] = filter
                        
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                        
                queryset =  capacitacion_metrica_experiencia_puesto.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_metrica_experiencia_puesto.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_experiencia_puestoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_metrica_experiencia_puesto.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_metrica_experiencia_puesto.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_experiencia_puestoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
        else:
            if filter!='' and tipo_busqueda!='':
                
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                        
                    if tipo_busqueda =='de':
                        filter_kwargs['de'] = filter
                        
                    if tipo_busqueda =='hasta':
                        filter_kwargs['hasta'] = filter
                        
                    if tipo_busqueda =='porcentaje':
                        filter_kwargs['porcentaje__icontains'] = filter
                        
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter

                        
                queryset =  capacitacion_metrica_experiencia_puesto.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_metrica_experiencia_puesto.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_experiencia_puestoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_metrica_experiencia_puesto.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_metrica_experiencia_puesto.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_experiencia_puestoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = capacitacion_metrica_experiencia_puestoserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_metrica_experiencia_puesto.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)

            serializer= capacitacion_metrica_experiencia_puestoserializer(put,data=requets.data)
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

#capacitacion_matriz_9_cajaserializer

class capacitacion_matriz_9_cajaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_matriz_9_cajas.objects.all()
    serializer_class = capacitacion_matriz_9_cajaserializer
    def list(self, request):
        queryset = capacitacion_matriz_9_cajas.objects.all()
        serializer_class = capacitacion_matriz_9_cajaserializer(queryset, many=True)
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
                    if tipo_busqueda =='encabezado_cuadrante':
                        filter_kwargs['encabezado_cuadrante__icontains'] = filter
                        
 
                        
                queryset =  capacitacion_matriz_9_cajas.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_matriz_9_cajas.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_matriz_9_cajaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_matriz_9_cajas.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_matriz_9_cajas.objects.filter().count()
                serializer = capacitacion_matriz_9_cajaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='encabezado_cuadrante':
                        filter_kwargs['encabezado_cuadrante__icontains'] = filter

                        
                queryset =  capacitacion_matriz_9_cajas.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_matriz_9_cajas.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_matriz_9_cajaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_matriz_9_cajas.objects.filter().order_by('id')
                conteo =  capacitacion_matriz_9_cajas.objects.filter().count()
                serializer = capacitacion_matriz_9_cajaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        serializer = capacitacion_matriz_9_cajaserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_matriz_9_cajas.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_matriz_9_cajaserializer(put,data=requets.data)
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



class capacitacion_metrica_9_cajasViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_metrica_9_cajas.objects.all()
    serializer_class = capacitacion_metrica_9_cajasserializer
    def list(self, request):
        queryset = capacitacion_metrica_9_cajas.objects.all()
        serializer_class = capacitacion_metrica_9_cajasserializer(queryset, many=True)
        filter=''
        filter_2=''
        tipo_busqueda=''

        if self.request.query_params.get('filter_2'):
            filter_2 = self.request.query_params.get('filter_2')

        filter_kwargs={}
        if filter_2!='':
            filter_kwargs['anio']= filter_2
            
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                if tipo_busqueda:
                    if tipo_busqueda =='valor_minimo':
                        filter_kwargs['valor_minimo'] = filter
                    if tipo_busqueda =='valor_maximo':
                        filter_kwargs['valor_maximo'] = filter
                    if tipo_busqueda =='tipo_criterio':
                        filter_kwargs['tipo_criterio'] = filter
                        
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date'] = filter
                    if tipo_busqueda =='anio':
                        filter_kwargs['anio'] = filter
                        
                queryset =  capacitacion_metrica_9_cajas.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_metrica_9_cajas.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_9_cajasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_metrica_9_cajas.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_metrica_9_cajas.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_9_cajasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                if tipo_busqueda:
                    if tipo_busqueda =='valor_minimo':
                        filter_kwargs['valor_minimo'] = filter
                    if tipo_busqueda =='valor_maximo':
                        filter_kwargs['valor_maximo'] = filter
                    if tipo_busqueda =='tipo_criterio':
                        filter_kwargs['tipo_criterio'] = filter
                        
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date'] = filter
                    if tipo_busqueda =='anio':
                        filter_kwargs['anio'] = filter

                        
                queryset =  capacitacion_metrica_9_cajas.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_metrica_9_cajas.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_9_cajasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_metrica_9_cajas.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_metrica_9_cajas.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_9_cajasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        
        serializer = capacitacion_metrica_9_cajasserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_metrica_9_cajas.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_metrica_9_cajasserializer(put,data=requets.data)
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




class capacitacion_campaniaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_campania.objects.all()
    serializer_class = capacitacion_campaniaserializer
    def list(self, request):
        queryset = capacitacion_campania.objects.all()
        serializer_class = capacitacion_campaniaserializer(queryset, many=True)
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
                    if tipo_busqueda =='estado':
                        filter_kwargs['estado_id'] = filter
                    if tipo_busqueda =='estado_descripcion':
                        filter_kwargs['estado__descripcion__icontains'] = filter
                    if tipo_busqueda =='codigo_campania':
                        filter_kwargs['codigo_campania'] = filter
                    if tipo_busqueda =='nombre_campania':
                        filter_kwargs['nombre_campania__icontains'] = filter
                    if tipo_busqueda =='duracion_horas':
                        filter_kwargs['duracion_horas'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                    if tipo_busqueda =='fecha_fin':
                        filter_kwargs['fecha_fin__icontains'] = filter
                    if tipo_busqueda =='fecha_inicio':
                        filter_kwargs['fecha_inicio__icontains'] = filter

                queryset =  capacitacion_campania.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_campania.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_campaniaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_campania.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_campania.objects.filter().count()
                serializer = capacitacion_campaniaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='estado':
                        filter_kwargs['estado_id'] = filter
                    if tipo_busqueda =='estado_descripcion':
                        filter_kwargs['estado__descripcion__icontains'] = filter
                    if tipo_busqueda =='codigo_campania':
                        filter_kwargs['codigo_campania'] = filter
                    if tipo_busqueda =='nombre_campania':
                        filter_kwargs['nombre_campania__icontains'] = filter
                    if tipo_busqueda =='duracion_horas':
                        filter_kwargs['duracion_horas'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    if tipo_busqueda =='fecha_actualizacion':
                        filter_kwargs['fecha_actualizacion__icontains'] = filter
                    if tipo_busqueda =='fecha_fin':
                        filter_kwargs['fecha_fin__icontains'] = filter
                    if tipo_busqueda =='fecha_inicio':
                        filter_kwargs['fecha_inicio__icontains'] = filter

                        
                queryset =  capacitacion_campania.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_campania.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_campaniaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_campania.objects.filter().order_by('id')
                conteo =  capacitacion_campania.objects.filter().count()
                serializer = capacitacion_campaniaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        parametros = self.request.data.copy()
        estado_id=(capacitacion_estado.objects.filter(descripcion="Abierto").values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion="Abierto").values('id') else None
        parametros['estado']=estado_id
        serializer = capacitacion_campaniaserializer(data=parametros)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_campania.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_campaniaserializer(put,data=requets.data)
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


class ordenamiento_9cajasViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = capacitacion_matriz_9_cajas.objects.none() 
    def post(self,request):
        cajas = self.request.data['cajas']
        ids=[]
        for x in cajas:
            ids.append(x['id'])
            capacitacion_matriz_9_cajas.objects.filter(id=x['id']).update(x=x['x'],y=x['y'],orden=x['orden'])
        resultado=ids
        resultado=capacitacion_matriz_9_cajas.objects.filter(id__in=ids)
        #######print(ids)
        #######print(resultado)
        serializer_resultado=capacitacion_matriz_9_cajaserializer(resultado,many = True )
        #######print(serializer_resultado)
        return Response({"resultado": serializer_resultado.data},status= status.HTTP_200_OK)
        #return Response({"resultado":"No se puede verificar el contenido el detalle de la carpeta"},status= status.HTTP_404_NOT_FOUND)


    
        
class capacitacion_metrica_educacion_formalViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_metrica_educacion_formal.objects.all()
    serializer_class = capacitacion_metrica_educacion_formalserializer
    def list(self, request):
        queryset = capacitacion_metrica_educacion_formal.objects.all()
        serializer_class = capacitacion_metrica_educacion_formalserializer(queryset, many=True)
        filter=''
        filter_2=''
        tipo_busqueda=''

        if self.request.query_params.get('filter_2'):
            filter_2 = self.request.query_params.get('filter_2')

        filter_kwargs={}
        if filter_2!='':
            filter_kwargs['anio']= filter_2
            
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                
                if tipo_busqueda:
                    if tipo_busqueda =='nombre_metrica':
                        filter_kwargs['nombre_metrica__icontains'] = filter
                        
                    if tipo_busqueda =='porcentaje':
                        filter_kwargs['porcentaje'] = filter
                        
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion'] = filter
                       
                    if tipo_busqueda =='anio':
                        filter_kwargs['anio'] = filter
                        
                    
                        
                queryset =  capacitacion_metrica_educacion_formal.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_metrica_educacion_formal.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_educacion_formalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_metrica_educacion_formal.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_metrica_educacion_formal.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_educacion_formalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                if tipo_busqueda:
                    if tipo_busqueda =='nombre_metrica':
                        filter_kwargs['nombre_metrica'] = filter
                        
                    if tipo_busqueda =='porcentaje':
                        filter_kwargs['porcentaje'] = filter
                        
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion'] = filter
                       
                    if tipo_busqueda =='anio':
                        filter_kwargs['anio'] = filter

                        
                queryset =  capacitacion_metrica_educacion_formal.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_metrica_educacion_formal.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_educacion_formalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_metrica_educacion_formal.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_metrica_educacion_formal.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_metrica_educacion_formalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 

    def create(self, request):

        serializer = capacitacion_metrica_educacion_formalserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= capacitacion_metrica_educacion_formal.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= capacitacion_metrica_educacion_formalserializer(put,data=requets.data)
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



class capacitacion_monitor_colaboradorViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = capacitacion_monitor_colaboradoresserializer
    def list(self, request):
        queryset = Funcional_empleado.objects.all()
        serializer_class = capacitacion_monitor_colaboradoresserializer(queryset, many=True)
        filtrado = Funcional_empleado.objects.filter()
        empresa=0
        departamento=0
        unidad_organizativa=0
        empleado=0
        usuario = request.user
        usuario_codigo = request.user.username
        empleados_a_cargo= capacitacion_funcional_get_colaborador([usuario_codigo])
        
        hoy=datetime.now().date()
        año= hoy.year
        filter_anio=''
        if self.request.query_params.get('filter_anio'):
                # return Response({"mensaje":"El correo no ha sido enviado "}, status=status.HTTP_400_BAD_REQUEST)
                try:
                  filter_anio = int(self.request.query_params.get('filter_anio'))
                except ValueError:
                    return Response({"mensaje":"Dato ingresado incorrecto "}, status=status.HTTP_400_BAD_REQUEST)
                
        if filter_anio!='':
            filtrado= filtrado.filter(empleado_capacitacion_asistencia__evento_capacitacion__campania__fecha_inicio__year=filter_anio)
        
        if self.request.query_params.get('empresa'):
            empresa = json.loads(self.request.query_params.get('empresa'))
            # filter_kwargs['Q(unidad_organizativa__sociedad_financiera__nombre__icontains__in='+empresa+')|Q(unidad_organizativa__sociedad_financiera__codigo__in'+empresa+')'] 
            cod_empleados_empresa=[]
            for x in empresa:
                empleados_empresa= Funcional_empleado.objects.filter(Q(unidad_organizativa__sociedad_financiera__nombre__icontains=x)|Q(unidad_organizativa__sociedad_financiera__codigo=x)).values_list('codigo',flat=True) if Funcional_empleado.objects.filter(Q(unidad_organizativa__sociedad_financiera__nombre__icontains=x)|Q(unidad_organizativa__sociedad_financiera__codigo=x)).values_list('codigo',flat=True) else None
                if empleados_empresa!=None:
                    cod_empleados_empresa.extend(empleados_empresa)
            
            if len(cod_empleados_empresa)!=0:
                ########print('filtro')
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
                ########print('filtro')
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

        if 'empleado' in grupos and not 'Responsable_Capacitacion' in grupos and not 'jefe' in grupos  and not 'administrador' in grupos:
            filtrado = filtrado.filter(codigo=usuario_codigo)

        elif 'jefe' in grupos:
            filtrado = filtrado.filter(Q(codigo__in=empleados_a_cargo)| Q(codigo=usuario_codigo))
                

        
        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            listado_final_empleados= filtrado.values_list('id','codigo','empleado_capacitacion_asistencia__evento_capacitacion__campania__id','empleado_capacitacion_asistencia__evento_capacitacion__campania__nombre_campania','empleado_capacitacion_asistencia__evento_capacitacion__campania__estado__id','empleado_capacitacion_asistencia__evento_capacitacion__campania__fecha_inicio__year').exclude(empleado_capacitacion_asistencia__evento_capacitacion__campania__id=None).distinct().order_by('id')[offset:offset+limit]
            count=filtrado.values_list('codigo','empleado_capacitacion_asistencia__evento_capacitacion__campania__id','empleado_capacitacion_asistencia__evento_capacitacion__campania__nombre_campania','empleado_capacitacion_asistencia__evento_capacitacion__campania__estado__descripcion','empleado_capacitacion_asistencia__evento_capacitacion__campania__fecha_inicio__year',).exclude(empleado_capacitacion_asistencia__evento_capacitacion__campania__id=None).distinct().order_by('id').count()
            #######print('listado_final_empleados',listado_final_empleados)
            data_monitor=[]

            for id_empleado,empleado,campania_id,campania_nombre,estado,anio in listado_final_empleados:
                data={}
                nombre=(Funcional_empleado.objects.filter(codigo=empleado).values('nombre'))[0]['nombre'] if (Funcional_empleado.objects.filter(codigo=empleado).values('nombre'))[0]['nombre'] else None
                codigo=(Funcional_empleado.objects.filter(codigo=empleado).values('codigo'))[0]['codigo'] if (Funcional_empleado.objects.filter(codigo=empleado).values('codigo'))[0]['codigo'] else None
                ruta=campania_nombre
                estado_campania=estado
                contador=0
                capacitaciones=Funcional_empleado.objects.filter(codigo=empleado,empleado_capacitacion_asistencia__evento_capacitacion__campania__id=campania_id).values_list('empleado_capacitacion_asistencia','empleado_capacitacion_asistencia__recibidas')
                cantidad=capacitaciones.count()
                for capacitacion_id,horas_recibidas in capacitaciones:
                    duracion_horas=(Funcional_empleado.objects.filter(id=capacitacion_id).values_list('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas',flat=True))[0]['empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas'] if Funcional_empleado.objects.filter(id=capacitacion_id).values('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas') else None
                    if horas_recibidas==duracion_horas:
                        contador+=1
                capacitaciones_completadas= str(contador) + '/' + str(cantidad)
                capacitaciones_completadas_porcentaje=(int(contador)*100)/int(cantidad)
                data['id_empleado']=id_empleado
                data['nombre']= nombre
                data['codigo'] = codigo
                data['ruta'] = ruta
                # data['evento_id']=evento_id
                data['capacitaciones_completadas']=capacitaciones_completadas
                data['capacitaciones_completadas_porcentaje']=capacitaciones_completadas_porcentaje
                estado_query = capacitacion_estado.objects.filter(id=estado_campania) if capacitacion_estado.objects.filter(id=estado_campania)  else None
                estado_serializer = capacitacion_estadoserializer(estado_query, many=True)
                # Listado de eventos por campania#############################################################
                listado_eventos_x_campania=capacitacion_evento_capacitacion.objects.filter(campania__id=campania_id).values_list('id',flat=True)
                data['Eventos']=  listado_eventos_x_campania
                data['campania_id']=  campania_id
                #############################################
                if estado == None:
                    data['estado']= None
                else:
                    data['estado']= estado_serializer.data
                data['anio']=anio
                data_monitor.append(data)

            return Response({"data":data_monitor,"count":count})
            
        else:
            listado_final_empleados= filtrado.values_list('id','codigo','empleado_capacitacion_asistencia__evento_capacitacion__campania__id','empleado_capacitacion_asistencia__evento_capacitacion__campania__nombre_campania','empleado_capacitacion_asistencia__evento_capacitacion__campania__estado__id','empleado_capacitacion_asistencia__evento_capacitacion__campania__fecha_inicio__year','empleado_capacitacion_asistencia__evento_capacitacion__id').exclude(empleado_capacitacion_asistencia__evento_capacitacion__campania__id=None).distinct().order_by('id')
            count=filtrado.values_list('codigo','empleado_capacitacion_asistencia__evento_capacitacion__campania__id','empleado_capacitacion_asistencia__evento_capacitacion__campania__nombre_campania','empleado_capacitacion_asistencia__evento_capacitacion__campania__estado__descripcion','empleado_capacitacion_asistencia__evento_capacitacion__campania__fecha_inicio__year','empleado_capacitacion_asistencia__evento_capacitacion__id').exclude(empleado_capacitacion_asistencia__evento_capacitacion__campania__id=None).distinct().order_by('id').count()
            #######print('listado_final_empleados',listado_final_empleados)
            data_monitor=[]

            for id_empleado,empleado,campania_id,campania_nombre,estado,anio,evento_id in listado_final_empleados:
                data={}
                nombre=(Funcional_empleado.objects.filter(codigo=empleado).values('nombre'))[0]['nombre'] if (Funcional_empleado.objects.filter(codigo=empleado).values('nombre'))[0]['nombre'] else None
                codigo=(Funcional_empleado.objects.filter(codigo=empleado).values('codigo'))[0]['codigo'] if (Funcional_empleado.objects.filter(codigo=empleado).values('codigo'))[0]['codigo'] else None
                ruta=campania_nombre
                estado_campania=estado
                contador=0
                capacitaciones=Funcional_empleado.objects.filter(codigo=empleado,empleado_capacitacion_asistencia__evento_capacitacion__campania__id=campania_id,empleado_capacitacion_asistencia__evento_capacitacion__id=evento_id).values_list('empleado_capacitacion_asistencia','empleado_capacitacion_asistencia__recibidas')
                cantidad=capacitaciones.count()
                for capacitacion_id,horas_recibidas in capacitaciones:
                    duracion_horas=(Funcional_empleado.objects.filter(id=capacitacion_id).values_list('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas',flat=True))[0]['empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas'] if Funcional_empleado.objects.filter(id=capacitacion_id).values('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas') else None
                    if horas_recibidas==duracion_horas:
                        contador+=1
                capacitaciones_completadas= str(contador) + '/' + str(cantidad)
                capacitaciones_completadas_porcentaje=(int(contador)*100)/100
                data['id_empleado']=id_empleado
                data['nombre']= nombre
                data['codigo'] = codigo
                data['ruta'] = ruta
                data['capacitaciones_completadas']=capacitaciones_completadas
                data['capacitaciones_completadas_porcentaje']=capacitaciones_completadas_porcentaje
                estado_query = capacitacion_estado.objects.filter(id=estado_campania) if capacitacion_estado.objects.filter(id=estado_campania)  else None
                estado_serializer = capacitacion_estadoserializer(estado_query, many=True)
                if estado == None:
                    data['estado']= None
                else:
                    data['estado']= estado_serializer.data
                data['anio']=anio
                data_monitor.append(data)

            return Response({"data":data_monitor,"count":len(data_monitor)})
 

def capacitacion_funcional_get_colaborador(empleado_codigo):
    hoy=datetime.now().date()
    if not empleado_codigo:
        return []
    empleado = list(Funcional_empleado.objects.filter(jefe_inmediato__in=empleado_codigo).filter(Q(fecha_baja__gt=hoy)|Q(fecha_baja=None)).exclude(codigo__in=empleado_codigo).values_list("codigo",flat=True))
    result=[]
    # result = funcional_get_colaborador(empleado)
    result.extend(empleado)    

    return result




class capacitacion_evento_capacitacionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_evento_capacitacion.objects.all()
    serializer_class = capacitacion_evento_capacitacionserializer
    def list(self, request):
        queryset = capacitacion_evento_capacitacion.objects.all()
        serializer_class = capacitacion_evento_capacitacionserializer(queryset, many=True)
        filter=''
        filter_2=''
        tipo_busqueda=''
        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')
        
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        filter_kwargs={}
        if filter_2!='':
            filter_kwargs['campania_id'] = filter_2

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            if filter!='' and tipo_busqueda!='':
                
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='campania_id':
                        filter_kwargs['campania_id'] = filter
                    if tipo_busqueda =='responsable_id':
                        filter_kwargs['responsable_id'] = filter
                    if tipo_busqueda =='tipo_capacitacion_id':
                        filter_kwargs['tipo_capacitacion_id'] = filter
                    if tipo_busqueda =='enfoque_id':
                        filter_kwargs['enfoque_id'] = filter
                    if tipo_busqueda =='nivel_formacion_id':
                        filter_kwargs['nivel_formacion_id'] = filter
                    if tipo_busqueda =='formacion_id':
                        filter_kwargs['formacion_id'] = filter
                    if tipo_busqueda =='titulo_id':
                        filter_kwargs['titulo_id'] = filter
                    if tipo_busqueda =='especialidad_id':
                        filter_kwargs['especialidad_id'] = filter
                    if tipo_busqueda =='modalidad_id':
                        filter_kwargs['modalidad_id'] = filter
                    if tipo_busqueda =='fecha_inicio':
                        filter_kwargs['fecha_inicio__icontains'] = filter
                    if tipo_busqueda =='fecha_fin':
                        filter_kwargs['fecha_fin__icontains'] = filter
                    if tipo_busqueda =='duracion_horas':
                        filter_kwargs['duracion_horas'] = filter 
                    if tipo_busqueda =='impartido_por':
                        filter_kwargs['impartido_por__icontains'] = filter
                    if tipo_busqueda =='facilitador':
                        filter_kwargs['facilitador__icontains'] = filter
                    if tipo_busqueda =='horas_cumplidas':
                        filter_kwargs['horas_cumplidas'] = filter
                    if tipo_busqueda =='meta_horas':
                        filter_kwargs['meta_horas'] = filter
                    if tipo_busqueda =='costo_capacitacion':
                        filter_kwargs['costo_capacitacion__icontains'] = filter
                    if tipo_busqueda =='costo_empleado':
                        filter_kwargs['costo_empleado__icontains'] = filter 
                    if tipo_busqueda =='numero_empleados_recibir':
                        filter_kwargs['numero_empleados_recibir__icontains'] = filter
                    if tipo_busqueda =='dias_evaluacion':
                        filter_kwargs['dias_evaluacion__icontains'] = filter 
                    if tipo_busqueda =='nota_evaluacion':
                        filter_kwargs['nota_evaluacion'] = filter
                    if tipo_busqueda =='porcentaje_asistencia':
                        filter_kwargs['porcentaje_asistencia'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    

                queryset =  capacitacion_evento_capacitacion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_evento_capacitacion.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_evento_capacitacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_evento_capacitacion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_evento_capacitacion.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_evento_capacitacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='campania_id':
                        filter_kwargs['campania_id'] = filter
                    if tipo_busqueda =='responsable_id':
                        filter_kwargs['responsable_id'] = filter
                    if tipo_busqueda =='tipo_capacitacion_id':
                        filter_kwargs['tipo_capacitacion_id'] = filter
                    if tipo_busqueda =='enfoque_id':
                        filter_kwargs['enfoque_id'] = filter
                    if tipo_busqueda =='nivel_formacion_id':
                        filter_kwargs['nivel_formacion_id'] = filter
                    if tipo_busqueda =='formacion_id':
                        filter_kwargs['formacion_id'] = filter
                    if tipo_busqueda =='titulo_id':
                        filter_kwargs['titulo_id'] = filter
                    if tipo_busqueda =='especialidad_id':
                        filter_kwargs['especialidad_id'] = filter
                    if tipo_busqueda =='modalidad_id':
                        filter_kwargs['modalidad_id'] = filter
                    if tipo_busqueda =='fecha_inicio':
                        filter_kwargs['fecha_inicio__icontains'] = filter
                    if tipo_busqueda =='fecha_fin':
                        filter_kwargs['fecha_fin__icontains'] = filter
                    if tipo_busqueda =='duracion_horas':
                        filter_kwargs['duracion_horas'] = filter 
                    if tipo_busqueda =='impartido_por':
                        filter_kwargs['impartido_por__icontains'] = filter
                    if tipo_busqueda =='facilitador':
                        filter_kwargs['facilitador__icontains'] = filter
                    if tipo_busqueda =='horas_cumplidas':
                        filter_kwargs['horas_cumplidas'] = filter
                    if tipo_busqueda =='meta_horas':
                        filter_kwargs['meta_horas'] = filter
                    if tipo_busqueda =='costo_capacitacion':
                        filter_kwargs['costo_capacitacion__icontains'] = filter
                    if tipo_busqueda =='costo_empleado':
                        filter_kwargs['costo_empleado__icontains'] = filter 
                    if tipo_busqueda =='numero_empleados_recibir':
                        filter_kwargs['numero_empleados_recibir__icontains'] = filter
                    if tipo_busqueda =='dias_evaluacion':
                        filter_kwargs['dias_evaluacion__icontains'] = filter 
                    if tipo_busqueda =='nota_evaluacion':
                        filter_kwargs['nota_evaluacion'] = filter
                    if tipo_busqueda =='porcentaje_asistencia':
                        filter_kwargs['porcentaje_asistencia'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                    

                        
                queryset =  capacitacion_evento_capacitacion.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_evento_capacitacion.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_evento_capacitacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_evento_capacitacion.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_evento_capacitacion.objects.filter(**filter_kwargs).count()
                serializer = capacitacion_evento_capacitacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


    def create(self, request):
        usuario_id = request.user.id
        id_campania_f=''
        hoy=datetime.now().date()
        if "campania" in request.data:
            id_campania_f= request.data['campania']
        
        estado_campania=''
        if id_campania_f!='':
            estado_campania= (capacitacion_campania.objects.filter(id=id_campania_f).values('estado__descripcion'))[0]['estado__descripcion'] if capacitacion_campania.objects.filter(id=id_campania_f).values('estado__descripcion') else None
        
        # if estado_campania=='Cerrado':
        #     return Response({"La campaña se encuentra cerrada"}, status=status.HTTP_400_BAD_REQUEST)

        # usuario_id= Funcional_empleado.objects.get(codigo=usuario_codigo) if Funcional_empleado.objects.filter(codigo=usuario_codigo) else None
        serializer = capacitacion_evento_capacitacionserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()




            evento_id=serializer.data['id']
            if usuario_id!=None:
                capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(creado_por=usuario_id)
            



            capacitacion_campania_id=serializer.data['campania']
            ######################################HORAS_DURACION_CAMPANIA
            ##############################################
            duracion_horas= serializer.data['duracion_horas']
            fecha_f=datetime.strptime(serializer.data['fecha_fin'], '%Y-%m-%d').date()
            fecha_i=datetime.strptime(serializer.data['fecha_inicio'], '%Y-%m-%d').date() 
            n_estado_campania=''
            campania_fecha_f=(capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('fecha_fin'))[0]['fecha_fin'] if capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('fecha_fin') else None
            campania_fecha_i=(capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('fecha_inicio'))[0]['fecha_inicio'] if capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('fecha_inicio') else None
            campania_duracion_horas=(capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('duracion_horas'))[0]['duracion_horas'] if capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('duracion_horas') else None
            
            if campania_fecha_f!=None and  campania_fecha_i!=None:

                # if campania_fecha_f < fecha_f:
                #     capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_fin=fecha_f)
                
                # if campania_fecha_i < fecha_i:
                #     capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_inicio=fecha_i)
                #     n_estado_campania=(capacitacion_estado.objects.filter(descripcion='Abierto').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Abierto').values('id') else None
                #     capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=n_estado_campania)

                f_i=(capacitacion_evento_capacitacion.objects.filter().order_by('fecha_inicio').values('fecha_inicio'))[0]['fecha_inicio'] if capacitacion_evento_capacitacion.objects.filter().order_by('fecha_inicio').values('fecha_inicio') else None
                f_f=(capacitacion_evento_capacitacion.objects.filter().order_by('-fecha_fin').values('fecha_fin'))[0]['fecha_fin'] if capacitacion_evento_capacitacion.objects.filter().order_by('-fecha_fin').values('fecha_fin') else None
                capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_fin=f_f)
                capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_inicio=f_i)
                n_estado_campania=(capacitacion_estado.objects.filter(descripcion='Abierto').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Abierto').values('id') else None
                if hoy <= f_i:
                    capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=n_estado_campania)
                ##### eevaluando el estado despues de cambiar las fechas
                if hoy >= f_i:
                    estado_en_proceso_id=(capacitacion_estado.objects.filter(descripcion='En proceso').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='En proceso').values('id') else None
            
                    if estado_en_proceso_id!=None:
                        capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=estado_en_proceso_id)

                if hoy>=f_f:
                    estado_cerrado=(capacitacion_estado.objects.filter(descripcion='Cerrado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Cerrado').values('id') else None
                    if estado_cerrado!=None:
                        capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=estado_cerrado)
            
            else:
                capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_fin=fecha_f)
                capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_inicio=fecha_i)

            # duracion_horas_totales= int(campania_duracion_horas)+ int(duracion_horas)
            # capacitacion_campania_id=serializer.data['campania']
            campania_duracion_horas_totales = (capacitacion_evento_capacitacion.objects.filter(campania__id=capacitacion_campania_id).aggregate(Sum('duracion_horas')))['duracion_horas__sum']
            capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(duracion_horas=campania_duracion_horas_totales)
            ######################################Estado
            estado_abierto=(capacitacion_estado.objects.filter(descripcion='Abierto').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Abierto').values('id') else None
            if estado_abierto!=None:
                capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(estado=estado_abierto)
            
             #############################nuevo serializers
            nuevo_query= capacitacion_evento_capacitacion.objects.get(id=evento_id) if capacitacion_evento_capacitacion.objects.filter(id=evento_id) else None
            if nuevo_query!=None:
                serializer_evento_f= capacitacion_evento_capacitacionserializer(nuevo_query)
                return Response(serializer_evento_f.data,status=status.HTTP_200_OK)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def update(self,request,pk=None):
        id=pk
        hoy=datetime.now().date()
        id_campania_f=''
        if "campania" in request.data:
            id_campania_f= request.data['campania']
        
        estado_campania=''
        if id_campania_f!='':
            estado_campania= (capacitacion_campania.objects.filter(id=id_campania_f).values('estado__descripcion'))[0]['estado__descripcion'] if capacitacion_campania.objects.filter(id=id_campania_f).values('estado__descripcion') else None
        
        if estado_campania=='Cerrado':
            return Response({"La campaña se encuentra cerrada"}, status=status.HTTP_400_BAD_REQUEST)
        usuario_id = request.user.id
        existe= capacitacion_evento_capacitacion.objects.filter(id=id).count()
        horas_duracion_existentes=0
        if existe!=0:
            
            horas_duracion_existentes=(capacitacion_evento_capacitacion.objects.filter(id=id).values('duracion_horas'))[0]['duracion_horas'] if capacitacion_evento_capacitacion.objects.filter(id=id).values('duracion_horas') else 0
            put = capacitacion_evento_capacitacion.objects.get(id=pk)
            serializer= capacitacion_evento_capacitacionserializer(put,data=request.data)
            if serializer.is_valid():
                serializer.save()
                
                ###################HORAS METAS#######################
                numero_empleados_recibir_calculo=''
                duracion_horas_calculo=''
                horas_metas_calculo=''
                if "numero_empleados_recibir" in request.data:
                    numero_empleados_recibir_calculo = request.data['numero_empleados_recibir']
                    duracion_horas_calculo = (capacitacion_evento_capacitacion.objects.filter(id=id).values('duracion_horas'))[0]['duracion_horas'] if capacitacion_evento_capacitacion.objects.filter(id=id).values('duracion_horas') else None
                    horas_metas_calculo= int(duracion_horas_calculo)*int(numero_empleados_recibir_calculo)
                    capacitacion_evento_capacitacion.objects.filter(id=id).update(meta_horas=horas_metas_calculo)
                ##############################################
                horas_cumplidas_finales=''
                horas_cumplidas_finales=(capacitacion_evento_capacitacion.objects.filter(id=id,capacitacion_asistencia__asistio=True).annotate(Sum('capacitacion_asistencia__recibidas')).values('capacitacion_asistencia__recibidas__sum'))[0]['capacitacion_asistencia__recibidas__sum'] if capacitacion_evento_capacitacion.objects.filter(id=id,capacitacion_asistencia__asistio=True).annotate(Sum('capacitacion_asistencia__recibidas')).values('capacitacion_asistencia__recibidas__sum') else None
                capacitacion_evento_capacitacion.objects.filter(id=id).update(horas_cumplidas=horas_cumplidas_finales)
                
                evento_id=serializer.data['id']
                if usuario_id!=None:
                    capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(actualizado_por=usuario_id)


                capacitacion_campania_id=serializer.data['campania']
            
                duracion_horas= serializer.data['duracion_horas']
                fecha_f=datetime.strptime(serializer.data['fecha_fin'], '%Y-%m-%d').date()
                fecha_i=datetime.strptime(serializer.data['fecha_inicio'], '%Y-%m-%d').date() 
            
                campania_fecha_f=(capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('fecha_fin'))[0]['fecha_fin'] if capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('fecha_fin') else None
                campania_fecha_i=(capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('fecha_inicio'))[0]['fecha_inicio'] if capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('fecha_inicio') else None
                campania_duracion_horas=(capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('duracion_horas'))[0]['duracion_horas'] if capacitacion_campania.objects.filter(id=capacitacion_campania_id).values('duracion_horas') else None
                # if campania_fecha_f < fecha_f:
                #     capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_fin=fecha_f)
                #     # n_estado_campania=(capacitacion_estado.objects.filter(descripcion='Abierto').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Abierto').values('id') else None
                #     # capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=n_estado_campania)
                
                # if campania_fecha_i> fecha_i:
                #     capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_inicio=fecha_i)
                
                f_i=(capacitacion_evento_capacitacion.objects.filter().order_by('fecha_inicio').values('fecha_inicio'))[0]['fecha_inicio'] if capacitacion_evento_capacitacion.objects.filter().order_by('fecha_inicio').values('fecha_inicio') else None
                f_f=(capacitacion_evento_capacitacion.objects.filter().order_by('-fecha_fin').values('fecha_fin'))[0]['fecha_fin'] if capacitacion_evento_capacitacion.objects.filter().order_by('-fecha_fin').values('fecha_fin') else None
                capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_fin=f_f)
                capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_inicio=f_i)
                n_estado_campania=(capacitacion_estado.objects.filter(descripcion='Abierto').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Abierto').values('id') else None
                if hoy <= f_i:
                    capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=n_estado_campania)
                ##### eevaluando el estado despues de cambiar las fechas
                if hoy >= f_i:
                    estado_en_proceso_id=(capacitacion_estado.objects.filter(descripcion='En proceso').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='En proceso').values('id') else None
            
                    if estado_en_proceso_id!=None:
                        capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=estado_en_proceso_id)

                if hoy>=f_f:
                    estado_cerrado=(capacitacion_estado.objects.filter(descripcion='Cerrado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Cerrado').values('id') else None
                    if estado_cerrado!=None:
                        capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=estado_cerrado)
                
                ###########

                ###############################duracion_horas_campania
                # capacitacion_campania_id=serializer.data['campania']
                campania_duracion_horas_totales = (capacitacion_evento_capacitacion.objects.filter(campania__id=capacitacion_campania_id).aggregate(Sum('duracion_horas')))['duracion_horas__sum']
                capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(duracion_horas=campania_duracion_horas_totales)

                #############################nuevo serializers
                nuevo_query= capacitacion_evento_capacitacion.objects.get(id=id) if capacitacion_evento_capacitacion.objects.filter(id=id) else None
                if nuevo_query!=None:
                    serializer_evento_f= capacitacion_evento_capacitacionserializer(nuevo_query)
                    return Response(serializer_evento_f.data,status=status.HTTP_200_OK)
                
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response ({"Mensaje":"La información enviada no es valida","Error":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
     
    
    def destroy(self, request, pk):
        try:
            hoy=datetime.now().date()
            instance = self.get_object()
            asistencia = capacitacion_evento_capacitacion.objects.filter(id=instance.id).exclude(capacitacion_asistencia__empleado__id=None).values('capacitacion_asistencia__empleado__id') if capacitacion_evento_capacitacion.objects.filter(id=instance.id).exclude(capacitacion_asistencia__empleado__id=None).values('capacitacion_asistencia__empleado__id') else None
            if asistencia!=None:
                return Response ({"respuesta":"No se puede borrar el evento debido a que existe empleados ligado a el."},status=status.HTTP_400_BAD_REQUEST)

            capacitacion_campania_id = (capacitacion_evento_capacitacion.objects.filter(id=instance.id).values('campania__id'))[0]['campania__id'] if capacitacion_evento_capacitacion.objects.filter(id=instance.id) else None 
            self.perform_destroy(instance)

            f_i=(capacitacion_evento_capacitacion.objects.filter().order_by('fecha_inicio').values('fecha_inicio'))[0]['fecha_inicio'] if capacitacion_evento_capacitacion.objects.filter().order_by('fecha_inicio').values('fecha_inicio') else None
            f_f=(capacitacion_evento_capacitacion.objects.filter().order_by('-fecha_fin').values('fecha_fin'))[0]['fecha_fin'] if capacitacion_evento_capacitacion.objects.filter().order_by('-fecha_fin').values('fecha_fin') else None
            capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_fin=f_f)
            capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(fecha_inicio=f_i)
            n_estado_campania=(capacitacion_estado.objects.filter(descripcion='Abierto').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Abierto').values('id') else None
            if hoy <= f_i:
                capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=n_estado_campania)
            ##### eevaluando el estado despues de cambiar las fechas
            if hoy >= f_i:
                estado_en_proceso_id=(capacitacion_estado.objects.filter(descripcion='En proceso').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='En proceso').values('id') else None
        
                if estado_en_proceso_id!=None:
                    capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=estado_en_proceso_id)

            if hoy>=f_f:
                estado_cerrado=(capacitacion_estado.objects.filter(descripcion='Cerrado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Cerrado').values('id') else None
                if estado_cerrado!=None:
                    capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(estado=estado_cerrado)

            campania_duracion_horas_totales = (capacitacion_evento_capacitacion.objects.filter(campania__id=capacitacion_campania_id).aggregate(Sum('duracion_horas')))['duracion_horas__sum']
            capacitacion_campania.objects.filter(id=capacitacion_campania_id).update(duracion_horas=campania_duracion_horas_totales)
            
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)




class capacitacion_asistenciaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_asistencia.objects.all()
    serializer_class = capacitacion_asistenciaserializer
    def list(self, request):
        queryset = capacitacion_asistencia.objects.all()
        serializer_class = capacitacion_asistenciaserializer(queryset, many=True)
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
                    if tipo_busqueda =='empleado__nombre':
                        filter_kwargs['empleado__nombre__icontains'] = filter
                    if tipo_busqueda =='empleado__codigo':
                        filter_kwargs['empleado__codigo__icontains'] = filter
                    if tipo_busqueda =='evento_capacitacion__id':
                        filter_kwargs['evento_capacitacion__id'] = filter
                 
                 
                        
 
                        
                queryset =  capacitacion_asistencia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_asistencia.objects.filter(**filter_kwargs).count()
                asistencia_total=capacitacion_asistencia.objects.filter(**filter_kwargs).filter(asistio=True).count()
                inasistencia_total=capacitacion_asistencia.objects.filter(**filter_kwargs).filter(asistio=False).count()
                serializer = capacitacion_asistenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo,"asistencia_total":asistencia_total,"inasistencia_total":inasistencia_total}) 
            else: 
                queryset =  capacitacion_asistencia.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_asistencia.objects.filter().count()
                asistencia_total=capacitacion_asistencia.objects.filter().filter(asistio=True).count()
                inasistencia_total=capacitacion_asistencia.objects.filter().filter(asistio=False).count()
                serializer = capacitacion_asistenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo,"asistencia_total":asistencia_total,"inasistencia_total":inasistencia_total})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='empleado__nombre':
                        filter_kwargs['empleado__nombre__icontains'] = filter
                    if tipo_busqueda =='empleado__codigo':
                        filter_kwargs['empleado__codigo__icontains'] = filter
                    if tipo_busqueda =='evento_capacitacion__id':
                        filter_kwargs['evento_capacitacion__id'] = filter

                        
                queryset =  capacitacion_asistencia.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_asistencia.objects.filter(**filter_kwargs).count()
                asistencia_total=capacitacion_asistencia.objects.filter(**filter_kwargs).filter(asistio=True).count()
                inasistencia_total=capacitacion_asistencia.objects.filter(**filter_kwargs).filter(asistio=False).count()
                serializer = capacitacion_asistenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo,"asistencia_total":asistencia_total,"inasistencia_total":inasistencia_total}) 
            else: 
                queryset =  capacitacion_asistencia.objects.filter().order_by('id')
                conteo =  capacitacion_asistencia.objects.filter().count()
                asistencia_total=capacitacion_asistencia.objects.filter().filter(asistio=True).count()
                inasistencia_total=capacitacion_asistencia.objects.filter().filter(asistio=False).count()
                serializer = capacitacion_asistenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo,"asistencia_total":asistencia_total,"inasistencia_total":inasistencia_total})


    def create(self, request):
        serializer = capacitacion_asistenciaserializer(data=request.data)
        evento_id= request.data["evento_capacitacion"]
        print('evento_id',evento_id)
        duracion_horas= (capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('duracion_horas'))[0]['duracion_horas'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('duracion_horas') else None
        costo_capacitacion =(capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('costo_capacitacion'))[0]['costo_capacitacion'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('costo_capacitacion') else None
        numero_empleados_recibir =(capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('numero_empleados_recibir'))[0]['numero_empleados_recibir'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('numero_empleados_recibir') else None
        if serializer.is_valid(): 
            serializer.save()

            ######################estado
            asistencia_id=serializer.data['id']
            estado_nota=(capacitacion_estado.objects.filter(descripcion='Pendiente').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Pendiente').values('id') else None
            capacitacion_asistencia.objects.filter(id=asistencia_id).update(estado=estado_nota)
            ###########horas cumplidas
            cantidad_personas_que_asistieron=capacitacion_asistencia.objects.filter(evento_capacitacion=evento_id,asistio=True).count()
            cantidad_personas_invitadas=capacitacion_asistencia.objects.filter(evento_capacitacion=evento_id,asistio=True).count()
            horas_cumplidas=int(duracion_horas) * int(cantidad_personas_que_asistieron)
            capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(horas_cumplidas=horas_cumplidas)
            ####################costo de capacitacion
            if costo_capacitacion!=None and cantidad_personas_que_asistieron!=0:
                costo_empleado_calculo= int(costo_capacitacion)/int(cantidad_personas_que_asistieron)
                capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(costo_empleado=costo_empleado_calculo)
            #################porcentaje asistencia
            porcentaje_total= (int(cantidad_personas_que_asistieron)*100)/int(numero_empleados_recibir)
            print('porcentaje_total',porcentaje_total)
            capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(porcentaje_asistencia=porcentaje_total)

            ###########################Horas metas
            horas_m= int(duracion_horas)/int(numero_empleados_recibir)
            capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(meta_horas=horas_m)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        else:       
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
 
    def update(self,requets,pk=None):
        id=pk
        nota_aprovatoria=None
        nota_evaluacion=None
        estado_nota=''
        existe= capacitacion_asistencia.objects.filter(id=id).count()
        if existe!=0:
            
            put = capacitacion_asistencia.objects.get(id=id)
            ######print('equets.data',requets.data)
            serializer= capacitacion_asistenciaserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
            
                evento_id = serializer.data['evento_capacitacion']
                duracion_horas= (capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('duracion_horas'))[0]['duracion_horas'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('duracion_horas') else None
                costo_capacitacion =(capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('costo_capacitacion'))[0]['costo_capacitacion'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('costo_capacitacion') else None
                numero_empleados_recibir =(capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('numero_empleados_recibir'))[0]['numero_empleados_recibir'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('numero_empleados_recibir') else None
                ###########horas cumplidas
                cantidad_personas_que_asistieron=capacitacion_asistencia.objects.filter(evento_capacitacion=evento_id,asistio=True).count()
                cantidad_personas_invitadas=capacitacion_asistencia.objects.filter(evento_capacitacion=evento_id,id=id).count()
                horas_cumplidas_finales=(capacitacion_asistencia.objects.filter(evento_capacitacion=evento_id,asistio=True).aggregate(Sum('recibidas')))['recibidas__sum'] if (capacitacion_asistencia.objects.filter(evento_capacitacion=evento_id,asistio=True).aggregate(Sum('recibidas')))['recibidas__sum'] else None
                capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(horas_cumplidas=horas_cumplidas_finales)
                ####################costo de capacitacion
                if costo_capacitacion!=None and cantidad_personas_que_asistieron!=0:
                    costo_empleado_calculo= int(costo_capacitacion)/int(cantidad_personas_que_asistieron)
                    capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(costo_empleado=costo_empleado_calculo)
                #################porcentaje asistencia
                porcentaje_total= (int(cantidad_personas_que_asistieron)*100)/int(numero_empleados_recibir)
                print('porcentaje_total',porcentaje_total)
                capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(porcentaje_asistencia=porcentaje_total)

                ###########################Horas metas
                horas_m= int(duracion_horas)*int(numero_empleados_recibir)
                capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(meta_horas=horas_m)
                ################################estado dependiendo de la nota
                validacion_ne = serializer.data['nota_evaluacion']
                if validacion_ne!=None:
                    nota_evaluacion = float(serializer.data['nota_evaluacion'] )
                
                    if nota_evaluacion!=None:
                    
                
                        nota_aprovatoria= (capacitacion_asistencia.objects.filter(id=id).values('evento_capacitacion__nota_aprovatoria'))[0]['evento_capacitacion__nota_aprovatoria'] if capacitacion_asistencia.objects.filter(id=id).values('evento_capacitacion__nota_aprovatoria') else None
                        ######print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',nota_aprovatoria)
                        ######print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',nota_evaluacion)
                        if nota_aprovatoria!=None and int(nota_evaluacion) >= int(nota_aprovatoria):
                            estado_nota=(capacitacion_estado.objects.filter(descripcion='Aprobado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Aprobado').values('id') else None
                        
                        if nota_aprovatoria!=None and int(nota_evaluacion) <= int(nota_aprovatoria):
                            estado_nota=(capacitacion_estado.objects.filter(descripcion='Reprobado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Reprobado').values('id') else None

                        # estado_nota=(capacitacion_estado.objects.filter(descripcion='Pendiente').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Pendiente').values('id') else None
                        if estado_nota!='':   
                            capacitacion_asistencia.objects.filter(id=id).update(estado=estado_nota)
                
            
                #nuevo serializer############################################################
                nuevo_query= capacitacion_asistencia.objects.get(id=id) if capacitacion_asistencia.objects.filter(id=id) else None
                if nuevo_query!=None:
                    serializer_asistencia= capacitacion_asistenciaserializer(nuevo_query) 
                ##############################################################################
                    return Response(serializer_asistencia.data,status=status.HTTP_200_OK)
                else:
                    return Response ({"Problemas al serializar el objeto":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response ({"La información enviada no es valida":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
         
    
    def destroy(self, request, pk):
        print('entro al destroy')
        try:
            instance = self.get_object()
            evento_id = (capacitacion_asistencia.objects.filter(id=instance.id).values('evento_capacitacion'))[0]['evento_capacitacion'] if capacitacion_asistencia.objects.filter(id=instance.id) else None 
            print('evento_id',evento_id)
            self.perform_destroy(instance)
            
            if evento_id!=None:
                cantidad_personas_que_asistieron=capacitacion_asistencia.objects.filter(evento_capacitacion=evento_id,asistio=True).count()
                print('cantidad_personas_que_asistieron',cantidad_personas_que_asistieron)
                p=int(cantidad_personas_que_asistieron)
                print('cantidad_personas_que_asistieron__2',p)
                numero_empleados_recibir =(capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('numero_empleados_recibir'))[0]['numero_empleados_recibir'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('numero_empleados_recibir') else None
                # cantidad_personas_que_asistieron=capacitacion_asistencia.objects.filter(evento_capacitacion=evento_id,asistio=True).count()
                duracion_horas= (capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('duracion_horas'))[0]['duracion_horas'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('duracion_horas') else None
                costo_capacitacion =(capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('costo_capacitacion'))[0]['costo_capacitacion'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('costo_capacitacion') else None
                #################porcentaje asistencia
                if cantidad_personas_que_asistieron!=0 and numero_empleados_recibir!=None:  
                    print('entroooo')
                    porcentaje_total= (int(cantidad_personas_que_asistieron)*100)/int(numero_empleados_recibir)
                    print('porcentaje_total',porcentaje_total)
                    capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(porcentaje_asistencia=porcentaje_total)
                
                ###########horas cumplidas
                if cantidad_personas_que_asistieron!=0 and duracion_horas!=None:
                    horas_cumplidas=int(duracion_horas) * int(cantidad_personas_que_asistieron)
                    capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(horas_cumplidas=horas_cumplidas)

                ####################costo de capacitacion
                if costo_capacitacion!=None and cantidad_personas_que_asistieron!=0:
                    costo_empleado_calculo= int(costo_capacitacion)/int(cantidad_personas_que_asistieron)
                    capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(costo_empleado=costo_empleado_calculo)
                
                ###########################Horas metas
                if duracion_horas!=None and numero_empleados_recibir!=None:
                    horas_m= int(duracion_horas)/int(numero_empleados_recibir)
                    capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(meta_horas=horas_m)

        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)


class busqueda_personas_por_rolViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = Funcional_empleadoserializer
    def list(self, request):
        filter=''
       
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            usuarios_reponsables = User.objects.filter(groups__name=filter).values_list('username',flat=True) if User.objects.filter(groups__name=filter) else None
        
            queryset =  Funcional_empleado.objects.filter(codigo__in=usuarios_reponsables).order_by('id')[offset:offset+limit]
            conteo =  Funcional_empleado.objects.filter(codigo__in=usuarios_reponsables).count()
            serializer = Funcional_empleadoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":conteo})
            
        else:
            usuarios_reponsables = User.objects.filter(groups__name=filter).values_list('username',flat=True) if User.objects.filter(groups__name=filter) else None
        
            queryset =  Funcional_empleado.objects.filter(codigo__in=usuarios_reponsables).order_by('id')
            conteo =  Funcional_empleado.objects.filter(codigo__in=usuarios_reponsables).count()
            serializer = Funcional_empleadoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":conteo})
            
class capacitacion_llenado_9cajasViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = capacitacion_matriz_9_cajas.objects.none() 
    def get(self,request):
        #verificar rol del usuario
        filtros = {}
        roles=list(request.user.groups.values_list('name',flat = True))
        ########print(roles)
        #######print(roles)
        anio=None
        
        if self.request.query_params.get('anio'):
            anio=self.request.query_params.get('anio')
        else:
            return Response({"resultado":"el parametro anio es de caracter obligatorio"},status= status.HTTP_404_NOT_FOUND)


        if self.request.query_params.get('empresa'):
            empresa_list=json.loads(self.request.query_params.get('empresa'))
            filtros['unidad_organizativa__sociedad_financiera__id__in']=empresa_list
            
        if self.request.query_params.get('unidad'):
            unidad_list=json.loads(self.request.query_params.get('unidad'))
            if len(unidad_list):
                filtros['unidad_organizativa__id__in']=unidad_list

        if self.request.query_params.get('colaborador_id'):
            colab_list=json.loads(self.request.query_params.get('colaborador_id'))
            if len(colab_list)>0:
                filtros['id__in']=colab_list

        if self.request.query_params.get('colaborador'):
            colab_list=json.loads(self.request.query_params.get('colaborador'))
            if len(colab_list)>0:
                filtros['codigo__in']=colab_list

        if self.request.query_params.get('colaborador_nombre'):
            colab_list=self.request.query_params.get('colaborador_nombre')
            if len(colab_list)>0:
                filtros['nombre__in']=colab_list

        

        if self.request.query_params.get('departamento'): 
            division_personal_list=json.loads(self.request.query_params.get('departamento'))
            if len(division_personal_list):
                filtros['division__id__in']=division_personal_list
        if 'administrador' in roles:
            empleados= list(Funcional_empleado.objects.filter(antiguedad_laboral__gte=24).filter(**filtros).filter(Q(fecha_baja__isnull=True) | Q(fecha_baja__gte=datetime.date(datetime.now()))).values())
            #print('administrador')
            ######print(len(empleados),'conteo de resultados')
            contador=0
            potencial_promedio=0
            desempenio_promedio=0
            for x in empleados:
                contador=contador+1
                ######calculo de puntos por formacion 
                puntos_educacion=0
                primaria=['PRIMARIA','SECUNDARIA INCOMPLETA']
                secundaria=['CICLO COMUN']
                carrera =['BACHILLER TECNICO INDUSTRIAL','BACHILLER TECNICO PROFESIONAL','EDUCACION COMERCIAL','BACHILLER EN COMPUTACION','BACHILLER EN CIENCIAS Y LETRAS','PASANTE UNIVERSITARIO']
                universitario=['PROFESIONAL UNIVERSITARIO']
                postgrado=['MAESTRIA','DOCTORADO']


                educacion_primaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=primaria,fecha_fin__lte=datetime.now().date())
                educacion_secundaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=secundaria,fecha_fin__lte=datetime.now().date())
                educacion_carrera=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=carrera,fecha_fin__lte=datetime.now().date())
                educacion_universitaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=universitario,fecha_fin__lte=datetime.now().date())
                educacion_postgrado=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=postgrado,fecha_fin__lte=datetime.now().date())
                anio=self.request.query_params.get('anio')
                
                if educacion_primaria:
                    metrica_primaria=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado básico')
                    if metrica_primaria:
                        puntos_educacion=puntos_educacion + metrica_primaria[0].porcentaje
                if educacion_secundaria:
                    metrica_secundaria=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado media')
                    if metrica_secundaria:
                        puntos_educacion=puntos_educacion + metrica_secundaria[0].porcentaje                
                    metrica_carrera=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado diversificado')
                    if metrica_carrera:
                        puntos_educacion=puntos_educacion + metrica_carrera[0].porcentaje
                       
                if educacion_universitaria:
                    metrica_universitario=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Titulo universitario')
                    if metrica_universitario:
                        puntos_educacion=puntos_educacion + metrica_universitario[0].porcentaje
                if  educacion_postgrado:                       
                    metrica_postgrado=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Titulo postgrado')
                    if metrica_postgrado:
                        puntos_educacion=puntos_educacion + metrica_postgrado[0].porcentaje

                x['puntos_educacion']=puntos_educacion
##### fin calculo de puntos pór formacion
### calculo rendimiento capacitaciones
                #######print(x)
                primer_dia=date(int(anio), 1, 1)
                ultimo_dia=date(int(anio), 12, 31)

                nota_rendimiento=0
                campanias=capacitacion_campania.objects.filter(fecha_inicio__gte=primer_dia,fecha_fin__lte=ultimo_dia)
                eventos=capacitacion_evento_capacitacion.objects.filter(campania__in=campanias)
                evento_asistencia_nota=capacitacion_asistencia.objects.filter(evento_capacitacion__in=eventos,empleado__id=x['id']).exclude(evento_capacitacion__nota_aprovatoria=0).aggregate(Avg('nota_evaluacion'))
                evento_asistencia_nota=evento_asistencia_nota['nota_evaluacion__avg'] if evento_asistencia_nota['nota_evaluacion__avg'] else 0
                ######print(evento_asistencia_nota)
                puntos_metrica_capacitacion= capacitacion_metrica_evaluacion_factor.objects.get(anio=anio,valor_minimo__lte=evento_asistencia_nota,valor_maximo__gte=evento_asistencia_nota).porcentaje if capacitacion_metrica_evaluacion_factor.objects.filter(anio=anio,valor_minimo__lte=evento_asistencia_nota,valor_maximo__gte=evento_asistencia_nota) else 0               
                x['puntos_rendimiento_capacitacion']=puntos_metrica_capacitacion if puntos_metrica_capacitacion else 0
### calculo rendimiento 
                antiguedad=0
                
                if x['antiguedad_laboral']:
                    antiguedad=x['antiguedad_laboral'] / 12
                    antiguedad=round(antiguedad)
                puntos_experiencia=0
                if antiguedad>0:

                    puntos_experiencia=capacitacion_metrica_experiencia_puesto.objects.get(anio=anio,de__lte=antiguedad,hasta__gte=antiguedad).porcentaje if capacitacion_metrica_experiencia_puesto.objects.filter(anio=anio,de__lte=antiguedad,hasta__gte=antiguedad) else 0
                    if puntos_educacion:
                        pass
                    else:
                        puntos_experiencia =0

                x['puntos_experiencia']=puntos_experiencia if puntos_experiencia else 0
                
                puntos_total= puntos_educacion + puntos_metrica_capacitacion + puntos_experiencia
                x['puntos_total']=puntos_total if puntos_total else 0
                ######print(antiguedad)
                ######print(puntos_total)
                #experiencia = capacitacion_metrica_experiencia_puestoub
                periodicidad=evaluacion_periodicidad.objects.filter(anio=anio)
                evaluaciones= evaluacion_encabezado.objects.filter(periodicidad__in=periodicidad,evaluado__id=x['id'],estado=False).annotate(calificacion=Case(When(tipo_evaluacion_encabezado=2, then=Cast('nota_total_porcentaje',IntegerField())),When(tipo_evaluacion_encabezado=1, then=Cast('nota_total_porcentaje_prorateo',IntegerField())),default=Value(0))).aggregate(Avg('calificacion'))
                x['nota_evaluacion']=evaluaciones['calificacion__avg'] if evaluaciones['calificacion__avg'] else 0

                x['desempenio_percibido']=round((Decimal(puntos_total) + Decimal(x['nota_evaluacion']))/2)


#fin calculo desempeño percibido

#potencial
                ######print(x)
                puntaje_obtenido_competencia_org=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia_ger=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='GERENCIAL',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='GERENCIAL',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia_espe=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ESPECIFICA',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ESPECIFICA',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__in=['ORGANIZACIONAL','GERENCIAL','ESPECIFICA'],encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']) else 0
                x['puntaje_obtenido_competencia_org']=puntaje_obtenido_competencia_org
                x['puntaje_obtenido_competencia_espe']=puntaje_obtenido_competencia_espe
                x['puntaje_obtenido_competencia_ger']=puntaje_obtenido_competencia_ger
                x['potencial']=puntaje_obtenido_competencia

                desempenio_posicion_x=capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['desempenio_percibido'],valor_maximo__gte=x['desempenio_percibido'],tipo_criterio=2).first().cordenada if capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['desempenio_percibido'],valor_maximo__gte=x['desempenio_percibido'],tipo_criterio=2).count()>0 else None
                #####print(desempenio_posicion_x)
               
                potencial_posicion_y=capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['potencial'],valor_maximo__gte=x['potencial'],tipo_criterio=1).first().cordenada if capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['potencial'],valor_maximo__gte=x['potencial'],tipo_criterio=1).count()>0 else None
                #####print(potencial_posicion_y)
               
                caja=capacitacion_matriz_9_cajas.objects.get(x=desempenio_posicion_x,y=potencial_posicion_y,anio=anio).id if capacitacion_matriz_9_cajas.objects.filter(x=desempenio_posicion_x,y=potencial_posicion_y,anio=anio) else None
                #####print(caja)

                ######print(desempenio_posicion_x)
                ######print(potencial_posicion_y)
                ######print(caja)
                x['caja']=caja
                funciones=list(Funcional_empleado.objects.get(id=x['id']).posicion.all().values('id','descripcion')) if Funcional_empleado.objects.filter(id=x['id']) else None
                division = list(Funcional_Division_Personal.objects.filter(id=x['division_personal_id']).values()) 
                departamento = list(Funcional_empleado.objects.get(id=x['id']).unidad_organizativa.all().values('id','nombre')) if Funcional_empleado.objects.filter(id=x['id']) else None
                empresa = list(Funcional_empleado.objects.get(id=x['id']).unidad_organizativa.all().values('sociedad_financiera__id','sociedad_financiera__nombre')) if Funcional_empleado.objects.filter(id=x['id']) else None
                
                ######print(x)
               
                x['Funcion_List']=funciones
                x['division_List']=division
                x['departamento']=departamento
                x['empresa']=empresa
                potencial_promedio=potencial_promedio +  x['potencial']
                desempenio_promedio=desempenio_promedio + x['desempenio_percibido']
            cajas_correspondientes = capacitacion_matriz_9_cajas.objects.filter(anio=anio).values() if capacitacion_matriz_9_cajas.objects.filter(anio=anio) else None
            potencial_promedio=Decimal(potencial_promedio / contador).quantize(0, ROUND_HALF_UP) if contador > 0 else potencial_promedio
            desempenio_promedio=Decimal(desempenio_promedio /contador).quantize(0, ROUND_HALF_UP) if contador > 0 else desempenio_promedio

            cajas_correspondientes = capacitacion_matriz_9_cajas.objects.filter(anio=anio).values() if capacitacion_matriz_9_cajas.objects.filter(anio=anio) else None
            if cajas_correspondientes ==None:
                return Response({"resultado":"no existen cajas registradas para los parametros de busqueda, año:" + anio},status= status.HTTP_400_BAD_REQUEST)                                                                 

            for caja  in cajas_correspondientes:
                empleados_list=[]
                for emp in empleados:
                    if emp['caja']==caja['id']:
                        ######print('entro')
                        empleados_list.append(emp)
                caja['empleados']=empleados_list
            

            return Response({"resultado":cajas_correspondientes,"potencial_promedio":potencial_promedio,"desempenio_promedio":desempenio_promedio},status= status.HTTP_200_OK)

        if 'Responsable_Capacitacion' in roles:
            #print('Responsable_Capacitacion')
            Q(fecha_baja__gte=datetime.date(datetime.now())) 
            empleados= list(Funcional_empleado.objects.filter(antiguedad_laboral__gte=24).filter(**filtros).filter(Q(fecha_baja__isnull=True) | Q(fecha_baja__gte=datetime.date(datetime.now()))).values())
            ########print(len(empleados),'conteo de resultados')
            #print(empleados)
            contador=0
            potencial_promedio=0
            desempenio_promedio=0
            for x in empleados:
                contador=contador+1
                ######calculo de puntos por formacion 
                puntos_educacion=0
                primaria=['PRIMARIA','SECUNDARIA INCOMPLETA']
                secundaria=['CICLO COMUN']
                carrera =['BACHILLER TECNICO INDUSTRIAL','BACHILLER TECNICO PROFESIONAL','EDUCACION COMERCIAL','BACHILLER EN COMPUTACION','BACHILLER EN CIENCIAS Y LETRAS','PASANTE UNIVERSITARIO']
                universitario=['PROFESIONAL UNIVERSITARIO']
                postgrado=['MAESTRIA','DOCTORADO']


                educacion_primaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=primaria,fecha_fin__lte=datetime.now().date())
                educacion_secundaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=secundaria,fecha_fin__lte=datetime.now().date())
                educacion_carrera=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=carrera,fecha_fin__lte=datetime.now().date())
                educacion_universitaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=universitario,fecha_fin__lte=datetime.now().date())
                educacion_postgrado=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=postgrado,fecha_fin__lte=datetime.now().date())
                anio=self.request.query_params.get('anio')
                
                if educacion_primaria:
                    metrica_primaria=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado básico')
                    if metrica_primaria:
                        puntos_educacion=puntos_educacion + metrica_primaria[0].porcentaje
                if educacion_secundaria:
                    metrica_secundaria=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado media')
                    if metrica_secundaria:
                        puntos_educacion=puntos_educacion + metrica_secundaria[0].porcentaje                
                    metrica_carrera=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado diversificado')
                    if metrica_carrera:
                        puntos_educacion=puntos_educacion + metrica_carrera[0].porcentaje
                       
                if educacion_universitaria:
                    metrica_universitario=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Titulo universitario')
                    if metrica_universitario:
                        puntos_educacion=puntos_educacion + metrica_universitario[0].porcentaje
                if  educacion_postgrado:                       
                    metrica_postgrado=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Titulo postgrado')
                    if metrica_postgrado:
                        puntos_educacion=puntos_educacion + metrica_postgrado[0].porcentaje

                x['puntos_educacion']=puntos_educacion
##### fin calculo de puntos pór formacion
### calculo rendimiento capacitaciones
                #########print(x)
                primer_dia=date(int(anio), 1, 1)
                ultimo_dia=date(int(anio), 12, 31)

                nota_rendimiento=0
                campanias=capacitacion_campania.objects.filter(fecha_inicio__gte=primer_dia,fecha_fin__lte=ultimo_dia)
                eventos=capacitacion_evento_capacitacion.objects.filter(campania__in=campanias)
                evento_asistencia_nota=capacitacion_asistencia.objects.filter(evento_capacitacion__in=eventos,empleado__id=x['id']).exclude(evento_capacitacion__nota_aprovatoria=0).aggregate(Avg('nota_evaluacion'))
                evento_asistencia_nota=evento_asistencia_nota['nota_evaluacion__avg'] if evento_asistencia_nota['nota_evaluacion__avg'] else 0
                ########print(evento_asistencia_nota)
                puntos_metrica_capacitacion= capacitacion_metrica_evaluacion_factor.objects.get(anio=anio,valor_minimo__lte=evento_asistencia_nota,valor_maximo__gte=evento_asistencia_nota).porcentaje if capacitacion_metrica_evaluacion_factor.objects.filter(anio=anio,valor_minimo__lte=evento_asistencia_nota,valor_maximo__gte=evento_asistencia_nota) else 0               
                x['puntos_rendimiento_capacitacion']=puntos_metrica_capacitacion if puntos_metrica_capacitacion else 0
### calculo rendimiento 
                antiguedad=0
                
                if x['antiguedad_laboral']:
                    antiguedad=x['antiguedad_laboral'] / 12
                    antiguedad=round(antiguedad)
                puntos_experiencia=0
                if antiguedad>0:

                    puntos_experiencia=capacitacion_metrica_experiencia_puesto.objects.get(anio=anio,de__lte=antiguedad,hasta__gte=antiguedad).porcentaje if capacitacion_metrica_experiencia_puesto.objects.filter(anio=anio,de__lte=antiguedad,hasta__gte=antiguedad) else 0
                    if puntos_educacion:
                        pass
                    else:
                        puntos_experiencia =0

                x['puntos_experiencia']=puntos_experiencia if puntos_experiencia else 0
                
                puntos_total= puntos_educacion + puntos_metrica_capacitacion + puntos_experiencia
                x['puntos_total']=puntos_total if puntos_total else 0
                #######print(antiguedad)
                #######print(puntos_total)
                #experiencia = capacitacion_metrica_experiencia_puestoub
                periodicidad=evaluacion_periodicidad.objects.filter(anio=anio)
                evaluaciones= evaluacion_encabezado.objects.filter(periodicidad__in=periodicidad,evaluado__id=x['id'],estado=False).annotate(calificacion=Case(When(tipo_evaluacion_encabezado=2, then=Cast('nota_total_porcentaje',IntegerField())),When(tipo_evaluacion_encabezado=1, then=Cast('nota_total_porcentaje_prorateo',IntegerField())),default=Value(0))).aggregate(Avg('calificacion'))
                x['nota_evaluacion']=evaluaciones['calificacion__avg'] if evaluaciones['calificacion__avg'] else 0

                x['desempenio_percibido']=round((Decimal(puntos_total) + Decimal(x['nota_evaluacion']))/2)


#fin calculo desempeño percibido

#potencial
                #######print(x)
                puntaje_obtenido_competencia_org=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia_ger=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='GERENCIAL',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='GERENCIAL',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia_espe=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ESPECIFICA',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ESPECIFICA',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__in=['ORGANIZACIONAL','GERENCIAL','ESPECIFICA'],encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']) else 0
                x['puntaje_obtenido_competencia_org']=puntaje_obtenido_competencia_org if puntaje_obtenido_competencia_org else 0
                x['puntaje_obtenido_competencia_espe']=puntaje_obtenido_competencia_espe if puntaje_obtenido_competencia_espe else 0
                x['puntaje_obtenido_competencia_ger']=puntaje_obtenido_competencia_ger if  puntaje_obtenido_competencia_ger else 0
                x['potencial']=puntaje_obtenido_competencia if puntaje_obtenido_competencia else 0

                desempenio_posicion_x=capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['desempenio_percibido'],valor_maximo__gte=x['desempenio_percibido'],tipo_criterio=2).first().cordenada if capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['desempenio_percibido'],valor_maximo__gte=x['desempenio_percibido'],tipo_criterio=2).count()>0 else None
                #####print(desempenio_posicion_x)
               
                #####print(x['potencial'])
                potencial_posicion_y=capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['potencial'],valor_maximo__gte=x['potencial'],tipo_criterio=1).first().cordenada if capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['potencial'],valor_maximo__gte=x['potencial'],tipo_criterio=1).count()>0 else None
                ###print(potencial_posicion_y)
                #####print(potencial_posicion_y)
               
                caja=capacitacion_matriz_9_cajas.objects.get(x=desempenio_posicion_x,y=potencial_posicion_y,anio=anio).id if capacitacion_matriz_9_cajas.objects.filter(x=desempenio_posicion_x,y=potencial_posicion_y,anio=anio) else None
                #####print(caja)

                #######print(desempenio_posicion_x)
                #######print(potencial_posicion_y)
                #######print(caja)
                x['caja']=caja
                funciones=list(Funcional_empleado.objects.get(id=x['id']).posicion.all().values('id','descripcion')) if Funcional_empleado.objects.filter(id=x['id']) else None
                division = list(Funcional_Division_Personal.objects.filter(id=x['division_personal_id']).values()) 
                departamento = list(Funcional_empleado.objects.get(id=x['id']).unidad_organizativa.all().values('id','nombre')) if Funcional_empleado.objects.filter(id=x['id']) else None
                empresa = list(Funcional_empleado.objects.get(id=x['id']).unidad_organizativa.all().values('sociedad_financiera__id','sociedad_financiera__nombre')) if Funcional_empleado.objects.filter(id=x['id']) else None
                
                ######print(x)
               
                x['Funcion_List']=funciones
                x['division_List']=division
                x['departamento']=departamento
                x['empresa']=empresa
                potencial_promedio=potencial_promedio +  x['potencial']
                desempenio_promedio=desempenio_promedio + x['desempenio_percibido']
            cajas_correspondientes = capacitacion_matriz_9_cajas.objects.filter(anio=anio).values() if capacitacion_matriz_9_cajas.objects.filter(anio=anio) else None
            potencial_promedio=Decimal(potencial_promedio / contador).quantize(0, ROUND_HALF_UP) if contador > 0 else potencial_promedio
            desempenio_promedio=Decimal(desempenio_promedio /contador).quantize(0, ROUND_HALF_UP) if contador > 0 else desempenio_promedio
            if cajas_correspondientes ==None:
                return Response({"resultado":"no existen cajas registradas para los parametros de busqueda, año:" + anio},status= status.HTTP_400_BAD_REQUEST)
            if cajas_correspondientes: 
                for caja  in cajas_correspondientes:
                    empleados_list=[]
                    for emp in empleados:
                        if emp['caja']==caja['id']:
                            ######print('entro')
                            empleados_list.append(emp)
                    caja['empleados']=empleados_list
            else:
                return Response({"resultado":"no existen cajas registradas para los parametros de busqueda"},status= status.HTTP_404_NOT_FOUND)


            return Response({"resultado":cajas_correspondientes,"potencial_promedio":potencial_promedio,"desempenio_promedio":desempenio_promedio},status= status.HTTP_200_OK)



        if 'jefe':
            #print('jefe')
            empleados= list(Funcional_empleado.objects.filter(antiguedad_laboral__gte=24,jefe_inmediato=request.user.username).filter(**filtros).filter(Q(fecha_baja__isnull=True) | Q(fecha_baja__gte=datetime.date(datetime.now()))).values())
            contador=0
            potencial_promedio=0
            desempenio_promedio=0
            for x in empleados:
                contador=contador+1
                ######calculo de puntos por formacion 
                puntos_educacion=0
                primaria=['PRIMARIA','SECUNDARIA INCOMPLETA']
                secundaria=['CICLO COMUN']
                carrera =['BACHILLER TECNICO INDUSTRIAL','BACHILLER TECNICO PROFESIONAL','EDUCACION COMERCIAL','BACHILLER EN COMPUTACION','BACHILLER EN CIENCIAS Y LETRAS','PASANTE UNIVERSITARIO']
                universitario=['PROFESIONAL UNIVERSITARIO']
                postgrado=['MAESTRIA','DOCTORADO']


                educacion_primaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=primaria,fecha_fin__lte=datetime.now().date())
                educacion_secundaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=secundaria,fecha_fin__lte=datetime.now().date())
                educacion_carrera=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=carrera,fecha_fin__lte=datetime.now().date())
                educacion_universitaria=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=universitario,fecha_fin__lte=datetime.now().date())
                educacion_postgrado=Funcional_Educacion.objects.filter(empleado__codigo=x['codigo'],formacion__descripcion__in=postgrado,fecha_fin__lte=datetime.now().date())
                anio=self.request.query_params.get('anio')
                
                if educacion_primaria:
                    metrica_primaria=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado básico')
                    if metrica_primaria:
                        puntos_educacion=puntos_educacion + metrica_primaria[0].porcentaje
                if educacion_secundaria:
                    metrica_secundaria=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado media')
                    if metrica_secundaria:
                        puntos_educacion=puntos_educacion + metrica_secundaria[0].porcentaje                
                    metrica_carrera=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Certificado diversificado')
                    if metrica_carrera:
                        puntos_educacion=puntos_educacion + metrica_carrera[0].porcentaje
                       
                if educacion_universitaria:
                    metrica_universitario=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Titulo universitario')
                    if metrica_universitario:
                        puntos_educacion=puntos_educacion + metrica_universitario[0].porcentaje
                if  educacion_postgrado:                       
                    metrica_postgrado=capacitacion_metrica_educacion_formal.objects.filter(anio=anio,nombre_metrica__icontains='Titulo postgrado')
                    if metrica_postgrado:
                        puntos_educacion=puntos_educacion + metrica_postgrado[0].porcentaje

                x['puntos_educacion']=puntos_educacion
##### fin calculo de puntos pór formacion
### calculo rendimiento capacitaciones
                ########print(x)
                primer_dia=date(int(anio), 1, 1)
                ultimo_dia=date(int(anio), 12, 31)

                nota_rendimiento=0
                campanias=capacitacion_campania.objects.filter(fecha_inicio__gte=primer_dia,fecha_fin__lte=ultimo_dia)
                eventos=capacitacion_evento_capacitacion.objects.filter(campania__in=campanias)
                evento_asistencia_nota=capacitacion_asistencia.objects.filter(evento_capacitacion__in=eventos,empleado__id=x['id']).exclude(evento_capacitacion__nota_aprovatoria=0).aggregate(Avg('nota_evaluacion'))
                evento_asistencia_nota=evento_asistencia_nota['nota_evaluacion__avg'] if evento_asistencia_nota['nota_evaluacion__avg'] else 0
                #######print(evento_asistencia_nota)
                puntos_metrica_capacitacion= capacitacion_metrica_evaluacion_factor.objects.get(anio=anio,valor_minimo__lte=evento_asistencia_nota,valor_maximo__gte=evento_asistencia_nota).porcentaje if capacitacion_metrica_evaluacion_factor.objects.filter(anio=anio,valor_minimo__lte=evento_asistencia_nota,valor_maximo__gte=evento_asistencia_nota) else 0               
                x['puntos_rendimiento_capacitacion']=puntos_metrica_capacitacion
### calculo rendimiento 
                antiguedad=0
                
                if x['antiguedad_laboral']:
                    antiguedad=x['antiguedad_laboral'] / 12
                    antiguedad=round(antiguedad)
                puntos_experiencia=0
                if antiguedad>0:

                    puntos_experiencia=capacitacion_metrica_experiencia_puesto.objects.get(anio=anio,de__lte=antiguedad,hasta__gte=antiguedad).porcentaje if capacitacion_metrica_experiencia_puesto.objects.filter(anio=anio,de__lte=antiguedad,hasta__gte=antiguedad) else 0
                    if puntos_educacion:
                        pass
                    else:
                        puntos_experiencia =0

                x['puntos_experiencia']=puntos_experiencia

                puntos_total= puntos_educacion + puntos_metrica_capacitacion + puntos_experiencia
                x['puntos_total']=puntos_total if puntos_total else 0
                #######print(antiguedad)
                #######print(puntos_total)
                #experiencia = capacitacion_metrica_experiencia_puestoub
                periodicidad=evaluacion_periodicidad.objects.filter(anio=anio)
                evaluaciones= evaluacion_encabezado.objects.filter(periodicidad__in=periodicidad,evaluado__id=x['id'],estado=False).annotate(calificacion=Case(When(tipo_evaluacion_encabezado=2, then=Cast('nota_total_porcentaje',IntegerField())),When(tipo_evaluacion_encabezado=1, then=Cast('nota_total_porcentaje_prorateo',IntegerField())),default=Value(0))).aggregate(Avg('calificacion'))
                x['nota_evaluacion']=evaluaciones['calificacion__avg'] if evaluaciones['calificacion__avg'] else 0

                x['desempenio_percibido']=round((Decimal(puntos_total) + Decimal(x['nota_evaluacion']))/2)


#fin calculo desempeño percibido

#potencial
                #######print(x)
                puntaje_obtenido_competencia_org=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia_ger=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='GERENCIAL',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='GERENCIAL',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia_espe=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ESPECIFICA',encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ESPECIFICA',encabezado__evaluado__id=x['id']) else 0
                puntaje_obtenido_competencia=(detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__in=['ORGANIZACIONAL','GERENCIAL','ESPECIFICA'],encabezado__evaluado__id=x['id']).aggregate(Avg('nota_competencia_prorateada_decimal')))['nota_competencia_prorateada_decimal__avg'] if detalle_evaluacion_competencia.objects.filter(encabezado__periodicidad__in=periodicidad,evaluacion_plantilla_competencia__competencia__competencia__tipo_competencia__descripcion__icontains='ORGANIZACIONAL',encabezado__evaluado__id=x['id']) else 0
                x['puntaje_obtenido_competencia_org']=puntaje_obtenido_competencia_org if puntaje_obtenido_competencia_org else 0
                x['puntaje_obtenido_competencia_espe']=puntaje_obtenido_competencia_espe if puntaje_obtenido_competencia_espe else 0
                x['puntaje_obtenido_competencia_ger']=puntaje_obtenido_competencia_ger if puntaje_obtenido_competencia_ger else 0
                x['potencial']=puntaje_obtenido_competencia if puntaje_obtenido_competencia else 0

                desempenio_posicion_x=capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['desempenio_percibido'],valor_maximo__gte=x['desempenio_percibido'],tipo_criterio=2).first().cordenada if capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['desempenio_percibido'],valor_maximo__gte=x['desempenio_percibido'],tipo_criterio=2).count()>0 else None
                potencial_posicion_y=capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['potencial'],valor_maximo__gte=x['potencial'],tipo_criterio=1).first().cordenada if capacitacion_metrica_9_cajas.objects.filter(anio=anio,valor_minimo__lte=x['potencial'],valor_maximo__gte=x['potencial'],tipo_criterio=1).count()>0 else None
                caja=capacitacion_matriz_9_cajas.objects.get(x=desempenio_posicion_x,y=potencial_posicion_y,anio=anio).id if capacitacion_matriz_9_cajas.objects.filter(x=desempenio_posicion_x,y=potencial_posicion_y,anio=anio) else None
               

                #######print(desempenio_posicion_x)
                #######print(potencial_posicion_y)
                #######print(caja)
                x['caja']=caja
                funciones=list(Funcional_empleado.objects.get(id=x['id']).posicion.all().values('id','descripcion')) if Funcional_empleado.objects.filter(id=x['id']) else None
                division = list(Funcional_Division_Personal.objects.filter(id=x['division_personal_id']).values()) 
                departamento = list(Funcional_empleado.objects.get(id=x['id']).unidad_organizativa.all().values('id','nombre')) if Funcional_empleado.objects.filter(id=x['id']) else None
                empresa = list(Funcional_empleado.objects.get(id=x['id']).unidad_organizativa.all().values('sociedad_financiera__id','sociedad_financiera__nombre')) if Funcional_empleado.objects.filter(id=x['id']) else None
                
                ######print(x)
               
                x['Funcion_List']=funciones
                x['division_List']=division
                x['departamento']=departamento
                x['empresa']=empresa
                potencial_promedio=potencial_promedio +  x['potencial']
                desempenio_promedio=desempenio_promedio + x['desempenio_percibido']
            cajas_correspondientes = capacitacion_matriz_9_cajas.objects.filter(anio=anio).values() if capacitacion_matriz_9_cajas.objects.filter(anio=anio) else None
            potencial_promedio=Decimal(potencial_promedio / contador).quantize(0, ROUND_HALF_UP) if contador > 0 else potencial_promedio
            desempenio_promedio=Decimal(desempenio_promedio /contador).quantize(0, ROUND_HALF_UP) if contador > 0 else desempenio_promedio

            cajas_correspondientes = capacitacion_matriz_9_cajas.objects.filter(anio=anio).values() if capacitacion_matriz_9_cajas.objects.filter(anio=anio) else None
            if cajas_correspondientes ==None:
                return Response({"resultado":"no existen cajas registradas para los parametros de busqueda, año:" + anio},status= status.HTTP_400_BAD_REQUEST)           
            if cajas_correspondientes:
                for caja  in cajas_correspondientes:
                    empleados_list=[]
                    for emp in empleados:
                        if emp['caja']==caja['id']:
                            ######print('entro')
                            empleados_list.append(emp)
                    caja['empleados']=empleados_list
            else:
                return Response({"resultado":"no existen cajas registradas para los parametros de busqueda"},status= status.HTTP_404_NOT_FOUND)

            return Response({"resultado":cajas_correspondientes,"potencial_promedio":potencial_promedio,"desempenio_promedio":desempenio_promedio},status= status.HTTP_200_OK)
        else:
            pass


        # resultado=capacitacion_matriz_9_cajas.objects.filter(id__in=ids)
        # #######print(ids)
        # #######print(resultado)
        # serializer_resultado=capacitacion_matriz_9_cajaserializer(resultado,many = True )

        ########print(serializer_resultado)
        return Response({"resultado":1},status= status.HTTP_200_OK)
        #return Response({"resultado":"No se puede verificar el contenido el detalle de la carpeta"},status= status.HTTP_404_NOT_FOUND)

class monitor_capacitacionesViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = capacitacion_evento_capacitacion.objects.all()
    serializer_class = capacitacion_evento_capacitacionserializer
    def list(self, request):
        queryset = capacitacion_evento_capacitacion.objects.all()
        serializer_class = capacitacion_evento_capacitacionserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        evento_id=''
        campania_id=''

        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')

        if filter=='':
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
        
        ######################################
        # if self.request.query_params.get('evento_id'):
        #         evento_id = self.request.query_params.get('evento_id')

        if self.request.query_params.get('campania_id'):
            campania_id = self.request.query_params.get('campania_id')

        if campania_id!='':
            evento_id = capacitacion_evento_capacitacion.objects.filter(campania_id=campania_id).filter(capacitacion_asistencia__empleado__id=filter).values_list('id',flat=True)

        # print('evento_idasasas',evento_id)
          

        if evento_id=='':
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
        ######################################
        
        data_x=[]
        
        eventos=capacitacion_evento_capacitacion.objects.filter(capacitacion_asistencia__empleado__id=filter,id__in=evento_id).values_list('fecha_inicio','duracion_horas','responsable__nombre','capacitacion_asistencia__nota_evaluacion','capacitacion_asistencia__estado__descripcion','capacitacion_asistencia__asistio','campania__codigo_campania','campania__nombre_campania','id','capacitacion_asistencia__id','capacitacion_asistencia__archivo','nota_aprovatoria','capacitacion_asistencia__estado__id','campania__id')
        
        for fecha_inicio,duracion_horas,responsable,nota_evaluacion,estado,asitio,codigo,nombre,evento_id,capacitacion_asistencia__id,archivo_id,nota_aprovatoria,estado_id,campania_id in eventos:
            data={}
            
            data['nota_aprovatoria']=nota_aprovatoria
            data['capacitacion_asistencia_id']=capacitacion_asistencia__id
            data['fecha_inicio']=fecha_inicio
            data['duracion_horas']=duracion_horas
            data['responsable']=responsable
            data['calificacion']=nota_evaluacion
            data['estado']=estado
            data['asitio']=asitio
            data['codigo']=codigo
            ##################################
            data['estado_id']=estado_id
            estado_querys=capacitacion_estado.objects.filter(id=estado_id) 
            serializer_estadoo= capacitacion_estadoserializer(estado_querys, many=True)
            data['detalle_estado']=serializer_estadoo.data
            ##################################
            archivo_obj=capacitacion_archivo_gestor.objects.filter(id=archivo_id)
            serializer_archivo= capacitacion_archivo_gestorserializer(archivo_obj, many=True)
            data['archivo_id']=archivo_id
            data['list_archivo']=serializer_archivo.data
            ##################################
            ##################################
            campania_capa=capacitacion_campania.objects.filter(id=campania_id)
            serializer_campania_capa=capacitacion_campaniaserializer(campania_capa, many=True)
            data['campania_id']=campania_id
            data['serializer_campania_capa']=serializer_campania_capa.data
            ##################################
            empleado_obj=Funcional_empleado.objects.filter(id=filter) 
            serializer_empleado= Funcional_empleadoserializer(empleado_obj, many=True)
            data['list_empleado']=serializer_empleado.data
            ##################################
            data['nombre']=nombre
            evento_obj= capacitacion_evento_capacitacion.objects.filter(id=evento_id)
            serializer_evento = capacitacion_evento_capacitacionserializer(evento_obj, many=True)
            data['detalle_evento']=serializer_evento.data
            data_x.append(data)
            
        return Response({"data":data_x,"count":len(data_x)})

    def update(self,requets,pk=None):
        id=pk
        nota_aprovatoria=None
        nota_evaluacion=None
        estado_nota=''
        # print('requets.data',requets.data)
        filter=requets.data['filter']
        evento_id=requets.data['evento_id']
        campania_id_x=(capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('campania__id'))[0]['campania__id'] if capacitacion_evento_capacitacion.objects.filter(id=evento_id).values('campania__id') else None
        eventos_ids=  capacitacion_evento_capacitacion.objects.filter(campania_id=campania_id_x).filter(capacitacion_asistencia__empleado__id=filter).values_list('id',flat=True)

        if evento_id==None:
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)

        if filter==None:
            return Response({"La información enviada no es valida"}, status=status.HTTP_400_BAD_REQUEST)
        
        existe= capacitacion_asistencia.objects.filter(id=id).count()
        if existe!=0:
            
            put = capacitacion_asistencia.objects.get(id=id)

            serializer= capacitacion_asistenciaserializer(put,data=requets.data)
            if serializer.is_valid():
                serializer.save()
                ################################estado dependiendo de la nota
                nota_evaluacion = float(serializer.data['nota_evaluacion'] )
            
                if nota_evaluacion!=None:
                
            
                    nota_aprovatoria= (capacitacion_asistencia.objects.filter(id=id).values('evento_capacitacion__nota_aprovatoria'))[0]['evento_capacitacion__nota_aprovatoria'] if capacitacion_asistencia.objects.filter(id=id).values('evento_capacitacion__nota_aprovatoria') else None
                    ######print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',nota_aprovatoria)
                    ######print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',nota_evaluacion)
                    if nota_aprovatoria!=None and int(nota_evaluacion) >= int(nota_aprovatoria):
                        estado_nota=(capacitacion_estado.objects.filter(descripcion='Aprobado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Aprobado').values('id') else None
                    
                    if nota_aprovatoria!=None and int(nota_evaluacion) <= int(nota_aprovatoria):
                        estado_nota=(capacitacion_estado.objects.filter(descripcion='Reprobado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Reprobado').values('id') else None

                    # estado_nota=(capacitacion_estado.objects.filter(descripcion='Pendiente').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Pendiente').values('id') else None
                    if estado_nota!='':   
                        capacitacion_asistencia.objects.filter(id=id).update(estado=estado_nota)
            
                #############################################################

                data_x=[]
        
                eventos=capacitacion_evento_capacitacion.objects.filter(capacitacion_asistencia__empleado__id=filter,id__in=eventos_ids).values_list('fecha_inicio','duracion_horas','responsable__nombre','capacitacion_asistencia__nota_evaluacion','capacitacion_asistencia__estado__descripcion','capacitacion_asistencia__asistio','campania__codigo_campania','campania__nombre_campania','id','capacitacion_asistencia__id','capacitacion_asistencia__archivo','nota_aprovatoria','capacitacion_asistencia__estado__id')
                
                for fecha_inicio,duracion_horas,responsable,nota_evaluacion,estado,asitio,codigo,nombre,evento_id,capacitacion_asistencia__id,archivo_id,nota_aprovatoria,estado_id in eventos:
                    data={}
                    
                    data['nota_aprovatoria']=nota_aprovatoria
                    data['capacitacion_asistencia_id']=capacitacion_asistencia__id
                    data['fecha_inicio']=fecha_inicio
                    data['duracion_horas']=duracion_horas
                    data['responsable']=responsable
                    data['calificacion']=nota_evaluacion
                    data['estado']=estado
                    data['asitio']=asitio
                    data['codigo']=codigo
                    ##################################
                    data['estado_id']=estado_id
                    estado_querys=capacitacion_estado.objects.filter(id=estado_id) 
                    serializer_estadoo= capacitacion_estadoserializer(estado_querys, many=True)
                    data['detalle_estado']=serializer_estadoo.data
                    ##################################
                    archivo_obj=capacitacion_archivo_gestor.objects.filter(id=archivo_id)
                    serializer_archivo= capacitacion_archivo_gestorserializer(archivo_obj, many=True)
                    data['archivo_id']=archivo_id
                    data['list_archivo']=serializer_archivo.data
                    ##################################
                    empleado_obj=Funcional_empleado.objects.filter(id=filter) 
                    serializer_empleado= Funcional_empleadoserializer(empleado_obj, many=True)
                    data['list_empleado']=serializer_empleado.data
                    ##################################
                    ##################################
                    if campania_id_x!=None:
                        campania_capa=capacitacion_campania.objects.filter(id=campania_id_x)
                        serializer_campania_capa=capacitacion_campaniaserializer(campania_capa, many=True)
                        data['campania_id']=campania_id_x
                        data['serializer_campania_capa']=serializer_campania_capa.data
                    else:
                        data['campania_id']=None
                        data['serializer_campania_capa']=None

                    ##################################
                    ################################
                    data['nombre']=nombre
                    evento_obj= capacitacion_evento_capacitacion.objects.filter(id=evento_id)
                    serializer_evento = capacitacion_evento_capacitacionserializer(evento_obj, many=True)
                    data['detalle_evento']=serializer_evento.data
                    data_x.append(data)
                    
                return Response({"data":data_x,"count":len(data_x)})
            else:
                return Response ({"La información enviada no es valida":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
 

class capacitacion_archivo_gestor_formatos(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = capacitacion_archivo_gestor.objects.none()
    def post(self,request):
        url =  settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CrearDocumento'
        fecha=''
        hoy=datetime.now().date()
       #########print('entro')
        myobj = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado']}

        x = requests.post(url, data = myobj)
        response_dict = x.json()

        #######print('response_dict',response_dict)
        
        if len(response_dict)>0:
           #########print(response_dict)
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CrearDocumento'
            fecha= hoy.strftime("%Y%m%d")
            
            llave = (str(self.request.data['empresa']) +'-'+ str(self.request.data['division'])+'-'+str(self.request.data['tipo_documento'] )+'-'+str(self.request.data['descripcion']) +'-'+str(self.request.data['codigo_empleado']) +'-'+str(fecha) ).upper()
        
            objeto = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado'],'llave':llave,'origen':self.request.data['origen'],'documento':self.request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}
            x = requests.post(enlace, data = objeto)
            # #######print("resultado",settings.EMAIL_GESTOR_DOCCUMENTAL)
            
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


            docx= capacitacion_archivo_gestor.objects.create(id_documento=id_gestor, llave=llave,id_area=self.request.data['id_area'],id_carpeta_encabezado=self.request.data['id_carpeta_encabezado'],empresa=self.request.data['empresa'],tipo_documento=self.request.data['tipo_documento'],origen=self.request.data['origen'],extension=self.request.data['extension'],contentTypeGD=self.request.data['contentTypeGD'],nombre=self.request.data['nombre'],descripcion=self.request.data['descripcion'],division=self.request.data['division'],codigo_empleado=self.request.data['codigo_empleado'])
            # doc= evaluacion_archivo_plan_accion(id_documento=id_gestor, llave=llave,id_area=self.request.data['id_area'],id_carpeta_encabezado=self.request.data['id_carpeta_encabezado'],empresa=self.request.data['empresa'],tipo_documento=self.request.data['tipo_documento'],origen=self.request.data['origen'],extension=self.request.data['extension'],contentTypeGD=self.request.data['contentTypeGD'],nombre=self.request.data['nombre'],descripcion=self.request.data['descripcion'],division=self.request.data['division'],codigo_empleado=self.request.data['codigo_empleado'])
            
            return Response({"resultado": capacitacion_archivo_gestorserializer(docx).data},status= status.HTTP_200_OK)
        else:
            return Response({"resultado":"No se puede verificar el contenido el detalle de la carpeta"},status= status.HTTP_404_NOT_FOUND) 

    def get_object(self, pk):
        try:
            return capacitacion_archivo_gestor.objects.get(pk=pk)
        except capacitacion_archivo_gestor.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        #######print(post.id_documento)
        serializer = capacitacion_archivo_gestorserializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/ModificarDocumento'
            objeto = {'id':post.id_documento,'ceid':post.id_carpeta_encabezado,'llave':str(post.llave).upper(),'origen':post.origen,'documento':request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}            
            x = requests.post(enlace, data = objeto)
            resultado = x.json()
            #######print('objeto',objeto)
            #######print('X',x)
            #######print('resultadoresultado',resultado)
            

            # for result in resultado:
            #    ########print('resultado',result)
            #     if result['response'].find('Modificado Correctamente')==-1:
            #         return Response({"resultado":result['response']},status= status.HTTP_404_NOT_FOUND)
            if x.status_code==200:
                return Response(serializer.data)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        existe= capacitacion_archivo_gestor.objects.filter(id=pk).count()
        if existe!=0:
            get = self.get_object(pk)
            #get =  on_off_bording_bienvenida.objects.filter(id=id) if on_off_bording_bienvenida.objects.filter(id=id) else None 
            serializer=capacitacion_archivo_gestorserializer(get)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class capacitacion_archivo_gestor_formatos_gestorViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = capacitacion_archivo_gestor.objects.all()
    serializer_class = capacitacion_archivo_gestorserializer
    def list(self, request):
        queryset = capacitacion_archivo_gestor.objects.all()
        serializer_class = capacitacion_archivo_gestorserializer(queryset, many=True)
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
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='empresa':
                        filter_kwargs['empresa__icontains'] = filter
                    if tipo_busqueda =='zona':
                        filter_kwargs['zona__icontains'] = filter
                    if tipo_busqueda =='id_area':
                        filter_kwargs['id_area'] = filter
                    if tipo_busqueda =='id_carpeta_encabezado':
                        filter_kwargs['id_carpeta_encabezado'] = filter
                    if tipo_busqueda =='formatos':
                        filter_kwargs['formatos__icontains'] = filter
                    if tipo_busqueda =='origen':
                        filter_kwargs['origen__icontains'] = filter
                    if tipo_busqueda =='extension':
                        filter_kwargs['extension__icontains'] = filter
                    if tipo_busqueda =='id_documento':
                        filter_kwargs['id_documento'] = filter
                    if tipo_busqueda =='llave':
                        filter_kwargs['llave__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__icontains'] = filter
                    if tipo_busqueda =='contentTypeGD':
                        filter_kwargs['contentTypeGD__icontains'] = filter
        
                queryset =  capacitacion_archivo_gestor.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  capacitacion_archivo_gestor.objects.filter(**filter_kwargs).count()
                # asistencia_total=capacitacion_archivo_gestor.objects.filter(**filter_kwargs).filter(asistio=True).count()
                # inasistencia_total=capacitacion_archivo_gestor.objects.filter(**filter_kwargs).filter(asistio=False).count()
                serializer = capacitacion_archivo_gestorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_archivo_gestor.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  capacitacion_archivo_gestor.objects.filter().count()
                # asistencia_total=capacitacion_archivo_gestor.objects.filter().filter(asistio=True).count()
                # inasistencia_total=capacitacion_archivo_gestor.objects.filter().filter(asistio=False).count()
                serializer = capacitacion_archivo_gestorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='empresa':
                        filter_kwargs['empresa__icontains'] = filter
                    if tipo_busqueda =='zona':
                        filter_kwargs['zona__icontains'] = filter
                    if tipo_busqueda =='id_area':
                        filter_kwargs['id_area'] = filter
                    if tipo_busqueda =='id_carpeta_encabezado':
                        filter_kwargs['id_carpeta_encabezado'] = filter
                    if tipo_busqueda =='formatos':
                        filter_kwargs['formatos__icontains'] = filter
                    if tipo_busqueda =='origen':
                        filter_kwargs['origen__icontains'] = filter
                    if tipo_busqueda =='extension':
                        filter_kwargs['extension__icontains'] = filter
                    if tipo_busqueda =='id_documento':
                        filter_kwargs['id_documento'] = filter
                    if tipo_busqueda =='llave':
                        filter_kwargs['llave__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__icontains'] = filter
                    if tipo_busqueda =='contentTypeGD':
                        filter_kwargs['contentTypeGD__icontains'] = filter
                    

                        
                queryset =  capacitacion_archivo_gestor.objects.filter(**filter_kwargs).order_by('id')
                conteo =  capacitacion_archivo_gestor.objects.filter(**filter_kwargs).count()
                # asistencia_total=capacitacion_archivo_gestor.objects.filter(**filter_kwargs).filter(asistio=True).count()
                # inasistencia_total=capacitacion_archivo_gestor.objects.filter(**filter_kwargs).filter(asistio=False).count()
                serializer = capacitacion_archivo_gestorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  capacitacion_archivo_gestor.objects.filter().order_by('id')
                conteo =  capacitacion_archivo_gestor.objects.filter().count()
                # asistencia_total=capacitacion_archivo_gestor.objects.filter().filter(asistio=True).count()
                # inasistencia_total=capacitacion_archivo_gestor.objects.filter().filter(asistio=False).count()
                serializer = capacitacion_archivo_gestorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})



class correo_capacitaciones(APIView):
    authentication_classes=[TokenAuthentication]

    def post(self,request):
        notificaciones = self.request.data['data']
        id=''
        tipo_mensaje=''
        fun=''
        codigo_empleado=''
        evento_id=''
        
        
        for variable in notificaciones:
            
            
            if "evento_id" in variable:
                evento_id = variable['evento_id']
            
            if "tipo_mensaje" in variable:
                tipo_mensaje = variable['tipo_mensaje']
            
            if "codigo_empleado" in variable:
                codigo_empleado = variable['codigo_empleado']
                
            if evento_id!='' and tipo_mensaje!='' and codigo_empleado!='':
                fun = funcion_envio_correo(tipo_mensaje,evento_id,codigo_empleado)

            else:
                return Response({"mensaje":"No hemos recibido los valores completos"},status= status.HTTP_404_NOT_FOUND)

         
   
        return Response ({"mensaje":fun},status= status.HTTP_200_OK)



def funcion_envio_correo(tipo_mensaje,id,codigo_empleado):
    modulo='CAPACITACION'
    correo_colaborador=None
    if tipo_mensaje == 'convocado a capacitacion':
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            #######print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #######print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    ######print('valores',valores)
                    modelo_tb= apps.get_model(app,modelos)
                    valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir
                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                    else:
                        valor_a_sustituir_str =''
                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        
                
                correo_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('correo_empresarial') else None
                
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    # correo_a_enviar='hoscar161@gmail.com'
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            # notificacion=notificacion_aurora.objects.create(destinatario=encabezado.evaluado,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'inasistencia Colaborador:Empleado':
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            #######print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #######print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    ######print('valores',valores)
                    modelo_tb= apps.get_model(app,modelos)
                    valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                    if variable=='@@nombrecolaborador':
                        nombre_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre') else None
                        if nombre_colaborador!= None:
                            # nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                            valor_a_sustituir=nombre_colaborador
                            #######print('4')
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
                    elif variable=='@@codigocolaborador':
                        nombre_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('codigo'))[0]['codigo'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('codigo') else None
                        if nombre_colaborador!= None:
                            # nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                            valor_a_sustituir=nombre_colaborador
                            #######print('4')
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
                    elif variable=='@@motivoinasistencia':
                    # jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                        motivo=(capacitacion_asistencia.objects.filter(evento_capacitacion=id,empleado__codigo=codigo_empleado).values('motivo_inasistencia__descripcion'))[0]['motivo_inasistencia__descripcion'] if capacitacion_asistencia.objects.filter(evento_capacitacion=id,empleado__codigo=codigo_empleado).values('motivo_inasistencia__descripcion') else None
                        
                        if motivo!=None:
                            valor_a_sustituir=motivo
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                        else:
                            
                            return Response({"mensaje":"No se encontro la función del jefe"},status= status.HTTP_404_NOT_FOUND)
        
                
                    
                    else:
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                    
                        
                
                correo_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('correo_empresarial') else None
                
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    # correo_a_enviar='hoscar161@gmail.com'
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            # notificacion=notificacion_aurora.objects.create(destinatario=encabezado.evaluado,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'inasistencia Colaborador:Jefe':
        ######print('1111111111111111111111111111111')
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            ######print('222222222222222222222222222222')
            #######print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #######print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    ######print('valores',valores)
                    modelo_tb= apps.get_model(app,modelos)
                    valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                    if variable=='@@jefe':
                        codigo_jefe = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato') else None
                        #######print('3')
                        if codigo_jefe!=None:
                            #######print('x')
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                                    valor_a_sustituir=nombre
                                    #######print('4')
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
                    if variable=='@@nombrecolaborador':
                        nombre_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre') else None
                        if nombre_colaborador!= None:
                            # nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                            valor_a_sustituir=nombre_colaborador
                            #######print('4')
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
                    elif variable=='@@nombrefuncion':
                        # jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                        
                        funcion = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values("posicion__descripcion"))[0]['posicion__descripcion'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values("posicion__descripcion") else None
                        if funcion!=None:
                            valor_a_sustituir=funcion
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                        else:
                            
                            return Response({"mensaje":"No se encontro la función del jefe"},status= status.HTTP_404_NOT_FOUND)
                    elif variable=='@@codigocolaborador':
                        nombre_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('codigo'))[0]['codigo'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('codigo') else None
                        if nombre_colaborador!= None:
                            # nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                            valor_a_sustituir=nombre_colaborador
                            #######print('4')
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
                    
                    elif variable=='@@motivoinasistencia':
                    # jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                        motivo=(capacitacion_asistencia.objects.filter(evento_capacitacion=id,empleado__codigo=codigo_empleado).values('motivo_inasistencia__descripcion'))[0]['motivo_inasistencia__descripcion'] if capacitacion_asistencia.objects.filter(evento_capacitacion=id,empleado__codigo=codigo_empleado).values('motivo_inasistencia__descripcion') else None
                        
                        if motivo!=None:
                            valor_a_sustituir=motivo
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                        else:
                            
                            return Response({"mensaje":"No se encontro la función del jefe"},status= status.HTTP_404_NOT_FOUND)
        
                
                    else:
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        
                
                codigo_jefe = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato') else None
                
                correo_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial') else None
                ######print('3333333333333333',correo_colaborador)
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    # correo_a_enviar='hoscar161@gmail.com'
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            # documento=achivo_capacitacion_F439(id)
                            # direccion=str((documento.split('/AuroraHeadCountBackEnd/'))[1])
                            # ######print('direccion',direccion[1])
                            # msg_jefe.attach_file(direccion)
                            msg_jefe.send()
                            # notificacion=notificacion_aurora.objects.create(destinatario=encabezado.evaluado,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'evaluación capacitacion:jefe':
        ######print('1111111111111111111111111111111')
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            ######print('222222222222222222222222222222')
            #######print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #######print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    ######print('valores',valores)
                    modelo_tb= apps.get_model(app,modelos)
                    valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                    if variable=='@@jefe':
                        codigo_jefe = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato') else None
                        #######print('3')
                        if codigo_jefe!=None:
                            #######print('x')
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                                    valor_a_sustituir=nombre
                                    #######print('4')
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
                    elif variable=='@@nombrecolaborador':
                        nombre_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre') else None
                        if nombre_colaborador!= None:
                            # nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                            valor_a_sustituir=nombre_colaborador
                            #######print('4')
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
                    elif variable=='@@nombrefuncion':
                        # jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                        
                        funcion = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values("posicion__descripcion"))[0]['posicion__descripcion'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values("posicion__descripcion") else None
                        if funcion!=None:
                            valor_a_sustituir=funcion
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                        else:
                            
                            return Response({"mensaje":"No se encontro la función del jefe"},status= status.HTTP_404_NOT_FOUND)
                    elif variable=='@@codigocolaborador':
                        nombre_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('codigo'))[0]['codigo'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('codigo') else None
                        if nombre_colaborador!= None:
                            # nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                            valor_a_sustituir=nombre_colaborador
                            #######print('4')
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
                    elif variable=='@@codigofuncion':
                        # jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                        
                        funcion = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values("posicion__codigo"))[0]['posicion__codigo'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values("posicion__codigo") else None
                        if funcion!=None:
                            valor_a_sustituir=funcion
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                        else:
                            
                            return Response({"mensaje":"No se encontro la función del jefe"},status= status.HTTP_404_NOT_FOUND)
 
                    else:
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        
                
                codigo_jefe = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato'))[0]['jefe_inmediato'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('jefe_inmediato') else None
                
                correo_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial') else None
                ######print('3333333333333333',correo_colaborador)
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    # correo_a_enviar='hoscar161@gmail.com'
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            documento=achivo_capacitacion_F439(id)
                            direccion_archivo= str(settings.STATICFILES_DIRS[0]) + str('/capacitacion_evaluacion/formato_F-439v2.xls')
                        
                            ######print('direccion',direccion[1])
                            msg_jefe.attach_file(direccion_archivo)
                            msg_jefe.send()
                            # notificacion=notificacion_aurora.objects.create(destinatario=encabezado.evaluado,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Comienzo Ruta de Aprendizaje':
        
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            #######print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #######print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    ######print('valores',valores)
                    modelo_tb= apps.get_model(app,modelos)
                    valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                    if variable=='@@nombrecolaborador':
                        nombre_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre') else None
                        if nombre_colaborador!= None:
                            # nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                            valor_a_sustituir=nombre_colaborador
                            #######print('4')
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
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                       
                
                correo_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('correo_empresarial') else None
                
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    # correo_a_enviar='hoscar161@gmail.com'
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            # notificacion=notificacion_aurora.objects.create(destinatario=encabezado.evaluado,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Fin Ruta de Aprendizaje':
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        if configuracion_correo:
            #######print('2')
            asunto=configuracion_correo[0]['asunto']
            mensaje=configuracion_correo[0]['mensaje']
            variables_envio_correo= nucleo_variables_envio_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
            if variables_envio_correo:
                #######print('variables_envio_correo')
                for vec in variables_envio_correo:
                    variable= vec.variable
                    app= vec.app
                    modelos= vec.modelos
                    valores= vec.valores
                    ######print('valores',valores)
                    modelo_tb= apps.get_model(app,modelos)
                    valor_a_sustituir=list((modelo_tb.objects.filter(id=id).values(valores)[0]).values())[0]
                    if variable=='@@nombrecolaborador':
                        nombre_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('nombre') else None
                        if nombre_colaborador!= None:
                            # nombre=(Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0]['nombre'] if Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre') else None
                            valor_a_sustituir=nombre_colaborador
                            #######print('4')
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
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                       
                
                correo_colaborador = (Funcional_empleado.objects.filter(codigo=codigo_empleado).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=codigo_empleado).values('correo_empresarial') else None
                
                if correo_colaborador!=None:
                    correo_a_enviar=correo_colaborador
                    # correo_a_enviar='hoscar161@gmail.com'
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            # notificacion=notificacion_aurora.objects.create(destinatario=encabezado.evaluado,asunto=asunto,mensaje=mensaje)
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
                  

    return 'Proceso Exitoso'
