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
sys.setrecursionlimit(100000000)                                                        
from rest_framework import viewsets
from django.db.models.functions import Concat
from django.db.models import Value

class sanciones_categoria_desvinculacionViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = sanciones_categoria_desvinculacion.objects.all()
    serializer_class = sanciones_categoria_desvinculacionserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_categoria_desvinculacion.objects.all()
        serializer = sanciones_categoria_desvinculacionserializer(queryset, many=True)
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
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
            
                queryset =  sanciones_categoria_desvinculacion.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  sanciones_categoria_desvinculacion.objects.filter(**filter_kwargs).count()
                serializer = sanciones_categoria_desvinculacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  sanciones_categoria_desvinculacion.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  sanciones_categoria_desvinculacion.objects.filter().count()
                serializer = sanciones_categoria_desvinculacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                        
                queryset =  sanciones_categoria_desvinculacion.objects.filter(**filter_kwargs).order_by('id')
                serializer = sanciones_categoria_desvinculacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  sanciones_categoria_desvinculacion.objects.filter().order_by('id')
                serializer = sanciones_categoria_desvinculacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class sanciones_motivo_accion_disciplinariaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = sanciones_motivo_accion_disciplinaria.objects.all()
    serializer_class = sanciones_motivo_accion_disciplinariaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_motivo_accion_disciplinaria.objects.all()
        serializer = sanciones_motivo_accion_disciplinariaserializer(queryset, many=True)
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
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
            
                queryset =  sanciones_motivo_accion_disciplinaria.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  sanciones_motivo_accion_disciplinaria.objects.filter(**filter_kwargs).count()
                serializer = sanciones_motivo_accion_disciplinariaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  sanciones_motivo_accion_disciplinaria.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  sanciones_motivo_accion_disciplinaria.objects.filter().count()
                serializer = sanciones_motivo_accion_disciplinariaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                        
                queryset =  sanciones_motivo_accion_disciplinaria.objects.filter(**filter_kwargs).order_by('id')
                serializer = sanciones_motivo_accion_disciplinariaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  sanciones_motivo_accion_disciplinaria.objects.filter().order_by('id')
                serializer = sanciones_motivo_accion_disciplinariaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class sanciones_tipo_accion_disciplinariaViewSet(viewsets.ModelViewSet):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[DjangoModelPermissions]
    queryset = sanciones_tipo_accion_disciplinaria.objects.all()
    serializer_class = sanciones_tipo_accion_disciplinariaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_tipo_accion_disciplinaria.objects.all()
        serializer = sanciones_tipo_accion_disciplinariaserializer(queryset, many=True)
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
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda == 'mostrar_jefe':
                        filter_kwargs['mostrar_jefe'] = filter
            
                queryset =  sanciones_tipo_accion_disciplinaria.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  sanciones_tipo_accion_disciplinaria.objects.filter(**filter_kwargs).count()
                serializer = sanciones_tipo_accion_disciplinariaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  sanciones_tipo_accion_disciplinaria.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  sanciones_tipo_accion_disciplinaria.objects.filter().count()
                serializer = sanciones_tipo_accion_disciplinariaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda == 'mostrar_jefe':
                        filter_kwargs['mostrar_jefe'] = filter
                        
                queryset =  sanciones_tipo_accion_disciplinaria.objects.filter(**filter_kwargs).order_by('id')
                serializer = sanciones_tipo_accion_disciplinariaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  sanciones_tipo_accion_disciplinaria.objects.filter().order_by('id')
                serializer = sanciones_tipo_accion_disciplinariaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class sanciones_medidas_disciplinariasViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = sanciones_medidas_disciplinarias.objects.all()
    serializer_class = sanciones_medidas_disciplinariasserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_medidas_disciplinarias.objects.all()
        serializer = sanciones_medidas_disciplinariasserializer(queryset, many=True)
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
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda == 'mostrar_jefe':
                        filter_kwargs['mostrar_jefe'] = filter
            
                queryset =  sanciones_medidas_disciplinarias.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  sanciones_medidas_disciplinarias.objects.filter(**filter_kwargs).count()
                serializer = sanciones_medidas_disciplinariasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  sanciones_medidas_disciplinarias.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  sanciones_medidas_disciplinarias.objects.filter().count()
                serializer = sanciones_medidas_disciplinariasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda == 'mostrar_jefe':
                        filter_kwargs['mostrar_jefe'] = filter
                        
                queryset =  sanciones_medidas_disciplinarias.objects.filter(**filter_kwargs).order_by('id')
                serializer = sanciones_medidas_disciplinariasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  sanciones_medidas_disciplinarias.objects.filter().order_by('id')
                serializer = sanciones_medidas_disciplinariasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class sanciones_tipo_faltaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = sanciones_tipo_falta.objects.all()
    serializer_class = sanciones_tipo_faltaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_tipo_falta.objects.all()
        serializer = sanciones_tipo_faltaserializer(queryset, many=True)
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
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda == 'mostrar_jefe':
                        filter_kwargs['mostrar_jefe'] = filter
            
                queryset =  sanciones_tipo_falta.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  sanciones_tipo_falta.objects.filter(**filter_kwargs).count()
                serializer = sanciones_tipo_faltaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  sanciones_tipo_falta.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  sanciones_tipo_falta.objects.filter().count()
                serializer = sanciones_tipo_faltaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda == 'mostrar_jefe':
                        filter_kwargs['mostrar_jefe'] = filter
                        
                queryset =  sanciones_tipo_falta.objects.filter(**filter_kwargs).order_by('id')
                serializer = sanciones_tipo_faltaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  sanciones_tipo_falta.objects.filter().order_by('id')
                serializer = sanciones_tipo_faltaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class sanciones_estatusViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = sanciones_estatus.objects.all()
    serializer_class = sanciones_estatusserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_estatus.objects.all()
        serializer = sanciones_estatusserializer(queryset, many=True)
        
        queryset =  sanciones_estatus.objects.filter().order_by('id')
        serializer = sanciones_estatusserializer(queryset, many=True)
        return Response({"data":serializer.data,"count":queryset.count()})

