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
# from rest_framework.views import APIView
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
from base64 import b64decode
from django.core.files.base import ContentFile
import base64
from django.db.models import Value




class seleccion_contratacion_plaza_vacantesViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_Puesto.objects.all()
    serializer_class = funcional_puestoserializer
    def list(self, request):
        queryset = Funcional_Puesto.objects.all()
        serializer = funcional_puestoserializer(queryset, many=True)
        unidad_organizativa=''
        plazas_vacantes=''
        usuario = request.user
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        uni_org=Funcional_empleado.objects.filter(codigo=usuario).values('unidad_organizativa__codigo') if Funcional_empleado.objects.filter(codigo=usuario) else None
        unidad_organizativa=uni_org[0]['unidad_organizativa__codigo']
        lista_puesto=''
        if 'jefe' in grupos:
            listado_puestos= puestos_vacantes(usuario)
            lista_puestos= listado_puestos['plazas_vacantes']
        # print('Funcion puesto',lista_puesto)
        tipo_busqueda=''
        filter=''

        
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        ############################################################################### 
        
        if 'jefe' in grupos:
            
            if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))
                
                if filter!='' and tipo_busqueda!='':
                    
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='descripcion':
                            filter_kwargs['descripcion__icontains'] = filter
                        if tipo_busqueda =='codigo':
                            filter_kwargs['codigo'] = filter
                        if tipo_busqueda =='id':
                            filter_kwargs['id'] = filter
                    
                    # plazas_vacantes=Funcional_Puesto.objects.filter(codigo=unidad_organizativa).filter(funcional_puesto__funcional_empleado=None).values_list('funcional_puesto__codigo',flat=True)
                    

                    queryset =  Funcional_Puesto.objects.filter(**filter_kwargs).filter(codigo__in=lista_puestos).order_by('id')[offset:offset+limit]
                    conteo =  Funcional_Puesto.objects.filter(**filter_kwargs).filter(codigo__in=lista_puestos).count()
                    serializer = funcional_puestoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
                else:
                    # plazas_vacantes=Funcional_Unidad_Organizativa.objects.filter(codigo=unidad_organizativa).filter(funcional_puesto__funcional_empleado=None).values_list('funcional_puesto__codigo',flat=True)
                    
                    queryset =  Funcional_Puesto.objects.filter(codigo__in=lista_puestos).order_by('id')[offset:offset+limit]
                    conteo =  Funcional_Puesto.objects.filter(codigo__in=lista_puestos).count()
                    serializer = funcional_puestoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
            else:
                
                if filter!='' and tipo_busqueda:
                    
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='descripcion':
                            filter_kwargs['descripcion__icontains'] = filter
                        if tipo_busqueda =='codigo':
                            filter_kwargs['codigo'] = filter
                        if tipo_busqueda =='id':
                            filter_kwargs['id'] = filter

                        
            
                    # plazas_vacantes=Funcional_Unidad_Organizativa.objects.filter(codigo__in=unidad_organizativa).filter(funcional_puesto__funcional_empleado=None).values_list('funcional_puesto__codigo',flat=True)
                    queryset =  Funcional_Puesto.objects.filter(**filter_kwargs).filter(codigo__in=lista_puestos).order_by('id')
                    conteo=Funcional_Puesto.objects.filter(**filter_kwargs).filter(codigo__in=lista_puestos).count()
                    serializer = funcional_puestoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                    
                else:
                    
                    # plazas_vacantes=Funcional_Unidad_Organizativa.objects.filter(codigo__in=unidad_organizativa).filter(funcional_puesto__funcional_empleado=None).values_list('funcional_puesto__codigo',flat=True)
                    queryset =  Funcional_Puesto.objects.filter(codigo__in=lista_puestos).order_by('id')
                    serializer = funcional_puestoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
        
        else:
            if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))
                
                if filter!='' and tipo_busqueda!='':
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='descripcion':
                            filter_kwargs['descripcion__icontains'] = filter
                        if tipo_busqueda =='codigo':
                            filter_kwargs['codigo'] = filter
                        if tipo_busqueda =='id':
                            filter_kwargs['id'] = filter

                    plazas_vacantes=[]
                    puestos_vacios= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).values_list('codigo',flat=True)
                    # empleados_dados_baja= Funcional_empleado.objects.filter(fecha_baja__lt=datetime.now().date()).values_list('puesto__codigo',flat=True)
                    plazas_vacantes.extend(puestos_vacios)
                    # plazas_vacantes.extend(empleados_dados_baja)

                    # plazas_vacantes=[]
                    # plazas_vacantes.extend(Funcional_Unidad_Organizativa.objects.filter(funcional_puesto__funcional_empleado=None).values_list('funcional_puesto__codigo',flat=True))
                    # dados_de_baja=Funcional_empleado.objects.filter(fecha_baja__gt=datetime.now().date()).values_list('puesto__codigo',flat=True) if Funcional_empleado.objects.filter(fecha_baja__gt=datetime.now().date()) else None
                    # if dados_de_baja!=None:
                    #     plazas_vacantes.extend(dados_de_baja)

                    # queryset =  Funcional_Puesto.objects.filter(**filter_kwargs).filter(codigo__in=plazas_vacantes).order_by('id')[offset:offset+limit]
                    queryset = Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).filter(**filter_kwargs).count()
                    serializer = funcional_puestoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
                else:
                    plazas_vacantes=[]
                    puestos_vacios= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).values_list('codigo',flat=True)
                    # empleados_dados_baja= Funcional_empleado.objects.filter(fecha_baja__lt=datetime.now().date()).values_list('puesto__codigo',flat=True)
                    plazas_vacantes.extend(puestos_vacios)
                    # plazas_vacantes.extend(empleados_dados_baja)

                    # queryset =  Funcional_Puesto.objects.filter(codigo__in=plazas_vacantes).order_by('id')[offset:offset+limit]
                    queryset= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).order_by('id')[offset:offset+limit]
                    conteo =  Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).count()
                    serializer = funcional_puestoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
             
            else:
                if filter!='' and tipo_busqueda:
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='descripcion':
                            filter_kwargs['descripcion__icontains'] = filter
                        if tipo_busqueda =='codigo':
                            filter_kwargs['codigo'] = filter
                        if tipo_busqueda =='id':
                            filter_kwargs['id'] = filter
                    # plazas_vacantes=[]
                    # plazas_vacantes.extend(Funcional_Unidad_Organizativa.objects.filter(funcional_puesto__funcional_empleado=None).values_list('funcional_puesto__codigo',flat=True))
                    # dados_de_baja=Funcional_empleado.objects.filter(fecha_baja__gt=datetime.now().date()).values_list('puesto__codigo',flat=True) if Funcional_empleado.objects.filter(fecha_baja__gt=datetime.now().date()) else None
                    # if dados_de_baja!=None:
                    #     plazas_vacantes.extend(dados_de_baja)
                
                    plazas_vacantes=[]
                    puestos_vacios= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).values_list('codigo',flat=True)
                    # empleados_dados_baja= Funcional_empleado.objects.filter(fecha_baja__gt=datetime.now().date()).values_list('puesto__codigo',flat=True)
                    plazas_vacantes.extend(puestos_vacios)
                    # plazas_vacantes.extend(empleados_dados_baja)

                    # queryset =  Funcional_Puesto.objects.filter(**filter_kwargs).filter(codigo__in=plazas_vacantes).order_by('id')
                    queryset= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).filter(**filter_kwargs).order_by('id')
                    serializer = funcional_puestoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    # plazas_vacantes=[]
                    # plazas_vacantes.extend(Funcional_Unidad_Organizativa.objects.filter(funcional_puesto__funcional_empleado=None).values_list('funcional_puesto__codigo',flat=True))
                    # dados_de_baja=Funcional_empleado.objects.filter(fecha_baja__gt=datetime.now().date()).values_list('puesto__codigo',flat=True) if Funcional_empleado.objects.filter(fecha_baja__gt=datetime.now().date()) else None
                    # # print(plazas_vacantes)
                    # if dados_de_baja!=None:
                    #     # print()
                    #     plazas_vacantes.extend(dados_de_baja)

                    plazas_vacantes=[]
                    puestos_vacios= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).values_list('codigo',flat=True)
                    # empleados_dados_baja= Funcional_empleado.objects.filter(fecha_baja__gt=datetime.now().date()).values_list('puesto__codigo',flat=True)
                    plazas_vacantes.extend(puestos_vacios)
                    # plazas_vacantes.extend(empleados_dados_baja)

                    queryset =Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).order_by('id')
                    serializer = funcional_puestoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
        
            