class sanciones_casos_disciplinariosViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = sanciones_casos_disciplinarios.objects.all()
    serializer_class = sanciones_casos_disciplinariosserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_casos_disciplinarios.objects.all()
        serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            print(filter)
            print(tipo_busqueda)
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                    

                if tipo_busqueda:
                    if tipo_busqueda =='caso_disciplinario':
                        filter_kwargs['caso_disciplinario__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='creado_por':
                        filter_kwargs['full_name__icontains'] = filter
                    if tipo_busqueda =='encargado':
                        filter_kwargs['full_name__icontains'] = filter
                    if tipo_busqueda =='empleado':
                        filter_kwargs['codigo_empleado__nombre__icontains'] = filter
                    if tipo_busqueda =='empleado__codigo':
                        filter_kwargs['codigo_empleado__codigo__icontains'] = filter    
                    if tipo_busqueda =='jefe':
                        print(request)
                        empleado=Funcional_empleado.objects.filter(codigo=request.user.username)
                        unidad=list(empleado[0].unidad_organizativa.all().values_list('id',flat=True))
                        colaboradores=list(Funcional_empleado.objects.filter(jefe_inmediato=request.user.username).values_list('id',flat=True))
                        unidades=list(Funcional_Unidad_Organizativa.objects.filter(Dirigido_por=request.user.username).values_list('id',flat=True))
                        colaboradores_equipos=list(Funcional_empleado.objects.filter(unidad_organizativa__id__in=unidades).values_list('id',flat=True))
                        colaboradores.extend(colaboradores_equipos)
                        filter_kwargs['codigo_empleado__id__in'] = colaboradores 
                        filter_contenido= json.loads(self.request.query_params.get('filter'))
                        print('filter_contenido',filter_contenido)
                        tipo_busqueda_secundario = filter_contenido['tipo_busqueda']
                        filter_secundario = filter_contenido['filter']
                        filter_kwargs_secundario={}
                        if tipo_busqueda_secundario:
                            if tipo_busqueda_secundario =='caso_disciplinario':
                                filter_kwargs_secundario['caso_disciplinario__icontains'] = filter_secundario
                            if tipo_busqueda_secundario =='descripcion':
                                filter_kwargs_secundario['descripcion__icontains'] = filter_secundario
                            if tipo_busqueda_secundario == 'id':
                                filter_kwargs_secundario['id'] = filter_secundario
                            if tipo_busqueda_secundario =='creado_por':
                                filter_kwargs_secundario['full_name__icontains'] = filter_secundario
                            if tipo_busqueda_secundario =='encargado':
                                filter_kwargs_secundario['full_name__icontains'] = filter_secundario
                            if tipo_busqueda_secundario =='empleado':
                                filter_kwargs_secundario['codigo_empleado__nombre__icontains'] = filter_secundario
                            if tipo_busqueda_secundario =='empleado__codigo':
                                filter_kwargs_secundario['codigo_empleado__codigo__icontains'] = filter_secundario
                        
                        if tipo_busqueda_secundario=='empleado':
                            queryset =  sanciones_casos_disciplinarios.objects.filter((Q(**filter_kwargs_secundario) | Q(codigo_empleado__codigo__icontains=filter_secundario)),**filter_kwargs).order_by('id')[offset:offset+limit]
                            print('entro1 caso empleado')
                            conteo =  sanciones_casos_disciplinarios.objects.filter(Q(**filter_kwargs_secundario) | Q(codigo_empleado__codigo__icontains=filter_secundario),**filter_kwargs).count()
                            serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                            return Response({"data":serializer.data,"count":conteo})
                        elif tipo_busqueda_secundario=='encargado':
                            # print('entro1 encargado')
                            # print('filter_kwargs_secundario',filter_kwargs_secundario)
                            # print('filter_kwargs',filter_kwargs)
                            queryset =  sanciones_casos_disciplinarios.objects.annotate(full_name=Concat('id_encargado_id__first_name', Value(' '), 'id_encargado_id__last_name')).filter((Q(**filter_kwargs_secundario) | Q(id_encargado__username__icontains=filter_secundario)),**filter_kwargs).order_by('id')[offset:offset+limit]
                            serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                            return Response({"data":serializer.data,"count":queryset.count()})
                        elif tipo_busqueda_secundario=='creado_por':
                            print('entro1 creado por')
                            queryset =  sanciones_casos_disciplinarios.objects.annotate(full_name=Concat('creado_por__first_name', Value(' '), 'creado_por__last_name')).filter((Q(**filter_kwargs_secundario) | Q(creado_por__username__icontains=filter_secundario)),**filter_kwargs).order_by('id')[offset:offset+limit]
                            serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                            return Response({"data":serializer.data,"count":queryset.count()})
                        else:
                            queryset =  sanciones_casos_disciplinarios.objects.filter(**filter_kwargs_secundario,**filter_kwargs).order_by('id')[offset:offset+limit]
                            conteo =  sanciones_casos_disciplinarios.objects.filter(**filter_kwargs_secundario).count()
                            serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                            return Response({"data":serializer.data,"count":conteo}) 
                        
                        

                    
                    
                    
                if tipo_busqueda=='empleado':
                    queryset =  sanciones_casos_disciplinarios.objects.filter(Q(**filter_kwargs) | Q(codigo_empleado__codigo__icontains=filter)).order_by('id')[offset:offset+limit]
                    conteo =  sanciones_casos_disciplinarios.objects.filter(Q(**filter_kwargs) | Q(codigo_empleado__codigo__icontains=filter)).count()
                    serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
                elif tipo_busqueda=='encargado':
                    queryset =  sanciones_casos_disciplinarios.objects.annotate(full_name=Concat('id_encargado_id__first_name', Value(' '), 'id_encargado_id__last_name')).filter(Q(**filter_kwargs) | Q(id_encargado__username__icontains=filter)).order_by('id')[offset:offset+limit]
                    serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                elif tipo_busqueda=='creado_por':
                    queryset =  sanciones_casos_disciplinarios.objects.annotate(full_name=Concat('creado_por__first_name', Value(' '), 'creado_por__last_name')).filter(Q(**filter_kwargs) | Q(creado_por__username__icontains=filter)).order_by('id')[offset:offset+limit]
                    serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset =  sanciones_casos_disciplinarios.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo =  sanciones_casos_disciplinarios.objects.filter(**filter_kwargs).count()
                    serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                 
            else: 
                queryset =  sanciones_casos_disciplinarios.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  sanciones_casos_disciplinarios.objects.filter().count()
                serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                print('caso2')
                if tipo_busqueda:
                    if tipo_busqueda =='caso_disciplinario':
                        filter_kwargs['caso_disciplinario__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='creado_por':
                        filter_kwargs['full_name__icontains'] = filter
                    if tipo_busqueda =='encargado':
                        filter_kwargs['full_name__icontains'] = filter
                    if tipo_busqueda =='empleado':
                        filter_kwargs['codigo_empleado__nombre__icontains'] = filter
                    if tipo_busqueda =='empleado__codigo':
                        filter_kwargs['codigo_empleado__codigo__icontains'] = filter    
                    if tipo_busqueda =='jefe':
                        print('tomo el caso')
                        empleado=Funcional_empleado.objects.filter(codigo=request.user.username)
                        unidad=list(empleado[0].unidad_organizativa.all().values_list('id',flat=True))
                        colaboradores=list(Funcional_empleado.objects.filter(jefe_inmediato=request.user.username).values_list('id',flat=True))
                        unidades=list(Funcional_Unidad_Organizativa.objects.filter(Dirigido_por=request.user.username).values_list('id',flat=True))
                        colaboradores_equipos=list(Funcional_empleado.objects.filter(unidad_organizativa__id__in=unidades).values_list('id',flat=True))
                        colaboradores.extend(colaboradores_equipos)
                        filter_kwargs['codigo_empleado__id__in'] =colaboradores
                        filter_contenido= json.loads(self.request.query_params.get('filter'))
                        print('filter_contenido',filter_contenido)
                        tipo_busqueda_secundario = filter_contenido['tipo_busqueda']
                        filter_secundario = filter_contenido['filter']
                        filter_kwargs_secundario={}
                        if tipo_busqueda_secundario:
                            if tipo_busqueda_secundario =='caso_disciplinario':
                                filter_kwargs_secundario['caso_disciplinario__icontains'] = filter_secundario
                            if tipo_busqueda_secundario =='descripcion':
                                filter_kwargs_secundario['descripcion__icontains'] = filter_secundario
                            if tipo_busqueda_secundario == 'id':
                                filter_kwargs_secundario['id'] = filter_secundario
                            if tipo_busqueda_secundario =='creado_por':
                                filter_kwargs_secundario['full_name__icontains'] = filter_secundario
                            if tipo_busqueda_secundario =='encargado':
                                filter_kwargs_secundario['full_name__icontains'] = filter_secundario
                            if tipo_busqueda_secundario =='empleado':
                                filter_kwargs_secundario['codigo_empleado__nombre__icontains'] = filter_secundario
                            if tipo_busqueda_secundario =='empleado__codigo':
                                filter_kwargs_secundario['codigo_empleado__codigo__icontains'] = filter_secundario
                        
                        if tipo_busqueda_secundario=='empleado':
                            queryset =  sanciones_casos_disciplinarios.objects.filter((Q(**filter_kwargs_secundario) | Q(codigo_empleado__codigo__icontains=filter_secundario)),**filter_kwargs).order_by('id')
                            print('entro1 caso empleado')
                            conteo =  sanciones_casos_disciplinarios.objects.filter(Q(**filter_kwargs_secundario) | Q(codigo_empleado__codigo__icontains=filter_secundario),**filter_kwargs).count()
                            serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                            return Response({"data":serializer.data,"count":conteo})
                        elif tipo_busqueda_secundario=='encargado':
                            # print('entro1 encargado')
                            # print('filter_kwargs_secundario',filter_kwargs_secundario)
                            # print('filter_kwargs',filter_kwargs)
                            queryset =  sanciones_casos_disciplinarios.objects.annotate(full_name=Concat('id_encargado_id__first_name', Value(' '), 'id_encargado_id__last_name')).filter((Q(**filter_kwargs_secundario) | Q(id_encargado__username__icontains=filter_secundario)),**filter_kwargs).order_by('id')
                            serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                            return Response({"data":serializer.data,"count":queryset.count()})
                        elif tipo_busqueda_secundario=='creado_por':
                            print('entro1 creado por')
                            queryset =  sanciones_casos_disciplinarios.objects.annotate(full_name=Concat('creado_por__first_name', Value(' '), 'creado_por__last_name')).filter((Q(**filter_kwargs_secundario) | Q(creado_por__username__icontains=filter_secundario)),**filter_kwargs).order_by('id')
                            serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                            return Response({"data":serializer.data,"count":queryset.count()})
                        else:
                            queryset =  sanciones_casos_disciplinarios.objects.filter(**filter_kwargs_secundario,**filter_kwargs).order_by('id')
                            conteo =  sanciones_casos_disciplinarios.objects.filter(**filter_kwargs_secundario,**filter_kwargs).count()
                            serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                            return Response({"data":serializer.data,"count":conteo}) 
                        

                
                

                if tipo_busqueda=='empleado':
                    queryset =  sanciones_casos_disciplinarios.objects.filter(Q(**filter_kwargs) | Q(codigo_empleado__codigo__icontains=filter)).order_by('id')
                    serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                
                elif tipo_busqueda=='encargado':
                    queryset =  sanciones_casos_disciplinarios.objects.annotate(full_name=Concat('id_encargado_id__first_name', Value(' '), 'id_encargado_id__last_name')).filter(Q(**filter_kwargs) | Q(id_encargado__username__icontains=filter)).order_by('id')
                    serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                elif tipo_busqueda=='creado_por':
                    queryset =  sanciones_casos_disciplinarios.objects.annotate(full_name=Concat('creado_por__first_name', Value(' '), 'creado_por__last_name')).filter(Q(**filter_kwargs) | Q(creado_por__username__icontains=filter)).order_by('id')
                    serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset =  sanciones_casos_disciplinarios.objects.filter(**filter_kwargs).order_by('id')
                    serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  sanciones_casos_disciplinarios.objects.filter().order_by('id')
                serializer = sanciones_casos_disciplinariosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


class sanciones_accion_disciplinariaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = sanciones_accion_disciplinaria.objects.all()
    serializer_class = sanciones_accion_disciplinariaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_accion_disciplinaria.objects.all()
        usuario=request.user
        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
        filter=''
        lista_empleados_a_cargo =listado_empleados_a_cargo(usuario)
        empleados_a_cargo=lista_empleados_a_cargo['empleados']
        # print('empleados_a_cargo',empleados_a_cargo)
        tipo_busqueda=''
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if 'jefe' in grupos:
            if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))

                if filter!='' and tipo_busqueda!='':
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='medida_disciplinaria':
                            filter_kwargs['medida_disciplinaria__id'] = filter
                        if tipo_busqueda =='off_bording':
                            filter_kwargs['off_bording__id'] = filter
                        if tipo_busqueda == 'id':
                            filter_kwargs['id'] = filter
                        if tipo_busqueda =='aplicada_por':
                            filter_kwargs['nombre_completo__icontains'] = filter
                        if tipo_busqueda =='observacion':
                            filter_kwargs['observacion__icontains'] = filter
                        if tipo_busqueda =='codigo_empleado':
                            filter_kwargs['caso_disciplinario__codigo_empleado__codigo__icontains'] = filter
                        if tipo_busqueda =='fecha_vencimiento':
                            filter_kwargs['fecha_vencimiento__date'] = filter
                        if tipo_busqueda =='fecha_creacion':
                            filter_kwargs['fecha_creacion__date'] = filter
                        

                    if tipo_busqueda=='aplicada_por':
                        queryset =  sanciones_accion_disciplinaria.objects.filter(Q(**filter_kwargs)| Q(aplicada_por__username__icontains=filter) ).filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).annotate(nombre_completo=Concat('aplicada_por__first_name', Value(' '), 'aplicada_por__last_name')).order_by('id')[offset:offset+limit]
                        conteo = sanciones_accion_disciplinaria.objects.filter(Q(**filter_kwargs)| Q(aplicada_por__username__icontains=filter) ).filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).count()
                        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})
                    else:
                        queryset =  sanciones_accion_disciplinaria.objects.filter(**filter_kwargs).filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).order_by('id')[offset:offset+limit]
                        conteo = sanciones_accion_disciplinaria.objects.filter(**filter_kwargs).filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).order_by('id').count()
                        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})
                        
                else: 
                    queryset =  sanciones_accion_disciplinaria.objects.filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).order_by('id')[offset:offset+limit]
                    conteo =  sanciones_accion_disciplinaria.objects.filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).count()
                    serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
            else:
                if filter!='' and tipo_busqueda!='':
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='medida_disciplinaria':
                            filter_kwargs['medida_disciplinaria__id'] = filter
                        if tipo_busqueda =='off_bording':
                            filter_kwargs['off_bording__id'] = filter
                        if tipo_busqueda == 'id':
                            filter_kwargs['id'] = filter
                        if tipo_busqueda =='aplicada_por':
                            filter_kwargs['nombre_completo__icontains'] = filter
                        if tipo_busqueda =='observacion':
                            filter_kwargs['observacion__icontains'] = filter
                        if tipo_busqueda =='caso_disciplinario_empleado':
                            filter_kwargs['caso_disciplinario__codigo_empleado__codigo__icontains'] = filter
                    if tipo_busqueda=='aplicada_por':
                        queryset =  sanciones_accion_disciplinaria.objects.filter(Q(**filter_kwargs)| Q(aplicada_por__username__icontains=filter) ).filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).annotate(nombre_completo=Concat('aplicada_por__first_name', Value(' '), 'aplicada_por__last_name')).order_by('id')
                        conteo = sanciones_accion_disciplinaria.objects.filter(Q(**filter_kwargs)| Q(aplicada_por__username__icontains=filter) ).filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).count()
                        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})
                    else:
                        queryset =  sanciones_accion_disciplinaria.objects.filter(**filter_kwargs).filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).order_by('id')
                        conteo = sanciones_accion_disciplinaria.objects.filter(**filter_kwargs).filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).order_by('id').count()
                        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})
                        
                else: 
                    queryset =  sanciones_accion_disciplinaria.objects.filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).order_by('id')
                    conteo =  sanciones_accion_disciplinaria.objects.filter(caso_disciplinario__codigo_empleado__codigo__in=empleados_a_cargo).count()
                    serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
        else:
            if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))

                if filter!='' and tipo_busqueda!='':
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='medida_disciplinaria':
                            filter_kwargs['medida_disciplinaria__id'] = filter
                        if tipo_busqueda =='off_bording':
                            filter_kwargs['off_bording__id'] = filter
                        if tipo_busqueda == 'id':
                            filter_kwargs['id'] = filter
                        if tipo_busqueda =='aplicada_por':
                            filter_kwargs['nombre_completo__icontains'] = filter
                        if tipo_busqueda =='observacion':
                            filter_kwargs['observacion__icontains'] = filter
                        if tipo_busqueda =='codigo_empleado':
                            filter_kwargs['caso_disciplinario__codigo_empleado__codigo__icontains'] = filter
                        if tipo_busqueda =='fecha_vencimiento':
                            filter_kwargs['fecha_vencimiento__date'] = filter
                        if tipo_busqueda =='fecha_creacion':
                            filter_kwargs['fecha_creacion__date'] = filter
                        

                    if tipo_busqueda=='aplicada_por':
                        queryset =  sanciones_accion_disciplinaria.objects.filter(Q(**filter_kwargs)| Q(aplicada_por__username__icontains=filter) ).annotate(nombre_completo=Concat('aplicada_por__first_name', Value(' '), 'aplicada_por__last_name')).order_by('id')[offset:offset+limit]
                        conteo = sanciones_accion_disciplinaria.objects.filter(Q(**filter_kwargs)| Q(aplicada_por__username__icontains=filter) ).count()
                        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})
                    else:
                        queryset =  sanciones_accion_disciplinaria.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                        conteo = sanciones_accion_disciplinaria.objects.filter(**filter_kwargs).count()
                        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})
                        
                else: 
                    queryset =  sanciones_accion_disciplinaria.objects.filter().order_by('id')[offset:offset+limit]
                    conteo =  sanciones_accion_disciplinaria.objects.filter().count()
                    serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
            else:
                if filter!='' and tipo_busqueda!='':
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='medida_disciplinaria':
                            filter_kwargs['medida_disciplinaria__id'] = filter
                        if tipo_busqueda =='off_bording':
                            filter_kwargs['off_bording__id'] = filter
                        if tipo_busqueda == 'id':
                            filter_kwargs['id'] = filter
                        if tipo_busqueda =='aplicada_por':
                            filter_kwargs['nombre_completo__icontains'] = filter
                        if tipo_busqueda =='observacion':
                            filter_kwargs['observacion__icontains'] = filter
                        if tipo_busqueda =='caso_disciplinario_empleado':
                            filter_kwargs['caso_disciplinario__codigo_empleado__codigo__icontains'] = filter
                    if tipo_busqueda=='aplicada_por':
                        queryset =  sanciones_accion_disciplinaria.objects.filter(Q(**filter_kwargs)| Q(aplicada_por__username__icontains=filter) ).annotate(nombre_completo=Concat('aplicada_por__first_name', Value(' '), 'aplicada_por__last_name')).order_by('id')
                        conteo = sanciones_accion_disciplinaria.objects.filter(Q(**filter_kwargs)| Q(aplicada_por__username__icontains=filter) ).count()
                        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})
                    else:
                        queryset =  sanciones_accion_disciplinaria.objects.filter(**filter_kwargs).order_by('id')
                        conteo = sanciones_accion_disciplinaria.objects.filter(**filter_kwargs).count()
                        serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":conteo})
                        
                else: 
                    queryset =  sanciones_accion_disciplinaria.objects.filter().order_by('id')
                    conteo =  sanciones_accion_disciplinaria.objects.filter().count()
                    serializer = sanciones_accion_disciplinariaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})