class seleccion_contratacion_motivoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = seleccion_contratacion_motivo.objects.all()
    serializer_class = seleccion_contratacion_motivoserializer
    def list(self, request):
        queryset = seleccion_contratacion_motivo.objects.all()
        serializer_class = seleccion_contratacion_motivoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            # print(filter)
            # print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  seleccion_contratacion_motivo.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_motivo.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_motivoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_motivo.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_motivo.objects.filter().count()
                serializer = seleccion_contratacion_motivoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  seleccion_contratacion_motivo.objects.filter(**filter_kwargs).order_by('id')
                conteo =  seleccion_contratacion_motivo.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_motivoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_motivo.objects.filter().order_by('id')
                conteo =  seleccion_contratacion_motivo.objects.filter().count()
                serializer = seleccion_contratacion_motivoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        serializer = seleccion_contratacion_motivoserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            # print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El motivo no ha sido creado "}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        motivo = seleccion_contratacion_motivo.objects.filter(id=pk) if seleccion_contratacion_motivo.objects.filter(id=pk) else None

        if motivo!=None:
            queryset = seleccion_contratacion_motivo.objects.get(id=pk)
            serializer = seleccion_contratacion_motivoserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El motivo no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
  
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('seleccion_contratacion_motivo_id'):
            id = self.request.query_params.get('seleccion_contratacion_motivo_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        motivo = seleccion_contratacion_motivo.objects.filter(id=id).values() if seleccion_contratacion_motivo.objects.filter(id=id) else None

        
        if motivo:
            queryset = seleccion_contratacion_motivo.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El motivo no existe"},status=status.HTTP_404_NOT_FOUND)
 

class seleccion_contratacion_paisViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = seleccion_contratacion_pais.objects.all()
    serializer_class = seleccion_contratacion_paisserializer
    def list(self, request):
        queryset = seleccion_contratacion_pais.objects.all()
        serializer_class = seleccion_contratacion_paisserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            # print(filter)
            # print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre_pais':
                        filter_kwargs['nombre_pais__icontains'] = filter
                    if tipo_busqueda == 'codigo_pais':
                        filter_kwargs['codigo_pais__icontains'] = filter
                    if tipo_busqueda == 'fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  seleccion_contratacion_pais.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_pais.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_paisserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_pais.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_pais.objects.filter().count()
                serializer = seleccion_contratacion_paisserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre_pais':
                        filter_kwargs['nombre_pais__icontains'] = filter
                    if tipo_busqueda == 'codigo_pais':
                        filter_kwargs['codigo_pais__icontains'] = filter
                    if tipo_busqueda == 'fecha_creacion':
                        filter_kwargs['fecha_creacion__date__icontains'] = filter
                        
                queryset =  seleccion_contratacion_pais.objects.filter(**filter_kwargs).order_by('id')
                conteo =  seleccion_contratacion_pais.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_paisserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_pais.objects.filter().order_by('id')
                conteo =  seleccion_contratacion_pais.objects.filter().count()
                serializer = seleccion_contratacion_paisserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        serializer = seleccion_contratacion_paisserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # print(serializer.data)
            # print(request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El pais no ha sido creado "}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        pais = seleccion_contratacion_pais.objects.filter(id=pk) if seleccion_contratacion_pais.objects.filter(id=pk) else None

        if pais!=None:
            queryset = seleccion_contratacion_pais.objects.get(id=pk)
            serializer = seleccion_contratacion_paisserializer(instance=queryset, data=request.data)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El pais no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
 
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('seleccion_contratacion_pais_id'):
            id = self.request.query_params.get('seleccion_contratacion_pais_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        pais = seleccion_contratacion_pais.objects.filter(id=id).values() if seleccion_contratacion_pais.objects.filter(id=id) else None

        
        if pais:
            queryset = seleccion_contratacion_pais.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El pais no existe"},status=status.HTTP_404_NOT_FOUND)
 

class seleccion_contratacion_solicitud_plaza_vacanteViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.all()
    serializer_class = seleccion_contratacion_solicitud_plaza_vacanteserializer
    def list(self, request):
        queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.all()
        serializer_class = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
        filter=''
        filter2=''
        filter_2=''
        division=''
        tipo_busqueda=''
        tipo_busqueda_2=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('filter2'):
                filter2 = self.request.query_params.get('filter2')
        
        if self.request.query_params.get('filter_2'):
                filter_2 = self.request.query_params.get('filter_2')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
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
                    if tipo_busqueda == 'posicion_id':
                        filter_kwargs['posicion'] = filter
                    if tipo_busqueda == 'posicion_descripcion':
                        filter_kwargs['posicion__descripcion__icontains'] = filter
                    if tipo_busqueda == 'pais_id':
                        filter_kwargs['pais'] = filter
                    if tipo_busqueda == 'pais_nombre':
                        filter_kwargs['pais__nombre_pais__icontains'] = filter
                    if tipo_busqueda == 'pais_codigo':
                        filter_kwargs['pais__codigo_pais__icontains'] = filter
                    if tipo_busqueda == 'motivo_descripcion':
                        filter_kwargs['motivo__descripcion__icontains'] = filter
                    if tipo_busqueda == 'motivo_id':
                        filter_kwargs['motivo'] = filter
                    if tipo_busqueda == 'estado_id':
                        filter_kwargs['estado'] = filter
                    if tipo_busqueda == 'estado_nombre':
                        filter_kwargs['estado__nombre_estado__icontains'] = filter
                    if tipo_busqueda == 'fecha_solicitud':
                        filter_kwargs['fecha_solicitud__icontains'] = filter
                    if tipo_busqueda == 'jefe':
                        filter_kwargs['creador_plaza__first_name__icontains'] = filter
                    if tipo_busqueda == 'departamento_id':
                        filter_kwargs['departamento'] = filter
                    if tipo_busqueda == 'departamento_nombre':
                        filter_kwargs['departamento__descripcion__icontains'] = filter

                if tipo_busqueda_2!='' and filter_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 == 'posicion_id':
                            filter_kwargs_2['posicion'] = filter_2
                        if tipo_busqueda_2 == 'posicion_descripcion':
                            filter_kwargs_2['posicion__descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 == 'pais_id':
                            filter_kwargs_2['pais'] = filter_2
                        if tipo_busqueda_2 == 'pais_nombre':
                            filter_kwargs_2['pais__nombre_pais__icontains'] = filter_2
                        if tipo_busqueda_2 == 'pais_codigo':
                            filter_kwargs_2['pais__codigo_pais__icontains'] = filter_2
                        if tipo_busqueda_2 == 'motivo_descripcion':
                            filter_kwargs_2['motivo__descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 == 'motivo_id':
                            filter_kwargs_2['motivo'] = filter_2
                        if tipo_busqueda_2 == 'estado_id':
                            filter_kwargs_2['estado'] = filter_2
                        if tipo_busqueda_2 == 'estado_nombre':
                            filter_kwargs_2['estado__nombre_estado__icontains'] = filter_2
                        if tipo_busqueda_2 == 'fecha_solicitud':
                            filter_kwargs_2['fecha_solicitud__icontains'] = filter_2
                        if tipo_busqueda_2 == 'jefe':
                            filter_kwargs_2['creador_plaza__first_name__icontains'] = filter_2
                        if tipo_busqueda_2 == 'departamento_id':
                            filter_kwargs_2['departamento'] = filter_2
                        if tipo_busqueda_2 == 'departamento_nombre':
                            filter_kwargs_2['departamento__descripcion__icontains'] = filter_2
                    
                    queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs_2).filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =   seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs_2).filter(**filter_kwargs).count()
                    serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs).count()
                    serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
          
                queryset =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter().count()
                serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre_pais':
                        filter_kwargs['nombre_pais__icontains'] = filter
                    if tipo_busqueda == 'codigo_pais':
                        filter_kwargs['codigo_pais__icontains'] = filter
                    if tipo_busqueda == 'posicion_id':
                        filter_kwargs['posicion'] = filter
                    if tipo_busqueda == 'posicion_descripcion':
                        filter_kwargs['posicion__descripcion__icontains'] = filter
                    if tipo_busqueda == 'pais_id':
                        filter_kwargs['pais'] = filter
                    if tipo_busqueda == 'pais_nombre':
                        filter_kwargs['pais__nombre_pais__icontains'] = filter
                    if tipo_busqueda == 'pais_codigo':
                        filter_kwargs['pais__codigo_pais__icontains'] = filter
                    if tipo_busqueda == 'motivo_descripcion':
                        filter_kwargs['motivo__descripcion__icontains'] = filter
                    if tipo_busqueda == 'motivo_id':
                        filter_kwargs['motivo'] = filter
                    if tipo_busqueda == 'estado_id':
                        filter_kwargs['estado'] = filter
                    if tipo_busqueda == 'estado_nombre':
                        filter_kwargs['estado__nombre_estado__icontains'] = filter
                    if tipo_busqueda == 'fecha_solicitud':
                        filter_kwargs['fecha_solicitud__icontains'] = filter
                    if tipo_busqueda == 'jefe':
                        filter_kwargs['creador_plaza__first_name__icontains'] = filter
                    if tipo_busqueda == 'departamento_id':
                        filter_kwargs['departamento'] = filter
                    if tipo_busqueda == 'departamento_nombre':
                        filter_kwargs['departamento__descripcion__icontains'] = filter
                
                if tipo_busqueda_2!='' and filter_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 == 'posicion_id':
                            filter_kwargs_2['posicion'] = filter_2
                        if tipo_busqueda_2 == 'posicion_descripcion':
                            filter_kwargs_2['posicion__descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 == 'pais_id':
                            filter_kwargs_2['pais'] = filter_2
                        if tipo_busqueda_2 == 'pais_nombre':
                            filter_kwargs_2['pais__nombre_pais__icontains'] = filter_2
                        if tipo_busqueda_2 == 'pais_codigo':
                            filter_kwargs_2['pais__codigo_pais__icontains'] = filter_2
                        if tipo_busqueda_2 == 'motivo_descripcion':
                            filter_kwargs_2['motivo__descripcion__icontains'] = filter_2
                        if tipo_busqueda_2 == 'motivo_id':
                            filter_kwargs_2['motivo'] = filter_2
                        if tipo_busqueda_2 == 'estado_id':
                            filter_kwargs_2['estado'] = filter_2
                        if tipo_busqueda_2 == 'estado_nombre':
                            filter_kwargs_2['estado__nombre_estado__icontains'] = filter_2
                        if tipo_busqueda_2 == 'fecha_solicitud':
                            filter_kwargs_2['fecha_solicitud__icontains'] = filter_2
                        if tipo_busqueda_2 == 'jefe':
                            filter_kwargs_2['creador_plaza__first_name__icontains'] = filter_2
                        if tipo_busqueda_2 == 'departamento_id':
                            filter_kwargs_2['departamento'] = filter_2
                        if tipo_busqueda_2 == 'departamento_nombre':
                            filter_kwargs_2['departamento__descripcion__icontains'] = filter_2
                    queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs_2).filter(**filter_kwargs).order_by('id')
                    conteo =   seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs_2).filter(**filter_kwargs).count()
                    serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs).order_by('id')
                    conteo =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs).count()
                    serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})  

                queryset =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs).order_by('id')
                conteo =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter().order_by('id')
                conteo =  seleccion_contratacion_solicitud_plaza_vacante.objects.filter().count()
                serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        nombre_plan_induccion=''
        request.data._mutable = True

        puesto=seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion=self.request.data['posicion']).exclude(estado__nombre_estado="Cerrado") if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion=self.request.data['posicion']).exclude(estado__nombre_estado="Cerrado") else None

        if puesto!=None:
            return Response({"mensaje":"La plaza vacante ya tiene un proceso de contratación"}, status=status.HTTP_400_BAD_REQUEST)


        if 'plan_induccion' in request.data:
            nombre_plan_induccion=self.request.data['plan_induccion']
            request.data['nombre_plan_induccion']= str(nombre_plan_induccion)
        
        request.data['creador_plaza']= request.user.pk
        serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"mensaje":"asd"})
        else:
            return Response({"mensaje":"La solicitud no ha sido creada"}, status=status.HTTP_400_BAD_REQUEST)
   



    def update(self, request, pk=None):
        hoy=datetime.now().date()
        solicitud = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=pk) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=pk) else None
        parametros = self.request.data.copy()
        
        if solicitud!=None:
            queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.get(id=pk)
            
            # request.data._mutable = True
            if 'plan_induccion' in request.data:
                nombre_plan_induccion=self.request.data['plan_induccion']
                if nombre_plan_induccion!=None:
                    request.data['nombre_plan_induccion']= str(nombre_plan_induccion)

            #estado
            if 'estado' in parametros:
                estado= parametros['estado']
                estado_nombre = (seleccion_contratacion_estado.objects.filter(id=estado).values('nombre_estado'))[0]['nombre_estado']
                # print('estado_nombre',estado_nombre)
                if estado_nombre =='En proceso':
                    parametros['fecha_inicio_proceso'] = hoy

            serializer = seleccion_contratacion_solicitud_plaza_vacanteserializer(instance=queryset, data=parametros)
           
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"La solicitud no ha sido encontrada"},status=status.HTTP_404_NOT_FOUND)
  
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('seleccion_contratacion_solicitud_plaza_vacante_id'):
            id = self.request.query_params.get('seleccion_contratacion_solicitud_plaza_vacante_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        solicitud = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=id).values() if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=id) else None

        
        if motivo:
            queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"La solicitud no existe"},status=status.HTTP_404_NOT_FOUND)
 

class seleccion_contratacion_estadoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = seleccion_contratacion_estado.objects.all()
    serializer_class = seleccion_contratacion_estadoserializer
    def list(self, request):
        queryset = seleccion_contratacion_estado.objects.all()
        serializer_class = seleccion_contratacion_estadoserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')


        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            # print(filter)
            # print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre_estado__icontains'] = filter
                    
                        
                queryset =  seleccion_contratacion_estado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_estado.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_estadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_estado.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_estado.objects.filter().count()
                serializer = seleccion_contratacion_estadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre_estado__icontains'] = filter
                    
                        
                queryset =  seleccion_contratacion_estado.objects.filter(**filter_kwargs).order_by('id')
                conteo =  seleccion_contratacion_estado.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_estadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_estado.objects.filter().order_by('id')
                conteo =  seleccion_contratacion_estado.objects.filter().count()
                serializer = seleccion_contratacion_estadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        # do your thing here
        serializer = seleccion_contratacion_estadoserializer(data=request.data)
        nombre_estado= request.data['nombre_estado'].lower()
        
        lista=['abierto','cerrado','en proceso']
        if nombre_estado in lista:
            return Response({'Nombre reservado'},status=status.HTTP_400_BAD_REQUEST)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El estado no ha sido creado "}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        
        estado = seleccion_contratacion_estado.objects.filter(id=pk) if seleccion_contratacion_estado.objects.filter(id=pk) else None

        if estado!=None:
            queryset = seleccion_contratacion_estado.objects.get(id=pk)
            
            nombre_estado= request.data['nombre_estado'].lower()
            
            lista=['abierto','cerrado','en proceso']
            if nombre_estado in lista:
                return Response({'Nombre reservado'},status=status.HTTP_400_BAD_REQUEST)
            serializer = seleccion_contratacion_estadoserializer(instance=queryset, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El estado no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('seleccion_contratacion_estado_id'):
            id = self.request.query_params.get('seleccion_contratacion_estado_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        estado = seleccion_contratacion_estado.objects.filter(id=id).values() if seleccion_contratacion_estado.objects.filter(id=id) else None

        
        if estado:
            queryset = seleccion_contratacion_estado.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El estado no existe"},status=status.HTTP_404_NOT_FOUND)
 


class seleccion_contratacion_postulante_plazaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = seleccion_contratacion_postulante_plaza.objects.all()
    serializer_class = seleccion_contratacion_postulante_plazaserializer
    def list(self, request):
        queryset = seleccion_contratacion_postulante_plaza.objects.all()
        serializer_class = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
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
            # print(filter)
            # print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='profesion':
                        filter_kwargs['profesion__icontains'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre_postulante__icontains'] = filter
                    if tipo_busqueda =='estado_id':
                        filter_kwargs['estado'] = filter
                    if tipo_busqueda =='estado_nombre':
                        filter_kwargs['estado__nombre_estado__icontains'] = filter
                    if tipo_busqueda =='plaza_id':
                        filter_kwargs['plaza'] = filter
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='profesion':
                            filter_kwargs_2['profesion__icontains'] = filter_2
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre_postulante__icontains'] = filter_2
                        if tipo_busqueda_2 =='estado_id':
                            filter_kwargs_2['estado'] = filter_2
                        if tipo_busqueda_2 =='estado_nombre':
                            filter_kwargs_2['estado__nombre_estado__icontains'] = filter_2
                        if tipo_busqueda_2 =='plaza_id':
                            filter_kwargs_2['plaza'] = filter_2

                    queryset =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')[offset:offset+limit]
                    conteo =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                    serializer = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).count()
                    serializer = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
                    
                        
                queryset =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_postulante_plaza.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  seleccion_contratacion_postulante_plaza.objects.filter().count()
                serializer = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='profesion':
                        filter_kwargs['profesion__icontains'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre_postulante__icontains'] = filter
                    if tipo_busqueda =='estado_id':
                        filter_kwargs['estado'] = filter
                    if tipo_busqueda =='estado_nombre':
                        filter_kwargs['estado__nombre_estado__icontains'] = filter
                    if tipo_busqueda =='plaza_id':
                        filter_kwargs['plaza'] = filter    
                
                if filter_2!='' and tipo_busqueda_2!='':
                    filter_kwargs_2={}
                    if tipo_busqueda_2:
                        if tipo_busqueda_2 =='id':
                            filter_kwargs_2['id'] = filter_2
                        if tipo_busqueda_2 =='profesion':
                            filter_kwargs_2['profesion__icontains'] = filter_2
                        if tipo_busqueda_2 =='nombre':
                            filter_kwargs_2['nombre_postulante__icontains'] = filter_2
                        if tipo_busqueda_2 =='estado_id':
                            filter_kwargs_2['estado'] = filter_2
                        if tipo_busqueda_2 =='estado_nombre':
                            filter_kwargs_2['estado__nombre_estado__icontains'] = filter_2
                        if tipo_busqueda_2 =='plaza_id':
                            filter_kwargs_2['plaza'] = filter_2  

                        queryset =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).order_by('id')
                        conteo =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).filter(**filter_kwargs_2).count()
                        serializer = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo}) 
                    else: 
                        queryset =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).order_by('id')
                        conteo =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).count()
                        serializer = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})

                queryset =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).order_by('id')
                conteo =  seleccion_contratacion_postulante_plaza.objects.filter(**filter_kwargs).count()
                serializer = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  seleccion_contratacion_postulante_plaza.objects.filter().order_by('id')
                conteo =  seleccion_contratacion_postulante_plaza.objects.filter().count()
                serializer = seleccion_contratacion_postulante_plazaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

    def create(self, request):
        nombre_archivo_cv=''     
        request.data._mutable = True
        if 'archivo_cv' in request.data:
            nombre_archivo_cv=self.request.data['archivo_cv']
            request.data['nombre_archivo_cv']= str(nombre_archivo_cv)
        
        serializer = seleccion_contratacion_postulante_plazaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"Mensaje":"Correcto"})
        else:
            return Response({"mensaje":"La solicitud no ha sido creada"}, status=status.HTTP_400_BAD_REQUEST)
        

    def update(self, request, pk=None):
        
        postulante = seleccion_contratacion_postulante_plaza.objects.filter(id=pk) if seleccion_contratacion_postulante_plaza.objects.filter(id=pk) else None

        if postulante!=None:
            queryset = seleccion_contratacion_postulante_plaza.objects.get(id=pk)

            
            if 'archivo_cv' in request.data:
                nombre_archivo_cv=self.request.data['archivo_cv']
                if nombre_archivo_cv!=None:
                    request.data['nombre_archivo_cv']= str(nombre_archivo_cv)

            
            serializer = seleccion_contratacion_postulante_plazaserializer(instance=queryset, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"La información no ha sido guardada"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"El postulante no ha sido encontrado"},status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        id =''
       
        if self.request.query_params.get('seleccion_contratacion_postulante_plaza_id'):
            id = self.request.query_params.get('seleccion_contratacion_postulante_plaza_id') 
        else:
            return Response({"mensaje":"No se ha enviado el parámetro correcto"},status=status.HTTP_400_BAD_REQUEST)

        
        postulante = seleccion_contratacion_postulante_plaza.objects.filter(id=id).values() if seleccion_contratacion_postulante_plaza.objects.filter(id=id) else None

        
        if postulante:
            queryset = seleccion_contratacion_postulante_plaza.objects.get(id=id).delete()
            
            return Response({"mensaje":"La información ha sido eliminada"},status= status.HTTP_200_OK)
        else:
            return Response({"mensaje":"El postulante no existe"},status=status.HTTP_404_NOT_FOUND)
 