class sanciones_accion_disciplinaria_correosViewSet(viewsets.ModelViewSet):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[DjangoModelPermissions]
    queryset = sanciones_accion_disciplinaria_correos.objects.all()
    serializer_class = sanciones_accion_disciplinaria_correosserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_accion_disciplinaria_correos.objects.all()
        serializer = sanciones_accion_disciplinaria_correosserializer(queryset, many=True)
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
                    if tipo_busqueda =='accion_disciplinaria__id':
                        filter_kwargs['accion_disciplinaria__id'] = filter
                    if tipo_busqueda =='correo':
                        filter_kwargs['correo__icontains'] = filter
                    if tipo_busqueda == 'fecha_creacion':
                        filter_kwargs['fecha_creacion'] = filter


            
                queryset =  sanciones_accion_disciplinaria_correos.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  sanciones_accion_disciplinaria_correos.objects.filter(**filter_kwargs).count()
                serializer = sanciones_accion_disciplinaria_correosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  sanciones_accion_disciplinaria_correos.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  sanciones_accion_disciplinaria_correos.objects.filter().count()
                serializer = sanciones_accion_disciplinaria_correosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='accion_disciplinaria__id':
                        filter_kwargs['accion_disciplinaria__id'] = filter
                    if tipo_busqueda =='correo':
                        filter_kwargs['correo__icontains'] = filter
                    if tipo_busqueda == 'fecha_creacion':
                        filter_kwargs['fecha_creacion'] = filter
                        
                queryset =  sanciones_accion_disciplinaria_correos.objects.filter(**filter_kwargs).order_by('id')
                serializer = sanciones_accion_disciplinaria_correosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  sanciones_accion_disciplinaria_correos.objects.filter().order_by('id')
                serializer = sanciones_accion_disciplinaria_correosserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        # do your thing here
        serializer = sanciones_accion_disciplinaria_correosserializer(data=request.data)
        if serializer.is_valid(): #MAGIC HAPPENS HERE
            #... Here you do the routine you do when the data is valid
            #You can use the serializer as an object of you Assets Model
            #Save it
            serializer.save()
            # print(serializer.data)
            print(request.data)

            
            # correo_responsable="whernandez@farinter.hn"
            # if correo_responsable:
            #     from_email_responsable= settings.EMAIL_HOST_USER
            #     asunto="Solicitud de autorizacion"
            #     mensaje="Hola, esta Es una solicitud de autorizacion para el proceso de despido para el empleado prueba"
            #     try:
            #         msg_responsable = EmailMultiAlternatives(asunto, mensaje, from_email_responsable, [request.data['correo']])
            #         msg_responsable.send()
            #     except BadHeaderError:
            #         return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
            accion_disciplinaria = request.data['accion_disciplinaria']
            caso_disciplinario_id = sanciones_accion_disciplinaria.objects.filter(id=request.data['accion_disciplinaria']).values('caso_disciplinario__id') if sanciones_accion_disciplinaria.objects.filter(id=accion_disciplinaria) else None
            correo_responsable = request.data['correo_responsable']
            if caso_disciplinario_id != None:
                sanciones_notificaciones_ingreso_correo_manual('Correo manual-Accion disciplinaria',correo_responsable,accion_disciplinaria)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"mensaje":"Caso disciplinario no existe"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #return super().create(request)