class seleccion_contratacion_dashboard_motivo_solicitud(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.all()
    serializer_class = seleccion_contratacion_solicitud_plaza_vacanteserializer
    def get(self, request):
        queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.all()
        serializer_class = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
        filter=''
        unidad_organizativa=''
        usuario = request.user
        # print('usuario',usuario)
        listado_puestos= puestos_vacantes(usuario)
        lista_puestos= listado_puestos['plazas_vacantes']
        grupos = list(usuario.groups.all().values_list('name',flat=True))

        if 'jefe' in grupos:
            
            lista_motivos=[]
            lista_nombres=[]
            tabla_motivos=''
            tabla_motivos=seleccion_contratacion_motivo.objects.filter().values_list('descripcion',flat=True)
            # print(tabla_motivos)
            for motivo in tabla_motivos:
                conteo= seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=lista_puestos).filter(motivo__descripcion__icontains=motivo).count()
                lista_motivos.append(conteo)
                lista_nombres.append(motivo)


            data={}
            labels=[]
            dataset=[]
            dataset.extend([
                        {   
                            'data': lista_motivos,
                            "backgroundColor": ["rgb(0, 112, 188)","rgb(228, 129, 0 )","rgb(155,155,155)","rgb(54, 162, 235)","rgb(255, 0, 0)"],
                            "borderColor": ["rgb(0, 112, 188)","rgb(228, 129, 0 )","rgb(155,155,155)", "rgb(54, 162, 235)","rgb(255, 0, 0)"],
                            "borderWidth": 1
                        },
                    ]),   
            data_add={}
            # dataset.append(datadd1)
            labels.extend(lista_nombres)
            data['labels']=labels
            data['datasets']=dataset
        else:
            lista_motivos=[]
            lista_nombres=[]
            tabla_motivos=''
            tabla_motivos=seleccion_contratacion_motivo.objects.filter().values_list('descripcion',flat=True)
            print(tabla_motivos)
            for motivo in tabla_motivos:
                conteo= seleccion_contratacion_solicitud_plaza_vacante.objects.filter(motivo__descripcion__icontains=motivo).count()
                lista_motivos.append(conteo)
                lista_nombres.append(motivo)


            data={}
            labels=[]
            dataset=[]
            dataset.extend([
                        {   
                            'data': lista_motivos,
                            "backgroundColor": ["rgb(0, 112, 188)","rgb(228, 129, 0 )","rgb(155,155,155)","rgb(54, 162, 235)","rgb(255, 0, 0)"],
                            "borderColor": ["rgb(0, 112, 188)","rgb(228, 129, 0 )","rgb(155,155,155)","rgb(54, 162, 235)","rgb(255, 0, 0)"],
                            "borderWidth": 1
                        },
                    ]),   
            data_add={}
            # dataset.append(datadd1)
            labels.extend(lista_nombres)
            data['labels']=labels
            data['datasets']=dataset
            
        return Response(data,status= status.HTTP_200_OK)


class seleccion_contratacion_dashboard_contrataciones(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.all()
    serializer_class = seleccion_contratacion_solicitud_plaza_vacanteserializer

    def get(self, request):
        queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.all()
        serializer_class = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
        filter=''
        filter_puesto=''
        filter_nombre_puesto=''
        unidad_organizativa=''
        usuario = request.user
        unidad=''
        empleados_unidad=''
        hoy=datetime.now().date()
        año= hoy.year
        lista_meses_abierto=[0,0,0,0,0,0,0,0,0,0,0,0]
        lista_meses_en_proceso=[0,0,0,0,0,0,0,0,0,0,0,0]
        lista_meses_cerrado=[0,0,0,0,0,0,0,0,0,0,0,0]
        labels= ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

        # print('alnne',len(lista_meses_abierto))

        fecha_inicio_año_actual=hoy.replace(month=1,day=1)
        fecha_fin_año_anterior = fecha_inicio_año_actual - timedelta(days=1)
        fecha_inicio_año_anterior = fecha_fin_año_anterior.replace(month=1,day=1)
        lista_meses_contrataciones_abiertas=''
        # print('hoy',hoy)
        # print('hoy',hoy)
        # print('fecha_inicio_año_actual',fecha_inicio_año_actual)
        # print('fecha_fin_año_anterior',fecha_fin_año_anterior)
        # print('fecha_inicio_año_anterior',fecha_inicio_año_anterior)
        grupos = list(usuario.groups.all().values_list('name',flat=True))

        filter_anio=''
        if self.request.query_params.get('filter_anio'):
                # return Response({"mensaje":"El correo no ha sido enviado "}, status=status.HTTP_400_BAD_REQUEST)
                try:
                  filter_anio = int(self.request.query_params.get('filter_anio'))
                except ValueError:
                    return Response({"mensaje":"Dato ingresado incorrecto "}, status=status.HTTP_400_BAD_REQUEST)
                
        else:
            filter_anio=año

        if self.request.query_params.get('filter_puesto'):
                filter_puesto = self.request.query_params.get('filter_puesto')
        
        if self.request.query_params.get('filter_nombre_puesto'):
                filter_nombre_puesto = self.request.query_params.get('filter_nombre_puesto')
        
                    
        
        lista_puestos=''
        listado_puestos=puestos_vacantes(usuario)
        lista_puestos=listado_puestos['plazas_vacantes']
        # print('lista_puestos',lista_puestos)
        if 'jefe' in grupos:
            # jefe_unidad= Funcional_empleado.objects.filter(codigo=usuario).values('unidad_organizativa') if Funcional_empleado.objects.filter(codigo=usuario) else None
            # if jefe_unidad!=None:
            #     unidad= jefe_unidad[0]['unidad_organizativa']
            # print('unidad',unidad)
            # plazas_vacantes=Funcional_Unidad_Organizativa.objects.filter(id__in=unidad).values_list('funcional_puesto__codigo',flat=True)
            puestos =  Funcional_Puesto.objects.filter(codigo__in=lista_puestos,funcional_empleado=None).values_list('id',flat=True)
            #######################################################################################################
            #estado abierto
            if filter_puesto!='':
                abierto = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__codigo=filter_puesto,fecha_solicitud__year=filter_anio).values_list('fecha_solicitud__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__codigo=filter_puesto,fecha_solicitud__year=filter_anio) else None
            
            if filter_nombre_puesto!='':
                abierto = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__descripcion__icontains=filter_nombre_puesto,fecha_solicitud__year=filter_anio).values_list('fecha_solicitud__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__descripcion__icontains=filter_nombre_puesto,fecha_solicitud__year=filter_anio) else None 
            
            if filter_puesto=='' and  filter_nombre_puesto=='':
                abierto = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__in=puestos,fecha_solicitud__year=filter_anio).values_list('fecha_solicitud__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__in=puestos,fecha_solicitud__year=filter_anio) else None

            if abierto!=None:    
                for mes in abierto:
                    if mes==1:
                        lista_meses_abierto[0]+=1
                    if mes==2:
                        lista_meses_abierto[1]+=1
                    if mes==3:
                        lista_meses_abierto[2]+=1
                    if mes==4:
                        lista_meses_abierto[3]+=1
                    if mes==5:
                        lista_meses_abierto[4]+=1
                    if mes==6:
                        lista_meses_abierto[5]+=1
                    if mes==7:
                        lista_meses_abierto[6]+=1
                    if mes==8:
                        lista_meses_abierto[7]+=1
                    if mes==9:
                        lista_meses_abierto[8]+=1
                    if mes==10:
                        lista_meses_abierto[9]+=1
                    if mes==11:
                        lista_meses_abierto[10]+=1
                    if mes==12:
                        lista_meses_abierto[11]+=1

            # print(lista_meses_abierto)
            #estado en proceso
            if filter_puesto!='':
                en_proceso = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__codigo=filter_puesto,fecha_inicio_proceso__year=filter_anio).values_list('fecha_inicio_proceso__month',flat=True).exclude(estado__nombre_estado='Cerrado') if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__codigo=filter_puesto,fecha_inicio_proceso__year=filter_anio) else None
            
            if filter_nombre_puesto!='':
                en_proceso = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__descripcion__icontains=filter_nombre_puesto,fecha_inicio_proceso__year=filter_anio).values_list('fecha_inicio_proceso__month',flat=True).exclude(estado__nombre_estado='Cerrado') if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__descripcion__icontains=filter_nombre_puesto,fecha_inicio_proceso__year=filter_anio) else None

            if filter_puesto=='' and filter_nombre_puesto=='':
                en_proceso = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__in=puestos,fecha_inicio_proceso__year=filter_anio).values_list('fecha_inicio_proceso__month',flat=True).exclude(estado__nombre_estado='Cerrado') if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__in=puestos,fecha_inicio_proceso__year=filter_anio) else None
            
            # print('en_proceso',en_proceso)
            if en_proceso!=None:
                for mes in en_proceso:
                    if mes==1:
                        lista_meses_en_proceso[0]+=1
                    if mes==2:
                        lista_meses_en_proceso[1]+=1
                    if mes==3:
                        lista_meses_en_proceso[2]+=1
                    if mes==4:
                        lista_meses_en_proceso[3]+=1
                    if mes==5:
                        lista_meses_en_proceso[4]+=1
                    if mes==6:
                        lista_meses_en_proceso[5]+=1
                    if mes==7:
                        lista_meses_en_proceso[6]+=1
                    if mes==8:
                        lista_meses_en_proceso[7]+=1
                    if mes==9:
                        lista_meses_en_proceso[8]+=1
                    if mes==10:
                        lista_meses_en_proceso[9]+=1
                    if mes==11:
                        lista_meses_en_proceso[10]+=1
                    if mes==12:
                        lista_meses_en_proceso[11]+=1
            # print('lista_meses_en_proceso',lista_meses_en_proceso)
            
            #Cerrado
            if filter_puesto!='':
                cerrado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__codigo=filter_puesto,fecha_actualizacion__year=filter_anio).values_list('fecha_actualizacion__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__codigo=filter_puesto,fecha_actualizacion__year=filter_anio) else None
            
            if filter_nombre_puesto!='':
                cerrado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__descripcion__icontains=filter_nombre_puesto,fecha_actualizacion__year=filter_anio).values_list('fecha_actualizacion__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__descripcion__icontains=filter_nombre_puesto,fecha_actualizacion__year=filter_anio) else None
            
            if filter_puesto=='' and filter_nombre_puesto=='':
                cerrado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__in=puestos,fecha_actualizacion__year=filter_anio).values_list('fecha_actualizacion__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__in=puestos,fecha_actualizacion__year=filter_anio) else None

            if cerrado!=None:
                for mes in cerrado:
                    if mes==1:
                        lista_meses_cerrado[0]+=1
                    if mes==2:
                        lista_meses_cerrado[1]+=1
                    if mes==3:
                        lista_meses_cerrado[2]+=1
                    if mes==4:
                        lista_meses_cerrado[3]+=1
                    if mes==5:
                        lista_meses_cerrado[4]+=1
                    if mes==6:
                        lista_meses_cerrado[5]+=1
                    if mes==7:
                        lista_meses_cerrado[6]+=1
                    if mes==8:
                        lista_meses_cerrado[7]+=1
                    if mes==9:
                        lista_meses_cerrado[8]+=1
                    if mes==10:
                        lista_meses_cerrado[9]+=1
                    if mes==11:
                        lista_meses_cerrado[10]+=1
                    if mes==12:
                        lista_meses_cerrado[11]+=1

            # print('lista_meses_cerrado',lista_meses_cerrado)
            data={}
            datasets=[]
            datasets.extend([
                        {   'label': 'Abiertos',
                            'data': lista_meses_abierto,
                            'backgroundColor': '#0070b8',
                            'hoverBackgorundColor': '#0070b8'
                        },
                        {   'label': 'En Procesos',
                            'data': lista_meses_en_proceso,
                            'backgroundColor': '#e48100',
                            'hoverBackgorundColor': '#e48100'
                        },
                        {   'label': 'Cerrados',
                            'data': lista_meses_cerrado,
                            'backgroundColor': 'grey',
                            'hoverBackgorundColor': 'grey'
                        },
                    ]),  
            data['labels']=labels
            data['datasets']=datasets
        else:
            #Abiertos
            if filter_puesto!='':
                abierto = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__codigo=filter_puesto,fecha_solicitud__year=filter_anio).values_list('fecha_solicitud__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__codigo=filter_puesto,fecha_solicitud__year=filter_anio) else None
            
            if filter_nombre_puesto!='':
                abierto = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__descripcion__icontains=filter_nombre_puesto,fecha_solicitud__year=filter_anio).values_list('fecha_solicitud__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__descripcion__icontains=filter_nombre_puesto,fecha_solicitud__year=filter_anio) else None

            
            if filter_puesto=='' and filter_nombre_puesto=='':
                abierto = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',fecha_solicitud__year=filter_anio).values_list('fecha_solicitud__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',fecha_solicitud__year=filter_anio) else None

            if abierto!=None:    
                for mes in abierto:
                    if mes==1:
                        lista_meses_abierto[0]+=1
                    if mes==2:
                        lista_meses_abierto[1]+=1
                    if mes==3:
                        lista_meses_abierto[2]+=1
                    if mes==4:
                        lista_meses_abierto[3]+=1
                    if mes==5:
                        lista_meses_abierto[4]+=1
                    if mes==6:
                        lista_meses_abierto[5]+=1
                    if mes==7:
                        lista_meses_abierto[6]+=1
                    if mes==8:
                        lista_meses_abierto[7]+=1
                    if mes==9:
                        lista_meses_abierto[8]+=1
                    if mes==10:
                        lista_meses_abierto[9]+=1
                    if mes==11:
                        lista_meses_abierto[10]+=1
                    if mes==12:
                        lista_meses_abierto[11]+=1

            # print(lista_meses_abierto)
            #estado en proceso
            if filter_puesto:
                en_proceso = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__codigo=filter_puesto,fecha_inicio_proceso__year=filter_anio).values_list('fecha_inicio_proceso__month',flat=True).exclude(estado__nombre_estado='Cerrado') if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__codigo=filter_puesto,fecha_inicio_proceso__year=filter_anio) else None
            
            if filter_nombre_puesto!='':
                en_proceso = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__descripcion__icontains=filter_nombre_puesto,fecha_inicio_proceso__year=filter_anio).values_list('fecha_inicio_proceso__month',flat=True).exclude(estado__nombre_estado='Cerrado') if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',posicion__descripcion__icontains=filter_nombre_puesto,fecha_inicio_proceso__year=filter_anio) else None

            
            if filter_puesto=='' and filter_nombre_puesto=='':
                en_proceso = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',fecha_inicio_proceso__year=filter_anio).values_list('fecha_inicio_proceso__month',flat=True).exclude(estado__nombre_estado='Cerrado') if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='En proceso',fecha_inicio_proceso__year=filter_anio) else None
            
            # print('en_proceso',en_proceso)
            if en_proceso!=None:
                for mes in en_proceso:
                    if mes==1:
                        lista_meses_en_proceso[0]+=1
                    if mes==2:
                        lista_meses_en_proceso[1]+=1
                    if mes==3:
                        lista_meses_en_proceso[2]+=1
                    if mes==4:
                        lista_meses_en_proceso[3]+=1
                    if mes==5:
                        lista_meses_en_proceso[4]+=1
                    if mes==6:
                        lista_meses_en_proceso[5]+=1
                    if mes==7:
                        lista_meses_en_proceso[6]+=1
                    if mes==8:
                        lista_meses_en_proceso[7]+=1
                    if mes==9:
                        lista_meses_en_proceso[8]+=1
                    if mes==10:
                        lista_meses_en_proceso[9]+=1
                    if mes==11:
                        lista_meses_en_proceso[10]+=1
                    if mes==12:
                        lista_meses_en_proceso[11]+=1
            # print('lista_meses_en_proceso',lista_meses_en_proceso)
            #Cerrado
            if filter_puesto!='':
                cerrado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__codigo=filter_puesto,fecha_actualizacion__year=filter_anio).values_list('fecha_actualizacion__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__codigo=filter_puesto,fecha_actualizacion__year=filter_anio) else None
            
            if filter_nombre_puesto!='':
                cerrado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__descripcion__icontains=filter_nombre_puesto,fecha_actualizacion__year=filter_anio).values_list('fecha_actualizacion__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__descripcion__icontains=filter_nombre_puesto,fecha_actualizacion__year=filter_anio) else None

            
            if filter_puesto=='' and filter_nombre_puesto=='':
                cerrado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',fecha_actualizacion__year=filter_anio).values_list('fecha_actualizacion__month',flat=True) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',fecha_actualizacion__year=filter_anio) else None

            if cerrado!=None:
                for mes in cerrado:
                    if mes==1:
                        lista_meses_cerrado[0]+=1
                    if mes==2:
                        lista_meses_cerrado[1]+=1
                    if mes==3:
                        lista_meses_cerrado[2]+=1
                    if mes==4:
                        lista_meses_cerrado[3]+=1
                    if mes==5:
                        lista_meses_cerrado[4]+=1
                    if mes==6:
                        lista_meses_cerrado[5]+=1
                    if mes==7:
                        lista_meses_cerrado[6]+=1
                    if mes==8:
                        lista_meses_cerrado[7]+=1
                    if mes==9:
                        lista_meses_cerrado[8]+=1
                    if mes==10:
                        lista_meses_cerrado[9]+=1
                    if mes==11:
                        lista_meses_cerrado[10]+=1
                    if mes==12:
                        lista_meses_cerrado[11]+=1

            # print('lista_meses_cerrado',lista_meses_cerrado)
            data={}
            datasets=[]
            datasets.extend([
                        {   'label': 'Abiertos',
                            'data': lista_meses_abierto,
                            'backgroundColor': '#0070b8',
                            'hoverBackgorundColor': '#0070b8'
                        },
                        {   'label': 'En Procesos',
                            'data': lista_meses_en_proceso,
                            'backgroundColor': '#e48100',
                            'hoverBackgorundColor': '#e48100'
                        },
                        {   'label': 'Cerrados',
                            'data': lista_meses_cerrado,
                            'backgroundColor': 'grey',
                            'hoverBackgorundColor': 'grey'
                        },
                    ]),  
            data['labels']=labels
            data['datasets']=datasets

        return Response(data,status= status.HTTP_200_OK) 