#correccion
class sanciones_plantilla_formatos_oficialesViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = sanciones_plantilla_formatos_oficiales.objects.all()
    serializer_class = sanciones_plantilla_formatos_oficialesserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = sanciones_plantilla_formatos_oficiales.objects.all()
        serializer = sanciones_plantilla_formatos_oficialesserializer(queryset, many=True)
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
            
                queryset =  sanciones_plantilla_formatos_oficiales.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  sanciones_plantilla_formatos_oficiales.objects.filter(**filter_kwargs).count()
                serializer = sanciones_plantilla_formatos_oficialesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  sanciones_plantilla_formatos_oficiales.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  sanciones_plantilla_formatos_oficiales.objects.filter().count()
                serializer = sanciones_plantilla_formatos_oficialesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                        
                queryset =  sanciones_plantilla_formatos_oficiales.objects.filter(**filter_kwargs).order_by('id')
                serializer = sanciones_plantilla_formatos_oficialesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  sanciones_plantilla_formatos_oficiales.objects.filter().order_by('id')
                serializer = sanciones_plantilla_formatos_oficialesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class Monitor_bajas(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    #serializer_class = funcional_unidad_organizativabasicoserializer

    def get(self,request):
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
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter
                    print('entro aqui')
                    nodisponibles=list(on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False).values_list('empleado__username',flat=True)) if on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False) else []
                    disponibles = list(Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles).values_list('codigo',flat=True)) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles) else None
                    print('estos son los disponibles')
                    resultado=list(Funcional_empleado.objects.filter(codigo__in=disponibles).filter(**filter_kwargs).values('codigo','situacion_actual__descripcion','relacion_laboral__descripcion','division_personal__descripcion','division_personal__codigo','nombre','puesto__descripcion','fecha_baja','centro_costo__descripcion','centro_costo__codigo','descripcion_motivo_clase_medida','clase_medida').order_by('id')[offset:offset+limit]) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).filter(**filter_kwargs) else None
                    

                    if resultado ==None:
                        return Response({"mensaje":"no existen datos"}, status=status.HTTP_400_BAD_REQUEST)
                    
                    for x in resultado:
                        usuario_id=User.objects.get(username=x['codigo']).id if User.objects.filter(username=x['codigo']) else None
                        x['usuario_id']=usuario_id

        
                    queryset =  resultado
                    conteo =  len(resultado)
                    serializer = resultado
                    return Response({"data":serializer,"count":conteo})  
            else: 
                nodisponibles=list(on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False).values_list('empleado__username',flat=True)) if on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False) else []
                disponibles = list(Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles).values_list('codigo',flat=True)) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles) else None
                resultado=list(Funcional_empleado.objects.filter(codigo__in=disponibles).values('codigo','situacion_actual__descripcion','relacion_laboral__descripcion','division_personal__descripcion','division_personal__codigo','nombre','puesto__descripcion','fecha_baja','centro_costo__descripcion','centro_costo__codigo','descripcion_motivo_clase_medida','clase_medida').order_by('id')[offset:offset+limit]) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()) else None
                

                if resultado ==None:
                    return Response({"mensaje":"no existen datos"}, status=status.HTTP_400_BAD_REQUEST)
                
                for x in resultado:
                    usuario_id=User.objects.get(username=x['codigo']).id if User.objects.filter(username=x['codigo']) else None
                    x['usuario_id']=usuario_id


                queryset =  resultado
                conteo =  len(resultado)
                serializer = resultado
                return Response({"data":serializer,"count":conteo})  
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter
                        
                    nodisponibles=list(on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False).values_list('empleado__username',flat=True)) if on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False) else []
                    disponibles = list(Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles).values_list('codigo',flat=True)) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles) else None
                    resultado=list(Funcional_empleado.objects.filter(codigo__in=disponibles).filter(**filter_kwargs).values('codigo','situacion_actual__descripcion','relacion_laboral__descripcion','division_personal__descripcion','division_personal__codigo','nombre','puesto__descripcion','fecha_baja','centro_costo__descripcion','centro_costo__codigo','descripcion_motivo_clase_medida','clase_medida').order_by('id')) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).filter(**filter_kwargs) else None
                    

                    if resultado ==None:
                        return Response({"mensaje":"no existen datos"}, status=status.HTTP_400_BAD_REQUEST)
                    
                    for x in resultado:
                        usuario_id=User.objects.get(username=x['codigo']).id if User.objects.filter(username=x['codigo']) else None
                        x['usuario_id']=usuario_id

        
                    queryset =  resultado
                    conteo =  len(resultado)
                    serializer = resultado
                    return Response({"data":serializer,"count":conteo})  
            else:
                nodisponibles=list(on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False).values_list('empleado__username',flat=True)) if on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False) else []
                disponibles = list(Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles).values_list('codigo',flat=True)) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles) else None
                resultado=list(Funcional_empleado.objects.filter(codigo__in=disponibles).values('codigo','situacion_actual__descripcion','relacion_laboral__descripcion','division_personal__descripcion','division_personal__codigo','nombre','puesto__descripcion','fecha_baja','centro_costo__descripcion','centro_costo__codigo','descripcion_motivo_clase_medida','clase_medida').order_by('id')) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()) else None                

                if resultado ==None:
                    return Response({"mensaje":"no existen datos"}, status=status.HTTP_400_BAD_REQUEST)
                
                for x in resultado:
                    usuario_id=User.objects.get(username=x['codigo']).id if User.objects.filter(username=x['codigo']) else None
                    x['usuario_id']=usuario_id

    
                queryset =  resultado
                conteo =  len(resultado)
                serializer = resultado
                return Response({"data":serializer,"count":conteo})  

        
        nodisponibles=list(on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False).values_list('empleado__username',flat=True)) if on_off_bording_workflow.objects.filter(tipo_workflow=2,estado=False) else []
        disponibles = list(Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles).values_list('codigo',flat=True)) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()).exclude(codigo__in=nodisponibles) else None
        resultado=list(Funcional_empleado.objects.filter(codigo__in=disponibles).values('codigo','situacion_actual__descripcion','relacion_laboral__descripcion','division_personal__descripcion','division_personal__codigo','nombre','puesto__descripcion','fecha_baja','centro_costo__descripcion','centro_costo__codigo','descripcion_motivo_clase_medida','clase_medida').order_by('id')) if Funcional_empleado.objects.filter(fecha_baja__lte=datetime.now().date()) else None                

        if resultado ==None:
            return Response({"mensaje":"no existen datos"}, status=status.HTTP_400_BAD_REQUEST)
        
        for x in resultado:
            usuario_id=User.objects.get(username=x['codigo']).id if User.objects.filter(username=x['codigo']) else None
            x['usuario_id']=usuario_id


        queryset =  resultado
        conteo =  len(resultado)
        serializer = resultado
        return Response({"resultado":resultado},status=status.HTTP_200_OK)