class seleccion_contratacion_dashboard_vacantes(APIView):
    def get(self, request):
        queryset = seleccion_contratacion_solicitud_plaza_vacante.objects.all()
        serializer_class = seleccion_contratacion_solicitud_plaza_vacanteserializer(queryset, many=True)
        hoy=datetime.now().date()
        año= hoy.year
        usuario = request.user
        # lista_puestos=puestos_vacantes(usuario)
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        total_plazas=''
        cerrados=''
        abierto=''
        cancelados=''
        en_proceso=''
        porcentaje_activos_vrs_anio_pasado=''
        total_plazas_año_anterior=''
        total_plazas_año_actual=''
        empleados_dados_baja=''
        total=''
        lista_empleados=''
        if 'jefe' in grupos:
            listado_puestos_vacantes=puestos_vacantes(usuario)
            puestos_vacante=listado_puestos_vacantes['plazas_vacantes']

            total_plazas= Funcional_Puesto.objects.filter(codigo__in=puestos_vacante).count()
            # total= seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=puestos_vacante).count()
            # print(total)
            total_plazas_año_actual= seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=puestos_vacante,fecha_inicio_proceso__year=año).count()
            total_plazas_año_anterior = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=puestos_vacante,fecha_inicio_proceso__year=(año-1)).count()
            
            if total_plazas_año_anterior!=0:
                
                porcentaje_activos_vrs_anio_pasado=((total_plazas_año_actual/total_plazas_año_anterior)*100)
            else:
                porcentaje_activos_vrs_anio_pasado=0

            en_proceso = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=puestos_vacante,estado__nombre_estado='En proceso').values_list('fecha_inicio_proceso__month',flat=True).count()
            cerrado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__codigo__in=puestos_vacante,fecha_actualizacion__year=año).count()
            abierto = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__codigo__in=puestos_vacante).count()
            total= (en_proceso+cerrado+abierto)
        else:
            plazas_vacantes=[]
            puestos_vacios= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).values('codigo')
            puestos_vacios_2 = Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).values_list('codigo',flat=True)
            # empleados_dados_baja= Funcional_empleado.objects.filter(fecha_baja__lt=datetime.now().date()).values_list('puesto__codigo',flat=True)
            plazas_vacantes.extend(puestos_vacios_2)
            print(plazas_vacantes)
            # plazas_vacantes.extend(empleados_dados_baja)
            
            total_plazas= puestos_vacios.count()
            # total = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=plazas_vacantes).count()
            total_plazas_año_actual= seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=plazas_vacantes,fecha_inicio_proceso__year=año).count()
            total_plazas_año_anterior = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=plazas_vacantes,fecha_inicio_proceso__year=(año-1)).count()
            
            if total_plazas_año_anterior!=0:
                
                porcentaje_activos_vrs_anio_pasado=((total_plazas_año_actual/total_plazas_año_anterior)*100)
            else:
                porcentaje_activos_vrs_anio_pasado=0
            
            en_proceso = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(posicion__codigo__in=plazas_vacantes,fecha_inicio_proceso__year=año).values_list('fecha_inicio_proceso__month',flat=True).exclude(estado__nombre_estado='Cerrado').count()
            cerrado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cerrado',posicion__codigo__in=plazas_vacantes,fecha_actualizacion__year=año).count()
            # cancelado = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Cancelado',posicion__codigo__in=plazas_vacantes,fecha_actualizacion__year=año).count()
            abierto = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(estado__nombre_estado='Abierto',posicion__codigo__in=plazas_vacantes).count()
            total= (en_proceso+cerrado+abierto)
        data={'Vacantes':total_plazas,'Total':total,'En_proceso':en_proceso,'Cerrado':cerrado,'Abierto':abierto,'porcentaje':porcentaje_activos_vrs_anio_pasado}    
        return Response(data,status= status.HTTP_200_OK)        
            

def puestos_vacantes(usuario):
        lista_puestos=[]
        unidad_organizativa=''
        unidad_organizativa = list(Funcional_Unidad_Organizativa.objects.filter(Dirigido_por=usuario).values_list('id',flat=True))
        bandera=None
        listado=[]
        filtros=unidad_organizativa
        puestos=''
       
        
        while bandera ==None:
            resultado=Funcional_Unidad_Organizativa.objects.filter(id__in=filtros).exclude(unidad_organizativa_jeraquia__id=None).values_list('unidad_organizativa_jeraquia__id',flat=True)           
            #print('filtros',filtros)
            #print('resultado',resultado)

            listado.extend(resultado)
            filtros = resultado
            if resultado.count()==0 or resultado==None:
                bandera=0

       
        uni= Funcional_Unidad_Organizativa.objects.filter(id__in=unidad_organizativa)
        Dirigido_por=uni[0].Dirigido_por
        padre = Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id__in=unidad_organizativa)
        if padre:
            hijos_list=padre[0].unidad_organizativa_jeraquia.all().values_list('id',flat=True)
        
        # equipo = Funcional_Unidad_Organizativa.objects.filter(id=unidad_organizativa).values_list('unidad_organizativa_jeraquia__id',flat=True)
        equipo =Funcional_Unidad_Organizativa.objects.filter(id__in=listado)
        
        lista_permiso=list(usuario.groups.all().values_list('name',flat=True))
       

        serializer_unidad = funcional_arbol_padre_serializer(uni[0])
        serializer_padre = funcional_arbol_padre_serializer(padre[0]).data if padre else []
        # lista_puestos.append(Funcional_empleado.objects.filter(codigo=codigo_padre).values('posicion__id')[0]['posicion__id'])
        serializer_equipo = funcional_arbol_padre_serializer(equipo,many=True).data

        lider = serializer_unidad.data['lider']

        lideres=[]
        
        # if serializer_unidad.data['lider']!=None:
        #     lideres.append(serializer_unidad.data['lider']['id'])
        
        # if 'empleado' in lista_permiso:
        #     serializer_equipo=[]
        #     listado=[unidad_organizativa]
           
        # else:
        #     for eq in serializer_equipo:
        #         if  eq['lider']!=None:
        #                 lideres.append(eq['lider']['id'])
        #     listado.append(unidad_organizativa)
           
        #print('listado',listado)    
        empleados_activos = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(fecha_baja__lt=datetime.now().date()) else None
        empleados_dados_de_baja = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()) else None
        puestos = Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None,activo=True) if Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None,activo=True) else None
        
        if lider!=None:
            empleados_activos = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) else None
            empleados_dados_de_baja = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()).exclude(id__in=lideres) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()).exclude(id__in=lideres) else None
            puestos = Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None,activo=True).exclude(id__in=lideres) if Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None,activo=True).exclude(id__in=lideres) else None
        
        #Empleados que pertenecen a determinado jefe encontrados mediante la unidad organizativa
        listado_puestos_empleados_activos=[]
        if empleados_activos!=None:
            lista_emple= empleados_activos.values_list('puesto__codigo',flat=True)
            listado_puestos_empleados_activos.extend(lista_emple)
        #No activos encontrados mediante la unidad organizativa en la tabla de empleados y la fecha de baja
        if empleados_dados_de_baja!=None:
            lista_puestos.extend(empleados_dados_de_baja.values_list('puesto__codigo',flat=True))
            #print('############################pruea correccion 2',len(lista_puestos))
        #No activos encontrados mediante la unidad organizativa
        if puestos!=None:
            lista_puestos.extend( puestos.values_list('codigo',flat=True))
            #print('############################pruea correccion 3',len(lista_puestos))
        
        #activos encontrados mediante el jefe inmediato
        empleados_con_jefe_inmediato= Funcional_empleado.objects.filter(jefe_inmediato=usuario).values_list('puesto__codigo',flat=True) if Funcional_empleado.objects.filter(jefe_inmediato=usuario) else None
        #inactivos encontrados mediante el jefe inmediato
        empleados_dados_baja_jefe_inmediato= Funcional_empleado.objects.filter(jefe_inmediato=usuario,fecha_baja__lt=datetime.now().date()).exclude(puesto__codigo=None).values_list('puesto__codigo',flat=True) if Funcional_empleado.objects.filter(jefe_inmediato=usuario,fecha_baja__lt=datetime.now().date()) else None
        #print('#######################################prueba correccion 4',len(empleados_dados_baja_jefe_inmediato))
        #puestos dirigido por vacantes
        puesto_dirigido_por_vacantes=Funcional_Puesto.objects.filter(unidad_organizativa__Dirigido_por=usuario,funcional_empleado=None,activo=True).values_list('codigo',flat=True) if Funcional_Puesto.objects.filter(unidad_organizativa__Dirigido_por=usuario,funcional_empleado=None,activo=True).values_list('codigo') else None  
        if puesto_dirigido_por_vacantes!=None:
            #print('puesto_dirigido_por_vacantes',len(puesto_dirigido_por_vacantes))
            lista_puestos.extend(puesto_dirigido_por_vacantes)


        #puestos dirigido por activos
        puesto_dirigido_por_activos=Funcional_Puesto.objects.filter(unidad_organizativa__Dirigido_por=usuario,activo=True).exclude(funcional_empleado=None).values_list('codigo',flat=True) if Funcional_Puesto.objects.filter(unidad_organizativa__Dirigido_por=usuario,activo=True).exclude(funcional_empleado=None).values_list('codigo') else None  
        if puesto_dirigido_por_activos!=None:
            listado_puestos_empleados_activos.extend(puesto_dirigido_por_activos)
            

        #nuevo llenado de lista activos 
        if empleados_con_jefe_inmediato!=None:
            listado_puestos_empleados_activos.extend(empleados_con_jefe_inmediato) 
             
        #nuevo llenado de lista inactivos
        if empleados_dados_baja_jefe_inmediato!=None:
            lista_puestos.extend(empleados_dados_baja_jefe_inmediato)
            #print('#############################prueba correccion 5',len(lista_puestos))


        nueva_lista_plaza_vacantes=[]
        nueva_lista_plazas_activas=[]

        if len(lista_puestos)!=0:
            for item in lista_puestos:
                if item not in nueva_lista_plaza_vacantes:
                    if item!=None:
                        nueva_lista_plaza_vacantes.append(item)

        if len(listado_puestos_empleados_activos)!=0:
            for item in listado_puestos_empleados_activos:
                if item not in nueva_lista_plazas_activas:
                    if item!=None:
                        nueva_lista_plazas_activas.append(item)
        
        if len(nueva_lista_plaza_vacantes)!=0:
            nueva_lista_plaza_vacantes.sort()
        
        if len(nueva_lista_plazas_activas)!=0:
            nueva_lista_plazas_activas.sort()
        # #print('nueva_lista_plaza_vacantes',nueva_lista_plaza_vacantes)
        data={'plazas_vacantes':nueva_lista_plaza_vacantes,'plazas_activas':nueva_lista_plazas_activas,'total_plazas_vacantes':len(nueva_lista_plaza_vacantes),'total_plazas_activas':len(nueva_lista_plazas_activas)}
        # #print(data)
        return data