# APIVIEW DE NOTIFICACIONES
class sanciones_envio_correoViewSet(APIView):
    authentication_classes=[TokenAuthentication]

    def get(self,request):
        caso_disciplinario_id=''
        empleado_id=''
        correo=''
        jefe_empleado=''
        modulo='SANCIONES'
        tipo_mensaje = ''

        if self.request.query_params.get('caso_disciplinario_id'):
            caso_disciplinario_id = self.request.query_params.get('caso_disciplinario_id')

        if self.request.query_params.get('tipo_mensaje'):
            tipo_mensaje=self.request.query_params.get('tipo_mensaje')
        
        if self.request.query_params.get('empleado_id'):
            empleado_id=self.request.query_params.get('empleado_id')
        
        if self.request.query_params.get('correo'):
            correo =self.request.query_params.get('correo')
        
        if self.request.query_params.get('accion_disciplinaria'):
            accion_disciplinaria =self.request.query_params.get('accion_disciplinaria')
        
        if caso_disciplinario_id!='' and tipo_mensaje!='' and correo=='':
            sanciones_notificaciones_envio_correo(tipo_mensaje,caso_disciplinario_id)
            return Response({"mensaje":"recibido","tipo mensaje":tipo_mensaje,"caso disciplinario":caso_disciplinario_id})

        elif tipo_mensaje!='' and empleado_id!='':
            sanciones_notificaciones_tres_o_mas_casos_envio_correo(tipo_mensaje, empleado_id)
            return Response({"mensaje":"recibido","tipo mensaje":tipo_mensaje,"empleado":empleado_id})

        elif correo!='' and tipo_mensaje!='' and accion_disciplinaria!='':
            sanciones_notificaciones_ingreso_correo_manual(tipo_mensaje,correo,accion_disciplinaria)
            return Response({"mensaje":"recibido","tipo mensaje":tipo_mensaje,"enviado a correo":correo,"Id accion disciplinaria":accion_disciplinaria})

        else:
            return Response({"mensaje":"No hemos recibido los valores completos"},status= status.HTTP_404_NOT_FOUND)


    def post(self,request):
        notificaciones = self.request.data['data']
        modulo='SANCIONES'
        caso_disciplinario_id=''
        empleado_id=''
        correo=''
        tipo_mensaje = ''
        accion_disciplinaria = ''
        
        for variable in notificaciones:
            
            
            if "caso_disciplinario_id" in variable:
                caso_disciplinario_id = variable['caso_disciplinario_id']
                

            if "tipo_mensaje" in variable:
                tipo_mensaje = variable['tipo_mensaje']
                

            if "empleado_id" in variable:
                empleado_id=variable['empleado_id']
               

            if "correo" in variable:
                correo = variable['correo']

            if "accion_disciplinaria" in variable:
                accion_disciplinaria=variable['accion_disciplinaria']
               

            if caso_disciplinario_id!='' and tipo_mensaje!='' and correo=='':
                sanciones_notificaciones_envio_correo(tipo_mensaje,caso_disciplinario_id)

               
            elif tipo_mensaje!='' and empleado_id!='':
                sanciones_notificaciones_tres_o_mas_casos_envio_correo(tipo_mensaje, empleado_id)

                
            elif correo!='' and tipo_mensaje!='' and accion_disciplinaria!='':
                sanciones_notificaciones_ingreso_correo_manual(tipo_mensaje,correo,accion_disciplinaria)

            else:
                return Response({"mensaje":"No hemos recibido los valores completos"},status= status.HTTP_404_NOT_FOUND)

         
   
        return Response ({"mensaje":"Proceso exitoso"},status= status.HTTP_200_OK)





# -------------------------------------------
def sanciones_notificaciones_envio_correo(tipo_mensaje,id_vario):
    modulo='SANCIONES'

    if tipo_mensaje == 'Jefe empleado-Caso disciplinario On':
        codigo_jefe=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@jefe_empleado':
                        codigo_empleado =  modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]
                        if codigo_empleado:
                            codigo_jefe= (modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values("codigo_empleado__jefe_inmediato")[0])["codigo_empleado__jefe_inmediato"] 
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    valor_a_sustituir=((Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0])["nombre"]
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
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_jefe = Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial')
                if correo_jefe:
                    correo_a_enviar=correo_jefe[0]['correo_empresarial']
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Jefe responsable sanciones-Caso disciplinario On':
        
        codigo_jefe=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@jefe_responsable_sanciones':
                        creado_por_id= (modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values("creado_por")[0]['creado_por'])
                        Username_creado_por = User.objects.filter(id=creado_por_id).values('username')[0]['username']
                        codigo_jefe = (Funcional_empleado.objects.filter(codigo=Username_creado_por).values('jefe_inmediato')[0])['jefe_inmediato']
                        if codigo_jefe:    
                            if codigo_jefe!= "00000000":
                                valor_a_sustituir=((Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0])["nombre"]
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
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                correo_jefe = Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial')
                
                if correo_jefe:
                    correo_a_enviar=correo_jefe[0]['correo_empresarial']
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Encargado sanciones-Asignar caso disciplinario':
        
        codigo_encargado_sanciones=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@encargado_sanciones':
                        codigo_encargado_sanciones = sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('id_encargado__username')
                        encargado_sanciones_nombre = sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('id_encargado__first_name')
                        
                        if codigo_encargado_sanciones:
                        
                            valor_a_sustituir= encargado_sanciones_nombre[0]["id_encargado__first_name"]
                         
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                       
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))

         
                correo_encargado_sanciones = Funcional_empleado.objects.filter(codigo=codigo_encargado_sanciones[0]['id_encargado__username']).values('correo_empresarial')
               
                if correo_encargado_sanciones:
                    correo_a_enviar=correo_encargado_sanciones[0]['correo_empresarial']
                   
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Jefe empleado-Accion disciplinaria':
        codigo_jefe=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@jefe_empleado':
                        
                        codigo_empleado =  modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]
                        if codigo_empleado:
                            codigo_jefe= (modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values("codigo_empleado__jefe_inmediato")[0])["codigo_empleado__jefe_inmediato"]
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    valor_a_sustituir=((Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0])["nombre"]
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
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_jefe = Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial')
                if correo_jefe:
                    correo_a_enviar=correo_jefe[0]['correo_empresarial']
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Jefe responsable sanciones-Accion disciplinaria':
        codigo_jefe=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@jefe_responsable_sanciones':
                        creado_por_id= (modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values("creado_por")[0]['creado_por'])
                        Username_creado_por = User.objects.filter(id=creado_por_id).values('username')[0]['username']
                        codigo_jefe = (Funcional_empleado.objects.filter(codigo=Username_creado_por).values('jefe_inmediato')[0])['jefe_inmediato']
                        if codigo_jefe:   
                            if codigo_jefe!= "00000000":
                                valor_a_sustituir=((Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0])["nombre"]
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
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_jefe = Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial')
                if correo_jefe:
                    correo_a_enviar=correo_jefe[0]['correo_empresarial']
                   
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Encargado caso-Accion disciplinaria':
        
        codigo_encargado_sanciones=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@encargado_sanciones':
                        
                        codigo_encargado_sanciones = sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('id_encargado__username')
                        encargado_sanciones_nombre = sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('id_encargado__first_name')
                        
                        if codigo_encargado_sanciones:
                        
                            valor_a_sustituir= encargado_sanciones_nombre[0]["id_encargado__first_name"]
                            
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                       
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))

                correo_encargado_sanciones = Funcional_empleado.objects.filter(codigo=codigo_encargado_sanciones[0]['id_encargado__username']).values('correo_empresarial')
                
                if correo_encargado_sanciones:
                    correo_a_enviar=correo_encargado_sanciones[0]['correo_empresarial']
                   
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Jefe empleado-Caso disciplinario Off':
        codigo_jefe=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@jefe_empleado':
                        codigo_empleado =  modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]
                        if codigo_empleado:
                            codigo_jefe= (modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values("codigo_empleado__jefe_inmediato")[0])["codigo_empleado__jefe_inmediato"]

                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    valor_a_sustituir=((Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0])["nombre"]
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
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_jefe = Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial')
                if correo_jefe:
                    correo_a_enviar=correo_jefe[0]['correo_empresarial']
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Jefe responsable sanciones-Caso disciplinario Off':
        codigo_jefe=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@jefe_responsable_sanciones':
                        creado_por_id= (modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values("creado_por")[0]['creado_por'])
                        Username_creado_por = User.objects.filter(id=creado_por_id).values('username')[0]['username']
                        codigo_jefe = (Funcional_empleado.objects.filter(codigo=Username_creado_por).values('jefe_inmediato')[0])['jefe_inmediato']
                        if codigo_jefe:    
                            if codigo_jefe!= "00000000":
                                valor_a_sustituir=((Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0])["nombre"]
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
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                
                correo_jefe = Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial')
                if correo_jefe:
                    correo_a_enviar=correo_jefe[0]['correo_empresarial']
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje == 'Encargado caso-Caso disciplinario Off':
        
        codigo_encargado_sanciones=''
        codigo_empleado=''
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@encargado_sanciones':
                        
                        codigo_encargado_sanciones = sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('id_encargado__username')
                        encargado_sanciones_nombre = sanciones_casos_disciplinarios.objects.filter(id=id_vario).values('id_encargado__first_name')
                        
                        if codigo_encargado_sanciones:
                        
                            valor_a_sustituir= encargado_sanciones_nombre[0]["id_encargado__first_name"]

                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado,id=id_vario).values(valores)[0]).values())[0]
                       
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))

                correo_encargado_sanciones = Funcional_empleado.objects.filter(codigo=codigo_encargado_sanciones[0]['id_encargado__username']).values('correo_empresarial')
                
                if correo_encargado_sanciones:
                    correo_a_enviar=correo_encargado_sanciones[0]['correo_empresarial']
                   
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND) 
    
    return 1
    