class envio_correo_seleccion_contratacion(APIView):
    authentication_classes=[TokenAuthentication]
    
    def post(self,request):
        notificaciones = self.request.data['data']
        
        modulo='SELECCION_CONTRATACION'
        plaza_id=''
        tipo_mensaje = ''
        estado_1=''
        estado_2=''
        fecha_baja=''
        usuario=request.user
        postulante_id=''
        empleado_codigo=''
        
        
        for variable in notificaciones:
            
           
            if "tipo_mensaje" in variable:
                tipo_mensaje = variable['tipo_mensaje']

            if "empleado_codigo" in variable:
                empleado_codigo = variable['empleado_codigo']
            
            if "plaza_id" in variable:
                plaza_id = variable['plaza_id']
            
            if "estado_1" in variable:
                estado_1 = variable['estado_1']
            
            if "estado_2" in variable:
                estado_2 = variable['estado_2']
            
            if "fecha_baja" in variable:
                fecha_baja = variable['fecha_baja']
            
            if "postulante_id" in variable:
                postulante_id = variable['postulante_id']

            if postulante_id!='' and tipo_mensaje!='':
                postulante_plaza_envio_correo(postulante_id,tipo_mensaje)
                return Response({"mensaje":"proceso terminado"},status= status.HTTP_200_OK)
            
            if plaza_id!='' and tipo_mensaje!='' and estado_1=='' and estado_2=='' and fecha_baja=='':
                seleccion_contratacion_solicitud_plaza_vacante_envio_correo(plaza_id,tipo_mensaje)
                return Response({"mensaje":"proceso terminado"},status= status.HTTP_200_OK) 

            elif empleado_codigo!='' and plaza_id=='' and tipo_mensaje!='' and estado_1=='' and estado_2=='' and fecha_baja!='':
                solicitud_plaza_fecha_baja_envio_correo(empleado_codigo,tipo_mensaje,fecha_baja)
                return Response({"mensaje":"proceso terminado"},status= status.HTTP_200_OK)  
            
            elif plaza_id!='' and tipo_mensaje!='' and estado_1!='' and estado_2!='' and fecha_baja=='':

                solicitud_plaza_cambio_estado_envio_correo(plaza_id,tipo_mensaje,estado_1,estado_2)
                return Response({"mensaje":"proceso terminado"},status= status.HTTP_200_OK)

            else:
                return Response({"mensaje":"El correo no ha sido enviado "}, status=status.HTTP_400_BAD_REQUEST)
                
         


def seleccion_contratacion_solicitud_plaza_vacante_envio_correo(plaza_id, tipo_mensaje):
    correo_responsable=''
    responsable=''
    modulo='SELECCION_CONTRATACION'
    if tipo_mensaje == 'Jefe solicita vacante':
      
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
        

        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                responsable=None
                correo_responsable=None
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
                                
                                #####################################
                                if variable=='@@ResponsableSeleccion':
                                    responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') else None
                                    if responsable!=None:
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
                                    else:
                                        correo_responsable=None
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir)) 

                                elif variable=='@@JefeSolicitaPlaza':
                                    jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                                    jefe = Funcional_empleado.objects.filter(codigo=jefe_codigo).values("nombre")
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
                                
                                elif variable=='@@Funcion':
                                    jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                                   
                                    jefe_funcion = Funcional_empleado.objects.filter(codigo=jefe_codigo).values("posicion__descripcion")
                                    if jefe_funcion:
                                        valor_a_sustituir=jefe_funcion[0]['posicion__descripcion']
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
                                    valor_a_sustituir=list((modelo_tb.objects.filter(id=plaza_id).values(valores)[0]).values())[0]
                                
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
            

                if correo_responsable!=None:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    # correo_a_enviar= 'hoscar161@gmail.com'
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                           
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
    if tipo_mensaje == 'Responsable envía candidatos':
        
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
        
         
        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                # correo_responsable = Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
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
                                
                                #####################################

                                if variable=='@@JefeSolicitaPlaza':
                                    jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username'] if  (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username'] else None
                                    if jefe_codigo!=None:
                                        jefe = Funcional_empleado.objects.filter(codigo=jefe_codigo).values("nombre")
                                        correo_responsable = Funcional_empleado.objects.filter(codigo=jefe_codigo).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=jefe_codigo) else None
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
                                        correo_responsable=None
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                        
                                elif variable=='@@Funcion':
                                    jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                                   
                                    jefe_funcion = Funcional_empleado.objects.filter(codigo=jefe_codigo).values("posicion__descripcion")
                                    if jefe_funcion:
                                        valor_a_sustituir=jefe_funcion[0]['posicion__descripcion']
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
                                    valor_a_sustituir=list((modelo_tb.objects.filter(id=plaza_id).values(valores)[0]).values())[0]
                                
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
            

                if correo_responsable!=None:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    # print(correo_a_enviar= correo_responsable[0]['correo_empresarial'])
                    # correo_a_enviar= 'hoscar161@gmail.com'
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
    if tipo_mensaje == 'Vacante nueva':
        
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
    
         
        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                correo_responsable = Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
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
                                
                                #####################################

                                if variable=='@@ResponsableSeleccion':
                                    
                                    if responsable:
                                        valor_a_sustituir=responsable[0]['nombre']
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
                                
                                else:
                                    valor_a_sustituir=list((modelo_tb.objects.filter(id=plaza_id).values(valores)[0]).values())[0]
                                
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
            

                if correo_responsable:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    # print(correo_a_enviar= correo_responsable[0]['correo_empresarial'])
                    # correo_a_enviar= 'hoscar161@gmail.com'
                   
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                           
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
    if tipo_mensaje == 'JefeResponsable: jefe Solicita Vacante':
        
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
        

        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                jefe_responsable_codigo_obj=None
                correo_responsable=None
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
                                
                                #####################################
                                if variable=='@@JefeResponsableSeleccion':
                                    jefe_responsable_codigo_obj= Funcional_empleado.objects.filter(codigo=usuario_responable).values('jefe_inmediato') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                                    jefe_responsable_codigo= jefe_responsable_codigo_obj[0]['jefe_inmediato']
                                    
                                    jefe_responsable = Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo).values('nombre') if Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo) else None
                                    
                                    if jefe_responsable!=None:
                                        correo_responsable = Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                                    else:
                                        correo_responsable=None

                                    if jefe_responsable!=None:
                                        valor_a_sustituir = jefe_responsable[0]['nombre'] 
                                        if valor_a_sustituir:
                                            valor_a_sustituir_str = valor_a_sustituir
                                            mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                            asunto= asunto.replace(variable,str(valor_a_sustituir))
                                        else:
                                            valor_a_sustituir_str =''
                                            mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                            asunto= asunto.replace(variable,str(valor_a_sustituir))
                                             
                                elif variable=='@@JefeSolicitaPlaza':
                                    jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                                    jefe = Funcional_empleado.objects.filter(codigo=jefe_codigo).values("nombre")
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
                                
                                elif variable=='@@Funcion':
                                    jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username']
                                   
                                    jefe_funcion = Funcional_empleado.objects.filter(codigo=jefe_codigo).values("posicion__descripcion")
                                    if jefe_funcion:
                                        valor_a_sustituir=jefe_funcion[0]['posicion__descripcion']
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
                                    valor_a_sustituir=list((modelo_tb.objects.filter(id=plaza_id).values(valores)[0]).values())[0]
                                
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
            

                if correo_responsable!=None:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    # correo_a_enviar= 'hoscar161@gmail.com'
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                           
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
     
        
    return 1


def solicitud_plaza_cambio_estado_envio_correo(plaza_id,tipo_mensaje,estado_1,estado_2):
    correo_responsable=''
    responsable=''
    asunto=''
    jefe=''
    estado_estado_nombre_1=''
    estado_estado_nombre_2=''
    mensaje=''
    modulo='SELECCION_CONTRATACION'
    if tipo_mensaje == 'Cambio de estado de la plaza':
        
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
        
         
        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                # correo_responsable = Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
               
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
                               
                                #####################################

                                if variable=='@@JefeSolicitaPlaza':
                                    jefe_codigo = (seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id).values('creador_plaza__username'))[0]['creador_plaza__username'] if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=plaza_id) else None 
                                    # print('jefe_codigo',jefe_codigo)
                                    if jefe_codigo!=None:
                                        jefe= Funcional_empleado.objects.filter(codigo=jefe_codigo).values('nombre')
                                        correo_responsable = Funcional_empleado.objects.filter(codigo=jefe_codigo).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=jefe_codigo) else None
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
                                        correo_responsable=None
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))

                                elif variable=='@@Estado1':
                                    estado_estado_nombre_1= seleccion_contratacion_estado.objects.filter(id=estado_1).values('nombre_estado') if seleccion_contratacion_estado.objects.filter(id=estado_1) else None
                                    
                                    if estado_estado_nombre_1!=None:
                                        valor_a_sustituir=estado_estado_nombre_1[0]['nombre_estado']
                                       
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
                                elif variable=='@@Estado2':
                                    
                                    estado_estado_nombre_2= seleccion_contratacion_estado.objects.filter(id=estado_2).values('nombre_estado') if seleccion_contratacion_estado.objects.filter(id=estado_2) else None
                                    
                                    if estado_estado_nombre_2!=None:
                                        valor_a_sustituir=estado_estado_nombre_2[0]['nombre_estado']

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
                                    valor_a_sustituir=list((modelo_tb.objects.filter(id=plaza_id).values(valores)[0]).values())[0]
                                
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
            

                if correo_responsable!=None:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    # print(correo_a_enviar= correo_responsable[0]['correo_empresarial'])
                    # correo_a_enviar= 'hoscar161@gmail.com'
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                           
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
    if tipo_mensaje == 'Jefe del Responsable Cambio de estado de la plaza':
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
        
         
        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                # correo_responsable = Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                # print('configuracion_correo',configuracion_correo)
                if configuracion_correo:
                        # print('segunda condicion')
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
                                
                                #####################################

                                if variable=='@@JefeResponsableSeleccion':
                                    jefe_responsable_codigo_obj= Funcional_empleado.objects.filter(codigo=usuario_responable).values('jefe_inmediato') if (Funcional_empleado.objects.filter(codigo=usuario_responable).values('jefe_inmediato'))[0]['jefe_inmediato'] else None
                                    if jefe_responsable_codigo_obj!=None:
                                        jefe_responsable_codigo= jefe_responsable_codigo_obj[0]['jefe_inmediato']
                                        jefe_responsable = Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo).values('nombre') if Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo) else None
                                        correo_responsable = Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                                        
                                        
                                        valor_a_sustituir = jefe_responsable[0]['nombre'] 
                                        if valor_a_sustituir:
                                            valor_a_sustituir_str = valor_a_sustituir
                                            mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                            asunto= asunto.replace(variable,str(valor_a_sustituir))
                                        else:
                                            valor_a_sustituir_str =''
                                            mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                            asunto= asunto.replace(variable,str(valor_a_sustituir)) 
                                    else:
                                        correo_responsable=None
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir)) 

                                elif variable=='@@Estado1':
                                    estado_estado_nombre_1= seleccion_contratacion_estado.objects.filter(id=estado_1).values('nombre_estado') if seleccion_contratacion_estado.objects.filter(id=estado_1) else None
                                    
                                    if estado_estado_nombre_1!=None:
                                        valor_a_sustituir=estado_estado_nombre_1[0]['nombre_estado']
                                       
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
                                elif variable=='@@Estado2':
                                    
                                    estado_estado_nombre_2= seleccion_contratacion_estado.objects.filter(id=estado_2).values('nombre_estado') if seleccion_contratacion_estado.objects.filter(id=estado_2) else None
                                    
                                    if estado_estado_nombre_2!=None:
                                        valor_a_sustituir=estado_estado_nombre_2[0]['nombre_estado']

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
                                    valor_a_sustituir=list((modelo_tb.objects.filter(id=plaza_id).values(valores)[0]).values())[0]
                                
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
            

                if correo_responsable!=None:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
        
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
         
    return 1

def solicitud_plaza_fecha_baja_envio_correo(empleado_codigo,tipo_mensaje,fecha_baja):
    correo_responsable=''
    responsable=''
    asunto=''
    mensaje=''
    modulo='SELECCION_CONTRATACION'
    if tipo_mensaje == 'Vacante nueva':
        
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
    
         
        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                correo_responsable = Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
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
                            
                            #####################################

                            if variable=='@@ResponsableSeleccion':
                                
                                if responsable:
                                    valor_a_sustituir=responsable[0]['nombre']
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    
                                    return Response({"mensaje":"No se encontro codigo de responsable"},status= status.HTTP_404_NOT_FOUND)
                            elif variable=='@@díaDeBaja':
                                if fecha_baja:
                                    valor_a_sustituir=str(fecha_baja)
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    
                                    return Response({"mensaje":"Falto la fecha de baja"},status= status.HTTP_404_NOT_FOUND)

                            else:
                                valor_a_sustituir=list((modelo_tb.objects.filter(codigo=empleado_codigo).values(valores)[0]).values())[0]
                            
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir
                                    mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                    asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                    asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
        

                if correo_responsable:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    # print(correo_a_enviar= correo_responsable[0]['correo_empresarial'])
                    # correo_a_enviar= 'hoscar161@gmail.com'
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
    if tipo_mensaje == 'Jefe del Responsable : Vacante nueva':
        
        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
    
         
        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                # correo_responsable = Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
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
                            
                            #####################################

                            if variable=='@@JefeResponsableSeleccion':
                                jefe_responsable_codigo_obj= Funcional_empleado.objects.filter(codigo=usuario_responable).values('jefe_inmediato') if (Funcional_empleado.objects.filter(codigo=usuario_responable).values('jefe_inmediato'))[0]['jefe_inmediato'] else None
                                if jefe_responsable_codigo_obj!=None:
                                    jefe_responsable_codigo= jefe_responsable_codigo_obj[0]['jefe_inmediato']
                                    
                                    jefe_responsable = Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo).values('nombre') if Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo) else None
                                    
                                    correo_responsable = Funcional_empleado.objects.filter(codigo=jefe_responsable_codigo).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                                    
                                    valor_a_sustituir = jefe_responsable[0]['nombre'] 
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir)) 
                                else:
                                    correo_responsable=None
                                    valor_a_sustituir_str =''
                                    mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                    asunto= asunto.replace(variable,str(valor_a_sustituir))
                            
                            elif variable=='@@díaDeBaja':
                                if fecha_baja:
                                    valor_a_sustituir=str(fecha_baja)
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                        asunto= asunto.replace(variable,str(valor_a_sustituir))
                                else:
                                    
                                    return Response({"mensaje":"Falto la fecha de baja"},status= status.HTTP_404_NOT_FOUND)

                            else:
                                valor_a_sustituir=list((modelo_tb.objects.filter(codigo=empleado_codigo).values(valores)[0]).values())[0]
                            
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir
                                    mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                    asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                    asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
        

                if correo_responsable!=None:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    # print(correo_a_enviar= correo_responsable[0]['correo_empresarial'])
                    # correo_a_enviar= 'hoscar161@gmail.com'
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
     
    return 1


def postulante_plaza_envio_correo(postulante_id,tipo_mensaje):
    
    correo_responsable=''
    responsable=''
    asunto=''
    hoy=datetime.now().date()
    mensaje=''
    modulo='SELECCION_CONTRATACION'
    if tipo_mensaje == 'Calificación y comentario del Jefe':

        configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Seleccion_Contratacion').values_list('username',flat=True) if User.objects.filter(groups__name='Responsable_Seleccion_Contratacion') else None
    
         
        if usuarios_reponsables!=None:
            
            for usuario_responable in usuarios_reponsables:
                responsable= Funcional_empleado.objects.filter(codigo=usuario_responable).values('nombre') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
                correo_responsable = Funcional_empleado.objects.filter(codigo=usuario_responable).values('correo_empresarial') if Funcional_empleado.objects.filter(codigo=usuario_responable) else None
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
                                
                                #####################################

                                if variable=='@@ResponsableSeleccion':
                                    
                                    if responsable:
                                        valor_a_sustituir=responsable[0]['nombre']
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
                                elif variable=='@@JefeSolicitaPlaza':
                                    jefe_codigo = (seleccion_contratacion_postulante_plaza.objects.filter(id=postulante_id).values('plaza__creador_plaza__username'))[0]['plaza__creador_plaza__username']
                                    jefe = Funcional_empleado.objects.filter(codigo=jefe_codigo).values("nombre")
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
                                elif variable=='@@Fechaactual':
                                    if hoy:
                                        valor_a_sustituir=str(hoy)
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
                                else:
                                    valor_a_sustituir=list((modelo_tb.objects.filter(id=postulante_id).values(valores)[0]).values())[0]
                                
                                    if valor_a_sustituir:
                                        valor_a_sustituir_str = valor_a_sustituir
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                                    else:
                                        valor_a_sustituir_str =''
                                        mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                                        asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
            

                if correo_responsable:
                    correo_a_enviar= correo_responsable[0]['correo_empresarial']
                    # print(correo_a_enviar= correo_responsable[0]['correo_empresarial'])
                    # correo_a_enviar= 'hoscar161@gmail.com'
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                            
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
        else:

            return Response({"mensaje":"No se encontro a ningun responsable de seleccion y contratacion"},status= status.HTTP_404_NOT_FOUND)
     
    return 1
    
class informacin_powerBIviewsets(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_Puesto.objects.all()
    serializer_class = funcional_puestoserializer
    def list(self, request):
        # queryset = Funcional_Puesto.objects.all()
        # serializer_class = funcional_puestoserializer(queryset, many=True)
        
        # puestos=[]
        # vacantes = Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).annotate(estado_puesto= Value('Vacante')).values('codigo','descripcion','descripcion_larga','funcional_empleado__codigo','funcional_empleado__nombre','unidad_organizativa__nombre','unidad_organizativa__codigo','estado_puesto')
        # no_vacantes= Funcional_Puesto.objects.filter().exclude(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).annotate(estado_puesto=Value('No vacante')).values('codigo','descripcion','descripcion_larga','funcional_empleado__codigo','funcional_empleado__nombre','unidad_organizativa__nombre','unidad_organizativa__codigo','estado_puesto')
        # puestos.extend(list(vacantes))
        # puestos.extend(list(no_vacantes))

        # total_vacantes=vacantes.count()
        # total_no_vacantes= no_vacantes.count()
        # total_puestos= total_no_vacantes+ total_vacantes
        
       
        # return Response({"data":puestos,"conteo_vacantes":total_vacantes,"conteo_no_vacantes":total_no_vacantes,"conteo_total":total_puestos})

        plazas_totales=[]
        puestos_vacios= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).annotate(estado_puesto= Value('vacante'),funcional_empleado_codigo=F('funcional_empleado__codigo'),funcional_empleado_nombre=F('funcional_empleado__nombre'),unidad_organizativa_nombre=F('unidad_organizativa__nombre'),unidad_organizativa_codigo=F('unidad_organizativa__codigo')).values('codigo','descripcion','descripcion_larga','funcional_empleado_codigo','funcional_empleado_nombre','unidad_organizativa_nombre','unidad_organizativa_codigo' ,'estado_puesto')
        
        plazas_totales.extend(list(puestos_vacios))
        puestos_ocupados= Funcional_Puesto.objects.filter().exclude(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).annotate(estado_puesto= Value('No vacante'),funcional_empleado_codigo=F('funcional_empleado__codigo'),funcional_empleado_nombre=F('funcional_empleado__nombre'),unidad_organizativa_nombre=F('unidad_organizativa__nombre'),unidad_organizativa_codigo=F('unidad_organizativa__codigo')).values('codigo','descripcion','descripcion_larga','funcional_empleado_codigo','funcional_empleado_nombre','unidad_organizativa_nombre','unidad_organizativa_codigo' ,'estado_puesto')
        plazas_totales.extend(list(puestos_ocupados))
        plazas_totales_count=puestos_ocupados.count()+puestos_vacios.count()
        
        return Response({"puestos":plazas_totales,"puestos totales":plazas_totales_count,"vacantes":puestos_vacios.count(),"No vacantes":puestos_ocupados.count()})