def sanciones_notificaciones_tres_o_mas_casos_envio_correo(tipo_mensaje,id_empleado):
    modulo='SANCIONES'

    if tipo_mensaje == 'Jefe empleado-Tres o mas casos creados':
        codigo_jefe=''
        codigo_empleado=''
        empleado= id_empleado
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
                    if variable=='@@jefe_empleado':
                        
                        codigo_empleado =  modelo_tb.objects.filter(codigo_empleado_id=empleado).values(valores)[0]
                       
                        if codigo_empleado:
                            jefe =   sanciones_casos_disciplinarios.objects.filter(codigo_empleado_id=empleado).order_by('id').values("codigo_empleado__jefe_inmediato")
                            codigo_jefe =list(jefe)[-1]['codigo_empleado__jefe_inmediato']
                            if codigo_jefe:    
                                if codigo_jefe!= "00000000":
                                    valor_a_sustituir=((Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0])["nombre"]
                                    
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
                    elif variable=='@@cantidad_casos':
                        cantidad_casos_disciplinarios = len(modelo_tb.objects.filter(codigo_empleado_id=empleado))
                        
                        if cantidad_casos_disciplinarios:
                            valor_a_sustituir=cantidad_casos_disciplinarios
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
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado).values(valores)[0]).values())[0]
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
                           
            correo_jefe = Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial')
            if correo_jefe:
                correo_a_enviar=correo_jefe[0]['correo_empresarial']
                if correo_a_enviar:
                    from_email_jefe= settings.EMAIL_HOST_USER
                    try:
                        msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                        msg_jefe.send()
                    except BadHeaderError:
                        return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
    elif tipo_mensaje == 'Jefe responsable sanciones-Tres o mas casos On':
        codigo_jefe=''
        codigo_empleado=''
        empleado= id_empleado
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
                    if variable=='@@jefe_responsable_sanciones':
                        creado_por = sanciones_casos_disciplinarios.objects.filter(codigo_empleado=empleado).order_by('id').values('creado_por')
                        codigo_creado_por =list(creado_por)[-1]['creado_por']
                        Username_creado_por = User.objects.filter(id=codigo_creado_por).values('username')[0]['username']
                        
                        codigo_jefe = (Funcional_empleado.objects.filter(codigo=Username_creado_por).values('jefe_inmediato')[0])['jefe_inmediato']
                       
                        if codigo_jefe:    
                            if codigo_jefe!= "00000000":
                                valor_a_sustituir=((Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre'))[0])["nombre"]
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
                    elif variable=='@@cantidad_casos':
                        cantidad_casos_disciplinarios = len(modelo_tb.objects.filter(codigo_empleado_id=empleado))
                        
                        if cantidad_casos_disciplinarios:
                            valor_a_sustituir=cantidad_casos_disciplinarios
                            
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                        else:
                            return Response({"mensaje":"casos no encontrados"},status= status.HTTP_404_NOT_FOUND)
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado).values(valores)[0]).values())[0]
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
                           
          
            correo_jefe = Funcional_empleado.objects.filter(codigo=codigo_jefe).values('correo_empresarial')
            if correo_jefe:
                correo_a_enviar=correo_jefe[0]['correo_empresarial']
                
                if correo_a_enviar:
                    from_email_jefe= settings.EMAIL_HOST_USER
                    try:
                        msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                        msg_jefe.send()
                    except BadHeaderError:
                        return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
    elif tipo_mensaje == 'Responsable modulo sanciones-Tres o mas casos On':
        
        codigo_encargado_sanciones=''
        codigo_empleado=''
        empleado= id_empleado
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
                    if variable=='@@encargado_sanciones':
                        busqueda_codigo_encargado_sanciones = sanciones_casos_disciplinarios.objects.filter(codigo_empleado=id_empleado).order_by('id').values('id_encargado__username')
                        codigo_encargado_sanciones = list(busqueda_codigo_encargado_sanciones)[-1]['id_encargado__username']

                        busqueda_encargado_sanciones_nombre = sanciones_casos_disciplinarios.objects.filter(codigo_empleado=id_empleado).values('id_encargado__first_name')
                        encargado_sanciones_nombre = list(busqueda_encargado_sanciones_nombre)[-1]["id_encargado__first_name"]

                        if encargado_sanciones_nombre:
                        
                            valor_a_sustituir= encargado_sanciones_nombre
                           
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                    elif variable=='@@cantidad_casos':
                        cantidad_casos_disciplinarios = len(modelo_tb.objects.filter(codigo_empleado_id=empleado))
                        
                        if cantidad_casos_disciplinarios:
                            valor_a_sustituir=cantidad_casos_disciplinarios
                            
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                        else:
                            
                            return Response({"mensaje":"casos no encontrados"},status= status.HTTP_404_NOT_FOUND)
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado).values(valores)[0]).values())[0]
                       
                        
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))

                correo_encargado_sanciones = Funcional_empleado.objects.filter(codigo=codigo_encargado_sanciones).values('correo_empresarial')
                
                if correo_encargado_sanciones:
                    correo_a_enviar=correo_encargado_sanciones[0]['correo_empresarial']
                    
                    if correo_a_enviar:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_a_enviar])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND) 
    
    return 1

def sanciones_notificaciones_ingreso_correo_manual(tipo_mensaje,correo,accion_disciplinaria_id):
    modulo='SANCIONES'
    if tipo_mensaje == 'Correo manual-Accion disciplinaria':
        codigo_jefe=''
        codigo_empleado=''

        caso_disciplinario_id = sanciones_accion_disciplinaria.objects.filter(id=accion_disciplinaria_id).values('caso_disciplinario_id')[0]['caso_disciplinario_id']
        caso_disciplinario= sanciones_casos_disciplinarios.objects.filter(id=caso_disciplinario_id).values('codigo_empleado_id')
        empleado= caso_disciplinario[0]['codigo_empleado_id']
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
                    if variable=='@@correo_manual':
                        if correo:
                            valor_a_sustituir = correo
                            
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))          
                    elif variable=='@@calculo_prestaciones':
                        calculo_prestaciones_empleado = sanciones_accion_disciplinaria.objects.filter(caso_disciplinario_id=caso_disciplinario_id).values("calculo_prestaciones")
                        if calculo_prestaciones_empleado:
                            valor_a_sustituir=calculo_prestaciones_empleado[0]['calculo_prestaciones']
                            
                            
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                            else:
                                valor_a_sustituir_str =''
                                mensaje= mensaje.replace(variable,str(valor_a_sustituir))
                                asunto= asunto.replace(variable,str(valor_a_sustituir))
                        else:
                            
                            return Response({"mensaje":"calculo de prestaciones no encontrado"},status= status.HTTP_404_NOT_FOUND)
                    else:
                        valor_a_sustituir=list((modelo_tb.objects.filter(codigo_empleado_id=empleado).values(valores)[0]).values())[0]
                       
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir)))
                        else:
                            valor_a_sustituir_str =''
                            mensaje= str(mensaje.replace(variable,str(valor_a_sustituir_str)))
                            asunto= str(asunto.replace(variable,str(valor_a_sustituir_str)))
                           
            if correo:
                correo_jefe=correo
                if correo_jefe:
                    from_email_jefe= settings.EMAIL_HOST_USER
                    try:
                        msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_jefe])
                        msg_jefe.send()
                    except BadHeaderError:
                        return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)               
    
    return 1

def listado_empleados_a_cargo(usuario):
        lista_puestos=[]
        unidad_organizativa = (Funcional_empleado.objects.filter(codigo=usuario).values('unidad_organizativa')[0])['unidad_organizativa']
        bandera=None
        listado=[]
        filtros=[unidad_organizativa]
        puestos=''
       
        
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
        
        # equipo = Funcional_Unidad_Organizativa.objects.filter(id=unidad_organizativa).values_list('unidad_organizativa_jeraquia__id',flat=True)
        equipo =Funcional_Unidad_Organizativa.objects.filter(id__in=listado)
        
        lista_permiso=list(usuario.groups.all().values_list('name',flat=True))
       

        serializer_unidad = funcional_arbol_padre_serializer(uni[0])
        serializer_padre = funcional_arbol_padre_serializer(padre[0]).data if padre else []
        # lista_puestos.append(Funcional_empleado.objects.filter(codigo=codigo_padre).values('posicion__id')[0]['posicion__id'])
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
           
            
        empleados_activos = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(fecha_baja__lt=datetime.now().date()) else None
        # empleados_dados_de_baja = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()) else None
        # puestos = Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None) if Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None) else None
        
        if lider!=None:
            empleados_activos = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) else None
            # empleados_dados_de_baja = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()).exclude(id__in=lideres) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()).exclude(id__in=lideres) else None
            # puestos = Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None).exclude(id__in=lideres) if Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None).exclude(id__in=lideres) else None
        
        #Empleados que pertenecen a determinado jefe encontrados mediante la unidad organizativa
        listado_puestos_empleados_activos=[]
        lista_emple= empleados_activos.values_list('codigo',flat=True)
        listado_puestos_empleados_activos.extend(lista_emple)
        #No activos encontrados mediante la unidad organizativa en la tabla de empleados y la fecha de baja
        # if empleados_dados_de_baja!=None:
        #     lista_puestos.extend(empleados_dados_de_baja.values_list('puesto__codigo',flat=True))
        #No activos encontrados mediante la unidad organizativa
        # if puestos!=None:
        #     lista_puestos.extend( puestos.values_list('codigo',flat=True))
        
        #activos encontrados mediante el jefe inmediato
        empleados_con_jefe_inmediato= Funcional_empleado.objects.filter(jefe_inmediato=usuario).values_list('codigo',flat=True) if Funcional_empleado.objects.filter(jefe_inmediato=usuario).values_list('codigo',flat=True) else None
        #inactivos encontrados mediante el jefe inmediato
        # empleados_dados_baja_jefe_inmediato= Funcional_empleado.objects.filter(jefe_inmediato=usuario,fecha_baja__lt=datetime.now().date()).values_list('puesto__codigo',flat=True) if Funcional_empleado.objects.filter(jefe_inmediato=usuario,fecha_baja__lt=datetime.now().date()) else None
        
        #nuevo llenado de lista activos 
        if empleados_con_jefe_inmediato!=None:
          
            listado_puestos_empleados_activos.extend(empleados_con_jefe_inmediato)
            
             
        #nuevo llenado de lista inactivos
        # if empleados_dados_baja_jefe_inmediato!=None:
        #     lista_puestos.extend(empleados_dados_baja_jefe_inmediato)


        # nueva_lista_plaza_vacantes=[]
        nueva_lista_plazas_activas=[]

        # if len(lista_puestos)!=0:
        #     for item in lista_puestos:
        #         if item not in nueva_lista_plaza_vacantes:
        #             nueva_lista_plaza_vacantes.append(item)

        if len(listado_puestos_empleados_activos)!=0:
            for item in listado_puestos_empleados_activos:
                if item not in nueva_lista_plazas_activas:
                    nueva_lista_plazas_activas.append(item)

        # nueva_lista_plaza_vacantes.sort()
        nueva_lista_plazas_activas.sort()
        data={'empleados':nueva_lista_plazas_activas}
        # print(data)
        return data

