#from tkinter.tix import CheckList
from django.db.models.functions import ExtractYear

from re import sub
from django.contrib.auth.models import User,Group
from django.http.response import Http404
from django.shortcuts import render
from calendar import monthrange
from HEADCOUNT.models.modelos_descriptor_perfil import descriptor_perfil_datos_generales
from HEADCOUNT.serializers.serializers_descriptor_perfil import descriptor_perfil_datos_generalesserializer
from rest_framework.generics import get_object_or_404
from ..serializers import  UsuariosSerializer, formal_puestoserializer, formal_unidad_organizativa_jerarquiaserializer,funcional_puestoserializer,formal_plazaserializer,funcional_plazaserializer
from ..serializers import AutorizarSerializer,LogoutSerializer
from ..serializers import groupserializer,funcional_unidad_organizativaserializer,formal_unidad_organizativaserializer,formal_unidad_organizativaserializer
from ..serializers import Funcional_Relacion_Laboralserializer,Formal_Relacion_Laboralserializer
from ..serializers import Formal_empleadoserializer,Funcional_empleadoserializer
from ..models import Formal_Diagnostico, Formal_Division, Formal_Division_Personal,Funcional_Division_Personal, Formal_Equipo, Formal_Especialidad, Formal_Estado_civil, Formal_Formacion, Formal_Historial_Laboral, Formal_Puesto, Formal_Salud, Formal_Situacion_Actual, Formal_empleado, Funcional_Diagnostico,Funcional_Puesto,Formal_plaza,Funcional_Plaza, Usuario_Log
from ..serializers import Formal_empleadoserializer,Funcional_empleadoserializer,Formal_Divisionserializer,Formal_Organizacionserializer
from ..serializers import Formal_Centro_Costoserializer,Formal_Estado_civilserializer,Funcional_Divisionserializer,Funcional_Centro_Costoserializer
from ..serializers import Funcional_Organizacionserializer,Funcional_Estado_civilserializer,Formal_Parentescoserializer
from ..serializers import Funcional_Parentescoserializer,Funcional_Generoserializer,Formal_Generoserializer
from ..serializers import Formal_Funcionesserializer,Funcional_Funcionesserializer,Formal_Situacion_Actualserializer,Funcional_Situacion_Actualserializer
from ..serializers import Formal_Compañiaserializer,Funcional_Compañiaserializer,Formal_Especialidadserializer,Funcional_Especialidadserializer,Funcional_Contacto_Emergenciaserializer,Formal_Contacto_Emergenciaserializer
from ..serializers import Formal_Dependientes_Economicoserializer,Funcional_Dependientes_Economicoserializer,Funcional_Beneficiario_Seguroserializer,Formal_Beneficiario_Seguroserializer
from ..serializers import Formal_Formacionserializer,Funcional_Formacionserializer,Funcional_Equiposerializer,Formal_Equiposerializer
from ..serializers import Formal_Historial_Laboralserializer,Funcional_Historial_Laboralserializer,formal_unidad_organizativa_jerarquiaserializer
from ..serializers import Formal_empleado_nodojerarquiaserializer,funcional_unidad_organizativa_jerarquiaserializer,Funcional_empleado_nodojerarquiaserializer
from ..serializers import Formal_Tituloserializer,Formal_Institutoserializer,Formal_Diagnosticoserializer,Formal_Saludserializer
from ..serializers import Formal_Educacionserializer
from ..serializers import Funcional_Tituloserializer,Funcional_Institutoserializer,Funcional_Diagnosticoserializer,Funcional_Saludserializer
from ..serializers import Funcional_Educacionserializer,Data_userserializer,Formal_Division_Personalserializer,Funcional_Division_Personalserializer
from ..serializers import Formal_Division_Personalserializer,Funcional_Division_Personalserializer
from ..serializers import Formal_empleado_jerarquiaserializer,Funcional_empleado_jerarquiaserializer
from ..serializers import formal_unidad_organizativabasicoserializer,funcional_unidad_organizativabasicoserializer
from ..serializers import Actualizacion_Contactoserializer,Actualizacion_Dependienteserializer,Actualizacion_Domicilioserializer,Actualizacion_Educacionserializer,Actualizacion_Estado_Civilserializer
from ..serializers import Funcional_Check_Listserializer,Funcional_Empleado_Check_Listserializer
from ..serializers import Formal_Check_Listserializer,Formal_Empleado_Check_Listserializer
from ..serializers import Configuracion_Actualizacion_Empleadoserializer
from ..serializers import Funcional_Laboratorioserializer,Funcional_Vacunaserializer,Funcional_Empleado_Vacunaserializer
from ..serializers import Formal_Laboratorioserializer,Formal_Vacunaserializer,Formal_Empleado_Vacunaserializer
from ..serializers import Formal_Relacion_Laboral_Anteriorserializer,Funcional_Relacion_Laboral_Anteriorserializer
from ..serializers import Funcional_empleado_foto_serializer,Formal_empleado_foto_serializer
from ..serializers import ApiJefesSerializer
from ..serializers import Tiempos_Empleadoserializer,Absentismo_Empleadoserializer,Dias_Laborados_Empleadoserializer
from ..serializers import Usuario_Logserializer
#Segunda Etapa Clima Laboral
from ..serializers import Clima_Objetoserializer,Clima_Sub_Objetoserializer,Clima_Tipo_Preguntaserializer,Clima_Tipo_Herramientaserializer
from ..serializers import Clima_Plantillaserializer,Clima_Plantilla_Preguntasserializer,Clima_Plantilla_Opcionesserializer
from ..serializers import Clima_Segmentoserializer,Clima_Cuestionarioserializer,Clima_Cuestionario_Preguntasserializer
from ..serializers import Clima_Cuestionario_Opcionesserializer,Clima_Usuarios_ResponsablesSerializer,Clima_Campañaserializer
from ..serializers import funcional_arbol_padre_serializer,Funcional_empleado_arbol_jerarquiaserializer
from ..serializers import Clima_Encuestaserializer,Clima_Respuestasserializer,archivos_gestorserializer,archivos_gestor_formatos_oficialesserializer
################################################
from ..models import Formal_Estado_civil, Formal_Puesto, Formal_empleado,Funcional_Puesto,Formal_plaza,Funcional_Plaza
from ..models import Formal_Unidad_Organizativa,Funcional_Unidad_Organizativa
from ..models import Funcional_Relacion_Laboral,Formal_Relacion_Laboral,Funcional_Organizacion
from ..models import Funcional_empleado,Formal_empleado,Formal_Division,Formal_Organizacion,Formal_Centro_Costo,Funcional_Division,Funcional_Centro_Costo
from ..models import Funcional_Estado_civil,Formal_Parentesco,Funcional_Parentesco,Funcional_Genero,Formal_Genero
from ..models import Formal_Funciones,Funcional_Funciones,Formal_Situacion_Actual,Funcional_Situacion_Actual
from ..models import Formal_Compañia,Funcional_Compañia,Formal_Especialidad,Funcional_Especialidad,Funcional_Contacto_Emergencia,Formal_Contacto_Emergencia
from ..models import Formal_Dependientes_Economico,Funcional_Dependientes_Economico,Funcional_Beneficiario_Seguro,Formal_Beneficiario_Seguro
from ..models import Formal_Formacion,Funcional_Formacion,Funcional_Equipo,Formal_Equipo,Formal_Historial_Laboral,Funcional_Historial_Laboral
from ..models import Funcional_Salud,Formal_Salud,Funcional_Diagnostico,Formal_Diagnostico,Formal_Educacion,Funcional_Educacion
from ..models import Formal_Titulo,Formal_Instituto,Funcional_Instituto,Funcional_Titulo
from ..models import Formal_Division_Personal,Funcional_Division_Personal
from ..models import Formal_Asignacion_Equipo,Funcional_Asignacion_Equipo
from ..models import Actualizacion_Contacto,Actualizacion_Dependiente,Actualizacion_Domicilio,Actualizacion_Educacion
from ..models import Actualizacion_Estado_Civil
from ..models import Funcional_Check_List,Funcional_Empleado_Check_List,Formal_Check_List,Formal_Empleado_Check_List
from ..models import Configuracion_Actualizacion_Empleado
from ..models import Funcional_Laboratorio,Funcional_Vacuna,Funcional_Empleado_Vacuna
from ..models import Formal_Laboratorio,Formal_Vacuna,Formal_Empleado_Vacuna
from ..models import Formal_Relacion_Laboral_Anterior,Funcional_Relacion_Laboral_Anterior
from ..models import Formal_Clasificacion,Funcional_Clasificacion
from .. models import Tiempos_Empleado,Absentismo_Empleado,Dias_Laborados_Empleado
from ..models import Usuario_Log,head_clima_pais,head_clima_departamento,head_clima_municipio
#Segunda Etapa Clima Laboral
from ..models import Clima_Objeto,Clima_Sub_Objeto,Clima_Tipo_Pregunta,Clima_Tipo_Herramienta
from ..models import Clima_Plantilla,Clima_Plantilla_Preguntas,Clima_Plantilla_Opciones,Clima_Segmento
from ..models import Clima_Cuestionario,Clima_Cuestionario_Preguntas,Clima_Cuestionario_Opciones,Clima_Campaña,Crjob_log_empledo,Crjob_log_complementaria
from ..models import Clima_Encuesta,Clima_Respuestas,archivos_gestor,archivos_gestor_formatos_oficiales
from ..models import descriptor_perfil_cursos_diplomados_seminario_pasantia
from ..serializers import descriptor_perfil_cursos_diplomados_seminario_pasantia
##############################################################################################
from ..serializers import Formal_Clasificacionserializer,Funcional_Clasificacionserializer
from ..serializers import descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer,head_clima_paisserializer,head_clima_departamentoserializer,head_clima_municipioserializer
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
from datetime import datetime,timedelta,date
import requests
# from .views_seleccion_contratacion import puestos_vacantes


import sys
sys.setrecursionlimit(100000000)

# Create your views here.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
from rest_framework import viewsets

def agent_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,login_url='/'):
    """
    Decorator for views that checks that the user is logged in and is a
    superuser, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u:  u.groups.filter(name='Linea_Etica').exists() ,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
    return render(request,'user/login.html',{})  

class head_clima_paisViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = head_clima_pais.objects.all()
    serializer_class = head_clima_paisserializer
    def list(self, request):
        queryset = head_clima_pais.objects.all()
        serializer_class = head_clima_paisserializer(queryset, many=True)
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
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter

        
                queryset =  head_clima_pais.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  head_clima_pais.objects.filter(**filter_kwargs).count()

                serializer = head_clima_paisserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  head_clima_pais.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  head_clima_pais.objects.filter().count()
                serializer = head_clima_paisserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter
                                       
                queryset =  head_clima_pais.objects.filter(**filter_kwargs).order_by('id')
                conteo =  head_clima_pais.objects.filter(**filter_kwargs).count()
                serializer = head_clima_paisserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  head_clima_pais.objects.filter().order_by('id')
                conteo =  head_clima_pais.objects.filter().count()
                serializer = head_clima_paisserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})



class head_clima_departamentoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = head_clima_departamento.objects.all()
    serializer_class = head_clima_departamentoserializer
    def list(self, request):
        queryset = head_clima_departamento.objects.all()
        serializer_class = head_clima_departamentoserializer(queryset, many=True)
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
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter
                    if tipo_busqueda =='pais_codigo':
                        filter_kwargs['pais__codigo__icontains'] = filter
                    if tipo_busqueda =='pais_id':
                        filter_kwargs['pais__id'] = filter
                    if tipo_busqueda =='pais_nombre':
                        filter_kwargs['pais__nombre__icontains'] = filter

        
                queryset =  head_clima_departamento.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  head_clima_departamento.objects.filter(**filter_kwargs).count()

                serializer = head_clima_departamentoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  head_clima_departamento.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  head_clima_departamento.objects.filter().count()

                serializer = head_clima_departamentoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter
                    if tipo_busqueda =='pais_codigo':
                        filter_kwargs['pais__codigo__icontains'] = filter
                    if tipo_busqueda =='pais_id':
                        filter_kwargs['pais__id'] = filter
                    if tipo_busqueda =='pais_nombre':
                        filter_kwargs['pais__nombre__icontains'] = filter
                                       
                queryset =  head_clima_departamento.objects.filter(**filter_kwargs).order_by('id')
                conteo =  head_clima_departamento.objects.filter(**filter_kwargs).count()
                serializer = head_clima_departamentoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  head_clima_departamento.objects.filter().order_by('id')
                conteo =  head_clima_departamento.objects.filter().count()
                serializer = head_clima_departamentoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

class head_clima_municipioViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = head_clima_municipio.objects.all()
    serializer_class = head_clima_municipioserializer
    def list(self, request):
        queryset = head_clima_municipio.objects.all()
        serializer_class = head_clima_municipioserializer(queryset, many=True)
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
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter
                    if tipo_busqueda =='departamento_id':
                        filter_kwargs['departamento__id'] = filter
                    if tipo_busqueda =='departamento_nombre':
                        filter_kwargs['departamento__nombre__icontains'] = filter
                    if tipo_busqueda =='departamento_pais_id':
                        filter_kwargs['departamento__pais__id'] = filter
                    if tipo_busqueda =='departamento_pais_nombre':
                        filter_kwargs['departamento__pais__nombre__icontains'] = filter

        
                queryset =  head_clima_municipio.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  head_clima_municipio.objects.filter(**filter_kwargs).count()

                serializer = head_clima_municipioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  head_clima_municipio.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  head_clima_municipio.objects.filter().count()

                serializer = head_clima_municipioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter
                    if tipo_busqueda =='departamento_id':
                        filter_kwargs['departamento__id'] = filter
                    if tipo_busqueda =='departamento_nombre':
                        filter_kwargs['departamento__nombre__icontains'] = filter
                    if tipo_busqueda =='departamento_pais_id':
                        filter_kwargs['departamento__pais__id'] = filter
                    if tipo_busqueda =='departamento_pais_nombre':
                        filter_kwargs['departamento__pais__nombre__icontains'] = filter
                                       
                queryset =  head_clima_municipio.objects.filter(**filter_kwargs).order_by('id')
                conteo =  head_clima_municipio.objects.filter(**filter_kwargs).count()
                serializer = head_clima_municipioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 
            else: 
                queryset =  head_clima_municipio.objects.filter().order_by('id')
                conteo =  head_clima_municipio.objects.filter().count()
                serializer = head_clima_municipioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})


class head_clima_pais_consultaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = head_clima_pais.objects.all()
    serializer_class = head_clima_paisserializer
    def list(self, request):
        queryset = head_clima_pais.objects.all()
        serializer_class = head_clima_paisserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if filter!='' and tipo_busqueda!='':
            filter_kwargs={}
            if tipo_busqueda:
                if tipo_busqueda =='id':
                    filter_kwargs['id'] = filter

                pais =list(head_clima_pais.objects.filter(**filter_kwargs).order_by('id').values())
                if pais==None or len(pais)==0:
                    return Response ({"mensaje":"no existe un pais con los parametros recibidos"},status=status.HTTP_400_BAD_REQUEST) 
                departamentos=list(head_clima_departamento.objects.filter(pais_id=pais[0]['id']).order_by('id').values())
                for depto in departamentos:
                    municipio = list(head_clima_municipio.objects.filter(departamento_id=depto['id']).order_by('id').values())
                    depto['municipios']=municipio
                pais[0]['departamentos']=departamentos

                
                return Response({"data":pais},status=status.HTTP_200_OK) 
        else:
            return Response ({"mensaje":"verifique los parametros recibidos"},status=status.HTTP_400_BAD_REQUEST) 



class Formal_PuestoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Puesto.objects.all()
    serializer_class = formal_puestoserializer
    def list(self, request):
        queryset = Formal_Puesto.objects.all()
        objeto= Formal_Puesto.objects.all()
        serializer = formal_puestoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        #print('este es el data',request.data)
        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
             #"id", "codigo", "descripcion"
            if  self.request.query_params.get('filter')!='':
                queryset = Formal_Puesto.objects.filter(descripcion__icontains=filter).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Puesto.objects.filter(descripcion__icontains=filter).order_by('-id')
                serializer = formal_puestoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Puesto.objects.filter().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Puesto.objects.filter().order_by('-id')
                serializer = formal_puestoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif   filter !='':
            queryset = Formal_Puesto.objects.filter(descripcion__icontains=filter).order_by('-id')
            serializer = formal_puestoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Puesto.objects.all().order_by('-id')
            serializer = formal_puestoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_PuestoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Puesto.objects.all()
    serializer_class = funcional_puestoserializer
    def list(self, request):
        queryset = Funcional_Puesto.objects.all()
        objeto= Funcional_Puesto.objects.all()
        serializer = funcional_puestoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        #print('este es el data',request.data)

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
             #"id", "codigo", "descripcion"
            if self.request.query_params.get('filter')!='':
                queryset = Funcional_Puesto.objects.filter(descripcion__icontains=filter).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Puesto.objects.filter(descripcion__icontains=filter).order_by('-id')
                serializer = funcional_puestoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Puesto.objects.filter().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Puesto.objects.filter().order_by('-id')
                serializer = funcional_puestoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            queryset = Funcional_Puesto.objects.filter(descripcion__icontains=filter).order_by('-id')
            serializer = funcional_puestoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Puesto.objects.all().order_by('-id')
            serializer = funcional_puestoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_PlazaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_plaza.objects.all()
    serializer_class = formal_plazaserializer
    def list(self, request):
        queryset = Formal_plaza.objects.all()
        objeto= Formal_plaza.objects.all()
        serializer = formal_plazaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        #print('este es el data',request.data)
        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
             #"id", "codigo", "descripcion"
            if self.request.query_params.get('filter')!='':
                queryset = Formal_plaza.objects.filter(descripcion__icontains=filter).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_plaza.objects.filter(descripcion__icontains=filter).order_by('-id')
                serializer = formal_plazaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_plaza.objects.filter().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_plaza.objects.filter().order_by('-id')
                serializer = formal_plazaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            queryset = Formal_plaza.objects.filter(descripcion__icontains=filter).order_by('-id')
            serializer = formal_plazaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_plaza.objects.all().order_by('-id')
            serializer = formal_plazaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_PlazaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Plaza.objects.all()
    serializer_class = funcional_plazaserializer
    def list(self, request):
        queryset = Funcional_Plaza.objects.all()
        objeto= Funcional_Plaza.objects.all()
        serializer = funcional_plazaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        #print('este es el data',request.data)
        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
             #"id", "codigo", "descripcion"
            if self.request.query_params.get('filter')!='':
                queryset = Funcional_Plaza.objects.filter(descripcion__icontains=filter).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Plaza.objects.filter(descripcion__icontains=filter).order_by('-id')
                serializer = funcional_plazaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Plaza.objects.filter().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Plaza.objects.filter().order_by('-id')[offset:offset+limit]
                serializer = funcional_plazaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            queryset = Funcional_Plaza.objects.filter(descripcion__icontains=filter).order_by('-id')
            serializer = funcional_plazaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Plaza.objects.all().order_by('-id')
            serializer = funcional_plazaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class AutorizacionViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    def get(self, request):
        yourdata= [{"autorizar": 10,"usuario":"whernandez"}, {"autorizar": 12,"usuario":"whernandez"}]
        results = AutorizarSerializer(yourdata, many=True).data

        return Response(results)


class LogoutViewset(APIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        yourdata= [{"autorizar": 10,"usuario":"whernandez"}, {"autorizar": 12,"usuario":"whernandez"}]
        results = AutorizarSerializer(yourdata, many=True).data
        return Response(results)

    def post(self, request):
        serializer = LogoutSerializer(request.data)
        llave=Token.objects.filter(key=serializer['token'].value)
        Token.objects.filter(key=serializer['token'].value).delete()
        if llave.count == 0:
            return Response({"mensaje":"No se encontro el token"},status= status.HTTP_404_NOT_FOUND)

        else:
            return Response({"mensaje":"Nos vemos pronto"},status= status.HTTP_200_OK)
        
       

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = User.objects.all()
    serializer_class = UsuariosSerializer
    def list(self, request):

        queryset = User.objects.all()
        objeto= User.objects.all()
        serializer = UsuariosSerializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        #print('este es el data',request.data)
        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #username, first_name, last_name, email
            if self.request.query_params.get('filter')!='':
                queryset = User.objects.filter(Q(username__icontains=filter)|Q(first_name__icontains=filter)|Q(last_name__icontains=filter)|Q(email__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = User.objects.filter(Q(username__icontains=filter)|Q(first_name__icontains=filter)|Q(last_name__icontains=filter)|Q(email__icontains=filter)).order_by('-id')
                serializer = UsuariosSerializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = User.objects.filter().order_by('-id')[offset:offset+limit]
                queryset2 = User.objects.filter().order_by('-id')
                serializer = UsuariosSerializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            queryset = User.objects.filter(Q(username__icontains=filter)|Q(first_name__icontains=filter)|Q(last_name__icontains=filter)|Q(email__icontains=filter)).order_by('-id')
            serializer = UsuariosSerializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = User.objects.all().order_by('-id')
            serializer = UsuariosSerializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class GroupViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Group.objects.all()
    serializer_class = groupserializer
    def list(self, request):
        queryset = Group.objects.all()
        objeto= Group.objects.all()
        serializer = groupserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        #print('este es el data',request.data)
        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            if self.request.query_params.get('filter')!='':
                queryset = Group.objects.filter(name__icontains=filter).order_by('-id')[offset:offset+limit]
                serializer = groupserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Group.objects.filter().order_by('-id')[offset:offset+limit]
                serializer = groupserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            queryset = Group.objects.filter(name__icontains=filter).order_by('-id')
            serializer = groupserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Group.objects.all().order_by('-id')
            serializer = groupserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
    



class Formal_unidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Unidad_Organizativa.objects.all()
    serializer_class = formal_unidad_organizativaserializer
    def list(self, request):
        #print('este es el data',request.data)
        queryset = Formal_Unidad_Organizativa.objects.all()
        objeto= Formal_Unidad_Organizativa.objects.all()
        serializer = formal_unidad_organizativaserializer(queryset, many=True)
        filter=''
        orga=0
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('orga'):
            orga = self.request.query_params.get('orga')


        if 'orga' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 queryset = Formal_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')[offset:offset+limit]
                 queryset2 = Formal_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')
                 serializer = formal_unidad_organizativaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset2.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
                queryset = Formal_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')
                serializer = formal_unidad_organizativaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})



        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
                serializer = formal_unidad_organizativaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Unidad_Organizativa.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Unidad_Organizativa.objects.all().order_by('-id')
                serializer = formal_unidad_organizativaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = formal_unidad_organizativaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Unidad_Organizativa.objects.all().order_by('-id')
            serializer = formal_unidad_organizativaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
    



class Formal_unidadjerarquiaViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = Formal_Unidad_Organizativa.objects.all()
    serializer_class = formal_unidad_organizativa_jerarquiaserializer
    def list(self, request):
        #print('este es el data',request.data)
        queryset = Formal_Unidad_Organizativa.objects.all()
        objeto= Formal_Unidad_Organizativa.objects.all()
        serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
        filter=''
        orga=0
        padre =0
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('orga'):
            orga = self.request.query_params.get('orga')
        
        if self.request.query_params.get('padre'):
            padre = self.request.query_params.get('padre')


        if 'padre' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 p= Formal_Unidad_Organizativa.objects.filter(id=padre).values_list('unidad_organizativa_jeraquia__id')
                 queryset = Formal_Unidad_Organizativa.objects.filter(id__in=p).order_by('id')[offset:offset+limit]
                 serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
                p= Formal_Unidad_Organizativa.objects.filter(id=padre).values_list('unidad_organizativa_jeraquia__id')
                queryset = Formal_Unidad_Organizativa.objects.filter(id__in=p).order_by('id')
                serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})




        if 'orga' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 queryset = Formal_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')[offset:offset+limit]
                 serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
                queryset = Formal_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')
                serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})



        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Unidad_Organizativa.objects.all().order_by('-id')[offset:offset+limit]
                serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Unidad_Organizativa.objects.all().order_by('-id')
            serializer = formal_unidad_organizativa_jerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Funcional_unidadjerarquiaViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Unidad_Organizativa.objects.all()
    serializer_class = funcional_unidad_organizativa_jerarquiaserializer
    def list(self, request):
        #print('este es el data',request.data)
        queryset = Funcional_Unidad_Organizativa.objects.all()
        objeto= Funcional_Unidad_Organizativa.objects.all()
        serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
        filter=''
        orga=0
        padre =0
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('orga'):
            orga = self.request.query_params.get('orga')
        
        if self.request.query_params.get('padre'):
            padre = self.request.query_params.get('padre')


        if 'padre' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 p= Funcional_Unidad_Organizativa.objects.filter(id=padre).values_list('unidad_organizativa_jeraquia__id')
                 queryset = Funcional_Unidad_Organizativa.objects.filter(id__in=p).order_by('id')[offset:offset+limit]
                 serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
                p= Funcional_Unidad_Organizativa.objects.filter(id=padre).values_list('unidad_organizativa_jeraquia__id')
                queryset = Funcional_Unidad_Organizativa.objects.filter(id__in=p).order_by('id')
                serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})




        if 'orga' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 queryset = Funcional_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')[offset:offset+limit]
                 serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
                queryset = Funcional_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')
                serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})



        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Unidad_Organizativa.objects.all().order_by('-id')[offset:offset+limit]
                serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Unidad_Organizativa.objects.all().order_by('-id')
            serializer = funcional_unidad_organizativa_jerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_unidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Unidad_Organizativa.objects.all()
    serializer_class = funcional_unidad_organizativaserializer
    def list(self, request):
        #print('este es el data',request.data)
        queryset = Funcional_Unidad_Organizativa.objects.all()
        objeto= Funcional_Unidad_Organizativa.objects.all()
        serializer = funcional_unidad_organizativaserializer(queryset, many=True)
        filter=''
        orga=0
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('orga'):
            orga = self.request.query_params.get('orga')


        if 'orga' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 queryset = Funcional_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')[offset:offset+limit]
                 queryset2 = Funcional_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')
                 serializer = funcional_unidad_organizativaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset2.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
                queryset = Funcional_Unidad_Organizativa.objects.filter(sociedad_financiera__id=orga).order_by('id')
                serializer = funcional_unidad_organizativaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})



        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
                serializer = funcional_unidad_organizativaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Unidad_Organizativa.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Unidad_Organizativa.objects.all().order_by('-id')
                serializer = funcional_unidad_organizativaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Unidad_Organizativa.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = funcional_unidad_organizativaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Unidad_Organizativa.objects.all().order_by('-id')
            serializer = funcional_unidad_organizativaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})



class SendmailViewset(APIView):
     def post(self, request):
        subject = 'AURORA Cambio de Contraseña QA'

        message = 'sige el enlace para cambiar tu contraseña' +'esto es'
        from_email = settings.EMAIL_HOST_USER
        to=request.data['correo']
        text_content ='Hemos Recibido una solicitud de cambio de contraseña. Su nueva contraseña sera la siguiente'
        #print('este es el correo',to)   
        conteo= User.objects.filter(email=to).count()
        if conteo > 0:
            try:
                code = get_random_string(10, allowed_chars=string.ascii_uppercase + string.digits)
                text_content = text_content + ': '+code + '\nSe recomienda hacer el cambio de contraseña ya que la misma es temporal'
                password=code
                u = User.objects.get(email=to)
                u.set_password(password)
                u.save()
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                #print('este es el mensaje',msg)
                #msg.attach_alternative(text_content, "text/html")
                msg.send()    
                #send_mail(subject, message, from_email, [to])
                return Response({"mensaje":"El correo ha sido enviado con exito"},status= status.HTTP_200_OK)
            except BadHeaderError:
                return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)

        else:
             return Response({"mensaje":"Favor verificar la cuenta de correo"},status= status.HTTP_404_NOT_FOUND)
class ResetPasswordViewset(APIView):
    def post(self,request):
        conteo= User.objects.filter(Q(username=request.data['username'])|Q(email=request.data['username'])).count()

        if conteo <= 0:
            return Response({"mensaje":"La cuenta no existe"},status= status.HTTP_404_NOT_FOUND)
        if request.data['new_password'] and request.data['password']:
            try:
                usuario=User.objects.get(Q(username=request.data['username'])|Q(email=request.data['username']))
                #print('este es el usuario',usuario)
                user = authenticate(username=usuario.username, password=request.data['password'])
                if user is None:
                    return Response({"mensaje":"Verifique el usuario y contraseña"},status= status.HTTP_404_NOT_FOUND)
                password="password"
                u = User.objects.get(Q(username=request.data['username'])|Q(email=request.data['username']))
                u.set_password(request.data['new_password'])
                u.save()
                return Response({"mensaje":"La operacion fue exitosa"},status= status.HTTP_200_OK)
            except BadHeaderError:
                    return Response({"mensaje":"Ha Sucedido un error,contacta al administrador"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"No hemos recibido tus datos"},status= status.HTTP_404_NOT_FOUND)

class ResetPassword_administradorViewset(APIView):
    def post(self,request):
        conteo= User.objects.filter(Q(username=request.data['username'])|Q(email=request.data['username'])).count()

        if conteo <= 0:
            return Response({"mensaje":"La cuenta no existe"},status= status.HTTP_404_NOT_FOUND)
        if request.data['email'] and request.data['password'] and request.data['username']:
            try:
                u=User.objects.get(username=request.data['username'])
                u.set_password(request.data['password'])
                u.save()
                subject = 'AURORA Cambio de Contraseña prd'
                message = 'el administrador ha realizado un cambio de contraseña para el usuario: ' + request.data['username']
                from_email = settings.EMAIL_HOST_USER
                to=request.data['email']
                text_content ='Hemos procesado una solicitud de cambio de contraseña para el usuario:' +  request.data['username'] + '. Su nueva contraseña sera la siguiente'
                text_content = text_content + ': '+ request.data['password'] + '\nSe recomienda hacer el cambio de contraseña ya que la misma es temporal'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.send()   

                return Response({"mensaje":"La operacion fue exitosa"},status= status.HTTP_200_OK)
            except BadHeaderError:
                    return Response({"mensaje":"Ha Sucedido un error,contacta al administrador"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"No hemos recibido tus datos"},status= status.HTTP_404_NOT_FOUND)



class Formal_RFC_Carga_Masiva(APIView):    
    def post(self,request):
        IRG_PERNR=[{
        "LOW":"00508745",
        "OPTION":"",
        "SIGN":"",
            },
            {
        "LOW":"00503816",
        "OPTION":"",
        "SIGN":"",
            },
            {
        "LOW":"00500463",
        "OPTION":"",
        "SIGN":"",
            },
            {
        "LOW":"00500080",
        "OPTION":"",
        "SIGN":"",
            },
            {
        "LOW":"00501134",
        "OPTION":"",
        "SIGN":"",
            }]
        with Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300') as conx:
        #wit Connection(user='INTERFACESAP', passwd='1nt3rf4c3sF4r!n73r',ashost='172.10.0.6', sysnr='00', client='300') as conx:
            #r2 = conx.call('ZRFC_HEADCOUNT_AURORA',IRG_PERNR=IRG_PERNR)
            #r2 = conx.call('ZRFC_HEADCOUNT_AURORA')
            #for empleado in r2['ET_HEADCOUNT']:
            #    relacion_laboral=Formal_Estado_civil.objects.get(relacion_laboral=empleado['PERSG'])
            #    puesto = Formal_Puesto.objects.get(codigo=empleado['STELL'])
            #    formal_empleado = Formal_empleado(identidad=empleado['ICNUM'], nombre=empleado['ENAME'], codigo=empleado['PERNR'], fecha_ingreso=empleado['INDAT'], division=empleado['WERKS'], centro_costo=empleado['KOSTL'], antiguedad_laboral=empleado['ANTLAB'], fecha_cumpleaños=empleado['GBDAT'], edad=empleado["EDAD"], saldo_vacaciones=empleado["ANZHL"], absentismo=empleado["AWART"], domicilio=empleado["ORT01"], historial_laboral=empleado["ARBGB"])
            #    if  relacion_laboral:
            #        formal_empleado.relacion_laboral=relacion_laboral.codigo
            #    if  puesto:
            #        formal_empleado.puesto.add(relacion_laboral)
                

            for empleado in r2['ET_HEADCOUNT']:
                #print('variable',empleado)
                #print('esta es la relacion',Formal_Relacion_Laboral.objects.get(codigo=empleado['PERSG']))
                relacion_laboral=Formal_Relacion_Laboral.objects.filter(codigo=empleado['PERSG'])[0] if Formal_Relacion_Laboral.objects.filter(codigo=empleado['PERSG']) else None
                #puesto = Formal_Puesto.objects.get(codigo=empleado['PLANS'])
                #print('este es la fecha',datetime.strptime(empleado['INDAT'], '%Y%m%d').date())
                #print('antiguedad_laboral',empleado['ANTLAB'])
                #print('edad',empleado["EDAD"])
                #print('saldo_Vacaciones',empleado["ANZHL"])
                #print('absentismo',empleado["AWART"] )
                absentismo = 0.00 if empleado["AWART"]==""  else empleado["AWART"]
                saldo_vacaciones= 0.00 if empleado["ANZHL"]=="" else empleado["ANZHL"]
                antiguedad_laboral= 0.00 if empleado['ANTLAB']=="" else empleado['ANTLAB']
                
                centro =  Formal_Centro_Costo.objects.filter(codigo=empleado['KOSTL']) if Formal_Centro_Costo.objects.filter(codigo=empleado['KOSTL']) else None                                         
                division =  Formal_Division.objects.filter(codigo=empleado['GSBER']) if Formal_Division.objects.filter(codigo=empleado['GSBER']) else None                                         
                division_personal =  Formal_Division_Personal.objects.filter(codigo=empleado['PERSA']) if Formal_Division_Personal.objects.filter(codigo=empleado['PERSA']) else None                                         
                puesto = Formal_Puesto.objects.filter(codigo=empleado['PLANS']) if Formal_Puesto.objects.filter(codigo=empleado['PLANS']) else None                                         
                posicion = Formal_Funciones.objects.filter(codigo=empleado['STELL']) if Formal_Funciones.objects.filter(codigo=empleado['STELL']) else None                                         
                formacion = Formal_Formacion.objects.filter(codigo=empleado['AUSBI']) if Formal_Formacion.objects.filter(codigo=empleado['AUSBI']) else None                                         
                especialidad = Formal_Especialidad.objects.filter(codigo=empleado['SLTP1']) if Formal_Especialidad.objects.filter(codigo=empleado['SLTP1']) else None                                         
                situacion = Formal_Situacion_Actual.objects.filter(codigo=empleado['STAT2']) if Formal_Situacion_Actual.objects.filter(codigo=empleado['STAT2']) else None                                         
                unidad = Formal_Unidad_Organizativa.objects.filter(codigo=empleado['ORGEH']) if Formal_Unidad_Organizativa.objects.filter(codigo=empleado['ORGEH']) else None                                         
                estado_civil = (Formal_Estado_civil.objects.filter(codigo=empleado['FAMST']) if Formal_Estado_civil.objects.filter(codigo=empleado['FAMST']) else None) if 'FAMST' in empleado else None 
                
                #print(empleado["PERNR_JEFE"])
                obj, created = Formal_empleado.objects.update_or_create(
                    codigo=empleado['PERNR'],
                    defaults={
                        'identidad':empleado['ICNUM'], 
                        'nombre':empleado['ENAME'], 
                        'telefono':empleado['TELNR'], 
                        'celular':empleado['CELNR'],
                        'codigo':empleado['PERNR'], 
                        'correo_empresarial':empleado['EMAIL_EMP'].lower(),
                        'correo_personal':empleado['EMAIL_PER'].lower(),
                        'fecha_ingreso':datetime.strptime(empleado['INDAT'], '%Y%m%d').date() if empleado['INDAT']!='' else None,
                        'fecha_baja':datetime.strptime(empleado['OUTDAT'], '%Y%m%d').date() if empleado['OUTDAT']!='' else None,
                        'relacion_laboral':relacion_laboral,
                        'genero':empleado['SEXO'], 
                        'tipo_sangre':empleado['TIPO_SANGRE'], 
                        'antiguedad_laboral':antiguedad_laboral, 
                        'fecha_cumpleaños':datetime.strptime(empleado['GBDAT'], '%Y%m%d').date(), 
                        'edad':empleado["EDAD"], 
                        'saldo_vacaciones':saldo_vacaciones, 
                        #'absentismo':absentismo, 
                        'domicilio':empleado["ORT01"], 
                        #'historial_laboral':empleado["ARBGB"]
                        'jefe_inmediato':empleado["PERNR_JEFE"],
                        'estado_civil':estado_civil[0] if estado_civil!=None else None,
                        'clase_medida':empleado["MASSN"],
                        'descripcion_clase_medida':empleado["MASSN_DESC"],
                        'motivo_clase_medida':empleado["MASSG_IN"],
                        'descripcion_motivo_clase_medida':empleado["MASSG_IN_DESC"],
                    }
                )

                for equipo in empleado['T_EQASIG']:
                    asignacion = Formal_Equipo.objects.filter(codigo=equipo['ANLN1']) if Formal_Equipo.objects.filter(codigo=equipo['ANLN1']) else None
                    if asignacion!=None:
                        equi, created = Formal_Asignacion_Equipo.objects.update_or_create(
                        empleado=obj,
                        equipo=asignacion[0],
                        defaults={
                            'empleado':obj,
                            'equipo':asignacion[0],
                        }
                        )


                Formal_Historial_Laboral.objects.filter(empleado=obj).delete()
                for historial in empleado['T_HIST_TRAB']:
                    puesto_anterior = Formal_Relacion_Laboral_Anterior.objects.filter(codigo=historial['RELACION_LAB'])[0] if Formal_Relacion_Laboral_Anterior.objects.filter(codigo=historial['RELACION_LAB']) else None
                    histo, created = Formal_Historial_Laboral.objects.update_or_create(
                    empleado=obj,
                    descripcion=historial['NOMBRE_EMP'],
                    defaults={
                        'descripcion':historial['NOMBRE_EMP'], 
                        'empleado':obj, 
                        'puesto':puesto_anterior
                    }
                )
                Formal_Contacto_Emergencia.objects.filter(empleado=obj).delete()
                for contacto_emer in empleado['T_CONTACT_EMERG']:
                    sunombre=contacto_emer['NOMBRE'] +' '+ contacto_emer['APELLIDO']
                    contac, created = Formal_Contacto_Emergencia.objects.update_or_create(
                    empleado=obj,
                    nombre=contacto_emer['NOMBRE'],
                    defaults={
                        'nombre':contacto_emer['NOMBRE'], 
                        'apellido':contacto_emer['APELLIDO'],
                        'identidad':contacto_emer['NUM_ID'],
                        'telefono':contacto_emer['TELEFONO'],
                        'empleado':obj, 
                    }
                )
                Formal_Dependientes_Economico.objects.filter(empleado=obj).delete()
                for depend in empleado['T_DEPEND_ECO']:
                    if  depend['SUBTY']!= '7':
                        sunombre=depend['NOMBRE'] +' '+ depend['APELLIDO_1']+' '+ depend['APELLIDO_2']
                        parent, created = Formal_Parentesco.objects.update_or_create(
                        codigo=depend['PARENTESCO'],
                        defaults={
                            'codigo':depend['PARENTESCO'], 
                            'nombre':depend['PARENTESCO_DESC'], 
                            
                        }
                        )
                        contac, created = Formal_Dependientes_Economico.objects.update_or_create(
                        empleado=obj,
                        identidad=depend['NUM_ID'],
                        secuencia=depend['SEC_PARENT'],
                        subtipo=depend['SUBTY'],
                        defaults={
                            'nombre':depend['NOMBRE'], 
                            'primer_apellido':depend['APELLIDO_1'],
                            'segundo_apellido':depend['APELLIDO_2'],
                            'empleado':obj, 
                            'identidad':depend['NUM_ID'],
                            'subtipo':depend['SUBTY'],
                            'secuencia':depend['SEC_PARENT'],
                            'dependiente':depend['DEPENDIENTE'],
                            #'parentesco':contac,
                            'fecha_nacimiento':datetime.strptime(depend['FECHA_NAC'], '%Y%m%d').date(),

                        }
                        )
                        contac.parentesco=parent
                        contac.save()

                for enfermedad in empleado['T_ENFERMEDADES']:
                    #print(empleado['T_ENFERMEDADES'])
                    diagnostico =  Formal_Diagnostico.objects.filter(codigo=enfermedad['RESUL']) if Formal_Diagnostico.objects.filter(codigo=enfermedad['RESUL']) else None                                         
                    if diagnostico:
                        fecha = enfermedad['EXDAT'] if  'EXDAT'  in enfermedad else None
                        diag, created = Formal_Salud.objects.update_or_create(
                        empleado=obj,
                        diagnostico=diagnostico[0],
                        defaults={
                            'empleado':obj, 
                            'diagnostico':diagnostico[0],
                            'fecha': datetime.strptime(fecha, '%Y%m%d').date() if fecha !='' else None, 
                            'enfermedad':enfermedad['DIANR'],
                        }
                )
                Formal_Educacion.objects.filter(empleado=obj).delete()
                for educacion in empleado['T_EDUCACION']:
                    formacion =  Formal_Formacion.objects.filter(codigo=educacion['AUSBI'])[0] if Formal_Formacion.objects.filter(codigo=educacion['AUSBI']) else None                                         
                    especialidad =  Formal_Especialidad.objects.filter(codigo=educacion['FACHR'])[0] if Formal_Especialidad.objects.filter(codigo=educacion['FACHR']) else None                                         
                    titulo = Formal_Titulo.objects.filter(codigo=educacion['SLABS'])[0] if Formal_Titulo.objects.filter(codigo=educacion['SLABS']) else None                                         
                    instituto = Formal_Instituto.objects.filter(codigo=educacion['SLART'])[0] if Formal_Instituto.objects.filter(codigo=educacion['SLART']) else None                                         
                #print('esta es la especilidad',especialidad)
                    if formacion:
                        
                        edu, created = Formal_Educacion.objects.update_or_create(
                        empleado=obj,
                        formacion=formacion,
                        especialidad=especialidad,
                        instituto=instituto,
                        titulo=titulo,
                        defaults={
                            'empleado':obj, 
                            'formacion':formacion,
                            'especialidad':especialidad,
                            'instituto':instituto,
                            'titulo':titulo,
                            'fecha_inicio': datetime.strptime(educacion['FECHA_INI'], '%Y%m%d').date(),
                            'fecha_fin': datetime.strptime(educacion['FECHA_FIN'], '%Y%m%d').date(),
                            'subtipo':educacion['SUBTY'],
                        }
                        )
                        # if especialidad!=None:
                        #     edu.especialidad=especialidad
                            


                # if formacion!=None:
                #     for f in formacion:
                        
                #         obj.formacion.add(f)
                #         obj.save()
                # if especialidad!=None:
                #     for e in especialidad:
                #         obj.especialidad.add(e)
                #         obj.save()
                    
                if puesto!=None:
                    obj.puesto.clear()
                    obj.save()
                    for p in puesto:
                        #print(p.codigo)
                        obj.puesto.add(p)
                        obj.save()
                
                if posicion!=None:
                    for pp in posicion:
                        #print(p.codigo)
                        obj.posicion.add(pp)
                        obj.save()

                if unidad!=None:
                    obj.unidad_organizativa.clear()
                    obj.save()
                    for u in unidad:
                        #print(p.codigo)
                        obj.unidad_organizativa.add(u)
                        obj.save()
                

                

                if centro!=None:
                    for cc in centro:
                        obj.centro_costo=cc
                        obj.save()
                if division!=None:
                    for dv in division:
                        obj.division=dv
                        obj.save()

                if division_personal!=None:
                    for dv in division_personal:
                        obj.division_personal=dv
                        obj.save()

                if situacion!=None:
                    for sit in situacion:
                        obj.situacion_actual=sit
                        obj.save()

                
            #return Response(status= status.HTTP_200_OK)
            return Response(r2,status= status.HTTP_200_OK)


class Funcional_RFC_Carga_Masiva(APIView):    
    def post(self,request):
        IRG_PERNR=[{
        "LOW":"00500046",
        "OPTION":"",
        "SIGN":"",
            }]
        with Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300') as conx:
        #with Connection(user='INTERFACESAP', passwd='1nt3rf4c3sF4r!n73r',ashost='172.10.0.6', sysnr='00', client='300') as conx:
            #r2 = conx.call('ZRFC_HEADCOUNT_AURORA',IRG_PERNR=IRG_PERNR)
            r2 = conx.call('ZRFC_HEADCOUNT_AURORA')
            #for empleado in r2['ET_HEADCOUNT']:
            #    relacion_laboral=Funcional_Estado_civil.objects.get(relacion_laboral=empleado['PERSG'])
            #    puesto = Funcional_Puesto.objects.get(codigo=empleado['STELL'])
            #    formal_empleado = Funcional_empleado(identidad=empleado['ICNUM'], nombre=empleado['ENAME'], codigo=empleado['PERNR'], fecha_ingreso=empleado['INDAT'], division=empleado['WERKS'], centro_costo=empleado['KOSTL'], antiguedad_laboral=empleado['ANTLAB'], fecha_cumpleaños=empleado['GBDAT'], edad=empleado["EDAD"], saldo_vacaciones=empleado["ANZHL"], absentismo=empleado["AWART"], domicilio=empleado["ORT01"], historial_laboral=empleado["ARBGB"])
            #    if  relacion_laboral:
            #        formal_empleado.relacion_laboral=relacion_laboral.codigo
            #    if  puesto:
            #        formal_empleado.puesto.add(relacion_laboral)
                

            for empleado in r2['ET_HEADCOUNT']:
                Crjob_log_empledo.objects.create(empleado=str(empleado))
                #print('variable',empleado)
                #print('esta es la relacion',Funcional_Relacion_Laboral.objects.get(codigo=empleado['PERSG']))
                relacion_laboral=Funcional_Relacion_Laboral.objects.filter(codigo=empleado['PERSG'])[0] if Funcional_Relacion_Laboral.objects.filter(codigo=empleado['PERSG']) else None
                #puesto = Funcional_Puesto.objects.get(codigo=empleado['PLANS'])
                #print('este es la fecha',datetime.strptime(empleado['INDAT'], '%Y%m%d').date())
                #print('antiguedad_laboral',empleado['ANTLAB'])
                #print('edad',empleado["EDAD"])
                #print('saldo_Vacaciones',empleado["ANZHL"])
                #print('absentismo',empleado["AWART"] )
                absentismo = 0.00 if empleado["AWART"]==""  else empleado["AWART"]
                saldo_vacaciones= 0.00 if empleado["ANZHL"]=="" else empleado["ANZHL"]
                antiguedad_laboral= 0.00 if empleado['ANTLAB']=="" else empleado['ANTLAB']
                
                centro =  Funcional_Centro_Costo.objects.filter(codigo=empleado['KOSTL']) if Funcional_Centro_Costo.objects.filter(codigo=empleado['KOSTL']) else None                                         
                division =  Funcional_Division.objects.filter(codigo=empleado['GSBER']) if Funcional_Division.objects.filter(codigo=empleado['GSBER']) else None                                         
                division_personal =  Funcional_Division_Personal.objects.filter(codigo=empleado['PERSA']) if Funcional_Division_Personal.objects.filter(codigo=empleado['PERSA']) else None                                         
                puesto = Funcional_Puesto.objects.filter(codigo=empleado['PLANS']) if Funcional_Puesto.objects.filter(codigo=empleado['PLANS']) else None                                         
                posicion = Funcional_Funciones.objects.filter(codigo=empleado['STELL']) if Funcional_Funciones.objects.filter(codigo=empleado['STELL']) else None   
                formacion = Funcional_Formacion.objects.filter(codigo=empleado['AUSBI']) if Funcional_Formacion.objects.filter(codigo=empleado['AUSBI']) else None                                         
                especialidad = Funcional_Especialidad.objects.filter(codigo=empleado['SLTP1']) if Funcional_Especialidad.objects.filter(codigo=empleado['SLTP1']) else None                                         
                situacion = Funcional_Situacion_Actual.objects.filter(codigo=empleado['STAT2']) if Funcional_Situacion_Actual.objects.filter(codigo=empleado['STAT2']) else None                                         
                unidad = Funcional_Unidad_Organizativa.objects.filter(codigo=empleado['ORGEH']) if Funcional_Unidad_Organizativa.objects.filter(codigo=empleado['ORGEH']) else None                                         
                estado_civil = (Funcional_Estado_civil.objects.filter(codigo=empleado['FAMST']) if Funcional_Estado_civil.objects.filter(codigo=empleado['FAMST']) else None) if 'FAMST' in empleado else None 
                
                #print(empleado["PERNR_JEFE"])
                obj, created = Funcional_empleado.objects.update_or_create(
                    codigo=empleado['PERNR'],
                    defaults={
                        'identidad':empleado['ICNUM'], 
                        'nombre':empleado['ENAME'], 
                        'telefono':empleado['TELNR'], 
                        'celular':empleado['CELNR'],
                        'codigo':empleado['PERNR'], 
                        'correo_empresarial':empleado['EMAIL_EMP'].lower(),
                        'correo_personal':empleado['EMAIL_PER'].lower(),
                        'fecha_ingreso':datetime.strptime(empleado['INDAT'], '%Y%m%d').date() if empleado['INDAT']!='' else None,
                        'fecha_baja':datetime.strptime(empleado['OUTDAT'], '%Y%m%d').date() if empleado['OUTDAT']!='' else None,
                        'relacion_laboral':relacion_laboral,
                        'genero':empleado['SEXO'], 
                        'tipo_sangre':empleado['TIPO_SANGRE'], 
                        'antiguedad_laboral':antiguedad_laboral, 
                        'fecha_cumpleaños':datetime.strptime(empleado['GBDAT'], '%Y%m%d').date(), 
                        'edad':empleado["EDAD"], 
                        'saldo_vacaciones':saldo_vacaciones, 
                        #'absentismo':absentismo, 
                        'domicilio':empleado["ORT01"], 
                        #'historial_laboral':empleado["ARBGB"]
                        'jefe_inmediato':empleado["PERNR_JEFE"],
                        'estado_civil':estado_civil[0] if estado_civil!=None else None,
                        'clase_medida':empleado["MASSN"],
                        'descripcion_clase_medida':empleado["MASSN_DESC"],
                        'motivo_clase_medida':empleado["MASSG_IN"],
                        'descripcion_motivo_clase_medida':empleado["MASSG_IN_DESC"],
                    }
                )

                for equipo in empleado['T_EQASIG']:
                    asignacion = Funcional_Equipo.objects.filter(codigo=equipo['ANLN1']) if Funcional_Equipo.objects.filter(codigo=equipo['ANLN1']) else None
                    if asignacion!=None:
                        equi, created = Funcional_Asignacion_Equipo.objects.update_or_create(
                        empleado=obj,
                        equipo=asignacion[0],
                        defaults={
                            'empleado':obj,
                            'equipo':asignacion[0],
                        }
                        )


                Funcional_Historial_Laboral.objects.filter(empleado=obj).delete()
                for historial in empleado['T_HIST_TRAB']:
                    puesto_anterior = Funcional_Relacion_Laboral_Anterior.objects.filter(codigo=historial['RELACION_LAB'])[0] if Funcional_Relacion_Laboral_Anterior.objects.filter(codigo=historial['RELACION_LAB']) else None
                    histo, created = Funcional_Historial_Laboral.objects.update_or_create(
                    empleado=obj,
                    descripcion=historial['NOMBRE_EMP'],
                    defaults={
                        'descripcion':historial['NOMBRE_EMP'], 
                        'empleado':obj, 
                        'puesto':puesto_anterior
                    }
                )
                Funcional_Contacto_Emergencia.objects.filter(empleado=obj).delete()
                for contacto_emer in empleado['T_CONTACT_EMERG']:
                    sunombre=contacto_emer['NOMBRE'] +' '+ contacto_emer['APELLIDO']
                    contac, created = Funcional_Contacto_Emergencia.objects.update_or_create(
                    empleado=obj,
                    nombre=contacto_emer['NOMBRE'],
                    defaults={
                            'nombre':contacto_emer['NOMBRE'], 
                            'apellido':contacto_emer['APELLIDO'],
                            'identidad':contacto_emer['NUM_ID'],
                            'telefono':contacto_emer['TELEFONO'],
                            'empleado':obj, 
                        }
                )
                Funcional_Dependientes_Economico.objects.filter(empleado=obj).delete()
                for depend in empleado['T_DEPEND_ECO']:
                    if depend['SUBTY']!= '7':
                        sunombre=depend['NOMBRE'] +' '+ depend['APELLIDO_1']+' '+ depend['APELLIDO_2']
                        parent, created = Funcional_Parentesco.objects.update_or_create(
                        codigo=depend['PARENTESCO'],
                        defaults={
                            'codigo':depend['PARENTESCO'], 
                            'nombre':depend['PARENTESCO_DESC'], 
                            
                        }
                        )
                        contac, created = Funcional_Dependientes_Economico.objects.update_or_create(
                        empleado=obj,
                        identidad=depend['NUM_ID'],
                        secuencia=depend['SEC_PARENT'],
                        subtipo=depend['SUBTY'],
                        defaults={
                            'nombre':depend['NOMBRE'], 
                            'primer_apellido':depend['APELLIDO_1'],
                            'segundo_apellido':depend['APELLIDO_2'],
                            'empleado':obj, 
                            'identidad':depend['NUM_ID'],
                            'subtipo':depend['SUBTY'],
                            'secuencia':depend['SEC_PARENT'],
                            'dependiente':depend['DEPENDIENTE'],
                            #'parentesco':contac,
                            'fecha_nacimiento':datetime.strptime(depend['FECHA_NAC'], '%Y%m%d').date(),

                        }
                        )
                        contac.parentesco=parent
                        contac.save()

                for enfermedad in empleado['T_ENFERMEDADES']:
                    #print(empleado['T_ENFERMEDADES'])
                    diagnostico =  Funcional_Diagnostico.objects.filter(codigo=enfermedad['RESUL']) if Funcional_Diagnostico.objects.filter(codigo=enfermedad['RESUL']) else None                                         
                    if diagnostico:
                        fecha = enfermedad['EXDAT'] if  'EXDAT'  in enfermedad else None
                        diag, created = Funcional_Salud.objects.update_or_create(
                        empleado=obj,
                        diagnostico=diagnostico[0],
                        defaults={
                            'empleado':obj, 
                            'diagnostico':diagnostico[0],
                            'fecha': datetime.strptime(fecha, '%Y%m%d').date() if fecha !='' else None, 
                            'enfermedad':enfermedad['DIANR'],
                        }
                )
                Funcional_Educacion.objects.filter(empleado=obj).delete()
                for educacion in empleado['T_EDUCACION']:
                    formacion =  Funcional_Formacion.objects.filter(codigo=educacion['AUSBI'])[0] if Funcional_Formacion.objects.filter(codigo=educacion['AUSBI']) else None                                         
                    especialidad =  Funcional_Especialidad.objects.filter(codigo=educacion['FACHR'])[0] if Funcional_Especialidad.objects.filter(codigo=educacion['FACHR']) else None                                         
                    titulo = Funcional_Titulo.objects.filter(codigo=educacion['SLABS'])[0] if Funcional_Titulo.objects.filter(codigo=educacion['SLABS']) else None                                         
                    instituto = Funcional_Instituto.objects.filter(codigo=educacion['SLART'])[0] if Funcional_Instituto.objects.filter(codigo=educacion['SLART']) else None                                         
                    
                    if formacion:
                        edu, created = Funcional_Educacion.objects.update_or_create(
                        empleado=obj,
                        formacion=formacion,
                        especialidad=especialidad,
                        instituto=instituto,
                        titulo=titulo,
                        defaults={
                            'empleado':obj, 
                            'formacion':formacion,
                            'especialidad':especialidad,
                            'instituto':instituto,
                            'titulo':titulo,
                            'fecha_inicio': datetime.strptime(educacion['FECHA_INI'], '%Y%m%d').date(),
                            'fecha_fin': datetime.strptime(educacion['FECHA_FIN'], '%Y%m%d').date(),
                            'subtipo':educacion['SUBTY'],
                        }
                        )
                        # if especialidad!=None:
                        #     edu.especialidad=especialidad
                            


                # if formacion!=None:
                #     for f in formacion:
                        
                #         obj.formacion.add(f)
                #         obj.save()
                # if especialidad!=None:
                #     for e in especialidad:
                #         obj.especialidad.add(e)
                #         obj.save()
                    
                if puesto!=None:
                    obj.puesto.clear()
                    obj.save()
                    for p in puesto:
                        #print(p.codigo)
                        obj.puesto.add(p)
                        obj.save()
                        
                if posicion!=None:
                    for pp in posicion:
                        #print(p.codigo)
                        obj.posicion.add(pp)
                        obj.save()
                
                if unidad!=None:
                    obj.unidad_organizativa.clear()
                    obj.save()
                    for u in unidad:
                        #print(p.codigo)
                        obj.unidad_organizativa.add(u)
                        obj.save()
                

                

                if centro!=None:
                    for cc in centro:
                        obj.centro_costo=cc
                        obj.save()
                if division!=None:
                    for dv in division:
                        obj.division=dv
                        obj.save()

                if division_personal!=None:
                    for dv in division_personal:
                        obj.division_personal=dv
                        obj.save()

                if situacion!=None:
                    for sit in situacion:
                        obj.situacion_actual=sit
                        obj.save()
                
            #return Response(status= status.HTTP_200_OK)
            return Response(r2,status= status.HTTP_200_OK)


class Formal_RFC_Carga_Masiva_Complementaria(APIView):    
    def get(self,request):
        with Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300') as conx:
        #with Connection(user='INTERFACESAP', passwd='1nt3rf4c3sF4r!n73r',ashost='172.10.0.6', sysnr='00', client='300') as conx:
            #r2 = conx.call('ZRFC_HEADCOUNT_AURORA',IRG_PERNR=IRG_PERNR)
            r2 = conx.call('ZRFC_SUPPL_TABLES_AURORA')
            for division in r2['ET_DIVISIONES']:
                  obj, created = Formal_Division.objects.update_or_create(
                    codigo=division['GSBER'],
                    defaults={
                        'codigo':division['GSBER'], 
                        'descripcion':division['GTEXT'], 

                    }
                )

            for division in r2['ET_DIVISIONES_PERSA']:
                  obj, created = Formal_Division_Personal.objects.update_or_create(
                    codigo=division['PERSA'],
                    defaults={
                        'codigo':division['PERSA'], 
                        'descripcion':division['NAME1'], 

                    }
                )
            if 'ET_EQUIPOS' in r2:
                for equipo in r2['ET_EQUIPOS']:
                    sociedad=Formal_Organizacion.objects.get(codigo=equipo['ANLN1']) if Formal_Organizacion.objects.get(codigo=equipo['ANLN1']) else None
                    obj, created = Formal_Equipo.objects.update_or_create(
                    codigo=equipo['ANLN1'],         
                    defaults={
                        'codigo':equipo['ANLN1'], 
                        'nombre':equipo['ANTLX'], 
                        'BURKS': Formal_Organizacion.objects.get(codigo=equipo['ANLN1']).id if Formal_Organizacion.objects.get(codigo=equipo['ANLN1']) else None

                    }
                )
            if 'ET_ESPECIALIDAD' in r2:
                for especialidad in r2['ET_ESPECIALIDAD']:                
                    obj, created = Formal_Especialidad.objects.update_or_create(
                    codigo=especialidad['FACHR'],         
                    defaults={
                        'codigo':especialidad['FACHR'], 
                        'descripcion':especialidad['FTEXT'],                        

                    }
                )
                
            if 'ET_ESTADOS_CIVIL' in r2:
                for estado_civil in r2['ET_ESTADOS_CIVIL']:                
                    obj, created = Formal_Estado_civil.objects.update_or_create(
                    codigo=estado_civil['FAMST'],         
                    defaults={
                        'codigo':estado_civil['FAMST'], 
                        'nombre':estado_civil['FTEXT'],                        

                    }
                )
            if 'ET_FORMACION' in r2:
                for formacion in r2['ET_FORMACION']:                
                    obj, created = Formal_Formacion.objects.update_or_create(
                        codigo=formacion['AUSBI'],         
                        defaults={
                            'codigo':formacion['AUSBI'], 
                            'descripcion':formacion['ATEXT'],                        

                        }
                    )
                
            if 'ET_PUESTOS' in r2:
                Formal_Puesto.objects.filter(sap=True).delete()
                for puesto in r2['ET_PUESTOS']:                
                    obj, created = Formal_Puesto.objects.update_or_create(
                        codigo=puesto['PLANS'],         
                        defaults={
                            'codigo':puesto['PLANS'], 
                            'descripcion':puesto['PLSTX'],   
                            'descripcion_larga':puesto['PLSTX2'],                       

                        }
                    )
            if 'ET_FUNCIONES' in r2:
                for posicion in r2['ET_FUNCIONES']:                
                    obj, created = Formal_Funciones.objects.update_or_create(
                        codigo=posicion['STELL'],         
                        defaults={
                            'nombre':posicion['STLTX'], 
                            'descripcion':posicion['STLTX2'],                        

                        }
                    )
            if 'ET_RELACION_LABORAL' in r2:
                for relacion_laboral in r2['ET_RELACION_LABORAL']:                
                    obj, created = Formal_Relacion_Laboral.objects.update_or_create(
                        codigo=relacion_laboral['PERSG'],         
                        defaults={
                            'codigo':relacion_laboral['PERSG'], 
                            'descripcion':relacion_laboral['PTEXT'],                        

                        }
                    )

            if 'ET_SITUACION_ACTUAL' in r2:
                for situacion_actual in r2['ET_SITUACION_ACTUAL']:                
                    obj, created = Formal_Situacion_Actual.objects.update_or_create(
                        codigo=situacion_actual['STATV'],         
                        defaults={
                            'codigo':situacion_actual['STATV'], 
                            'descripcion':situacion_actual['TEXT1'],                        

                        }
                    )
            if 'ET_SOCIEDADES' in r2:
                for organizacion in r2['ET_SOCIEDADES']:                
                    obj, created = Formal_Organizacion.objects.update_or_create(
                        codigo=organizacion['BUKRS'],         
                        defaults={
                            'codigo':organizacion['BUKRS'], 
                            'nombre':organizacion['BUTXT'],                        

                        }
                    )
            if 'ET_SITUACION_ACTUAL' in r2:
                for situacion in r2['ET_SITUACION_ACTUAL']:                
                    obj, created = Formal_Situacion_Actual.objects.update_or_create(
                        codigo=situacion['STATV'],         
                        defaults={
                            'codigo':situacion['STATV'], 
                            'descripcion':situacion['TEXT1'],                        

                        }
                    )

            if 'ET_CENTRO_COSTOS' in r2:
                for centro in r2['ET_CENTRO_COSTOS']:   
                    orga =  Formal_Organizacion.objects.filter(codigo=centro['BUKRS']) if Formal_Organizacion.objects.filter(codigo=centro['BUKRS']) else None                                         
                    obj, created = Formal_Centro_Costo.objects.update_or_create(
                        codigo=centro['KOSTL'],         
                        defaults={
                            'codigo':centro['KOSTL'], 
                            'descripcion':centro['LTEXT'],                        

                        }

                    )
                    if orga!=None:
                        for org in orga:
                             obj.organizacion=org
                             obj.save()

            if 'ET_DIAGNOSTICOS' in r2:
                for enfermedad in r2['ET_DIAGNOSTICOS']:   
                    obj, created = Formal_Diagnostico.objects.update_or_create(
                        codigo=enfermedad['RESUL'],         
                        defaults={
                            'codigo':enfermedad['RESUL'], 
                            'descripcion':enfermedad['RSTXT'],                        

                        }

                    )

            if 'ET_CLASE_INST' in r2:
                for instituto in r2['ET_CLASE_INST']:   
                    obj, created = Formal_Instituto.objects.update_or_create(
                        codigo=instituto['SLART'],         
                        defaults={
                            'codigo':instituto['SLART'], 
                            'descripcion':instituto['STEXT'],                        

                        }

                    )
    
            if 'ET_TITULOS' in r2:
                for titulo in r2['ET_TITULOS']:   
                    obj, created = Formal_Titulo.objects.update_or_create(
                        codigo=titulo['SLABS'],         
                        defaults={
                            'codigo':titulo['SLABS'], 
                            'descripcion':titulo['STEXT'],                        

                        }

                    )

            
            if 'ET_REL_CLINST_TITULOS' in r2:
                for relacion in r2['ET_REL_CLINST_TITULOS']:
                    institutos=Formal_Instituto.objects.filter(codigo=relacion['SLART'])
                    titulos=Formal_Titulo.objects.filter(codigo=relacion['SLABS'])
                    for instituto in institutos:
                        for titulo in titulos:
                            titulo.universidad.add(instituto)


            if 'ET_REL_CLINST_ESPECIALIDAD' in r2:
                for relacion in r2['ET_REL_CLINST_ESPECIALIDAD']:
                    institutos=Formal_Instituto.objects.filter(codigo=relacion['SLART'])
                    especialidades=Formal_Especialidad.objects.filter(codigo=relacion['FACHR'])
                    for instituto in institutos:
                        for especialidad in especialidades:
                            especialidad.universidad.add(instituto)


            if 'ET_RELACION_LAB_ANT' in r2:
                for antiguedad in r2['ET_RELACION_LAB_ANT']:   
                    obj, created = Formal_Relacion_Laboral_Anterior.objects.update_or_create(
                        codigo=antiguedad['ANSVX'],         
                        defaults={
                            'codigo':antiguedad['ANSVX'], 
                            'descripcion':antiguedad['ANSTX'],                        

                        }

                    )


            if 'ET_UNIDAD_ORG' in r2:
                for unidad_organizativa in r2['ET_UNIDAD_ORG']: 
                    orga =  Formal_Organizacion.objects.filter(codigo=unidad_organizativa['BUKRS']) if Formal_Organizacion.objects.filter(codigo=unidad_organizativa['BUKRS']) else None                            
                   
                    obj, created = Formal_Unidad_Organizativa.objects.update_or_create(
                        codigo=unidad_organizativa['ORGEH'],         
                        defaults={
                            'codigo':unidad_organizativa['ORGEH'], 
                            'nombre':unidad_organizativa['ORGTX'],  
                            'Dirigido_por':unidad_organizativa['PERNR_D'],
                            'principal':True if unidad_organizativa['PRINCIPAL'] =="X" else False,
                        }
                    )
                    if orga!=None:
                        for org in orga:
                             obj.sociedad_financiera.add(org.id)
                             obj.save()
                for unidad_organizativa in r2['ET_UNIDAD_ORG']:  
                    orga =  Formal_Organizacion.objects.filter(codigo=unidad_organizativa['BUKRS']) if Formal_Organizacion.objects.filter(codigo=unidad_organizativa['BUKRS']) else None                            
                    obj, created = Formal_Unidad_Organizativa.objects.update_or_create(
                        codigo=unidad_organizativa['ORGEH'],         
                        defaults={
                            'codigo':unidad_organizativa['ORGEH'], 
                            'nombre':unidad_organizativa['ORGTX'],  
                            'Dirigido_por':unidad_organizativa['PERNR_D'],
                            'principal':True if unidad_organizativa['PRINCIPAL'] =="X" else False,
                        }

                    )
                    for puesto in unidad_organizativa['T_PLANS']:
                        ppuesto, created = Formal_Puesto.objects.update_or_create(
                        codigo=puesto['PLANS'],         
                        defaults={
                            'codigo':puesto['PLANS'], 
                        })
                        ppuesto.unidad_organizativa.remove(*ppuesto.unidad_organizativa.all())

                    for puesto in unidad_organizativa['T_PLANS']:
                        ppuesto, created = Formal_Puesto.objects.update_or_create(
                        codigo=puesto['PLANS'],         
                        defaults={
                            'codigo':puesto['PLANS'], 
                        })
                        ppuesto.unidad_organizativa.add(obj)


                    for unidad in unidad_organizativa['T_ORGEH_H']:
                        padre=Formal_Unidad_Organizativa.objects.get(codigo=unidad_organizativa['ORGEH']) if Formal_Unidad_Organizativa.objects.get(codigo=unidad_organizativa['ORGEH']) else None            
                        uni=Formal_Unidad_Organizativa.objects.get(codigo=unidad['ORGEH']) if Formal_Unidad_Organizativa.objects.get(codigo=unidad['ORGEH']) else None            
                        if uni!= None and padre!=None:
                            padres_anteriores=Formal_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id__in=[uni.id])
                            for pppp in padres_anteriores:
                                pppp.unidad_organizativa_jeraquia.remove(uni.id)
                                
                            padre.unidad_organizativa_jeraquia.add(uni.id)
                            uni.sociedad_financiera.remove(*uni.sociedad_financiera.all())
                            if orga!=None:
                                    for org in orga:
                                        uni.sociedad_financiera.add(org.id)
                                        uni.save()
                    
                for unidad in  Formal_Unidad_Organizativa.objects.filter(principal=True):
                 
                    orgas=Formal_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('sociedad_financiera',flat=True)
                    #print('estas son las org',orgas)
                    orga =  Formal_Organizacion.objects.filter(id__in=orgas) if Formal_Organizacion.objects.filter(id__in=orgas) else None                            
                    nodos = Formal_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('unidad_organizativa_jeraquia',flat=True)
                    #for uni in Formal_Unidad_Organizativa.objects.filter(id__in=nodos).values_list('id',flat=True):     
                    #print('estos son los hijos de primer nivel',nodos)
                    sub_nodo = Formal_Unidad_Organizativa.objects.get(id=unidad.id)
                    for soc in orgas:    
                        if soc !=None:
                            sub_nodo.sociedad_financiera.add(soc)
                            sub_nodo.save()
                    x=1
                    while x==1:
                        x=formal_hijos(nodos,orgas)

                # for unidad in  Formal_Unidad_Organizativa.objects.filter().order_by('-principal','id'):
                #     uni = list(Formal_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('unidad_organizativa_jeraquia__id',flat=True))
                #     orga = list(Formal_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('sociedad_financiera__id',flat=True))
                #     #print(unidad.id,uni,orga)
                #     if uni:
                #         for un in uni:
                #             for org in orga:
                #                 if org!=None and un!=None:
                #                     #print(un)
                #                     FUO=Formal_Unidad_Organizativa.objects.get(id=un)
                #                     FUO.sociedad_financiera.add(org)
                #                     FUO.save()

                un=Formal_Unidad_Organizativa.objects.filter(principal=True)
                for uni in un:
                    soci=Formal_Organizacion.objects.filter(id__in=uni.sociedad_financiera.all())
                    unidades = formal_get_sub_unidades([uni.codigo])
                    unidades_sin_none =list(filter(None, unidades))
                    unidades = unidades_sin_none
                    unidad = Formal_Unidad_Organizativa.objects.filter(codigo__in=unidades)
                    for u in unidad:
                        for so in soci:
                            u.sociedad_financiera.add(so)
                            u.save()
            return Response(r2,status= status.HTTP_200_OK)
            #return Response(status= status.HTTP_200_OK)


class Funcional_RFC_Carga_Masiva_Complementaria(APIView):    
    def get(self,request):
        with Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300') as conx:
        #with Connection(user='INTERFACESAP', passwd='1nt3rf4c3sF4r!n73r',ashost='172.10.0.6', sysnr='00', client='300') as conx:
            #r2 = conx.call('ZRFC_HEADCOUNT_AURORA',IRG_PERNR=IRG_PERNR)
            r2 = conx.call('ZRFC_SUPPL_TABLES_AURORA')
            for division in r2['ET_DIVISIONES']:
                  obj, created = Funcional_Division.objects.update_or_create(
                    codigo=division['GSBER'],
                    defaults={
                        'codigo':division['GSBER'], 
                        'descripcion':division['GTEXT'], 

                    }
                )
            
            for division in r2['ET_DIVISIONES_PERSA']:
                  obj, created = Funcional_Division_Personal.objects.update_or_create(
                    codigo=division['PERSA'],       
                    defaults={
                        'codigo':division['PERSA'], 
                        'descripcion':division['NAME1'], 

                    }
                )

            if 'ET_EQUIPOS' in r2:
                for equipo in r2['ET_EQUIPOS']:
                    sociedad=Funcional_Organizacion.objects.get(codigo=equipo['ANLN1']) if Funcional_Organizacion.objects.get(codigo=equipo['ANLN1']) else None
                    obj, created = Funcional_Equipo.objects.update_or_create(
                    codigo=equipo['ANLN1'],         
                    defaults={
                        'codigo':equipo['ANLN1'], 
                        'nombre':equipo['ANTLX'], 
                        'BURKS': Funcional_Organizacion.objects.get(codigo=equipo['ANLN1']).id if Funcional_Organizacion.objects.get(codigo=equipo['ANLN1']) else None

                    }
                )
            if 'ET_ESPECIALIDAD' in r2:
                for especialidad in r2['ET_ESPECIALIDAD']:                
                    obj, created = Funcional_Especialidad.objects.update_or_create(
                    codigo=especialidad['FACHR'],         
                    defaults={
                        'codigo':especialidad['FACHR'], 
                        'descripcion':especialidad['FTEXT'],                        

                    }
                )
                
            if 'ET_ESTADOS_CIVIL' in r2:
                for estado_civil in r2['ET_ESTADOS_CIVIL']:                
                    obj, created = Funcional_Estado_civil.objects.update_or_create(
                    codigo=estado_civil['FAMST'],         
                    defaults={
                        'codigo':estado_civil['FAMST'], 
                        'nombre':estado_civil['FTEXT'],                        

                    }
                )
            if 'ET_FORMACION' in r2:
                for formacion in r2['ET_FORMACION']:                
                    obj, created = Funcional_Formacion.objects.update_or_create(
                        codigo=formacion['AUSBI'],         
                        defaults={
                            'codigo':formacion['AUSBI'], 
                            'descripcion':formacion['ATEXT'],                        

                        }
                    )
                
            if 'ET_PUESTOS' in r2:
                Funcional_Puesto.objects.filter(sap=True).delete()
                for puesto in r2['ET_PUESTOS']:                
                    obj, created = Funcional_Puesto.objects.update_or_create(
                        codigo=puesto['PLANS'],         
                        defaults={
                            'codigo':puesto['PLANS'], 
                            'descripcion':puesto['PLSTX'],  
                            'descripcion_larga':puesto['PLSTX2'],                        

                        }
                    )

            if 'ET_FUNCIONES' in r2:
                for posicion in r2['ET_FUNCIONES']:                
                    obj, created = Funcional_Funciones.objects.update_or_create(
                        codigo=posicion['STELL'],         
                        defaults={
                            'nombre':posicion['STLTX'], 
                            'descripcion':posicion['STLTX2'],                        

                        }
                    )
            if 'ET_RELACION_LABORAL' in r2:
                for relacion_laboral in r2['ET_RELACION_LABORAL']:                
                    obj, created = Funcional_Relacion_Laboral.objects.update_or_create(
                        codigo=relacion_laboral['PERSG'],         
                        defaults={
                            'codigo':relacion_laboral['PERSG'], 
                            'descripcion':relacion_laboral['PTEXT'],                        

                        }
                    )

            if 'ET_SITUACION_ACTUAL' in r2:
                for situacion_actual in r2['ET_SITUACION_ACTUAL']:                
                    obj, created = Funcional_Situacion_Actual.objects.update_or_create(
                        codigo=situacion_actual['STATV'],         
                        defaults={
                            'codigo':situacion_actual['STATV'], 
                            'descripcion':situacion_actual['TEXT1'],                        

                        }
                    )
            if 'ET_SOCIEDADES' in r2:
                for organizacion in r2['ET_SOCIEDADES']:                
                    obj, created = Funcional_Organizacion.objects.update_or_create(
                        codigo=organizacion['BUKRS'],         
                        defaults={
                            'codigo':organizacion['BUKRS'], 
                            'nombre':organizacion['BUTXT'],                        

                        }
                    )
            if 'ET_SITUACION_ACTUAL' in r2:
                for situacion in r2['ET_SITUACION_ACTUAL']:                
                    obj, created = Funcional_Situacion_Actual.objects.update_or_create(
                        codigo=situacion['STATV'],         
                        defaults={
                            'codigo':situacion['STATV'], 
                            'descripcion':situacion['TEXT1'],                        

                        }
                    )

            if 'ET_CENTRO_COSTOS' in r2:
                for centro in r2['ET_CENTRO_COSTOS']:   
                    orga =  Funcional_Organizacion.objects.filter(codigo=centro['BUKRS']) if Funcional_Organizacion.objects.filter(codigo=centro['BUKRS']) else None                                         
                    obj, created = Funcional_Centro_Costo.objects.update_or_create(
                        codigo=centro['KOSTL'],         
                        defaults={
                            'codigo':centro['KOSTL'], 
                            'descripcion':centro['LTEXT'],                        

                        }

                    )
                    if orga!=None:
                        for org in orga:
                             obj.organizacion=org
                             obj.save()


            if 'ET_DIAGNOSTICOS' in r2:
                for enfermedad in r2['ET_DIAGNOSTICOS']:   
                    obj, created = Funcional_Diagnostico.objects.update_or_create(
                        codigo=enfermedad['RESUL'],         
                        defaults={
                            'codigo':enfermedad['RESUL'], 
                            'descripcion':enfermedad['RSTXT'],                        

                        }

                    )
            if 'ET_CLASE_INST' in r2:
                for instituto in r2['ET_CLASE_INST']:   
                    obj, created = Funcional_Instituto.objects.update_or_create(
                        codigo=instituto['SLART'],         
                        defaults={
                            'codigo':instituto['SLART'], 
                            'descripcion':instituto['STEXT'],                        

                        }

                    )
    
            if 'ET_TITULOS' in r2:
                for titulo in r2['ET_TITULOS']:   
                    obj, created = Funcional_Titulo.objects.update_or_create(
                        codigo=titulo['SLABS'],         
                        defaults={
                            'codigo':titulo['SLABS'], 
                            'descripcion':titulo['STEXT'],                        

                        }

                    )
            if 'ET_REL_CLINST_TITULOS' in r2:
                for relacion in r2['ET_REL_CLINST_TITULOS']:
                    institutos=Funcional_Instituto.objects.filter(codigo=relacion['SLART'])
                    titulos=Funcional_Titulo.objects.filter(codigo=relacion['SLABS'])
                    for instituto in institutos:
                        for titulo in titulos:
                            titulo.universidad.add(instituto)


            if 'ET_REL_CLINST_ESPECIALIDAD' in r2:
                for relacion in r2['ET_REL_CLINST_ESPECIALIDAD']:
                    institutos=Funcional_Instituto.objects.filter(codigo=relacion['SLART'])
                    especialidades=Funcional_Especialidad.objects.filter(codigo=relacion['FACHR'])
                    for instituto in institutos:
                        for especialidad in especialidades:
                            especialidad.universidad.add(instituto)

            if 'ET_RELACION_LAB_ANT' in r2:
                for antiguedad in r2['ET_RELACION_LAB_ANT']:   
                    obj, created = Funcional_Relacion_Laboral_Anterior.objects.update_or_create(
                        codigo=antiguedad['ANSVX'],         
                        defaults={
                            'codigo':antiguedad['ANSVX'], 
                            'descripcion':antiguedad['ANSTX'],                        

                        }

                    )

            

            if 'ET_UNIDAD_ORG' in r2:
                for unidad_organizativa in r2['ET_UNIDAD_ORG']: 
                    orga =  Funcional_Organizacion.objects.filter(codigo=unidad_organizativa['BUKRS']) if Funcional_Organizacion.objects.filter(codigo=unidad_organizativa['BUKRS']) else None                            
                   
                    obj, created = Funcional_Unidad_Organizativa.objects.update_or_create(
                        codigo=unidad_organizativa['ORGEH'],         
                        defaults={
                            'codigo':unidad_organizativa['ORGEH'], 
                            'nombre':unidad_organizativa['ORGTX'],  
                            'Dirigido_por':unidad_organizativa['PERNR_D'], #comentado para evitar modificar la estructura
                            'principal':True if unidad_organizativa['PRINCIPAL'] =="X" else False,
                        }
                    )
                    if orga!=None:
                        for org in orga:
                             obj.sociedad_financiera.add(org.id)
                             obj.save()
                for unidad_organizativa in r2['ET_UNIDAD_ORG']:  
                    orga =  Funcional_Organizacion.objects.filter(codigo=unidad_organizativa['BUKRS']) if Funcional_Organizacion.objects.filter(codigo=unidad_organizativa['BUKRS']) else None                            
                    obj, created = Funcional_Unidad_Organizativa.objects.update_or_create(
                        codigo=unidad_organizativa['ORGEH'],         
                        defaults={
                            'codigo':unidad_organizativa['ORGEH'], 
                            'nombre':unidad_organizativa['ORGTX'],  
                            'Dirigido_por':unidad_organizativa['PERNR_D'],
                            'principal':True if unidad_organizativa['PRINCIPAL'] =="X" else False,
                        }

                    )
                    for puesto in unidad_organizativa['T_PLANS']:
                        ppuesto, created = Funcional_Puesto.objects.update_or_create(
                        codigo=puesto['PLANS'],         
                        defaults={
                            'codigo':puesto['PLANS'], 
                        })
                        ppuesto.unidad_organizativa.remove(*ppuesto.unidad_organizativa.all())
                    for puesto in unidad_organizativa['T_PLANS']:
                        ppuesto, created = Funcional_Puesto.objects.update_or_create(
                        codigo=puesto['PLANS'],         
                        defaults={
                            'codigo':puesto['PLANS'], 
                        })
                        ppuesto.unidad_organizativa.add(obj)


                    for unidad in unidad_organizativa['T_ORGEH_H']:
                        padre=Funcional_Unidad_Organizativa.objects.get(codigo=unidad_organizativa['ORGEH']) if Funcional_Unidad_Organizativa.objects.get(codigo=unidad_organizativa['ORGEH']) else None            
                        uni=Funcional_Unidad_Organizativa.objects.get(codigo=unidad['ORGEH']) if Funcional_Unidad_Organizativa.objects.get(codigo=unidad['ORGEH']) else None            
                        if uni!= None and padre!=None:
                            padre.unidad_organizativa_jeraquia.add(uni.id)
                            if orga!=None:
                                    for org in orga:
                                        uni.sociedad_financiera.add(org.id)
                                        uni.save()
                    
                for unidad in  Funcional_Unidad_Organizativa.objects.filter(principal=True):
                 
                    orgas=Funcional_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('sociedad_financiera',flat=True)
                    #print('estas son las org',orgas)
                    orga =  Funcional_Organizacion.objects.filter(id__in=orgas) if Funcional_Organizacion.objects.filter(id__in=orgas) else None                            
                    nodos = Funcional_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('unidad_organizativa_jeraquia',flat=True)
                    #for uni in Formal_Unidad_Organizativa.objects.filter(id__in=nodos).values_list('id',flat=True):     
                    #print('estos son los hijos de primer nivel',nodos)
                    sub_nodo = Funcional_Unidad_Organizativa.objects.get(id=unidad.id)
                    for soc in orgas:    
                        if soc !=None:
                            sub_nodo.sociedad_financiera.add(soc)
                            sub_nodo.save()
                    x=1
                    while x==1:
                        x=funcional_hijos(nodos,orgas)

                # for unidad in  Funcional_Unidad_Organizativa.objects.filter().order_by('-principal','id'):
                #     uni = list(Funcional_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('unidad_organizativa_jeraquia__id',flat=True))
                #     orga = list(Funcional_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('sociedad_financiera__id',flat=True))
                #     #print(unidad.id,uni,orga)
                #     if uni:
                #         for un in uni:
                #             for org in orga:
                #                 if org!=None and un!=None:
                #                     #print(un)
                #                     FUO=Funcional_Unidad_Organizativa.objects.get(id=un)
                #                     FUO.sociedad_financiera.add(org)
                #                     FUO.save()


            un=Funcional_Unidad_Organizativa.objects.filter(principal=True)
            for uni in un:
                soci=Funcional_Organizacion.objects.filter(id__in=uni.sociedad_financiera.all())
                unidades = funcional_get_sub_unidades([uni.codigo])
                unidades_sin_none =list(filter(None, unidades))
                unidades = unidades_sin_none
                unidad = Funcional_Unidad_Organizativa.objects.filter(codigo__in=unidades)
                for u in unidad:
                    for so in soci:
                        u.sociedad_financiera.add(so)
                        u.save()
            return Response(r2,status= status.HTTP_200_OK)
            #return Response(status= status.HTTP_200_OK)
def funcional_hijos(unidad,orga):
    
    #print('unidades hijas', Formal_Unidad_Organizativa.objects.filter(id__in=unidad).values('codigo'))
    #print('oraganizaciones',orga)
    for uni in unidad:
        #un=Formal_Unidad_Organizativa.objects.filter(id=uni).values('codigo')
        sub_nodo = Funcional_Unidad_Organizativa.objects.filter(id=uni)[0] if Funcional_Unidad_Organizativa.objects.filter(id=uni) else None
        if sub_nodo!=None:
            for soc in orga:    
                #print('unidad',sub_nodo.codigo)
                #print('orga',soc)
                if soc !=None:
                    sub_nodo.sociedad_financiera.add(soc)
                    sub_nodo.save()

    if Funcional_Organizacion.objects.filter(id__in=orga):

        for uni in unidad:
            if Funcional_Unidad_Organizativa.objects.filter(id=uni):
                un=Funcional_Unidad_Organizativa.objects.filter(id=uni)[:1][0]
                #print('este es el nodo padre',un.codigo)
                #print('estos son los hijos',Formal_Unidad_Organizativa.objects.filter(id=uni).values_list('unidad_organizativa_jeraquia__codigo',flat=True))
                nodos  = Funcional_Unidad_Organizativa.objects.filter(id=uni).values_list('unidad_organizativa_jeraquia',flat=True)
                for org in orga:
                    if org !=None:
                        un.sociedad_financiera.add(org)
                if Funcional_Unidad_Organizativa.objects.filter(id__in=nodos):
                    a=Funcional_Unidad_Organizativa.objects.filter(id__in=nodos).values_list('unidad_organizativa_jeraquia',flat=True)
                    b=orga
                    funcional_hijos(a,b)        
                    
    return 0


def formal_hijos(unidad,orga):
    
    #print('unidades hijas', Formal_Unidad_Organizativa.objects.filter(id__in=unidad).values('codigo'))
    #print('oraganizaciones',orga)
    for uni in unidad:
        #un=Formal_Unidad_Organizativa.objects.filter(id=uni).values('codigo')
        sub_nodo = Formal_Unidad_Organizativa.objects.filter(id=uni)[0] if Formal_Unidad_Organizativa.objects.filter(id=uni) else None
        if sub_nodo!=None:
            for soc in orga:    
                #print('unidad',sub_nodo.codigo)
                #print('orga',soc)
                if soc !=None:
                    sub_nodo.sociedad_financiera.add(soc)
                    sub_nodo.save()


    if Formal_Organizacion.objects.filter(id__in=orga):

        for uni in unidad:
            if Formal_Unidad_Organizativa.objects.filter(id=uni):
                un=Formal_Unidad_Organizativa.objects.filter(id=uni)[:1][0]
                #print('este es el nodo padre',un.codigo)
                #print('estos son los hijos',Formal_Unidad_Organizativa.objects.filter(id=uni).values_list('unidad_organizativa_jeraquia__codigo',flat=True))
                nodos  = Formal_Unidad_Organizativa.objects.filter(id=uni).values_list('unidad_organizativa_jeraquia',flat=True)
                for org in orga:
                    if org !=None:
                        un.sociedad_financiera.add(org)
                if Formal_Unidad_Organizativa.objects.filter(id__in=nodos):
                    a=Formal_Unidad_Organizativa.objects.filter(id__in=nodos).values_list('unidad_organizativa_jeraquia',flat=True)
                    b=orga
                    formal_hijos(a,b)
                 
                    
    return 0


class formal_unidad_jerarquiaviewset(APIView):
    def post(self,request):

        #print('este es el request',request.data)
        if 'hijos' in request.data:
            try:
                unidad=Formal_Unidad_Organizativa.objects.filter(id__in=request.data['hijos'])
                
                
                if not unidad :
                    return Response({"mensaje":"Verifique los datos enviados"},status= status.HTTP_404_NOT_FOUND)
                
                data=formal_unidad_organizativaserializer(unidad,many=True)
                return Response(data.data,status= status.HTTP_200_OK)
            except BadHeaderError:
                    return Response({"mensaje":"Ha Sucedido un error,contacta al administrador"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"No hemos recibido tus datos"},status= status.HTTP_404_NOT_FOUND)

class funcional_unidad_jerarquiaviewset(APIView):
    def post(self,request):

        #print('este es el request',request.data)
        if 'hijos' in request.data:
            try:
                unidad=Funcional_Unidad_Organizativa.objects.filter(id__in=request.data['hijos'])
                
                
                if not unidad :
                    return Response({"mensaje":"Verifique los datos enviados"},status= status.HTTP_404_NOT_FOUND)
                
                data=funcional_unidad_organizativaserializer(unidad,many=True)
                return Response(data.data,status= status.HTTP_200_OK)
            except BadHeaderError:
                    return Response({"mensaje":"Ha Sucedido un error,contacta al administrador"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"No hemos recibido tus datos"},status= status.HTTP_404_NOT_FOUND)

def funcional_get_colaborador(empleado_codigo):
    if not empleado_codigo:
        return []
    empleado = list(Funcional_empleado.objects.filter(jefe_inmediato__in=empleado_codigo).exclude(codigo__in=empleado_codigo).values_list("codigo",flat=True))
    result = funcional_get_colaborador(empleado)
    result.extend(empleado)    

    return result

class Funcional_ClasificacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Clasificacion.objects.all()
    serializer_class = Funcional_Clasificacionserializer

class descriptor_perfil_cursos_diplomados_seminario_pasantiaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.all()
    serializer_class = descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.all()
        serializer = descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(queryset, many=True)
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
                        filter_kwargs['fecha_creacion__icontains'] = filter

                queryset =  descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter(**filter_kwargs).count()
                serializer = descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter().count()
                serializer = descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='fecha_creacion':
                        filter_kwargs['fecha_creacion__icontains'] = filter

                        
                queryset =  descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter(**filter_kwargs).order_by('id')
                serializer = descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter().order_by('id')
                serializer = descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


    def create(self, request):
        serializer = descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:       
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def put(self,requets,id):
        existe= descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(put,data=requets.data)
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
    

class Funcional_empleadoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = Funcional_empleadoserializer
    def list(self, request):
        #print(request.data)
        usuario = request.user
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        if 'jefe' in grupos:
            #print('si entro como jefe',usuario.username)
            colaboradores = funcional_get_colaborador([usuario.username])
            #print('colaboradores',colaboradores)
            queryset = Funcional_empleado.objects.all()
            objeto= Funcional_empleado.objects.filter(codigo__in=colaboradores)
            serializer = Funcional_empleadoserializer(queryset, many=True)
            filter=''        
            orga=0
            activo=''
            if self.request.query_params.get('activo'):
                activo=self.request.query_params.get('activo')
            
            if activo!='':
               #print('Activos')
               #print("ingreso1")
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                   #print("ingreso2")
                if self.request.query_params.get('orga'):
                    orga = self.request.query_params.get('orga')
                    objeto= Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct()
                   #print("ingreso3")
        
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                   #print("ingreso4")
                    if self.request.query_params.get('filter')!='':
                        #comentado porque hay jefes que tiene subordinados en mas de una empresa, se quito filtro orga
                        #queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')[offset:offset+limit]
                        #queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')
                        
                        queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                       #print("ingreso4")
                        for x in serializer.data:
                            if x['posicion']:
                                ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                                if ff:
                                    descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                    if descriptor:
                                        #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                        
                                        x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                    else: 
                                        x['descriptor']=''
                                else:
                                    x['descriptor']=''
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        ##cometado porque hay jefes que tienen colaboradores en distintas empresa se quito filtro orga
                        ##queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')[offset:offset+limit]
                        ##queryset2 = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')
                        queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')
                    
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                       #print("ingreso5")
                        for x in serializer.data:
                            if x['posicion']:
                                ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                                if ff:
                                    descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                    if descriptor:
                                        #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                        
                                        x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                    else: 
                                        x['descriptor']=''
                                else:
                                    x['descriptor']=''                        
                        return Response({"data":serializer.data,"count":queryset2.count()})
                        #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
                elif  filter !='':
                    
                    #print(filter) 
                    filtro=str(filter).strip()
                    #comentado porque existen jefes que tienen colaboradores en mas de una empresa se quito filtro orga
                    #queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')
                    queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).distinct().order_by('-id')
                    #print('resultados',queryset.query)
                    serializer = Funcional_empleadoserializer(queryset, many=True)
              
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores,unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).distinct().order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
              
                    return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('Todos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                
                if self.request.query_params.get('orga'):
                    orga = self.request.query_params.get('orga')
                    #comentado porque existen jefes que tienen colaboradores en mas de una empresa se quito filtro orga
                    #objeto= Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).distinct()
                    objeto= Funcional_empleado.objects.filter(codigo__in=colaboradores).distinct()
        
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    
                    if self.request.query_params.get('filter')!='':
                        #comentado porque existen jefes que tienen colaboradores en mas de una empresa se quito filtro orga
                        #queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).distinct().order_by('-id')[offset:offset+limit]
                        #queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).distinct().order_by('-id')
                        queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),codigo__in=colaboradores).distinct().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),codigo__in=colaboradores).distinct().order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        for x in serializer.data:
                            if x['posicion']:
                                ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                                if ff:
                                    descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                    if descriptor:
                                        #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                        
                                        x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                    else: 
                                        x['descriptor']=''
                                else:
                                    x['descriptor']=''                        
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        #comentado porque existen jefes que tienen colaboradores en mas de una empresa se quito filtro orga
                        #queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).distinct().order_by('-id')[offset:offset+limit]
                        #queryset2 = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).distinct().order_by('-id')
                        queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores).distinct().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(codigo__in=colaboradores).distinct().order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        for x in serializer.data:
                            if x['posicion']:
                                ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                                if ff:
                                    descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                    if descriptor:
                                        #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                        
                                        x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                    else: 
                                        x['descriptor']=''
                                else:
                                    x['descriptor']=''                        
                        return Response({"data":serializer.data,"count":queryset2.count()})
                        #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
                elif  filter !='':
                    
                    #print(filter) 
                    filtro=str(filter).strip()
                    #print('entro a solo filter',filtro)
                    #comentado porque existen jefes que tienen colaboradores en mas de una empresa se quito filtro orga
                    #queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).distinct().order_by('-id')
                    queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),codigo__in=colaboradores).distinct().order_by('-id')
                    #print('resultados',queryset.query)
                    serializer = Funcional_empleadoserializer(queryset, many=True)
              
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    #comentado porque existen jefes que tienen colaboradores en mas de una empresa se quito filtro orga

                    #queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores,unidad_organizativa__sociedad_financiera__id=orga).distinct().order_by('-id')
                    queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores).distinct().order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
              
                    return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_empleado.objects.all()
            objeto= Funcional_empleado.objects.all()
            serializer = Funcional_empleadoserializer(queryset, many=True)
            filter=''        
            orga=0
            activo=''

            if self.request.query_params.get('activo'):
                activo=self.request.query_params.get('activo')

            if activo!='':
               #print('Activos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                
                if self.request.query_params.get('orga'):
                    orga = self.request.query_params.get('orga')
                    objeto= Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).distinct()

        
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    
                    if self.request.query_params.get('filter')!='':
                       #print('como empleado')
                       #print(filter)
                       #print(orga)
                       #print(activo)
                        queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).distinct().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).distinct().order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        
                        for x in serializer.data:
                            if x['posicion']:
                                ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                                if ff:
                                    descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                    if descriptor:
                                        #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                        
                                        x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                    else: 
                                        x['descriptor']=''
                                else:
                                    x['descriptor']=''


                        
                        return Response({"data":serializer.data,"count":queryset2.count()})

                    else:
                        queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).distinct().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).distinct().order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        for x in serializer.data:
                            if x['posicion']:
                                ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                                if ff:
                                    descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                    if descriptor:
                                        #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                        
                                        x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                    else: 
                                        x['descriptor']=''
                                else:
                                    x['descriptor']=''
                        return Response({"data":serializer.data,"count":queryset2.count()})
                        #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
                elif  filter !='':
                    
                    #print(filter) 
                    filtro=str(filter).strip()
                    #print('entro a solo filter',filtro)
                    queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).distinct().order_by('-id')
                    #print('resultados',queryset.query)
                    serializer = Funcional_empleadoserializer(queryset, many=True)
              
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).distinct().order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    for x in serializer.data:
                        if x['posicion']:
                            ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                            if ff:
                                descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                if descriptor:
                                    #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                    
                                    x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                else: 
                                    x['descriptor']=''
                            else:
                                x['descriptor']=''
                    return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('Todos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                
                if self.request.query_params.get('orga'):
                    orga = self.request.query_params.get('orga')
                    objeto= Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).distinct()

        
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    
                    if self.request.query_params.get('filter')!='':
                        
                        queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).distinct().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).distinct().order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        for x in serializer.data:
                            if x['posicion']:
                                ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                                if ff:
                                    descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                    if descriptor:
                                        #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                        
                                        x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                    else: 
                                        x['descriptor']=''
                                else:
                                    x['descriptor']=''                        
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).distinct().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).distinct().order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        for x in serializer.data:
                            if x['posicion']:
                                ff=Funcional_Funciones.objects.filter(id=x['posicion'][0]).order_by('-id')
                                if ff:
                                    descriptor=descriptor_perfil_datos_generales.objects.filter(posicion=ff[0].id)
                                    if descriptor:
                                        #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                                        
                                        x['descriptor']={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                                    else: 
                                        x['descriptor']=''
                                else:
                                    x['descriptor']=''
                        return Response({"data":serializer.data,"count":queryset2.count()})
                        #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
                elif  filter !='':
                    
                    #print(filter) 
                    filtro=str(filter).strip()
                    #print('entro a solo filter',filtro)
                    queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).distinct().order_by('-id')
                    #print('resultados',queryset.query)
                    serializer = Funcional_empleadoserializer(queryset, many=True)
              
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).distinct().order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
              
                    return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_empleado_fotoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = Funcional_empleado_foto_serializer



def formal_get_colaborador(empleado_codigo):
    if not empleado_codigo:
        return []
    empleado = list(Formal_empleado.objects.filter(jefe_inmediato__in=empleado_codigo).exclude(codigo__in=empleado_codigo).values_list("codigo",flat=True))
    result = formal_get_colaborador(empleado)
    result.extend(empleado)    

    return result

def formal_get_sub_unidades(unidad_codigo):
    if not unidad_codigo:
        return []
    unidad = list(Formal_Unidad_Organizativa.objects.filter(codigo__in=unidad_codigo).exclude(unidad_organizativa_jeraquia__codigo__in=unidad_codigo).values_list("unidad_organizativa_jeraquia__codigo",flat=True))
    result = formal_get_sub_unidades(unidad)
    result.extend(unidad_codigo)    

    return result

def funcional_get_sub_unidades(unidad_codigo):
    if not unidad_codigo:
        return []
    unidad = list(Funcional_Unidad_Organizativa.objects.filter(codigo__in=unidad_codigo).exclude(unidad_organizativa_jeraquia__codigo__in=unidad_codigo).values_list("unidad_organizativa_jeraquia__codigo",flat=True))
    result = funcional_get_sub_unidades(unidad)
    result.extend(unidad_codigo)    

    return result



class Formal_ClasificacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Clasificacion.objects.all()
    serializer_class = Formal_Clasificacionserializer


class Formal_empleadoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_empleado.objects.all()
    serializer_class = Formal_empleadoserializer
    def list(self, request):
        usuario = request.user
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        if 'jefe' in grupos:

            #print('si entro como jefe',usuario.username)
            colaboradores = formal_get_colaborador([usuario.username])
            #print('colaboradores',colaboradores)
            queryset = Formal_empleado.objects.all()
            objeto= Formal_empleado.objects.filter(codigo__in=colaboradores)
            serializer = Formal_empleadoserializer(queryset, many=True)
            filter=''        
            orga=0
            activo=''
            if self.request.query_params.get('activo'):
                activo=self.request.query_params.get('activo')
            
            if activo!='':
               #print('solo activos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                
                if self.request.query_params.get('orga'):
                    orga = self.request.query_params.get('orga')
                    objeto= Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo)
                
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                   #print('opcion1')
                    if self.request.query_params.get('filter')!='':
                       #print('opcion2')
                        queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                       #print('opcion3')
                        queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                        #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
                elif  filter !='':
                   #print('opcion4')
                    #print(filter) 
                    filtro=str(filter).strip()
                    #print('entro a solo filter',filtro)
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                    #print('resultados',queryset.query)
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                   #print('opcion5')
                    queryset = Formal_empleado.objects.filter(Q(codigo__in=colaboradores),unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('todos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                
                if self.request.query_params.get('orga'):
                    orga = self.request.query_params.get('orga')
                    objeto= Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores)
                
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                   #print('opcion1')
                    if self.request.query_params.get('filter')!='':
                       #print('opcion2')
                        queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                       #print('opcion3')
                        queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                        #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
                elif  filter !='':
                   #print('opcion4')
                    #print(filter) 
                    filtro=str(filter).strip()
                    #print('entro a solo filter',filtro)
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).order_by('-id')
                    #print('resultados',queryset.query)
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                   #print('opcion5')
                    queryset = Formal_empleado.objects.filter(Q(codigo__in=colaboradores),unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
        else: #para otro perfil distinto a jefe
            queryset = Formal_empleado.objects.all()
            objeto= Formal_empleado.objects.all()
            serializer = Formal_empleadoserializer(queryset, many=True)
            filter=''        
            orga=0
            activo=''

            if self.request.query_params.get('activo'):
                activo=self.request.query_params.get('activo')
            
            if activo!='':
               #print('Activos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                
                if self.request.query_params.get('orga'):
                    orga = self.request.query_params.get('orga')
                    objeto= Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo)
                
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                   #print('opcion10')
                    if self.request.query_params.get('filter')!='':
                       #print('opcion20')
                        queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                       #print('opcion30')
                        queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                        #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
                elif  filter !='':
                   #print('opcion40')
                    #print(filter) 
                    filtro=str(filter).strip()
                    #print('entro a solo filter',filtro)
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).order_by('-id')
                    #print('resultados',queryset.query)
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                   #print('opcion50')
                    queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
            else: 
               #print('Todos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                
                if self.request.query_params.get('orga'):
                    orga = self.request.query_params.get('orga')
                    objeto= Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga)
                
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                   #print('opcion10')
                    if self.request.query_params.get('filter')!='':
                       #print('opcion20')
                        queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                       #print('opcion30')
                        queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                        #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
                elif  filter !='':
                   #print('opcion40')
                    #print(filter) 
                    filtro=str(filter).strip()
                    #print('entro a solo filter',filtro)
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')
                    #print('resultados',queryset.query)
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                   #print('opcion50')
                    queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})



class Formal_empleado_fotoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_empleado.objects.all()
    serializer_class = Formal_empleado_foto_serializer




class Formal_empleadonodoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_empleado.objects.all()
    serializer_class = Formal_empleado_nodojerarquiaserializer
    def list(self, request):
        #print(request.data)

        queryset = Formal_empleado.objects.all()
        objeto= Formal_empleado.objects.all()
        serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
        filter=''        
        orga=0
        unidad =0
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('orga'):
            orga = self.request.query_params.get('orga')
        
        if self.request.query_params.get('unidad'):
            unidad = self.request.query_params.get('unidad')

        if 'unidad' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 dirige = Formal_Unidad_Organizativa.objects.filter(id=unidad).values_list('Dirigido_por',flat=True)
                 queryset = Formal_empleado.objects.filter(unidad_organizativa__id=unidad,fecha_baja=None).exclude(codigo__in=dirige,situacion_actual__descripcion='Dado de baja').order_by('nombre')[offset:offset+limit]
                 serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('unidad')!=0:
                dirige = Formal_Unidad_Organizativa.objects.filter(id=unidad).values_list('Dirigido_por',flat=True)
                queryset = Formal_empleado.objects.filter(unidad_organizativa__id=unidad,fecha_baja=None).exclude(codigo__in=dirige,situacion_actual__descripcion='Dado de baja').order_by('nombre')
                serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})



        if 'orga' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('nombre')[offset:offset+limit]
                 serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
                queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('nombre')
                serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})





        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('-id')[offset:offset+limit]
                serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_empleado.objects.filter(fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('-id')[offset:offset+limit]
                serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_empleado.objects.filter(fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('-id')
            serializer = Formal_empleado_nodojerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_empleadonodoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = Funcional_empleado_nodojerarquiaserializer
    def list(self, request):
        #print(request.data)

        queryset = Funcional_empleado.objects.all()
        objeto= Funcional_empleado.objects.all()
        serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
        filter=''        
        orga=0
        unidad =0
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('orga'):
            orga = self.request.query_params.get('orga')
        
        if self.request.query_params.get('unidad'):
            unidad = self.request.query_params.get('unidad')

        if 'unidad' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 dirige = Funcional_Unidad_Organizativa.objects.filter(id=unidad).values_list('Dirigido_por',flat=True)
                 queryset = Funcional_empleado.objects.filter(unidad_organizativa__id=unidad,fecha_baja=None).exclude(codigo__in=dirige,situacion_actual__descripcion='Dado de baja').order_by('nombre')[offset:offset+limit]
                 serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('unidad')!=0:
                dirige = Funcional_Unidad_Organizativa.objects.filter(id=unidad).values_list('Dirigido_por',flat=True)
                queryset = Funcional_empleado.objects.filter(unidad_organizativa__id=unidad,fecha_baja=None).exclude(codigo__in=dirige,situacion_actual__descripcion='Dado de baja').order_by('nombre')
                serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})



        if 'orga' in self.request.query_params:
            #print('este es el filtro',orga)
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                 offset=int(self.request.query_params.get('offset'))
                 limit=int(self.request.query_params.get('limit'))
                 queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('nombre')[offset:offset+limit]
                 serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
                 return Response({"data":serializer.data,"count":queryset.count()})
            elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
                queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('nombre')
                serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})





        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('-id')[offset:offset+limit]
                serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_empleado.objects.filter(fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('-id')[offset:offset+limit]
                serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_empleado.objects.filter(fecha_baja=None).exclude(situacion_actual__descripcion='Dado de baja').order_by('-id')
            serializer = Funcional_empleado_nodojerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


#agregado
class Formal_Relacion_LaboralViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Relacion_Laboral.objects.all()
    serializer_class = Formal_Relacion_Laboralserializer
    def list(self, request):
        queryset = Formal_Relacion_Laboral.objects.all()
        objeto= Formal_Relacion_Laboral.objects.all()
        serializer = Formal_Relacion_Laboralserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Relacion_Laboral.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Relacion_Laboralserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Relacion_Laboral.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Relacion_Laboralserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Relacion_Laboral.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Relacion_Laboralserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Relacion_Laboral.objects.all().order_by('-id')
            serializer = Formal_Relacion_Laboralserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_DivisionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Division.objects.all()
    serializer_class = Formal_Divisionserializer
    def list(self, request):
        queryset = Formal_Division.objects.all()
        objeto= Formal_Division.objects.all()
        serializer = Formal_Divisionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Division.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Division.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Formal_Divisionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Division.objects.all().order_by('-id')[offset:offset+limit]
                queryset = Formal_Division.objects.all().order_by('-id')
                serializer = Formal_Divisionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Division.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Divisionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Division.objects.all().order_by('-id')
            serializer = Formal_Divisionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_Division_PersonalViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Division_Personal.objects.all()
    serializer_class = Formal_Division_Personalserializer
    def list(self, request):
        queryset = Formal_Division_Personal.objects.all()
        objeto= Formal_Division_Personal.objects.all()
        serializer = Formal_Division_Personalserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Division_Personal.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Division_Personal.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Formal_Division_Personalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Division_Personal.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Division_Personal.objects.all().order_by('-id')
                serializer = Formal_Division_Personalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Division_Personal.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Division_Personalserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Division_Personal.objects.all().order_by('-id')
            serializer = Formal_Division_Personalserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_OrganizacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Organizacion.objects.all()
    serializer_class = Formal_Organizacionserializer
    def list(self, request):
        queryset = Formal_Organizacion.objects.all()
        objeto= Formal_Organizacion.objects.all()
        serializer = Formal_Organizacionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Organizacion.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Organizacion.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
                serializer = Formal_Organizacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Organizacion.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Organizacion.objects.all().order_by('-id')
                serializer = Formal_Organizacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Organizacion.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Organizacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Organizacion.objects.all().order_by('-id')
            serializer = Formal_Organizacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_Centro_CostoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Centro_Costo.objects.all()
    serializer_class = Formal_Centro_Costoserializer
    def list(self, request):
        queryset = Formal_Centro_Costo.objects.all()
        objeto= Formal_Centro_Costo.objects.all()
        serializer = Formal_Centro_Costoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Centro_Costo.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Centro_Costoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Centro_Costo.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Centro_Costoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Centro_Costo.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Centro_Costoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Centro_Costo.objects.all().order_by('-id')
            serializer = Formal_Centro_Costoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_Estado_civilViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Estado_civil.objects.all()
    serializer_class = Formal_Estado_civilserializer
    def list(self, request):
        queryset = Formal_Estado_civil.objects.all()
        objeto= Formal_Estado_civil.objects.all()
        serializer = Formal_Estado_civilserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Estado_civil.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Estado_civilserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Estado_civil.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Estado_civilserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Estado_civil.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Estado_civilserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Estado_civil.objects.all().order_by('-id')
            serializer = Formal_Estado_civilserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_Relacion_LaboralViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Relacion_Laboral.objects.all()
    serializer_class = Funcional_Relacion_Laboralserializer
    def list(self, request):
        queryset = Funcional_Relacion_Laboral.objects.all()
        objeto= Funcional_Relacion_Laboral.objects.all()
        serializer = Funcional_Relacion_Laboralserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Relacion_Laboral.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Relacion_Laboralserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Relacion_Laboral.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Relacion_Laboralserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Relacion_Laboral.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Relacion_Laboralserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Relacion_Laboral.objects.all().order_by('-id')
            serializer = Funcional_Relacion_Laboralserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_DivisionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Division.objects.all()
    serializer_class = Funcional_Divisionserializer
    def list(self, request):
        queryset = Funcional_Division.objects.all()
        objeto= Funcional_Division.objects.all()
        serializer = Funcional_Divisionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Division.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Division.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Funcional_Divisionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Division.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Division.objects.all().order_by('-id')
                serializer = Funcional_Divisionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Division.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Divisionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Division.objects.all().order_by('-id')
            serializer = Funcional_Divisionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_Division_PersonalViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Division_Personal.objects.all()
    serializer_class = Funcional_Division_Personalserializer
    def list(self, request):
        queryset = Funcional_Division_Personal.objects.all()
        objeto= Funcional_Division_Personal.objects.all()
        serializer = Funcional_Division_Personalserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Division_Personal.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Division_Personal.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Funcional_Division_Personalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Division_Personal.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Division_Personal.objects.all().order_by('-id')
                serializer = Funcional_Division_Personalserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Division_Personal.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Division_Personalserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Division_Personal.objects.all().order_by('-id')
            serializer = Funcional_Division_Personalserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Funcional_Centro_CostoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Centro_Costo.objects.all()
    serializer_class = Funcional_Centro_Costoserializer
    def list(self, request):
        queryset = Funcional_Centro_Costo.objects.all()
        objeto= Funcional_Centro_Costo.objects.all()
        serializer = Funcional_Centro_Costoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Centro_Costo.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Centro_Costoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Centro_Costo.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Centro_Costoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Centro_Costo.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Centro_Costoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Centro_Costo.objects.all().order_by('-id')
            serializer = Funcional_Centro_Costoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_OrganizacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Organizacion.objects.all()
    serializer_class = Funcional_Organizacionserializer
    def list(self, request):
        queryset = Funcional_Organizacion.objects.all()
        objeto= Funcional_Organizacion.objects.all()
        serializer = Funcional_Organizacionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Organizacion.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Organizacion.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
                serializer = Funcional_Organizacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Organizacion.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Organizacion.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Organizacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Organizacion.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Organizacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Organizacion.objects.all().order_by('-id')
            serializer = Funcional_Organizacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_Estado_civilViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Estado_civil.objects.all()
    serializer_class = Funcional_Estado_civilserializer
    def list(self, request):
        queryset = Funcional_Estado_civil.objects.all()
        objeto= Funcional_Estado_civil.objects.all()
        serializer = Funcional_Estado_civilserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Estado_civil.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Estado_civilserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Estado_civil.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Estado_civilserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Estado_civil.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Estado_civilserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Estado_civil.objects.all().order_by('-id')
            serializer = Funcional_Estado_civilserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_ParentescoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Parentesco.objects.all()
    serializer_class = Formal_Parentescoserializer
    def list(self, request):
        queryset = Formal_Parentesco.objects.all()
        objeto= Formal_Parentesco.objects.all()
        serializer = Formal_Parentescoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Parentesco.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Parentescoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Parentesco.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Parentescoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Parentesco.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Parentescoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Parentesco.objects.all().order_by('-id')
            serializer = Formal_Parentescoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_ParentescoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Parentesco.objects.all()
    serializer_class = Funcional_Parentescoserializer
    def list(self, request):
        queryset = Funcional_Parentesco.objects.all()
        objeto= Funcional_Parentesco.objects.all()
        serializer = Funcional_Parentescoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Parentesco.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Parentescoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Parentesco.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Parentescoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Parentesco.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Parentescoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Parentesco.objects.all().order_by('-id')
            serializer = Funcional_Parentescoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_GeneroViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Genero.objects.all()
    serializer_class = Formal_Generoserializer
    def list(self, request):
        queryset = Formal_Genero.objects.all()
        objeto= Formal_Genero.objects.all()
        serializer = Formal_Generoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Genero.objects.filter(nombre__icontains=filter).order_by('-id')[offset:offset+limit]
                serializer = Formal_Generoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Genero.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Generoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Genero.objects.filter(nombre__icontains=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Generoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Genero.objects.all().order_by('-id')
            serializer = Formal_Generoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_GeneroViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Genero.objects.all()
    serializer_class = Funcional_Generoserializer
    def list(self, request):
        queryset = Funcional_Genero.objects.all()
        objeto= Funcional_Genero.objects.all()
        serializer = Funcional_Generoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Genero.objects.filter(nombre__icontains=filter).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Generoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Genero.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Generoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Genero.objects.filter(nombre__icontains=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Generoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Genero.objects.all().order_by('-id')
            serializer = Funcional_Generoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_FuncionesViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Funciones.objects.all()
    serializer_class = Formal_Funcionesserializer
    def list(self, request):
        queryset = Formal_Funciones.objects.all()
        objeto= Formal_Funciones.objects.all()
        serializer = Formal_Funcionesserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Funciones.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2= Formal_Funciones.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Formal_Funcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Funciones.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Funciones.objects.all().order_by('-id')
                serializer = Formal_Funcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Funciones.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Funcionesserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Funciones.objects.all().order_by('-id')
            serializer = Formal_Funcionesserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_FuncionesViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Funciones.objects.all()
    serializer_class = Funcional_Funcionesserializer
    def list(self, request):
        queryset = Funcional_Funciones.objects.all()
        objeto= Funcional_Funciones.objects.all()
        serializer = Funcional_Funcionesserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Funciones.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Funciones.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Funcional_Funcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Funciones.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Funciones.objects.all().order_by('-id')
                serializer = Funcional_Funcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Funciones.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Funcionesserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Funciones.objects.all().order_by('-id')
            serializer = Funcional_Funcionesserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

#agregado 2
class Formal_Situacion_ActualViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Situacion_Actual.objects.all()
    serializer_class = Formal_Situacion_Actualserializer
    def list(self, request):
        queryset = Formal_Situacion_Actual.objects.all()
        objeto= Formal_Situacion_Actual.objects.all()
        serializer = Formal_Situacion_Actualserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Situacion_Actual.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Situacion_Actualserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Situacion_Actual.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Situacion_Actualserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Situacion_Actual.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Situacion_Actualserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Situacion_Actual.objects.all().order_by('-id')
            serializer = Formal_Situacion_Actualserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_Situacion_ActualViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Situacion_Actual.objects.all()
    serializer_class = Funcional_Situacion_Actualserializer
    def list(self, request):
        queryset = Funcional_Situacion_Actual.objects.all()
        objeto= Funcional_Situacion_Actual.objects.all()
        serializer = Funcional_Situacion_Actualserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Situacion_Actual.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Situacion_Actualserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Situacion_Actual.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Situacion_Actualserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Situacion_Actual.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Situacion_Actualserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Situacion_Actual.objects.all().order_by('-id')
            serializer = Funcional_Situacion_Actualserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_CompañiaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Compañia.objects.all()
    serializer_class = Formal_Compañiaserializer
    def list(self, request):
        queryset = Formal_Compañia.objects.all()
        objeto= Formal_Compañia.objects.all()
        serializer = Formal_Compañiaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Compañia.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Compañiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Compañia.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Compañiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Compañia.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Compañiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Compañia.objects.all().order_by('-id')
            serializer = Formal_Compañiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_CompañiaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Compañia.objects.all()
    serializer_class = Funcional_Compañiaserializer
    def list(self, request):
        queryset = Funcional_Compañia.objects.all()
        objeto= Funcional_Compañia.objects.all()
        serializer = Funcional_Compañiaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Compañia.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Compañiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Compañia.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Compañiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Compañia.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Compañiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Compañia.objects.all().order_by('-id')
            serializer = Funcional_Compañiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_EspecialidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Especialidad.objects.all()
    serializer_class = Formal_Especialidadserializer
    def list(self, request):
        queryset = Formal_Especialidad.objects.all()
        objeto= Formal_Especialidad.objects.all()
        serializer = Formal_Especialidadserializer(queryset, many=True)
        filter=''

        if self.request.query_params.get('instituto')!='' and self.request.query_params.get('instituto')!=None :    
           #print('si entro1')
            instituto=self.request.query_params.get('instituto')            
            queryset = Formal_Especialidad.objects.filter(universidad__id=instituto).order_by('-id')
            queryset2 = Formal_Especialidad.objects.filter(universidad__id=instituto).order_by('-id')
            serializer = Formal_Especialidadserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset2.count()})


        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
           #print('si entro2')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
           #print('si entro2')
            if self.request.query_params.get('filter')!='':
               #print('si entro3')
                queryset = Formal_Especialidad.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Especialidad.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Formal_Especialidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
               #print('si entro4')
                queryset = Formal_Especialidad.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Especialidad.objects.all().order_by('-id')
                serializer = Formal_Especialidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
           #print('si entro5')
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Especialidad.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Especialidadserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
           #print('si entro5')
            queryset = Formal_Especialidad.objects.all().order_by('-id')
            serializer = Formal_Especialidadserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_EspecialidadViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Especialidad.objects.all()
    serializer_class = Funcional_Especialidadserializer
    def list(self, request):
        queryset = Funcional_Especialidad.objects.all()
        objeto= Funcional_Especialidad.objects.all()
        serializer = Funcional_Especialidadserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('instituto')!='' and self.request.query_params.get('instituto')!=None :   
            instituto=self.request.query_params.get('instituto')            
            queryset = Funcional_Especialidad.objects.filter(universidad__id=instituto).order_by('-id')
            queryset2 = Funcional_Especialidad.objects.filter(universidad__id=instituto).order_by('-id')
            serializer = Funcional_Especialidadserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset2.count()})

        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Especialidad.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Especialidad.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Funcional_Especialidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Especialidad.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Especialidad.objects.all().order_by('-id')
                serializer = Funcional_Especialidadserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Especialidad.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Especialidadserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Especialidad.objects.all().order_by('-id')
            serializer = Funcional_Especialidadserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_Contacto_EmergenciaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Contacto_Emergencia.objects.all()
    serializer_class = Formal_Contacto_Emergenciaserializer
    def list(self, request):
        queryset = Formal_Contacto_Emergencia.objects.all()
        objeto= Formal_Contacto_Emergencia.objects.all()
        serializer = Formal_Contacto_Emergenciaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Contacto_Emergencia.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Formal_Contacto_Emergenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Contacto_Emergencia.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Contacto_Emergenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Contacto_Emergencia.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Contacto_Emergenciaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Contacto_Emergencia.objects.all().order_by('-id')
            serializer = Formal_Contacto_Emergenciaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_Contacto_EmergenciaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Contacto_Emergencia.objects.all()
    serializer_class = Funcional_Contacto_Emergenciaserializer
    def list(self, request):
        queryset = Funcional_Contacto_Emergencia.objects.all()
        objeto= Funcional_Contacto_Emergencia.objects.all()
        serializer = Funcional_Contacto_Emergenciaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Contacto_Emergencia.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Contacto_Emergenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Contacto_Emergencia.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Contacto_Emergenciaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Contacto_Emergencia.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Contacto_Emergenciaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Contacto_Emergencia.objects.all().order_by('-id')
            serializer = Funcional_Contacto_Emergenciaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_Dependientes_EconomicoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Dependientes_Economico.objects.all()
    serializer_class = Formal_Dependientes_Economicoserializer
    def list(self, request):
        queryset = Formal_Dependientes_Economico.objects.all()
        objeto= Formal_Dependientes_Economico.objects.all()
        serializer = Formal_Dependientes_Economicoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Dependientes_Economico.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Formal_Dependientes_Economicoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Dependientes_Economico.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Dependientes_Economicoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Dependientes_Economico.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Dependientes_Economicoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Dependientes_Economico.objects.all().order_by('-id')
            serializer = Formal_Dependientes_Economicoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_Dependientes_EconomicoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Dependientes_Economico.objects.all()
    serializer_class = Funcional_Dependientes_Economicoserializer
    def list(self, request):
        queryset = Funcional_Dependientes_Economico.objects.all()
        objeto= Funcional_Dependientes_Economico.objects.all()
        serializer = Funcional_Dependientes_Economicoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Dependientes_Economico.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Dependientes_Economicoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Dependientes_Economico.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Dependientes_Economicoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Dependientes_Economico.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Dependientes_Economicoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Dependientes_Economico.objects.all().order_by('-id')
            serializer = Funcional_Dependientes_Economicoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_Beneficiario_SeguroViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Beneficiario_Seguro.objects.all()
    serializer_class = Formal_Beneficiario_Seguroserializer
    def list(self, request):
        queryset = Formal_Beneficiario_Seguro.objects.all()
        objeto= Formal_Beneficiario_Seguro.objects.all()
        serializer = Formal_Beneficiario_Seguroserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Beneficiario_Seguro.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Formal_Beneficiario_Seguroserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Beneficiario_Seguro.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Beneficiario_Seguroserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Beneficiario_Seguro.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Beneficiario_Seguroserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Beneficiario_Seguro.objects.all().order_by('-id')
            serializer = Formal_Beneficiario_Seguroserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_Beneficiario_SeguroViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Beneficiario_Seguro.objects.all()
    serializer_class = Funcional_Beneficiario_Seguroserializer
    def list(self, request):
        queryset = Funcional_Beneficiario_Seguro.objects.all()
        objeto= Funcional_Beneficiario_Seguro.objects.all()
        serializer = Funcional_Beneficiario_Seguroserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Beneficiario_Seguro.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Beneficiario_Seguroserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Beneficiario_Seguro.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Beneficiario_Seguroserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Beneficiario_Seguro.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Beneficiario_Seguroserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Beneficiario_Seguro.objects.all().order_by('-id')
            serializer = Funcional_Beneficiario_Seguroserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_FormacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Formacion.objects.all()
    serializer_class = Formal_Formacionserializer
    def list(self, request):
        queryset = Formal_Formacion.objects.all()
        objeto= Formal_Formacion.objects.all()
        serializer = Formal_Formacionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Formacion.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Formacion.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Formal_Formacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Formacion.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Formacion.objects.all().order_by('-id')
                serializer = Formal_Formacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Formacion.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Formacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Formacion.objects.all().order_by('-id')
            serializer = Formal_Formacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_FormacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Formacion.objects.all()
    serializer_class = Funcional_Formacionserializer
    def list(self, request):
        queryset = Funcional_Formacion.objects.all()
        objeto= Funcional_Formacion.objects.all()
        serializer = Funcional_Formacionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Formacion.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Formacion.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Funcional_Formacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Formacion.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Formacion.objects.all().order_by('-id')
                serializer = Funcional_Formacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Formacion.objects.filter(Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Formacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Formacion.objects.all().order_by('-id')
            serializer = Funcional_Formacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_EquipoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Equipo.objects.all()
    serializer_class = Funcional_Equiposerializer
    def list(self, request):
        queryset = Funcional_Equipo.objects.all()
        objeto= Funcional_Equipo.objects.all()
        serializer = Funcional_Equiposerializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Equipo.objects.filter(Q(service_tag__icontains=filter)|Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Equiposerializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Equipo.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Equiposerializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Equipo.objects.filter(Q(service_tag__icontains=filter)|Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Equiposerializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Equipo.objects.all().order_by('-id')
            serializer = Funcional_Equiposerializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_EquipoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Equipo.objects.all()
    serializer_class = Formal_Equiposerializer
    def list(self, request):
        queryset = Formal_Equipo.objects.all()
        objeto= Formal_Equipo.objects.all()
        serializer = Formal_Equiposerializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Equipo.objects.filter(Q(service_tag__icontains=filter)|Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Equiposerializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Equipo.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Equiposerializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Equipo.objects.filter(Q(service_tag__icontains=filter)|Q(codigo__icontains=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Equiposerializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Equipo.objects.all().order_by('-id')
            serializer = Formal_Equiposerializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Formal_Relacion_Laboral_AnteriorViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Relacion_Laboral_Anterior.objects.all()
    serializer_class = Formal_Relacion_Laboral_Anteriorserializer
    def list(self, request):
        queryset = Formal_Relacion_Laboral_Anterior.objects.all()
        objeto= Formal_Relacion_Laboral_Anterior.objects.all()
        serializer = Formal_Relacion_Laboral_Anterior(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Relacion_Laboral_Anterior.objects.filter(Q(codigo=filter)|Q(descripcion=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Relacion_Laboral_Anteriorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Relacion_Laboral_Anterior.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Relacion_Laboral_Anteriorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset =Formal_Relacion_Laboral_Anterior.objects.filter(Q(codigo=filter)|Q(descripcion=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Relacion_Laboral_Anteriorserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Relacion_Laboral_Anterior.objects.all().order_by('-id')
            serializer = Formal_Relacion_Laboral_Anteriorserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})



class Formal_Historial_LaboralViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Historial_Laboral.objects.all()
    serializer_class = Formal_Historial_Laboralserializer
    def list(self, request):
        queryset = Formal_Historial_Laboral.objects.all()
        objeto= Formal_Historial_Laboral.objects.all()
        serializer = Formal_Historial_Laboralserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Historial_Laboral.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Formal_Historial_Laboralserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Historial_Laboral.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Historial_Laboralserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Historial_Laboral.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Historial_Laboralserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Historial_Laboral.objects.all().order_by('-id')
            serializer = Formal_Historial_Laboralserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Funcional_Relacion_Laboral_AnteriorViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Relacion_Laboral_Anterior.objects.all()
    serializer_class = Funcional_Relacion_Laboral_Anteriorserializer
    def list(self, request):
        queryset = Funcional_Relacion_Laboral_Anterior.objects.all()
        objeto= Funcional_Relacion_Laboral_Anterior.objects.all()
        serializer = Funcional_Relacion_Laboral_Anterior(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Relacion_Laboral_Anterior.objects.filter(Q(codigo=filter)|Q(descripcion=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Relacion_Laboral_Anteriorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Relacion_Laboral_Anterior.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Relacion_Laboral_Anteriorserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset =Funcional_Relacion_Laboral_Anterior.objects.filter(Q(codigo=filter)|Q(descripcion=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Relacion_Laboral_Anteriorserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Relacion_Laboral_Anterior.objects.all().order_by('-id')
            serializer = Funcional_Relacion_Laboral_Anteriorserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Funcional_Historial_LaboralViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Historial_Laboral.objects.all()
    serializer_class = Funcional_Historial_Laboralserializer
    def list(self, request):
        queryset = Funcional_Historial_Laboral.objects.all()
        objeto= Funcional_Historial_Laboral.objects.all()
        serializer = Funcional_Historial_Laboralserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Historial_Laboral.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Historial_Laboralserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Historial_Laboral.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Historial_Laboralserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Historial_Laboral.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Historial_Laboralserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Historial_Laboral.objects.all().order_by('-id')
            serializer = Funcional_Historial_Laboralserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Formal_InstitutoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Instituto.objects.all()
    serializer_class = Formal_Institutoserializer
    def list(self, request):
        queryset = Formal_Instituto.objects.all()
        objeto= Formal_Instituto.objects.all()
        serializer = Formal_Institutoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Instituto.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Instituto.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Formal_Institutoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Instituto.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Instituto.objects.all().order_by('-id')
                serializer = Formal_Institutoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Instituto.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Institutoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Instituto.objects.all().order_by('-id')
            serializer = Formal_Institutoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_TituloViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Titulo.objects.all()
    serializer_class = Formal_Tituloserializer
    def list(self, request):
        queryset = Formal_Titulo.objects.all()
        objeto= Formal_Titulo.objects.all()
        serializer = Formal_Tituloserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('instituto'):
                instituto=self.request.query_params.get('instituto')
                queryset = Formal_Titulo.objects.filter(Q(universidad=instituto)).order_by('-id')
                queryset2 = Formal_Titulo.objects.filter(Q(universidad=instituto)).order_by('-id')
                serializer = Formal_Tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Titulo.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Titulo.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Formal_Tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Titulo.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Titulo.objects.all().order_by('-id')
                serializer = Formal_Tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Titulo.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Tituloserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Titulo.objects.all().order_by('-id')
            serializer = Formal_Tituloserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_DiagnosticoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Diagnostico.objects.all()
    serializer_class = Formal_Diagnosticoserializer
    def list(self, request):
        queryset = Formal_Diagnostico.objects.all()
        objeto= Formal_Diagnostico.objects.all()
        serializer = Formal_Diagnosticoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Diagnostico.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Diagnostico.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Formal_Diagnosticoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Diagnostico.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Diagnostico.objects.all().order_by('-id')
                serializer = Formal_Diagnosticoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Diagnostico.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Diagnosticoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Diagnostico.objects.all().order_by('-id')
            serializer = Formal_Diagnosticoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})



class Formal_SaludViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Salud.objects.all()
    serializer_class = Formal_Saludserializer
    def list(self, request):
        queryset = Formal_Salud.objects.all()
        objeto= Formal_Salud.objects.all()
        serializer = Formal_Saludserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Salud.objects.filter(Q(diagnostico=filter)|Q(empleado=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Saludserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Salud.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Saludserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Salud.objects.filter(Q(diagnostico=filter)|Q(empleado=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Saludserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Salud.objects.all().order_by('-id')
            serializer = Formal_Saludserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_EducacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Educacion.objects.all()
    serializer_class = Formal_Educacionserializer
    def list(self, request):
        queryset = Formal_Educacion.objects.all()
        objeto= Formal_Educacion.objects.all()
        serializer = Formal_Educacionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Educacion.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Formal_Educacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Educacion.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Educacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Educacion.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Educacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Educacion.objects.all().order_by('-id')
            serializer = Formal_Educacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

#nuevos funcional

class Funcional_InstitutoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Instituto.objects.all()
    serializer_class = Funcional_Institutoserializer
    def list(self, request):
        queryset = Funcional_Instituto.objects.all()
        objeto= Funcional_Instituto.objects.all()
        serializer = Funcional_Institutoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Instituto.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Instituto.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Funcional_Institutoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Instituto.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Instituto.objects.all().order_by('-id')
                serializer = Funcional_Institutoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Instituto.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Institutoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Instituto.objects.all().order_by('-id')
            serializer = Funcional_Institutoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_TituloViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Titulo.objects.all()
    serializer_class = Funcional_Tituloserializer
    def list(self, request):
        queryset = Funcional_Titulo.objects.all()
        objeto= Funcional_Titulo.objects.all()
        serializer = Funcional_Tituloserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('instituto'):
            instituto=self.request.query_params.get('instituto')
            queryset = Funcional_Titulo.objects.filter(Q(universidad=instituto)).order_by('-id')
            queryset2 = Funcional_Titulo.objects.filter(Q(universidad=instituto)).order_by('-id')
            serializer = Funcional_Tituloserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset2.count()})

        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Titulo.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Titulo.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Funcional_Tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Titulo.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Titulo.objects.all().order_by('-id')
                serializer = Funcional_Tituloserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Titulo.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Tituloserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Titulo.objects.all().order_by('-id')
            serializer = Funcional_Tituloserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_DiagnosticoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Diagnostico.objects.all()
    serializer_class = Funcional_Diagnosticoserializer
    def list(self, request):
        queryset = Funcional_Diagnostico.objects.all()
        objeto= Funcional_Diagnostico.objects.all()
        serializer = Funcional_Diagnosticoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Diagnostico.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Diagnostico.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
                serializer = Funcional_Diagnosticoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Diagnostico.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Diagnostico.objects.all().order_by('-id')
                serializer = Funcional_Diagnosticoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Diagnostico.objects.filter(Q(codigo=filter)|Q(descripcion__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Diagnosticoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Diagnostico.objects.all().order_by('-id')
            serializer = Funcional_Diagnosticoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})



class Funcional_SaludViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Salud.objects.all()
    serializer_class = Funcional_Saludserializer
    def list(self, request):
        queryset = Funcional_Salud.objects.all()
        objeto= Funcional_Salud.objects.all()
        serializer = Funcional_Saludserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Salud.objects.filter(Q(diagnostico=filter)|Q(empleado=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Saludserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Salud.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Saludserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Salud.objects.filter(Q(diagnostico=filter)|Q(empleado=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Saludserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Salud.objects.all().order_by('-id')
            serializer = Funcional_Saludserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_EducacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Educacion.objects.all()
    serializer_class = Funcional_Educacionserializer
    def list(self, request):
        queryset = Funcional_Educacion.objects.all()
        objeto= Funcional_Educacion.objects.all()
        serializer = Funcional_Educacionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Educacion.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Educacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Educacion.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Educacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Educacion.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Educacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Educacion.objects.all().order_by('-id')
            serializer = Funcional_Educacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})




class Formal_User_DataViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    def get(self, request):
        usuario=request.user
        #Usuario_Log.objects.create(usuario=usuario,actividad='login')
        estructura=0
        actualizacion=Configuracion_Actualizacion_Empleado.objects.filter(activo=True).order_by("-id") if Configuracion_Actualizacion_Empleado.objects.filter(activo=True) else None
        actualizacion_fecha_inicial = actualizacion[0].fecha_inicio if actualizacion !=None else None
        actualizacion_fecha_final = actualizacion[0].fecha_fin if actualizacion !=None else None
        actualizado = False
        unidad=''
        organizacion=''
        username =usuario.username
        username = username.zfill(8)
        
        empleado=Funcional_empleado.objects.filter(codigo=username) [0] if Funcional_empleado.objects.filter(codigo=username) else None

        if empleado == None:
            empleado=Formal_empleado.objects.filter(codigo=username)[0] if Formal_empleado.objects.filter(codigo=username) else None
            if empleado == None:
                return Response({"mensaje":"No Existe el usuario"},status= status.HTTP_404_NOT_FOUND)
            else:
                estructura=1

                if actualizacion !=None:
                    if (datetime.now().date() >= actualizacion_fecha_inicial and datetime.now().date()<=actualizacion_fecha_final):
                        actualizado=True if (empleado.updated_at >= actualizacion_fecha_inicial and  empleado.updated_at <=actualizacion_fecha_final) or  empleado.updated_at >=actualizacion_fecha_final else False
                    else:
                        actualizado=True
                else:
                    actualizado = True
                
                unidad = formal_unidad_organizativabasicoserializer(empleado.unidad_organizativa.all(),many=True).data
                organizacion = Formal_Organizacionserializer(Formal_Organizacion.objects.filter(codigo__in=list(empleado.unidad_organizativa.all().values_list('sociedad_financiera__codigo',flat=True))),many=True).data
        else:
            estructura=2

            if actualizacion !=None:
                if (datetime.now().date() >= actualizacion_fecha_inicial and datetime.now().date()<=actualizacion_fecha_final):
                    actualizado=True if (empleado.updated_at >= actualizacion_fecha_inicial and  empleado.updated_at <=actualizacion_fecha_final) or  empleado.updated_at >=actualizacion_fecha_final else False
                else:
                    actualizado=True
            else:
                actualizado = True

            unidad = funcional_unidad_organizativabasicoserializer(empleado.unidad_organizativa.all(),many=True).data
            organizacion = Funcional_Organizacionserializer(Funcional_Organizacion.objects.filter(codigo__in=list(empleado.unidad_organizativa.all().values_list('sociedad_financiera__codigo',flat=True))),many=True).data
       
        if empleado == None:
            return Response({"mensaje":"No Existe el usuario"},status= status.HTTP_404_NOT_FOUND)
        #empleado=empleado[0]
        #print('grupos',list(usuario.groups.all().values_list('id',flat=True)))
        id_user = User.objects.filter(username=username).values('id')[0]
        id_user = id_user['id']
        #print (id_user)
        yourdata= [{"id_user":id_user,"id": empleado.id,"username":usuario.username,"nombre":empleado.nombre,"grupo":list(usuario.groups.all().values_list('name',flat=True)),"foto":empleado.foto,"actualizado":actualizado}]
        #print (yourdata)
        results = Data_userserializer(yourdata,many=True).data
        #print (results)
        #unidades = Formal_Unidad_Organizativa.objects.filter(codigo__in=list(empleado.unidad_organizativa.all().values('codigo')))
        
        results={"empleado":results,"unidad":unidad,"empresa":organizacion,"estructura":estructura}

        return Response(results)

class Funcional_User_DataViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    def get(self, request):
        usuario=request.user
        #Usuario_Log.objects.create(usuario=usuario,actividad='login')
        
        username =usuario.username
        username = username.zfill(8)
        empleado=Funcional_empleado.objects.filter(codigo=username) if Funcional_empleado.objects.filter(codigo=username) else None
        
        if empleado == None:
            return Response({"mensaje":"No Existe el usuario"},status= status.HTTP_404_NOT_FOUND)
        empleado=empleado[0]
        #print('grupos',list(usuario.groups.all().values_list('id',flat=True)))
        yourdata= [{"id": empleado.id,"username":usuario.username,"nombre":empleado.nombre,"grupo":list(usuario.groups.all().values_list('name',flat=True)),"foto":empleado.foto}]
        results = Data_userserializer(yourdata,many=True).data
        #unidades = Formal_Unidad_Organizativa.objects.filter(codigo__in=list(empleado.unidad_organizativa.all().values('codigo')))
        unidad = funcional_unidad_organizativabasicoserializer(empleado.unidad_organizativa.all(),many=True).data
        organizacion = Funcional_Organizacionserializer(Funcional_Organizacion.objects.filter(codigo__in=list(empleado.unidad_organizativa.all().values_list('sociedad_financiera__codigo',flat=True))),many=True).data
        results={"empleado":results,"unidad":unidad,"empresa":organizacion}
        return Response(results)


class Formal_empleado_jerarquiaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_empleado.objects.all()
    serializer_class = Formal_empleado_jerarquiaserializer
    def list(self, request):
        #print(request.data)

        queryset = Formal_empleado.objects.all()
        objeto= Formal_empleado.objects.all()
        serializer = Formal_empleado_jerarquiaserializer(queryset, many=True)
        filter=''        
        orga=0
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('orga'):
            orga = self.request.query_params.get('orga')
            objeto= Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga)


        # if 'orga' in self.request.query_params:
        #     #print('este es el filtro',orga)
        #     if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
        #          offset=int(self.request.query_params.get('offset'))
        #          limit=int(self.request.query_params.get('limit'))
        #          queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('nombre')[offset:offset+limit]
        #          serializer = Formal_empleadoserializer(queryset, many=True)
        #          return Response({"data":serializer.data,"count":objeto.count()})
        #     elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
        #         queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('nombre')
        #         serializer = Formal_empleadoserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":objeto.count()})





        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
           #print('opcion1')
            if self.request.query_params.get('filter')!='':
               #print('opcion2')
                queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')[offset:offset+limit]
                serializer = Formal_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('opcion3')
                queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')[offset:offset+limit]
                serializer = Formal_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
           #print('opcion4')
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_empleado_jerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
           #print('opcion5')
            queryset = Formal_empleado.objects.all().order_by('-id')
            serializer = Formal_empleado_jerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Funcional_empleado_jerarquiaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = Funcional_empleado_jerarquiaserializer
    def list(self, request):
        #print(request.data)

        queryset = Funcional_empleado.objects.all()
        objeto= Funcional_empleado.objects.all()
        serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
        filter=''        
        orga=0
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        
        if self.request.query_params.get('orga'):
            orga = self.request.query_params.get('orga')
            objeto= Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga)
            

        # if 'orga' in self.request.query_params:
        #     #print('este es el filtro',orga)
        #     if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
        #          offset=int(self.request.query_params.get('offset'))
        #          limit=int(self.request.query_params.get('limit'))
        #          queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('nombre')[offset:offset+limit]
        #          serializer = Formal_empleadoserializer(queryset, many=True)
        #          return Response({"data":serializer.data,"count":objeto.count()})
        #     elif not (self.request.query_params.get('limit') and self.request.query_params.get('offset')) and self.request.query_params.get('orga')!=0:
        #         queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('nombre')
        #         serializer = Formal_empleadoserializer(queryset, many=True)
        #         return Response({"data":serializer.data,"count":objeto.count()})





        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
           #print('opcion1')
            if self.request.query_params.get('filter')!='':
               #print('opcion2')
                queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')[offset:offset+limit]
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('opcion3')
                queryset = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')[offset:offset+limit]
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
           #print('opcion4')
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
           #print('opcion5')
            queryset = Funcional_empleado.objects.all().order_by('-id')
            serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
            
class dashboard_plazas_contratacionesViewset(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    def get(self, request):
        usuario=request.user
        ####################################
        listado_puestos_vacantes=''
        listado_puestos_vacantes= puestos(usuario)
        lista_puestos_vacantes = listado_puestos_vacantes['plazas_vacantes']
        #####################################
        listado_puestos_activos=''
        listado_puestos_activos= puestos(usuario)
        lista_puestos_activos= listado_puestos_activos['plazas_activas']
        
        username =usuario.username
        username = username.zfill(8)
        empleado=Funcional_empleado.objects.filter(codigo=username) if Funcional_empleado.objects.filter(codigo=username) else None
        
        fecha_min=None
        fecha_max=None
        if empleado == None:
            return Response({"mensaje":"No Existe el usuario"},status= status.HTTP_404_NOT_FOUND)
        if  self.request.query_params.get('fecha_min') and self.request.query_params.get('fecha_max'):
            fecha_min=self.request.query_params.get('fecha_min')
            fecha_max=self.request.query_params.get('fecha_max')
        
        else:
            return Response({"mensaje":"Faltan parametros filtro"},status= status.HTTP_404_NOT_FOUND)
        colaboradores = funcional_get_colaborador([usuario.username])  
        colaboradores.append(usuario.username)
        unidades_jefe = list(Funcional_empleado.objects.filter(codigo=usuario.username).values_list('unidad_organizativa__codigo',flat=True))
       #print("antes",unidades_jefe)
        unidades = funcional_get_sub_unidades(unidades_jefe)
       #print("estas son las unidades",unidades)
       #print("estos son los colaboradores",colaboradores)

       
        bandera=None
        listado=[]
        unidad = Funcional_empleado.objects.filter(codigo=usuario.username).values_list('puesto__unidad_organizativa__id',flat=True)[0]
        filtros=[unidad]
        while bandera ==None:
           #print('filtros,antes',filtros)
            resultado=Funcional_Unidad_Organizativa.objects.filter(id__in=filtros).values_list('unidad_organizativa_jeraquia__id',flat=True)
           #print('filtros despues',filtros)
            listado.extend(resultado)
            
            filtros = resultado

            if resultado.count()==0 or resultado==None:
                bandera=0
        listado.append(unidad)
       #print('este es el listado',listado)


        estados=['Activo']
        empleado=empleado[0]
        empleadosXempresa= Funcional_empleado.objects.filter(codigo__in=colaboradores).values(empresa =F('unidad_organizativa__sociedad_financiera__nombre')).annotate(conteo=Count('codigo'))
        puesto_cod= list(Funcional_empleado.objects.filter(codigo__in=colaboradores).values_list('puesto__codigo',flat=True))
        puestos_existentes = Funcional_Puesto.objects.filter(activo=True).filter(Q(codigo__in=lista_puestos_vacantes)|Q(codigo__in=lista_puestos_activos)).values(empresa =F('unidad_organizativa__sociedad_financiera__nombre')).annotate(conteo=Count('codigo'))
        puestos_vacantes = Funcional_Puesto.objects.filter(activo=True).filter(codigo__in=lista_puestos_vacantes).values(empresa =F('unidad_organizativa__sociedad_financiera__nombre')).annotate(conteo=Count('codigo'))
        puestos_cubiertos = Funcional_Puesto.objects.filter(activo=True).filter(codigo__in=lista_puestos_activos).values(empresa =F('unidad_organizativa__sociedad_financiera__nombre')).annotate(conteo=Count('codigo'))
        personal_tipo_relacion = Funcional_empleado.objects.filter(codigo__in=colaboradores).values(relacion =F('relacion_laboral__descripcion')).annotate(conteo=Count('codigo'))
       
        entrada = Funcional_empleado.objects.filter((Q(codigo__in=colaboradores)|Q(unidad_organizativa__id__in=listado)),fecha_ingreso__range=[fecha_min, fecha_max]).values(anio =F('fecha_ingreso__year'),mes =F('fecha_ingreso__month')).annotate(conteo=Count('codigo')).order_by('fecha_ingreso__month','fecha_ingreso__year')
        baja = Funcional_empleado.objects.filter((Q(codigo__in=colaboradores)|Q(unidad_organizativa__id__in=listado)),fecha_baja__range=[fecha_min, fecha_max]).values(anio =F('fecha_baja__year'),mes =F('fecha_baja__month')).annotate(conteo=Count('codigo')).order_by('fecha_baja__month','fecha_baja__year')
        
        entrada_anual = Funcional_empleado.objects.filter((Q(codigo__in=colaboradores)|Q(unidad_organizativa__id__in=listado)),fecha_ingreso__range=[fecha_min, fecha_max]).values(mes =F('fecha_ingreso__month'),anio =F('fecha_ingreso__year')).annotate(conteo=Count('codigo')).order_by('fecha_ingreso__year','fecha_ingreso__month')
        entrada_baja = Funcional_empleado.objects.filter((Q(codigo__in=colaboradores)|Q(unidad_organizativa__id__in=listado)),fecha_baja__range=[fecha_min, fecha_max]).values(mes =F('fecha_baja__month'),anio =F('fecha_baja__year')).annotate(conteo=Count('codigo')).order_by('fecha_baja__year','fecha_baja__month')
        
        empleado_zona = Funcional_empleado.objects.filter(codigo__in=colaboradores).values(zona =F('division_personal__descripcion')).annotate(conteo=Count('codigo'))
        empleado_departamento = Funcional_empleado.objects.filter(codigo__in=colaboradores).values(zona =F('division__descripcion')).annotate(conteo=Count('codigo'))
        empleado_genero = Funcional_empleado.objects.filter(codigo__in=colaboradores).values('genero').annotate(conteo=Count('codigo'))
        empleado_formacion = Funcional_Educacion.objects.filter(empleado__codigo__in=colaboradores).values('formacion__descripcion').annotate(conteo=Count('empleado'))
        empleado_antiguedad = Funcional_empleado.objects.filter(codigo__in=colaboradores).values(antiguedad=(datetime.now().year-F('fecha_ingreso__year'))).annotate(conteo=Count('codigo')).order_by('antiguedad')
        empleado_centro_costo = Funcional_empleado.objects.filter(codigo__in=colaboradores).values(centro=F('centro_costo__descripcion')).annotate(conteo=Count('codigo'))
        
        lista =[]
        puesto=Funcional_Puesto.objects.filter(activo=True).filter(unidad_organizativa__codigo__in=unidades).values('descripcion').distinct()
        for x in puesto:
        
            vacante=Funcional_Puesto.objects.filter(activo=True).filter(unidad_organizativa__codigo__in=unidades,descripcion=x['descripcion']).exclude(codigo__in=puesto_cod).values('descripcion').annotate(conteo=Count('descripcion'))[:1][0] if Funcional_Puesto.objects.filter(activo=True).filter(unidad_organizativa__codigo__in=unidades,descripcion=x['descripcion']).exclude(codigo__in=puesto_cod).annotate(conteo=Count('descripcion')) else {'descripcion':x['descripcion'],'conteo':0}
            cubierto=Funcional_Puesto.objects.filter(activo=True).filter(unidad_organizativa__codigo__in=unidades,codigo__in=puesto_cod,descripcion=x['descripcion']).values('descripcion').annotate(conteo=Count('descripcion'))[:1][0] if Funcional_Puesto.objects.filter(activo=True).filter(unidad_organizativa__codigo__in=unidades,codigo__in=puesto_cod,descripcion=x['descripcion']).values('descripcion').annotate(conteo=Count('descripcion')) else {'descripcion':x['descripcion'],'conteo':0}                         
            conteo=Funcional_Puesto.objects.filter(activo=True).filter(unidad_organizativa__codigo__in=unidades,descripcion=x['descripcion']).values('descripcion').annotate(conteo=Count('descripcion'))[:1][0] if Funcional_Puesto.objects.filter(activo=True).filter(unidad_organizativa__codigo__in=unidades,descripcion=x['descripcion']).values('descripcion').annotate(conteo=Count('descripcion')) else {'descripcion':x['descripcion'],'conteo':0}
            objeto = {"puesto":x['descripcion'],"vacantes":vacante,"cubiertos":cubierto,"conteo":conteo }                
            lista.append(objeto)


        entrada_anual=list(entrada_anual)
        entrada_baja=list(entrada_baja)


       #print('antes',entrada_baja)
        for mes in entrada_anual:
            if len(list(filter(lambda item: item['anio'] == mes['anio'] and item['mes']==mes['mes'] , entrada_baja)))==0:

                entrada_baja.append({'anio':mes['anio'],'mes':mes['mes'],'conteo':0})
                
        for mes in entrada_baja:
            if len(list(filter(lambda item: item['anio'] == mes['anio'] and item['mes']==mes['mes'] , entrada_anual)))==0:

                entrada_anual.append({'anio':mes['anio'],'mes':mes['mes'],'conteo':0})
        
        entrada_anual = sorted(entrada_anual, key=lambda k: k['mes'])
        entrada_baja = sorted(entrada_baja, key=lambda k: k['mes'])
        
       #print('entrada anula',list(entrada_anual))
       #print('entrada_baja',list(entrada_baja))


        yourdata= {"empleadosXempresa": empleadosXempresa,"puestos_existentes":puestos_existentes,
        "puestos_existentes":puestos_existentes,"puestos_vacantes":puestos_vacantes,"puestos_cubiertos":puestos_cubiertos,
        "personal_tipo_relacion":personal_tipo_relacion,"entrada":entrada,"baja":baja,
        "entrada_anual":entrada_anual,"entrada_baja":entrada_baja,"empleado_zona":empleado_zona
        ,"empleado_genero":empleado_genero,"empleado_antiguedad":empleado_antiguedad,"empleado_departamento":empleado_departamento,
        "empleado_formacion":empleado_formacion,"empleado_centro_costo":empleado_centro_costo,
        "Datosxpuesto":lista
        }
        results = yourdata
        #results=1
        return Response(results)

class Funcional_EducacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Educacion.objects.all()
    serializer_class = Funcional_Educacionserializer
    def list(self, request):
        queryset = Funcional_Educacion.objects.all()
        objeto= Funcional_Educacion.objects.all()
        serializer = Funcional_Educacionserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Educacion.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Educacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Educacion.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Educacionserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Educacion.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Educacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Educacion.objects.all().order_by('-id')
            serializer = Funcional_Educacionserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Actualizacion_ContactoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = Actualizacion_Contacto.objects.all()
    serializer_class = Actualizacion_Contactoserializer



class Actualizacion_DependienteViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Actualizacion_Dependiente.objects.all()
    serializer_class = Actualizacion_Dependienteserializer

class Actualizacion_DomicilioViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Actualizacion_Domicilio.objects.all()
    serializer_class = Actualizacion_Domicilioserializer

class Actualizacion_EducacionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Actualizacion_Educacion.objects.all()
    serializer_class = Actualizacion_Educacionserializer

class Actualizacion_Estado_CivilViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Actualizacion_Estado_Civil.objects.all()
    serializer_class = Actualizacion_Estado_Civilserializer


class Actualizacion_Datos_Excel(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    def get(self, request):
        usuario=request.user
        username =usuario.username
        username = username.zfill(8)
        lista_AC=[]
        lista_ADEP=[]
        lista_ADOM=[]
        lista_AE=[]
        lista_AEC=[]
        
        AC = Actualizacion_Contacto.objects.filter(cargado=False).values('id','codigo_empleado','subtipo','valor','fecha')
        ADEP =Actualizacion_Dependiente.objects.filter(cargado=False).values('id','codigo_empleado','subtipo','secuencia','nombre','primer_apellido','segundo_apellido','identidad','dependiente','secuencia','apellido_soltera','de','hasta','genero','fecha_nacimiento','ciudad_nacimiento','pais_nacimiento','nacionalidad','fecha')
        ADOM=Actualizacion_Domicilio.objects.filter(cargado=False).values('id','codigo_empleado','subtipo','domicilio','telefono','de','hasta','colonia','region','tipo_residencia','fecha')
        AE=Actualizacion_Educacion.objects.filter(cargado=False).values('id','codigo_empleado','subtipo','formacion','especialidad','titulo','instituto','fecha_inicio','fecha_fin','clave_pais','fecha')
        AEC =Actualizacion_Estado_Civil.objects.filter(cargado=False).values('id','codigo_empleado','estado_civil','fecha')
        lista_AC=list(AC)
        lista_ADEP=list(ADEP)
        lista_ADOM=list(ADOM)
        lista_AE=list(AE)
        lista_AEC=list(AEC)

        yourdata= {'Actualizacion_Contacto':lista_AC,'Actualizacion_Dependiente':lista_ADEP,'Actualizacion_Domicilio':lista_ADOM,'Actualizacion_Educacion':lista_AE,'Actualizacion_Estado_Civil':lista_AEC}
        results = yourdata
        #results=1
        return Response(results)

class Formal_Check_ListViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Check_List.objects.all()
    serializer_class = Formal_Check_Listserializer

class Funcional_Check_ListViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Check_List.objects.all()
    serializer_class = Funcional_Check_Listserializer

class Formal_Empleado_Check_ListViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Empleado_Check_List.objects.all()
    serializer_class = Formal_Empleado_Check_Listserializer
    def list(self, request):
        queryset = Formal_Empleado_Check_List.objects.all()
        objeto= Formal_Empleado_Check_List.objects.all()
        serializer = Formal_Empleado_Check_Listserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Empleado_Check_List.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Formal_Empleado_Check_Listserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Empleado_Check_List.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Empleado_Check_Listserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Empleado_Check_List.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Empleado_Check_Listserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Empleado_Check_List.objects.all().order_by('-id')
            serializer = Formal_Empleado_Check_Listserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Funcional_Empleado_Check_ListViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Empleado_Check_List.objects.all()
    serializer_class = Funcional_Empleado_Check_Listserializer
    def list(self, request):
        queryset = Funcional_Empleado_Check_List.objects.all()
        objeto= Funcional_Empleado_Check_List.objects.all()
        serializer = Funcional_Empleado_Check_Listserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Empleado_Check_List.objects.filter(empleado=filter).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Empleado_Check_Listserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Empleado_Check_List.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Empleado_Check_Listserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Empleado_Check_List.objects.filter(empleado=filter).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Empleado_Check_Listserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Empleado_Check_List.objects.all().order_by('-id')
            serializer = Funcional_Empleado_Check_Listserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})


class Configuracion_Actualizacion_EmpleadoViewset(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Configuracion_Actualizacion_Empleado.objects.all()
    serializer_class = Configuracion_Actualizacion_Empleadoserializer



class Actualizacion_Datos_Actualizado(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    def post(self, request):
        ##print('este es el request',request)
        ##print('este es el request',request.data)
        ##print('este es el request',request.data['userId'])
        
        #username =User.objects.filter(id=request.data['userId'])[0].username if User.objects.filter(id=request.data['userId']) else None
        #empleado = Formal_empleado.objects.filter(codigo=usuario.username).update(updated_at=datetime.now())
        Formal_empleado.objects.filter(codigo=request.data['userId']).update(updated_at=datetime.now())
        Funcional_empleado.objects.filter(codigo=request.data['userId']).update(updated_at=datetime.now())
        #empleado.updated_at=datetime.now()
        #results=1
        return Response({"mensaje":"operacion exitosa"},status= status.HTTP_200_OK)


#Agregado Para manejo de Vacunas
class Funcional_LaboratorioViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Laboratorio.objects.all()
    serializer_class = Funcional_Laboratorioserializer
    def list(self, request):
        queryset = Funcional_Laboratorio.objects.all()
        objeto= Funcional_Laboratorio.objects.all()
        serializer = Funcional_Laboratorioserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Laboratorio.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Laboratorio.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Funcional_Laboratorioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
               #print('filter vacio limit y offset bien')
                queryset = Funcional_Laboratorio.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Laboratorio.objects.all().order_by('-id')
                serializer = Funcional_Laboratorioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Laboratorio.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Laboratorioserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Laboratorio.objects.all().order_by('-id')
            serializer = Funcional_Laboratorioserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_VacunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Vacuna.objects.all()
    serializer_class = Funcional_Vacunaserializer
    def list(self, request):
        queryset = Funcional_Vacuna.objects.all()
        objeto= Funcional_Vacuna.objects.all()
        serializer = Funcional_Vacunaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Vacuna.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Vacuna.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Funcional_Vacunaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Funcional_Vacuna.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Funcional_Vacuna.objects.all().order_by('-id')
                serializer = Funcional_Vacunaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Vacuna.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Vacunaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Vacuna.objects.all().order_by('-id')
            serializer = Funcional_Vacunaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})	

class Funcional_Empleado_VacunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_Empleado_Vacuna.objects.all()
    serializer_class = Funcional_Empleado_Vacunaserializer
    def list(self, request):
        queryset = Funcional_Empleado_Vacuna.objects.all()
        objeto= Funcional_Empleado_Vacuna.objects.all()
        serializer = Funcional_Empleado_Vacunaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Funcional_Empleado_Vacuna.objects.filter(Q(vacuna=filter)|Q(empleado=filter)).order_by('-id')[offset:offset+limit]
                serializer = Funcional_Empleado_Vacunaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Funcional_Empleado_Vacuna.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Funcional_Empleado_Vacunaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Funcional_Empleado_Vacuna.objects.filter(Q(vacuna=filter)|Q(empleado=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Funcional_Empleado_Vacunaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Empleado_Vacuna.objects.all().order_by('-id')
            serializer = Funcional_Empleado_Vacunaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_LaboratorioViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Laboratorio.objects.all()
    serializer_class = Formal_Laboratorioserializer
    def list(self, request):
        queryset = Formal_Laboratorio.objects.all()
        objeto= Formal_Laboratorio.objects.all()
        serializer = Formal_Laboratorioserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Laboratorio.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Laboratorio.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Formal_Laboratorioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Laboratorio.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Laboratorio.objects.all().order_by('-id')
                serializer = Formal_Laboratorioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Laboratorio.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Laboratorioserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Laboratorio.objects.all().order_by('-id')
            serializer = Formal_Laboratorioserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_VacunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Vacuna.objects.all()
    serializer_class = Formal_Vacunaserializer
    def list(self, request):
        queryset = Formal_Vacuna.objects.all()
        objeto= Formal_Vacuna.objects.all()
        serializer = Formal_Vacunaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Vacuna.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Vacuna.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Formal_Vacunaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Formal_Vacuna.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Formal_Vacuna.objects.all().order_by('-id')
                serializer = Formal_Vacunaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Vacuna.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Vacunaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Vacuna.objects.all().order_by('-id')
            serializer = Formal_Vacunaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Formal_Empleado_VacunaViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_Empleado_Vacuna.objects.all()
    serializer_class = Formal_Empleado_Vacunaserializer
    def list(self, request):
        queryset = Formal_Empleado_Vacuna.objects.all()
        objeto= Formal_Empleado_Vacuna.objects.all()
        serializer = Formal_Empleado_Vacunaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Formal_Empleado_Vacuna.objects.filter(Q(vacuna=filter)|Q(empleado=filter)).order_by('-id')[offset:offset+limit]
                serializer = Formal_Empleado_Vacunaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Formal_Empleado_Vacuna.objects.all().order_by('-id')[offset:offset+limit]
                serializer = Formal_Empleado_Vacunaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Formal_Empleado_Vacuna.objects.filter(Q(vacuna=filter)|Q(empleado=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Formal_Empleado_Vacunaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_Empleado_Vacuna.objects.all().order_by('-id')
            serializer = Formal_Empleado_Vacunaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})




			
class Formal_filtro_empleadoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_empleado.objects.all()
    serializer_class = Formal_empleadoserializer
    def list(self, request):
        usuario = request.user
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        if 'jefe' in grupos:
            
           #print('si entro como jefe',usuario.username)
            colaboradores = formal_get_colaborador([usuario.username])
            #print('colaboradores',colaboradores)
            queryset = Formal_empleado.objects.all()
            objeto= Formal_empleado.objects.filter(codigo__in=colaboradores)
            serializer = Formal_empleadoserializer(queryset, many=True)
            filter=''        
            orga=0
            if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')
            
            if self.request.query_params.get('orga'):
                orga = self.request.query_params.get('orga')
                objeto= Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores)
            
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))
            #print('opcion1')
                if self.request.query_params.get('filter')!='':
                #print('opcion2')
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).order_by('-id')[offset:offset+limit]
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                #print('opcion3')
                    queryset = Formal_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).order_by('-id')[offset:offset+limit]
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                    #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
            elif  filter !='':
            #print('opcion4')
                #print(filter) 
                filtro=str(filter).strip()
                #print('entro a solo filter',filtro)
                queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(identidad__icontains=filter)|Q(correo_empresarial__icontains=filter)|Q(correo_personal__icontains=filter),unidad_organizativa__sociedad_financiera__id=orga,codigo__in=colaboradores).order_by('-id')
                #print('resultados',queryset.query)
                serializer = Formal_empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
            #print('opcion5')
                queryset = Formal_empleado.objects.filter(codigo__in=colaboradores).order_by('-id')
                serializer = Formal_empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
        else: #para otro perfil distinto a jefe
            queryset = Formal_empleado.objects.all()
            objeto= Formal_empleado.objects.all()
            serializer = Formal_empleadoserializer(queryset, many=True)
            filter=''        
            orga=0
            if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')
            

            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))
                filtros = {}
                for x in self.request.query_params:
                    if x!='limit' and x!='offset':
                        filtros[x]=self.request.query_params.get(x)
                   
                #print('opcion4')
                #print(filter) 
                filtro=str(filter).strip()
                #print('entro a solo filter',filtro)
                queryset = Formal_empleado.objects.filter(**filtros).order_by('-id')
                #print('resultados',queryset.query)
                serializer = Formal_empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('opcion5')
                queryset = Formal_empleado.objects.all().order_by('-id')
                serializer = Formal_empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

#Nueva Busqueda
class Formal_busqueda_empleadoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Formal_empleado.objects.all()
    serializer_class = Formal_empleadoserializer
    def list(self,request):
        usuario=request.user
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        
        if 'jefe' in grupos:
            colaboradores = formal_get_colaborador([usuario.username])
            objects.all()
            objeto= Formal_empleado.objects.filter(codigo__in=colaboradores)
            serializer = Formal_empleadoserializer(queryset, many=True)
            filter=''  
            activo=''
            if self.request.query_params.get('activo'):
                activo=self.request.query_params.get('activo')
            
            if activo!='':
               #print('Activos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    if self.request.query_params.get('filter')!='':
                        queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Formal_empleado.objects.filter(codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                elif  filter !='':
                    filtro=str(filter).strip()
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Formal_empleado.objects.filter(codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('Todos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    if self.request.query_params.get('filter')!='':
                        queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Formal_empleado.objects.filter(codigo__in=colaboradores).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(codigo__in=colaboradores).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                elif  filter !='':
                    filtro=str(filter).strip()
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Formal_empleado.objects.filter(codigo__in=colaboradores).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Formal_empleado.objects.all()
            objeto= Formal_empleado.objects.all()
            serializer = Formal_empleadoserializer(queryset, many=True)
            filter=''        
            orga=0
            activo=''
            if self.request.query_params.get('activo'):
                activo=self.request.query_params.get('activo')
            
            if activo!='':
               #print('Activos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    if self.request.query_params.get('filter')!='':
                        queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Formal_empleado.objects.filter(situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                elif  filter !='':
                    filtro=str(filter).strip()
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Formal_empleado.objects.filter(situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('Todos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    if self.request.query_params.get('filter')!='':
                        queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter)).order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Formal_empleado.objects.filter().order_by('-id')[offset:offset+limit]
                        queryset2 = Formal_empleado.objects.filter().order_by('-id')
                        serializer = Formal_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                elif  filter !='':
                    filtro=str(filter).strip()
                    queryset = Formal_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter)).order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Formal_empleado.objects.all().order_by('-id')
                    serializer = Formal_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_busqueda_empleadoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = Funcional_empleadoserializer
    def list(self,request):
        usuario=request.user
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        
        if 'jefe' in grupos:
            colaboradores = formal_get_colaborador([usuario.username])
            objects.all()
            objeto= Funcional_empleado.objects.filter(codigo__in=colaboradores)
            serializer = Funcional_empleadoserializer(queryset, many=True)
            filter=''  
            activo=''
            if self.request.query_params.get('activo'):
                activo=self.request.query_params.get('activo')
            
            if activo!='':
               #print('Activos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    if self.request.query_params.get('filter')!='':
                        queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                elif  filter !='':
                    filtro=str(filter).strip()
                    queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores,situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('Todos')            
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    if self.request.query_params.get('filter')!='':
                        queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores).order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores).order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores).order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(codigo__in=colaboradores).order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                elif  filter !='':
                    filtro=str(filter).strip()
                    queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),codigo__in=colaboradores).order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Funcional_empleado.objects.filter(codigo__in=colaboradores).order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_empleado.objects.all()
            objeto= Funcional_empleado.objects.all()
            serializer = Funcional_empleadoserializer(queryset, many=True)
            filter=''        
            orga=0
            activo=''

            if self.request.query_params.get('activo'):
                activo=self.request.query_params.get('activo')
            
            if activo!='':
               #print('Activos')
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    if self.request.query_params.get('filter')!='':
                        queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Funcional_empleado.objects.filter(situacion_actual__descripcion=activo).order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(situacion_actual__descripcion=activo).order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                elif  filter !='':
                    filtro=str(filter).strip()
                    queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter),situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Funcional_empleado.objects.filter(situacion_actual__descripcion=activo).order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('Todos')                
                if self.request.query_params.get('filter'):
                    filter = self.request.query_params.get('filter')
                if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))
                    if self.request.query_params.get('filter')!='':
                        queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter)).order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter)).order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                    else:
                        queryset = Funcional_empleado.objects.filter().order_by('-id')[offset:offset+limit]
                        queryset2 = Funcional_empleado.objects.filter().order_by('-id')
                        serializer = Funcional_empleadoserializer(queryset, many=True)
                        return Response({"data":serializer.data,"count":queryset2.count()})
                elif  filter !='':
                    filtro=str(filter).strip()
                    queryset = Funcional_empleado.objects.filter(Q(codigo__icontains=filter)|Q(nombre__icontains=filter)|Q(puesto__descripcion__icontains=filter)).order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
                else:
                    queryset = Funcional_empleado.objects.all().order_by('-id')
                    serializer = Funcional_empleadoserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})

#agrega para api de jefes
class Formal_JefesViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Formal_empleado.objects.all()
    serializer_class = ApiJefesSerializer
    def list(self,request):
        jefes=Formal_empleado.objects.filter().values('jefe_inmediato').distinct()
        datos_jefes=Formal_empleado.objects.filter(Q(codigo__in=jefes)|Q(es_jefe=True)).values('id','codigo','nombre')
        serializer = ApiJefesSerializer(datos_jefes,many=True)
        return Response({"data":serializer.data})

class Funcional_JefesViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = ApiJefesSerializer
    def list(self,request):
        jefes=Funcional_empleado.objects.filter().values('jefe_inmediato').distinct()
        datos_jefes=Funcional_empleado.objects.filter(Q(codigo__in=jefes)|Q(es_jefe=True)).values('id','codigo','nombre')
        serializer = ApiJefesSerializer(datos_jefes,many=True)
        return Response({"data":serializer.data})

class Existe_CorreoViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    #serializer_class = Existe_CorreoSerializer
    def get(self, request):
        username=''
        email=''
        mensajeusername=''
        mensajeemail=''
        if self.request.query_params.get('username'):
            username=self.request.query_params.get('username')
        
        if username!='':
            queri1=User.objects.filter(Q(username=username)).count()
            if queri1 !=0:
                mensajeusername='Usuario ya existe'
        else:
            mensajeusername='No se envio Usuario'

        if self.request.query_params.get('email'):
            email=self.request.query_params.get('email')
        
        if email!='':
            queri= User.objects.filter(email=email).count()
            if queri !=0:
                mensajeemail='Correo ya existe'
        else:
            mensajeemail='No se envio el Email'

        if mensajeemail=='' and mensajeusername=='':
            #print ('Entro a decision')
            return Response({"mensaje_username":mensajeusername,"mensaje_email":mensajeemail})
        else:
            return Response({"mensaje_username":mensajeusername,"mensaje_email":mensajeemail},status= status.HTTP_404_NOT_FOUND)

#Modulo de tiempos
#log de ingresos de usuario a la plataforma
class RFC_Tiempos_Empleadoviewset(APIView):    
    def post(self,request):
        IRG_PERNR=[{
        "LOW":"00508745",
        "OPTION":"",
        "SIGN":"",
            }]
        #conexion= Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300')
        
        with Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300') as conx:
        #with Connection(user='INTERFACESAP', passwd='1nt3rf4c3sF4r!n73r',ashost='172.10.0.6', sysnr='00', client='300') as conx:
            #r2 = conx.call('ZRFC_HEADCOUNT_TIEMPOS_AURORA',IRG_PERNR=IRG_PERNR)
            
            #print('este es el post',request.data) 
            if not 'codigo' in request.data and 'anio' in request.data :
                return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)

            r2 = conx.call('ZRFC_HEADCOUNT_TIEMPOS_AURORA',IP_PERNR=request.data['codigo'],IP_FECHA_INI=request.data['anio']+'0101',IP_FECHA_FIN=request.data['anio']+'1231')
           #print('valores',r2)
            if r2:
                empleado=User.objects.filter(username=request.data['codigo'])
                if empleado.count()==0:
                    return Response({"ERROR":"El empleado consultado no tiene cuenta de usuario"},status= status.HTTP_404_NOT_FOUND)
                empleado=empleado[0]
                tiempos= Tiempos_Empleado.objects.filter(empleado=empleado)[0] if Tiempos_Empleado.objects.filter(empleado=empleado) else None
                if tiempos== None:
                    # obj, created = Tiempos_Empleado.objects.update_or_create(
                    # empleado=empleado,
                    # defaults={
                    #     'incapacidad_enfermedad_anual':r2['EP_INCAPACIDACES_ENFERM_ANUAL'], 
                    #     'tiempo_compensatorio':r2['EP_TIEMPO_COMPENSATORIO'], 
                    #     'vacaciones':r2['EP_VACACIONES'], 
                    #         })
                    TE= Tiempos_Empleado.objects.create(empleado=empleado,incapacidad_enfermedad_anual=r2['EP_INCAPACIDACES_ENFERM_ANUAL'],tiempo_compensatorio=r2['EP_TIEMPO_COMPENSATORIO'],vacaciones=r2['EP_VACACIONES']) 
                   #print("entro parte2")
                else:
                   #print("vacaciones",r2['EP_VACACIONES'])
                    Tiempos_Empleado.objects.filter(empleado=empleado).update(incapacidad_enfermedad_anual=r2['EP_INCAPACIDACES_ENFERM_ANUAL'],tiempo_compensatorio=r2['EP_TIEMPO_COMPENSATORIO'],vacaciones=r2['EP_VACACIONES'])
                    #tiempos.save()

                   #print("entro parte2")
                    t=Tiempos_Empleado.objects.filter(empleado=empleado)

                   #print("objeto actualizado",t.values())
                for x in r2['ET_ABSENTISMOS']:
                    obj2, created = Absentismo_Empleado.objects.update_or_create(
                    empleado=empleado,
                    codigo=x['SUBTY'],
                    anio=request.data['anio'],
                    defaults={
                        'descripcion':x['ATEXT'], 
                        'dias':x['ABWTG'], 
                            })
                for x in r2['ET_DIAS_LABORADOS_X_MES']:
                    obj2, created = Dias_Laborados_Empleado.objects.update_or_create(
                    empleado=empleado,
                    anio=x['ANIO'],
                    mes=x['MES'],
                    defaults={
                        'dias':x['DIAS'],
                        'dias_asuentes':x['DIAS_AUSENTES'], 
                        'dias_laborados':x['DIAS_LABORADOS'], 
                            })
                tiempos=list(Tiempos_Empleado.objects.filter(empleado=empleado).annotate(EP_INCAPACIDACES_ENFERM_ANUAL =F('incapacidad_enfermedad_anual'),EP_TIEMPO_COMPENSATORIO =F('tiempo_compensatorio'),EP_VACACIONES = F('vacaciones')).values('EP_INCAPACIDACES_ENFERM_ANUAL','EP_TIEMPO_COMPENSATORIO','EP_VACACIONES'))
                 
                if tiempos !=None:
                    tiempos=tiempos[0]
                else:
                     return Response({"mensaje":"No se encontraron datos"},status= status.HTTP_404_NOT_FOUND)
                absentismo=list(Absentismo_Empleado.objects.filter(empleado=empleado,anio=request.data['anio'] ).annotate(SUBTY =F('codigo'),ATEXT =F('descripcion'),ABWTG = F('dias')).values('SUBTY','ATEXT','ABWTG'))
                tiempos['ET_ABSENTISMOS']=absentismo
                dias=list(Dias_Laborados_Empleado.objects.filter(empleado=empleado,anio=request.data['anio']).annotate(ANIO =F('anio'),MES =F('mes'),DIAS = F('dias'),DIAS_AUSENTES=F('dias_asuentes'),DIAS_LABORADOS=F('dias_laborados')).values('ANIO','MES','DIAS','DIAS_AUSENTES','DIAS_LABORADOS').order_by('MES'))
                if   len(list(filter(lambda resultado: resultado['MES'] == '01', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '01', 'DIAS':monthrange(int(request.data['anio']),int('01'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '02', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '02', 'DIAS':monthrange(int(request.data['anio']),int('02'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '03', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '03', 'DIAS':monthrange(int(request.data['anio']),int('03'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '04', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '04', 'DIAS':monthrange(int(request.data['anio']),int('04'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '05', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '05', 'DIAS':monthrange(int(request.data['anio']),int('05'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '06', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '06', 'DIAS':monthrange(int(request.data['anio']),int('06'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '07', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '07', 'DIAS':monthrange(int(request.data['anio']),int('07'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '08', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '08', 'DIAS':monthrange(int(request.data['anio']),int('08'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '09', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '09', 'DIAS':monthrange(int(request.data['anio']),int('09'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '10', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '10', 'DIAS':monthrange(int(request.data['anio']),int('10'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '11', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '11', 'DIAS':monthrange(int(request.data['anio']),int('11'))[1] }) 
                if   len(list(filter(lambda resultado: resultado['MES'] == '12', dias)))==0:dias.append({'ANIO': request.data['anio'], 'DIAS_AUSENTES': 0.0, 'DIAS_LABORADOS': 0.0, 'MES': '12', 'DIAS':monthrange(int(request.data['anio']),int('12'))[1] }) 

                #print('estos son los dias',dias)
                tiempos['ET_DIAS_LABORADOS_X_MES']=dias

               

            #for empleado in r2['ET_HEADCOUNT']:
            #    relacion_laboral=Formal_Estado_civil.objects.get(relacion_laboral=empleado['PERSG'])
            #    puesto = Formal_Puesto.objects.get(codigo=empleado['STELL'])
            #    formal_empleado = Formal_empleado(identidad=empleado['ICNUM'], nombre=empleado['ENAME'], codigo=empleado['PERNR'], fecha_ingreso=empleado['INDAT'], division=empleado['WERKS'], centro_costo=empleado['KOSTL'], antiguedad_laboral=empleado['ANTLAB'], fecha_cumpleaños=empleado['GBDAT'], edad=empleado["EDAD"], saldo_vacaciones=empleado["ANZHL"], absentismo=empleado["AWART"], domicilio=empleado["ORT01"], historial_laboral=empleado["ARBGB"])
            #    if  relacion_laboral:
            #        formal_empleado.relacion_laboral=relacion_laboral.codigo
            #    if  puesto:
            #        formal_empleado.puesto.add(relacion_laboral)
                
            #return Response(status= status.HTTP_200_OK)
            #conx.close()
            return Response(tiempos,status= status.HTTP_200_OK)


class Tiempos_EmpleadoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = Tiempos_Empleado.objects.all()
    serializer_class = Tiempos_Empleadoserializer
    def list(self, request):
        queryset = Tiempos_Empleado.objects.all()
        objeto= Tiempos_Empleado.objects.all()
        serializer = Tiempos_Empleadoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Tiempos_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Tiempos_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')
                serializer = Tiempos_Empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Tiempos_Empleado.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Tiempos_Empleado.objects.all().order_by('-id')
                serializer = Tiempos_Empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Tiempos_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Tiempos_Empleadoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Tiempos_Empleado.objects.all().order_by('-id')
            serializer = Tiempos_Empleadoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})	

class Absentismo_EmpleadosViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = Absentismo_Empleado.objects.all()
    serializer_class = Absentismo_Empleadoserializer
    def list(self, request):
        queryset = Absentismo_Empleado.objects.all()
        objeto= Absentismo_Empleado.objects.all()
        serializer = Absentismo_Empleadoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Absentismo_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Absentismo_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')
                serializer = Absentismo_Empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Absentismo_Empleado.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Absentismo_Empleado.objects.all().order_by('-id')
                serializer = Absentismo_Empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Absentismo_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Absentismo_Empleadoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Absentismo_Empleado.objects.all().order_by('-id')
            serializer = Absentismo_Empleadoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})	


class Dias_Laborados_EmpleadoViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = Dias_Laborados_Empleado.objects.all()
    serializer_class = Dias_Laborados_Empleadoserializer
    def list(self, request):
        queryset = Dias_Laborados_Empleado.objects.all()
        objeto= Dias_Laborados_Empleado.objects.all()
        serializer = Dias_Laborados_Empleadoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='':
                
                queryset = Dias_Laborados_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Dias_Laborados_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')
                serializer = Dias_Laborados_Empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Dias_Laborados_Empleado.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Dias_Laborados_Empleado.objects.all().order_by('-id')
                serializer = Dias_Laborados_Empleadoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
                #return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        elif  filter !='':
            
            #print(filter) 
            filtro=str(filter).strip()
            #print('entro a solo filter',filtro)
            queryset = Dias_Laborados_Empleado.objects.filter(Q(empleado__username__icontains=filter)).order_by('-id')
            #print('resultados',queryset.query)
            serializer = Dias_Laborados_Empleadoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Dias_Laborados_Empleado.objects.all().order_by('-id')
            serializer = Dias_Laborados_Empleadoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})	

#Segunda Etapa Clima Laboral
##########################################PARA CLIMA LABORAL#################################################################################
class Clima_ObjetoViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Objeto.objects.all()
    serializer_class = Clima_Objetoserializer
    def list(self, request):
        queryset = Clima_Objeto.objects.all()
        objeto= Clima_Objeto.objects.all()
        serializer = Clima_Objetoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Objeto.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Objeto.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Clima_Objetoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Objeto.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Objeto.objects.all().order_by('-id')
                serializer = Clima_Objetoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Objeto.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            serializer = Clima_Objetoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Objeto.objects.all().order_by('-id')
            serializer = Clima_Objetoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Sub_ObjetoViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Sub_Objeto.objects.all()
    serializer_class = Clima_Sub_Objetoserializer
    def list(self, request):
        queryset = Clima_Sub_Objeto.objects.all()
        objeto= Clima_Sub_Objeto.objects.all()
        serializer = Clima_Sub_Objetoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Sub_Objeto.objects.filter(Q(nombre__icontains=filter)|Q(objeto__nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Sub_Objeto.objects.filter(Q(nombre__icontains=filter)|Q(objeto__nombre__icontains=filter)).order_by('-id')
                serializer = Clima_Sub_Objetoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Sub_Objeto.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Sub_Objeto.objects.all().order_by('-id')
                serializer = Clima_Sub_Objetoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Sub_Objeto.objects.filter(Q(nombre__icontains=filter)|Q(objeto__nombre__icontains=filter)).order_by('-id')
            serializer = Clima_Sub_Objetoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Sub_Objeto.objects.all().order_by('-id')
            serializer = Clima_Sub_Objetoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Tipo_PreguntaViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Tipo_Pregunta.objects.all()
    serializer_class = Clima_Tipo_Preguntaserializer
    def list(self, request):
        queryset = Clima_Tipo_Pregunta.objects.all()
        serializer = Clima_Tipo_Preguntaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Tipo_Pregunta.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Tipo_Pregunta.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Clima_Tipo_Preguntaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Tipo_Pregunta.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Tipo_Pregunta.objects.all().order_by('-id')
                serializer = Clima_Tipo_Preguntaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Tipo_Pregunta.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            serializer = Clima_Tipo_Preguntaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Tipo_Pregunta.objects.all().order_by('-id')
            serializer = Clima_Tipo_Preguntaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Tipo_HerramientaViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Tipo_Herramienta.objects.all()
    serializer_class = Clima_Tipo_Herramientaserializer
    def list(self, request):
        queryset = Clima_Tipo_Herramienta.objects.all()
        serializer = Clima_Tipo_Herramientaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Tipo_Herramienta.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Tipo_Herramienta.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Clima_Tipo_Herramientaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Tipo_Herramienta.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Tipo_Herramienta.objects.all().order_by('-id')
                serializer = Clima_Tipo_Herramientaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Tipo_Herramienta.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            serializer = Clima_Tipo_Herramientaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Tipo_Herramienta.objects.all().order_by('-id')
            serializer = Clima_Tipo_Herramientaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_PlantillaViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Plantilla.objects.all()
    serializer_class = Clima_Plantillaserializer
    def list(self, request):
        queryset = Clima_Plantilla.objects.all()
        #objeto= Clima_Objeto.objects.all()
        serializer = Clima_Plantillaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Plantilla.objects.filter(Q(nombre_plantilla__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Plantilla.objects.filter(Q(nombre_plantilla__icontains=filter)).order_by('-id')
                serializer = Clima_Plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Plantilla.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Plantilla.objects.all().order_by('-id')
                serializer = Clima_Plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Plantilla.objects.filter(Q(nombre_plantilla__icontains=filter)).order_by('-id')
            serializer = Clima_Plantillaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Plantilla.objects.all().order_by('-id')
            serializer = Clima_Plantillaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Plantilla_PreguntasViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Plantilla_Preguntas.objects.all()
    serializer_class = Clima_Plantilla_Preguntasserializer
    def list(self, request):
        queryset = Clima_Plantilla_Preguntas.objects.all()
        #objeto= Clima_Objeto.objects.all()
        serializer = Clima_Plantilla_Preguntasserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Plantilla_Preguntas.objects.filter(Q(pregunta__icontains=filter)|Q(plantilla__nombre_plantilla__icontains=filter)|Q(tipo__nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Plantilla_Preguntas.objects.filter(Q(pregunta__icontains=filter)|Q(plantilla__nombre_plantilla__icontains=filter)|Q(tipo__nombre__icontains=filter)).order_by('-id')
                serializer = Clima_Plantilla_Preguntasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Plantilla_Preguntas.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Plantilla_Preguntas.objects.all().order_by('-id')
                serializer = Clima_Plantilla_Preguntasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Plantilla_Preguntas.objects.filter(Q(pregunta__icontains=filter)|Q(plantilla__nombre_plantilla__icontains=filter)|Q(tipo__nombre__icontains=filter)).order_by('-id')
            serializer = Clima_Plantilla_Preguntasserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Plantilla_Preguntas.objects.all().order_by('-id')
            serializer = Clima_Plantilla_Preguntasserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Plantilla_OpcionesViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Plantilla_Opciones.objects.all()
    serializer_class = Clima_Plantilla_Opcionesserializer
    def list(self, request):
        queryset = Clima_Plantilla_Opciones.objects.all()
        #objeto= Clima_Objeto.objects.all()
        serializer = Clima_Plantilla_Opcionesserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Plantilla_Opciones.objects.filter(Q(respuesta__icontains=filter)|Q(pregunta__pregunta__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Plantilla_Opciones.objects.filter(Q(respuesta__icontains=filter)|Q(pregunta__pregunta__icontains=filter)).order_by('-id')
                serializer = Clima_Plantilla_Opcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Plantilla_Opciones.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Plantilla_Opciones.objects.all().order_by('-id')
                serializer = Clima_Plantilla_Opcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Plantilla_Opciones.objects.filter(Q(respuesta__icontains=filter)|Q(pregunta__pregunta__icontains=filter)).order_by('-id')
            serializer = Clima_Plantilla_Opcionesserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Plantilla_Opciones.objects.all().order_by('-id')
            serializer = Clima_Plantilla_Opcionesserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_SegmentoViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Segmento.objects.all()
    serializer_class = Clima_Segmentoserializer
    def list(self, request):
        queryset = Clima_Segmento.objects.all()
        #objeto= Clima_Objeto.objects.all()
        serializer = Clima_Segmentoserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            #empresa , unidad, puesto
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Segmento.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Segmento.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Clima_Segmentoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Segmento.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Segmento.objects.all().order_by('-id')
                serializer = Clima_Segmentoserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Segmento.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            serializer = Clima_Segmentoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Segmento.objects.all().order_by('-id')
            serializer = Clima_Segmentoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Funcional_Unidad_OrganizativaXOrganizacionViewset(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_Unidad_Organizativa.objects.all()
    serializer_class = funcional_unidad_organizativabasicoserializer
    def post(self, request):
        queryset = Funcional_Unidad_Organizativa.objects.all()
        serializer = funcional_unidad_organizativabasicoserializer(queryset, many=True)

        organizacion_id=''
        if len(request.data)!=0:
            if request.data["organizacion_id"]:
                organizacion_id=list(request.data["organizacion_id"])

        if  organizacion_id!='':
            queryset = Funcional_Unidad_Organizativa.objects.filter(sociedad_financiera__id__in=organizacion_id).order_by('nombre')
            serializer = funcional_unidad_organizativabasicoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Unidad_Organizativa.objects.all().order_by('nombre')
            serializer = funcional_unidad_organizativabasicoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Funcional_PuestoXUnidad_OrganizativaViewset(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_Puesto.objects.all()
    serializer_class = funcional_puestoserializer
    def post(self, request):
        queryset = Funcional_Puesto.objects.all()
       
        serializer = funcional_puestoserializer(queryset, many=True)
        unidad_organizativa_id=''
       
        if len(request.data)!=0:
            if request.data["unidad_organizativa_id"]:
                unidad_organizativa_id=list(request.data["unidad_organizativa_id"])

        if  unidad_organizativa_id !='':
            queryset = Funcional_Puesto.objects.filter(unidad_organizativa__id__in=unidad_organizativa_id).order_by('descripcion')
            serializer = funcional_puestoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
        else:
            queryset = Funcional_Puesto.objects.all().order_by('descripcion')
            serializer = funcional_puestoserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_CuestionarioViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Cuestionario.objects.all()
    serializer_class = Clima_Cuestionarioserializer
    def list(self, request):
        queryset = Clima_Cuestionario.objects.all()
        serializer = Clima_Cuestionarioserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Cuestionario.objects.filter(Q(nombre__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Cuestionario.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
                serializer = Clima_Cuestionarioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Cuestionario.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Cuestionario.objects.all().order_by('-id')
                serializer = Clima_Cuestionarioserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Cuestionario.objects.filter(Q(nombre__icontains=filter)).order_by('-id')
            serializer = Clima_Cuestionarioserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Cuestionario.objects.all().order_by('-id')
            serializer = Clima_Cuestionarioserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Cuestionario_PreguntasViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Cuestionario_Preguntas.objects.all()
    serializer_class = Clima_Cuestionario_Preguntasserializer
    def list(self, request):
        queryset = Clima_Cuestionario_Preguntas.objects.all()
        serializer = Clima_Cuestionario_Preguntasserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Cuestionario_Preguntas.objects.filter(Q(pregunta__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Cuestionario_Preguntas.objects.filter(Q(pregunta__icontains=filter)).order_by('-id')
                serializer = Clima_Cuestionario_Preguntasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Cuestionario_Preguntas.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Cuestionario_Preguntas.objects.all().order_by('-id')
                serializer = Clima_Cuestionario_Preguntasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            campo_filter=''
            if self.request.query_params.get('campo_filter'):
                campo_filter = self.request.query_params.get('campo_filter')

            if campo_filter == 'cuestionario_id':
                queryset = Clima_Cuestionario_Preguntas.objects.filter(Q(cuestionario__id__icontains=filter)).order_by('-id')
                serializer = Clima_Cuestionario_Preguntasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            elif campo_filter == 'pregunta':
                queryset = Clima_Cuestionario_Preguntas.objects.filter(Q(pregunta__icontains=filter)).order_by('-id')
                serializer = Clima_Cuestionario_Preguntasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Clima_Cuestionario_Preguntas.objects.all().order_by('-id')
                serializer = Clima_Cuestionario_Preguntasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
           
        else:
            queryset = Clima_Cuestionario_Preguntas.objects.all().order_by('-id')
            serializer = Clima_Cuestionario_Preguntasserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Cuestionario_OpcionesViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Cuestionario_Opciones.objects.all()
    serializer_class = Clima_Cuestionario_Opcionesserializer
    def list(self, request):
        queryset = Clima_Cuestionario_Opciones.objects.all()
        serializer = Clima_Cuestionario_Opcionesserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Cuestionario_Opciones.objects.filter(Q(respuesta__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Cuestionario_Opciones.objects.filter(Q(respuesta__icontains=filter)).order_by('-id')
                serializer = Clima_Cuestionario_Opcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Cuestionario_Opciones.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Cuestionario_Opciones.objects.all().order_by('-id')
                serializer = Clima_Cuestionario_Opcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            campo_filter=''
            if self.request.query_params.get('campo_filter'):
                campo_filter = self.request.query_params.get('campo_filter')

            if campo_filter == 'pregunta_id':
                queryset = Clima_Cuestionario_Opciones.objects.filter(Q(pregunta__id__icontains=filter)).order_by('-id')
                serializer = Clima_Cuestionario_Opcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            elif campo_filter == 'respuesta':
                queryset = Clima_Cuestionario_Opciones.objects.filter(Q(respuesta__icontains=filter)).order_by('-id')
                serializer = Clima_Cuestionario_Opcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset = Clima_Cuestionario_Opciones.objects.all().order_by('-id')
                serializer = Clima_Cuestionario_Opcionesserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Cuestionario_Opciones.objects.all().order_by('-id')
            serializer = Clima_Cuestionario_Opcionesserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

class Clima_Usuarios_ResponsablesViewSet(APIView):
    authenticate_classes = [TokenAuthentication]
    def get(self,request):
        rol_responsable=''
        if self.request.query_params.get('rol_responsable'):
            rol_responsable = self.request.query_params.get('rol_responsable')
        else:
            return Response({"mensaje":"Falta parámetro de rol_responsable"},status= status.HTTP_404_NOT_FOUND)
            
        responsables = User.objects.filter(groups__name=rol_responsable).values('id','username','first_name','last_name')
        serializer= Clima_Usuarios_ResponsablesSerializer(responsables,many=True)
        return Response({"data":serializer.data})

class Clima_CampañaViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Campaña.objects.all()
    serializer_class = Clima_Campañaserializer
    def list(self, request):
        queryset = Clima_Campaña.objects.all()
        serializer = Clima_Campañaserializer(queryset, many=True)
        filter=''
        campo_filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        if self.request.query_params.get('campo_filter'):
            campo_filter=self.request.query_params.get('campo_filter') 

        if campo_filter=='nombre_campaña':
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))
            
                if self.request.query_params.get('filter')!='': 
                    queryset = Clima_Campaña.objects.filter(Q(nombre_campaña__icontains=filter)).order_by('-nombre_campaña')[offset:offset+limit]
                    queryset2 = Clima_Campaña.objects.filter(Q(nombre_campaña__icontains=filter)).order_by('-nombre_campaña')
                    serializer = Clima_Campañaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset2.count()})

                else:
                    queryset = Clima_Campaña.objects.all().order_by('-nombre_campaña')[offset:offset+limit]
                    queryset2 = Clima_Campaña.objects.all().order_by('-nombre_campaña')
                    serializer = Clima_Campañaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset2.count()})

            elif  filter !='':
                queryset = Clima_Campaña.objects.filter(Q(nombre_campaña__icontains=filter)).order_by('-nombre_campaña')
                serializer = Clima_Campañaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

            else:
                queryset = Clima_Campaña.objects.all().order_by('-nombre_campaña')
                serializer = Clima_Campañaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

        elif campo_filter=='responsable':
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))
            
                if self.request.query_params.get('filter')!='': 
                    queryset = Clima_Campaña.objects.filter(Q(responsable__username__icontains=filter)).order_by('-nombre_campaña')[offset:offset+limit]
                    queryset2 = Clima_Campaña.objects.filter(Q(responsable__username__icontains=filter)).order_by('-nombre_campaña')
                    serializer = Clima_Campañaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset2.count()})

                else:
                    queryset = Clima_Campaña.objects.all().order_by('-nombre_campaña')[offset:offset+limit]
                    queryset2 = Clima_Campaña.objects.all().order_by('-nombre_campaña')
                    serializer = Clima_Campañaserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset2.count()})

            elif  filter !='':
                queryset = Clima_Campaña.objects.filter(Q(responsable__username__icontains=filter)).order_by('-nombre_campaña')
                serializer = Clima_Campañaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

            else:
                queryset = Clima_Campaña.objects.all().order_by('-nombre_campaña')
                serializer = Clima_Campañaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

        else:
            if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))

                queryset = Clima_Campaña.objects.all().order_by('-nombre_campaña')[offset:offset+limit]
                queryset2 = Clima_Campaña.objects.all().order_by('-nombre_campaña')
                serializer = Clima_Campañaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Clima_Campaña.objects.all().order_by('-nombre_campaña')
                serializer = Clima_Campañaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


class Formal_Checkear_Empleado(APIView):    
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    def post(self,request):
        #print(request.data)
        for empleado_lista in request.data['Hoja1']:
            Formal_Empleado_Check_List.objects.filter(empleado__codigo=empleado_lista['codigo'],checklist__id=empleado_lista['id']).update(activo=True)
        
        #return Response(r2,status= status.HTTP_200_OK)
        return Response(status= status.HTTP_200_OK)

class Funcional_Checkear_Empleado(APIView):    
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    def post(self,request):
        #print(request.data)
        for empleado_lista in request.data['Hoja1']:
            Funcional_Empleado_Check_List.objects.filter(empleado__codigo=empleado_lista['codigo'],checklist__id=empleado_lista['id']).update(activo=True)
        
        #return Response(r2,status= status.HTTP_200_OK)
        return Response(status= status.HTTP_200_OK)

class Clima_EncuestaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Encuesta.objects.all()
    serializer_class = Clima_Encuestaserializer
    def list(self, request):
        queryset = Clima_Encuesta.objects.all()
        serializer = Clima_Encuestaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Encuesta.objects.filter(Q(fecha_aplicacion__icontains=filter)|Q(campaña__responsable__username__icontains=filter)|Q(campaña__nombre_campaña__icontains=filter)).distinct().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Encuesta.objects.filter(Q(fecha_aplicacion__icontains=filter)|Q(campaña__responsable__username__icontains=filter)|Q(campaña__nombre_campaña__icontains=filter)).distinct().order_by('-id')
                serializer = Clima_Encuestaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Encuesta.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Encuesta.objects.all().order_by('-id')
                serializer = Clima_Encuestaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset =  Clima_Encuesta.objects.filter(Q(fecha_aplicacion__icontains=filter)|Q(campaña__responsable__username__icontains=filter)|Q(campaña__nombre_campaña__icontains=filter)).distinct().order_by('-id')
            serializer = Clima_Encuestaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Encuesta.objects.all().order_by('-id')
            serializer = Clima_Encuestaserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
    
class Clima_RespuestasViewset(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Respuestas.objects.all()
    serializer_class = Clima_Respuestasserializer
    def list(self, request):
        queryset = Clima_Respuestas.objects.all()
        serializer = Clima_Respuestasserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if  self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))
            
            if self.request.query_params.get('filter')!='': 
                queryset = Clima_Respuestas.objects.filter(Q(encuesta__campaña__nombre_campaña__icontains=filter)|Q(fecha_ingreso__icontains=filter)).order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Respuestas.objects.filter(Q(encuesta__campaña__nombre_campaña__icontains=filter)|Q(fecha_ingreso__icontains=filter)).order_by('-id')
                serializer = Clima_Respuestasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

            else:
                queryset = Clima_Respuestas.objects.all().order_by('-id')[offset:offset+limit]
                queryset2 = Clima_Respuestas.objects.all().order_by('-id')
                serializer = Clima_Respuestasserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

        elif  filter !='':
            queryset = Clima_Respuestas.objects.filter(Q(encuesta__campaña__nombre_campaña__icontains=filter)|Q(fecha_ingreso__icontains=filter)).order_by('-id')
            serializer = Clima_Respuestasserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})

        else:
            queryset = Clima_Respuestas.objects.all().order_by('-id')
            serializer = Clima_Respuestasserializer(queryset, many=True)
            return Response({"data":serializer.data,"count":queryset.count()})
            
class Creacion_Usuario_sin_correo(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = User.objects.none() 
    def post(self,request):

        lista_accesos = request.data['Hoja1']
        for nuevo_usuario in  lista_accesos:
            usuarios=list(User.objects.filter().values_list('username',flat=True))
            empleados_sin_usuario=Funcional_empleado.objects.exclude(codigo__in=usuarios).filter(codigo=nuevo_usuario['codigo'])
            for empleado in empleados_sin_usuario:
                code = get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
                #password=code
                password=nuevo_usuario['llave']
                user = User.objects.create_user(username=empleado.codigo,password=password,first_name=empleado.nombre,email=empleado.correo_personal)
                user.save()
                
                
                # subordinados=Funcional_empleado.objects.filter(jefe_inmediato=empleado.codigo).count()
                # liderados=  Funcional_Unidad_Organizativa.objects.filter(Dirigido_por=empleado.codigo).count() 
                # perfil_empleado = Group.objects.get(name='empleado') if Group.objects.filter(name='empleado') else None
                # perfil_jefe = Group.objects.get(name='jefe') if Group.objects.filter(name='jefe') else None

                # if subordinados>0 or liderados>0:
                #     if perfil_jefe !=None:
                #         user.groups.add(perfil_jefe) 
                # else:
                #     if perfil_empleado !=None:
                #         user.groups.add(perfil_empleado)
                perfil=Group.objects.get(name=nuevo_usuario['rol'])
                user.groups.add(perfil)

                user.save()

        return Response(status= status.HTTP_200_OK)  

    
class Funcional_Vacuna_Checkear_Empleado(APIView): 
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    def post(self,request):
        #print(request.data)
        for empleado_lista in request.data['Hoja1']:
            empleado=Funcional_empleado.objects.filter(codigo=empleado_lista['empleado'])
            vacuna = Funcional_Vacuna.objects.filter(id=empleado_lista['vacuna'])
            if empleado.count()>0 and vacuna.count()>0:
                obj, created = Funcional_Empleado_Vacuna.objects.update_or_create(
                    vacuna=vacuna[0],
                    empleado=empleado[0],
                    fecha=empleado_lista['fecha'],
                    defaults={})
        #return Response(r2,status= status.HTTP_200_OK)
        return Response(status= status.HTTP_200_OK)

class Clima_MonitorViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    def get(self,request):
        fecha_inicio=''
        fecha_fin=''
        usuario = request.user
        username = usuario.username
        username = username.zfill(8)
        encuestas_pendientes=0
        sumatoria_encuestas_aplicadas=0
        año_atras_sumatoria_encuestas_aplicadas=0
        porcentaje_encuestas_aplicadas_vrs_año_pasado=0
        encuestas_activas_del_mes=0
        mes_antes_encuestas_activas_del_mes=0
        porcentaje_encuestas_activas_vrs_mes_pasado=0
        porcentaje_llenado=0
        porcentaje_porcentaje_llenado_vrs_mes_pasado=0
        campañas_propias=0
        monitor_encuestas=[]
        encuestas_enviadas_x_mes_al_año=[]
       

        if self.request.query_params.get('fecha_inicio') and self.request.query_params.get('fecha_fin'):
            fecha_inicio=self.request.query_params.get('fecha_inicio')
            fecha_fin=self.request.query_params.get('fecha_fin')
            #datetime.strptime(begin_date, "%Y-%m-%d")
            cantidad_meses = clima_cantidad_meses_entre_fechas(datetime.strptime(fecha_inicio,"%Y-%m-%d"),datetime.strptime(fecha_fin,"%Y-%m-%d"))+1
           #print(cantidad_meses)
            if cantidad_meses >12:
                return Response({"mensaje":"Las fechas deben de tener un maximo de 12 meses entre ellas"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"Faltan parámetros para el filtro"},status= status.HTTP_404_NOT_FOUND)

        #comienza lectura para el monitor
        campañas_propias= Clima_Campaña.objects.filter(responsable__username__icontains=username).count()
        encuestas_pendientes= Clima_Encuesta.objects.filter(usuario__username__icontains=username,campaña__activa=True,fecha_llenado=None).count()
        #Sumatoria de encuestas aplicadas y tambien vrs para % anual
        actual_fecha_fin_encuestas_aplicadas=datetime.now().date()   
        actual_fecha_inicio_encuestas_aplicadas=actual_fecha_fin_encuestas_aplicadas.replace(month=1,day=1)
        año_atras_fecha_fin_encuestas_aplicadas= actual_fecha_inicio_encuestas_aplicadas- timedelta(days=1)
        años_atras_actual_fecha_inicio_encuestas_aplicadas=año_atras_fecha_fin_encuestas_aplicadas.replace(month=1,day=1)

       

        sumatoria_encuestas_aplicadas=Clima_Encuesta.objects.filter(fecha_aplicacion__range=[actual_fecha_inicio_encuestas_aplicadas,actual_fecha_fin_encuestas_aplicadas]).count()
        año_atras_sumatoria_encuestas_aplicadas=Clima_Encuesta.objects.filter(fecha_aplicacion__range=[años_atras_actual_fecha_inicio_encuestas_aplicadas,año_atras_fecha_fin_encuestas_aplicadas]).count()
        
        if año_atras_sumatoria_encuestas_aplicadas!=0:
            porcentaje_encuestas_aplicadas_vrs_año_pasado= (sumatoria_encuestas_aplicadas/año_atras_sumatoria_encuestas_aplicadas)*100
        else:
            porcentaje_encuestas_aplicadas_vrs_año_pasado=0

        #fin Sumatoria de encuestas aplicadas y tambien vrs para % anual
        #encuestas activas del mes y % vrs mes pasado 
        actual_fecha_fin_encuestas_activas_mes= datetime.now().date()
        actual_fecha_inicio_encuestas_activas_mes=actual_fecha_fin_encuestas_activas_mes.replace(day=1)

        mes_antes_fecha_fin_encuestas_activas_mes=actual_fecha_inicio_encuestas_activas_mes-timedelta(days=1)
        mes_antes_fecha_inicio_encuestas_activas_mes=mes_antes_fecha_fin_encuestas_activas_mes.replace(day=1)

        encuestas_activas_del_mes=Clima_Encuesta.objects.filter(campaña__activa=True,fecha_aplicacion__range=[actual_fecha_inicio_encuestas_activas_mes,actual_fecha_fin_encuestas_activas_mes]).count()

        mes_antes_encuestas_activas_del_mes=Clima_Encuesta.objects.filter(campaña__activa=True,fecha_aplicacion__range=[mes_antes_fecha_inicio_encuestas_activas_mes,mes_antes_fecha_fin_encuestas_activas_mes]).count()

        if mes_antes_encuestas_activas_del_mes!=0:
            porcentaje_encuestas_activas_vrs_mes_pasado= (encuestas_activas_del_mes/mes_antes_encuestas_activas_del_mes)*100
        else:
            porcentaje_encuestas_activas_vrs_mes_pasado=0

        #fin encuestas activas del mes y % vrs mes pasado
        #inicio porcentaje llenado 
        #fechas para mes actual
        actual_fecha_fin_encuestas_llenado= datetime.now().date()
        actual_fecha_inicio_encuestas_llenado=actual_fecha_fin_encuestas_llenado.replace(day=1)
        #fechas para mes anterior
        mes_antes_fecha_fin_encuestas_llenado=actual_fecha_inicio_encuestas_llenado-timedelta(days=1)
        mes_antes_fecha_inicio_encuestas_llenado=mes_antes_fecha_fin_encuestas_llenado.replace(day=1)
        
        actual_encuestas_llenado=0
        actual_encuestas_aplicadas=0
        actual_encuestas_llenado= Clima_Encuesta.objects.filter(fecha_llenado__range=[actual_fecha_inicio_encuestas_llenado,actual_fecha_fin_encuestas_llenado]).count()
        actual_encuestas_aplicadas= Clima_Encuesta.objects.filter(fecha_aplicacion__range=[actual_fecha_inicio_encuestas_llenado,actual_fecha_fin_encuestas_llenado]).count()
        
        if actual_encuestas_aplicadas!=0:
            porcentaje_llenado= (actual_encuestas_llenado/actual_encuestas_aplicadas)*100
        else:
            porcentaje_llenado=0
        
        mes_antes_encuestas_llenado=0
        mes_antes_encuestas_aplicadas=0
        mes_antes_encuestas_llenado=Clima_Encuesta.objects.filter(fecha_llenado__range=[mes_antes_fecha_inicio_encuestas_llenado,mes_antes_fecha_inicio_encuestas_llenado]).count()
        mes_antes_encuestas_aplicadas=Clima_Encuesta.objects.filter(fecha_aplicacion__range=[mes_antes_fecha_inicio_encuestas_llenado,mes_antes_fecha_inicio_encuestas_llenado]).count()
        porcentaje_llenado_mes_antes=0

        if mes_antes_encuestas_aplicadas!=0:
            porcentaje_llenado_mes_antes= (actual_encuestas_llenado/actual_encuestas_aplicadas)*100
        else:
            porcentaje_llenado_mes_antes=0

        if porcentaje_llenado_mes_antes!=0:
            porcentaje_porcentaje_llenado_vrs_mes_pasado= (porcentaje_llenado/porcentaje_llenado_mes_antes)*100
        else:
            porcentaje_porcentaje_llenado_vrs_mes_pasado=0
        

        #fin porcentaje llenado 
        objeto= {"sumatoria_encuestas_aplicadas":sumatoria_encuestas_aplicadas,"encuestas_pendientes":encuestas_pendientes,"porcentaje_encuestas_aplicadas_vrs_año_pasado":porcentaje_encuestas_aplicadas_vrs_año_pasado,
        "encuestas_activas_del_mes":encuestas_activas_del_mes,"porcentaje_encuestas_activas_vrs_mes_pasado":porcentaje_encuestas_activas_vrs_mes_pasado,
        "porcentaje_llenado":porcentaje_llenado,"porcentaje_porcentaje_llenado_vrs_mes_pasado":porcentaje_porcentaje_llenado_vrs_mes_pasado,"campañas_propias":campañas_propias}

        monitor_encuestas.append(objeto)
       
        #final lectura para el monitor
        #comienza grafica x mes
        
        
        listas=clima_obtener_entre_mes(fecha_inicio,fecha_fin)
        acum_x_mes= []
        for mes in listas:
            conteo= Clima_Encuesta.objects.filter(fecha_aplicacion__range=[listas[mes][0],listas[mes][1]]).count()
            mes_str=''
            if mes=='01':
                mes_str='enero'
            elif mes=='02':
                mes_str='febrero'
            elif mes=='03':
                mes_str='marzo'
            elif mes=='04':
                mes_str='abril'
            elif mes=='05':
                mes_str='mayo'
            elif mes=='06':
                mes_str='junio'
            elif mes=='07':
                mes_str='julio'
            elif mes=='08':
                mes_str='agosto'
            elif mes=='09':
                mes_str='septiembre'
            elif mes=='10':
                mes_str='octubre'
            elif mes=='11':
                mes_str='noviembre'
            else:
                mes_str='diciembre'
            
            objetoxmes={"mes":mes_str,"conteo":conteo}
            acum_x_mes.append(objetoxmes)

        encuestas_enviadas_x_mes_al_año.append(acum_x_mes)
        #final grafica x mes
        data={"Monitor_Encuestas":monitor_encuestas,"Encuesta_Enviadas_x_Mes_Al_Año":encuestas_enviadas_x_mes_al_año}
        return Response(data)


class Funcional_arbol_viewset(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_Unidad_Organizativa.objects.none() 
    def get(self, request):
        #print(request.data)
        filter=''        
        orga=0
        unidad =0
        Funcional_Funciones=''
        
        if self.request.query_params.get('unidad'):
            unidad = self.request.query_params.get('unidad')
        else:
            return Response({"mensaje":"No hemos recibido los datos necesarios"},status= status.HTTP_404_NOT_FOUND)
        
        bandera=None
        listado=[]
        filtros=[unidad]
       #print("listado",filtros)
        
        while bandera ==None:
           #print('filtros,antes',filtros)
            resultado=Funcional_Unidad_Organizativa.objects.filter(id__in=filtros).values_list('unidad_organizativa_jeraquia__id',flat=True)           
           #print('resultado en while',resultado)
            listado.extend(resultado)
            filtros = resultado
           #print("filtros en while",filtros)
            if resultado.count()==0 or resultado==None:
                bandera=0

       #print('unidad',unidad)
       #print('listado',listado)
        uni= Funcional_Unidad_Organizativa.objects.filter(id=unidad)
        Dirigido_por=uni[0].Dirigido_por
        padre = Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id=unidad)
        if padre:
            hijos_list=padre[0].unidad_organizativa_jeraquia.all().values_list('id',flat=True)
            hermanos=Funcional_Unidad_Organizativa.objects.filter(id__in=hijos_list, Dirigido_por=Dirigido_por).exclude(id=unidad).values_list('id',flat=True)
            listado.extend(hermanos)
        equipo = Funcional_Unidad_Organizativa.objects.filter(id=unidad).values_list('unidad_organizativa_jeraquia__id',flat=True)
        equipo =Funcional_Unidad_Organizativa.objects.filter(id__in=listado)
        
        lista_permiso=list(request.user.groups.all().values_list('name',flat=True))
       #print('uni',uni)
       #print('padre',padre)
       #print('equipo',equipo)
       #print('lista_permiso',lista_permiso)

       #print(lista_permiso)
       #print('si esta') if 'empleado' in lista_permiso else#print('no esta')

        serializer_unidad = funcional_arbol_padre_serializer(uni[0])
        serializer_padre = funcional_arbol_padre_serializer(padre[0]).data if padre else []
        serializer_equipo = funcional_arbol_padre_serializer(equipo,many=True).data

        lider = serializer_unidad.data['lider']

        lideres=[]
        if serializer_unidad.data['lider']!=None:
            lideres.append(serializer_unidad.data['lider']['id'])
        
        if 'empleado' in lista_permiso:
            serializer_equipo=[]
            listado=[unidad]
           #print(listado)
        else:
            for eq in serializer_equipo:
                if  eq['lider']!=None:
                        lideres.append(eq['lider']['id'])
            listado.append(unidad)
       #print('lider',lider)
       #print('lideres',lideres)
       #print('listado',listado)    
            
        empleados = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(fecha_baja__lt=datetime.now().date()) else None
       #print('esta es la unidad organizativa',listado)
        if lider!=None:
            empleados = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) else None

    

        
        return Response({"unidad":serializer_unidad.data,"padre":serializer_padre,"equipo":serializer_equipo,"empleados":Funcional_empleado_arbol_jerarquiaserializer(empleados, many=True).data})
        
#funciones hechas para monitor de clima laboral

def clima_agregar_meses(dt,meses): 
    #Regresar a la fecha después de dt meses, meses equivale a la longitud del paso 
    mes = dt.month - 1 + meses
    año = dt.year + mes / 12 
    año= int(año) 
    mes = mes % 12 + 1  
    dia = min(dt.day, monthrange(año, mes)[1])  
    return dt.replace(year=año, month=mes, day=dia) 


def clima_obtener_entre_mes(fecha_inicio, fecha_fin):
 # Devolver todos los meses y las fechas de inicio y finalización de cada mes, en formato de diccionario
    lista_dias = {}
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    while fecha_inicio <= fecha_fin:
        # fecha_str = fecha_inicio.strftime("%Y-%m")
        fecha_str = fecha_inicio.strftime("%m")
        lista_dias[fecha_str] = ['%d-%d-01'%(fecha_inicio.year, fecha_inicio.month),'%d-%d-%d'%(fecha_inicio.year, fecha_inicio.month, monthrange(fecha_inicio.year, fecha_inicio.month)[1])]
        fecha_inicio = clima_agregar_meses(fecha_inicio,1)

    return lista_dias

def clima_cantidad_meses_entre_fechas(fecha_inicio, fecha_fin):
    delta = 0
    while True:
        mdias = monthrange(fecha_inicio.year, fecha_inicio.month)[1]
        fecha_inicio += timedelta(days=mdias)
        if fecha_inicio <= fecha_fin:
            delta += 1
        else:
            break
    return delta

class Clima_Envio_Masivo_Encuestas_X_CorreoViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none() 
    def post(self,request):
        data={}
        listas=[]
        dataempleados={}
        campaña_recibida=0
        fecha_inicio=datetime.now().date()
        fecha_fin=datetime.now().date()
        if self.request.query_params.get('campaña_id'):
            campaña_recibida = self.request.query_params.get('campaña_id')
        else:
            return Response({"mensaje":"Faltan parámetros para el filtro"},status= status.HTTP_404_NOT_FOUND)
        
        
        # fecha_inicio='2021-11-01'
        # fecha_fin='2021-11-25'
        campañas_vigentes= Clima_Campaña.objects.filter(Q(fecha_inicio__lte=fecha_inicio),Q(fecha_fin__gte=fecha_fin),id=campaña_recibida,activa=True).values()
        #print (campañas_vigentes)
        for x in campañas_vigentes:
            segmentos=Clima_Segmento.objects.filter(id=x["segmento_id"])
            serializer= Clima_Segmentoserializer(segmentos,many=True)
            #print (serializer.data)
            for y in serializer.data:
                if y['empresas'] != None:
                    empresas=y['empresas']
                else:
                    empresas=None
                if y['unidades']!=None:
                    unidades=y['unidades']
                else:
                    unidades=None
                if y['puestos']!=None:
                    puestos=y['puestos']
                else:
                    puestos=None
                if y['edad_inicio']!=None:
                    edad_inicio=y['edad_inicio']
                else:
                    edad_inicio=None
                if y['edad_fin']!=None:
                    edad_fin=y['edad_fin']
                else:
                    edad_fin=None
                if y['genero']!=None:
                    genero=y['genero']
                else:
                    genero=None
                if y['antiguedad_inicio']!=None:
                    antiguedad_inicio=y['antiguedad_inicio']
                else:
                    antiguedad_inicio=None
                if y['antiguedad_fin']!=None:
                    antiguedad_fin=y['antiguedad_fin']
                else:
                    antiguedad_fin=None
                segmento_id=y['id']
                
                objeto={"empresas":empresas,"unidades":unidades,"puestos":puestos,"edad_inicio":edad_inicio,"edad_fin":edad_fin,"genero":genero,"antiguedad_inicio":antiguedad_inicio,"antiguedad_fin":antiguedad_fin,"segmento_id":segmento_id}
            #filtros para enviar las encuestas
            filter_kwargs={}
            if empresas:
                filter_kwargs['puesto__unidad_organizativa__sociedad_financiera__id__in']=empresas
            if unidades:
                filter_kwargs['unidad_organizativa__in']=unidades
            if puestos:
                filter_kwargs['puesto__in']=puestos
            if edad_inicio!=None and edad_fin!=None:
                filter_kwargs['edad__range']=[edad_inicio,edad_fin]
            if genero:
                filter_kwargs['genero']=genero
            if antiguedad_inicio!=None and antiguedad_fin!=None:
                meses_antiguedad_inicio= float(antiguedad_inicio) * 12.00
                meses_antiguedad_fin= float(antiguedad_fin) * 12.00
                filter_kwargs['antiguedad_laboral__range']=[meses_antiguedad_inicio,meses_antiguedad_fin]
            filter_kwargs['situacion_actual_id']=4
            #print("filter_kwargs", filter_kwargs)
            empleados= Funcional_empleado.objects.filter(**filter_kwargs).values('id','codigo','nombre','correo_empresarial')
            campaña_id= x['id']
            cuestionario_id=x['cuestionario_id']
            campaña_nombre=x['nombre_campaña']
            campaña_nombre=campaña_nombre.upper()
            campaña_fin=x['fecha_fin']
            campaña_fin=campaña_fin.strftime("%d/%m/%Y")
            objeto= Clima_Cuestionario.objects.filter(id=cuestionario_id).values('objeto__nombre')[0]
            objeto_nombre=objeto['objeto__nombre']
            
            #campaña_fin=campaña_fin.strftime("%A %d de %B de %Y")
            #print (campaña_fin)
            empleados_sin_correo=[]
            empleados_sin_usuario=[]
            #print(empleados)
            #print("campaña_id:",campaña_id,"Cuestionario_id:", cuestionario_id )
            for z in empleados:
                user_id=User.objects.filter(username=z['codigo']).values('id')
                if user_id.count()!=0:
                    existe= Clima_Encuesta.objects.filter(usuario=user_id[0]['id'],campaña=campaña_id,cuestionario=cuestionario_id).count()
                    if existe==0:
                        user = User.objects.get(id=user_id[0]['id'])
                        id_campaña= Clima_Campaña.objects.get(id=campaña_id)
                        id_cuestionario=Clima_Cuestionario.objects.get(id=cuestionario_id)
                        encuesta_empleado=Clima_Encuesta.objects.create(usuario=user,campaña=id_campaña,cuestionario=id_cuestionario,fecha_aplicacion=datetime.now())
                        encuesta_empleado.save()
                        encuesta_id= Clima_Encuesta.objects.filter(usuario=user_id[0]['id'],campaña=campaña_id,cuestionario=cuestionario_id).values('id')
                            #encuesta_empleado.save()
                        if z['correo_empresarial']!='' and user_id.count()!=0:
                            #envio de correos
                            responsables_campaña={}
                            usuario_responsable= Clima_Campaña.objects.filter(id=campaña_id).values('responsable')
                            for a in usuario_responsable:
                                usuario=User.objects.filter(id=a['responsable']).values('username')
                                nombre=User.objects.filter(id=a['responsable']).values('first_name','last_name')
                                empleado_responsable=Funcional_empleado.objects.filter(codigo__icontains=usuario).values('correo_empresarial')
                                if empleado_responsable.count()!=0:
                                    #aqui proceder a enviar correo
                                    responsables_campaña['Nombre']=nombre[0]['first_name'] + ' ' + nombre[0]['last_name']
                                    responsables_campaña['Correo']=empleado_responsable[0]['correo_empresarial']
                            
                            subject_encuestas='AURORA - CLIMA LABORAL ' + campaña_nombre
                            text_content_encuestas= 'Hola ' + z['nombre'] + '\n\n'
                            text_content_encuestas= text_content_encuestas + 'Para nosotros en Grupo Farinter es muy importante conocer tu opinión es por eso que solicitamos su apoyo con el llenado de ' + objeto_nombre +'.\n\n'
                            text_content_encuestas= text_content_encuestas + 'Por eso a través de las siguiente '+  campaña_nombre + ' queremos tus valiosos comentarios, la misma estará disponible hasta el ' + campaña_fin + '.\n\n'
                            text_content_encuestas= text_content_encuestas + 'Instrucciones:\n'
                            text_content_encuestas= text_content_encuestas + '1. Por favor, dedique unos minutos, Ingresa al siguiente enlace: '  + settings.URL_CLIMA_ENVIO_ENCUESTA + str(cuestionario_id) + '/' + str(encuesta_id[0]['id']) + '/' + str(campaña_id) + '\n'
                            text_content_encuestas= text_content_encuestas + '2. Recuerda que debes llegar hasta el final para poder contar con tus respuestas, el sistema no guarda resultados parciales. \n'
                            text_content_encuestas= text_content_encuestas + '3. Es muy importante que lo hagas a conciencia y con objetividad. La herramienta te garantiza la confidencialidad de la información.\n\n'
                            text_content_encuestas= text_content_encuestas + 'Cualquier duda o consulta, favor contactar a ' 
                            if responsables_campaña:
                                res_campaña_str= str(responsables_campaña)
                                res_campaña_str=res_campaña_str.replace("{","")
                                res_campaña_str=res_campaña_str.replace("'","")
                                res_campaña_str=res_campaña_str.replace("}","")
                                text_content_encuestas = text_content_encuestas + res_campaña_str
                            else:
                                text_content_encuestas = text_content_encuestas + ''
                            text_content_encuestas= text_content_encuestas + ' con gusto te ayudaremos.\n\n\n'
                            text_content_encuestas= text_content_encuestas + 'Tu opinión será utilizada para asegurar que continuemos satisfaciendo tus necesidades y sus respuestas serán tratadas de forma Confidencial y Anónima.\n\n\n'
                            text_content_encuestas= text_content_encuestas + 'Agradecemos de antemano su contribución\n'
                            text_content_encuestas= text_content_encuestas + 'Muchas Gracias ' +  z['nombre']

                            # text_content_encuestas='Por este medio se le solicita proceder a llenar la encuesta ' + campaña_nombre + ', la misma estará disponible hasta la fecha ' 
                            # text_content_encuestas = text_content_encuestas + campaña_fin + '.\n\nA continuación se envia el link para el llenado de la misma: ' + '\n\n '+ url_clima_envio_encuestas + str(cuestionario_id) + '/' + str(encuesta_id[0]['id']) + '/' + str(campaña_id)
                            # #text_content_encuestas = text_content_encuestas + campaña_fin + '.\n\nA continuación se envia el link para el llenado de la misma: ' + '\n\n http://172.16.2.223:8082/encuestas/' + str(cuestionario_id) + '/' + str(encuesta_id[0]['id']) + '/' + str(campaña_id)
                            # text_content_encuestas = text_content_encuestas + '\n\nCualquier duda o consulta, favor contactar a ' 
                            # if responsables_campaña:
                            #     res_campaña_str= str(responsables_campaña)
                            #     res_campaña_str=res_campaña_str.replace("{","")
                            #     res_campaña_str=res_campaña_str.replace("'","")
                            #     res_campaña_str=res_campaña_str.replace("}","")
                            #     text_content_encuestas = text_content_encuestas + res_campaña_str
                            # else:
                            #     text_content_encuestas = text_content_encuestas + ''
                            # text_content_encuestas = text_content_encuestas + '\n\nMuchas Gracias ' + z['nombre']

                            from_email_encuestas = settings.EMAIL_HOST_USER
                            #print (text_content_encuestas)
                            to_email_encuestas = z['correo_empresarial']
                            #print (z['nombre'])
                            try:
                                msg_encuestas = EmailMultiAlternatives(subject_encuestas, text_content_encuestas, from_email_encuestas, [to_email_encuestas])
                                msg_encuestas.send()
                                #print('CORREO ENVIADO CON EXITO')
                            except BadHeaderError:
                                return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
                            
                            #print('se envia correo')
                        else:
                            objeto_esc={"Código":z['codigo'],"Nombre":z['nombre'],"Enlace": settings.URL_CLIMA_ENVIO_ENCUESTA + str(cuestionario_id) + '/' + str(encuesta_id[0]['id']) + '/' + str(campaña_id)}
                            empleados_sin_correo.append(objeto_esc)
                    #print (empleados_sin_correo)
                else:
                    objeto_esu={"Código":z['codigo'],"Nombre":z['nombre']}
                    empleados_sin_usuario.append(objeto_esu)

                
            #print(empleados_sin_correo)
            if empleados_sin_correo:
                #envio de correo al responsable 
                usuario_responsable= Clima_Campaña.objects.filter(id=campaña_id).values('responsable')
                for a in usuario_responsable:
                    usuario=User.objects.filter(id=a['responsable']).values('username')
                    empleado_responsable=Funcional_empleado.objects.filter(codigo__icontains=usuario).values('correo_empresarial')
                    if empleado_responsable.count()!=0:
                        #aqui proceder a enviar correo
                        str_empleados_sin_correo=str(empleados_sin_correo)
                        str_empleados_sin_correo=str_empleados_sin_correo.replace(", ",",")
                        str_empleados_sin_correo=str_empleados_sin_correo.replace("[","")
                        str_empleados_sin_correo=str_empleados_sin_correo.replace("{","")
                        str_empleados_sin_correo=str_empleados_sin_correo.replace("'","")
                        str_empleados_sin_correo=str_empleados_sin_correo.replace("]","")
                        str_empleados_sin_correo=str_empleados_sin_correo.replace("}","")
                        str_empleados_sin_correo=str_empleados_sin_correo.replace(": ",":")
                        str_empleados_sin_correo=str_empleados_sin_correo.replace(",","\n")
                        subject_empleado_sin_correo='AURORA - CLIMA LABORAL CAMPAÑA ' + campaña_nombre + ' EMPLEADOS SIN CORREO EMPRESARIAL'
                        text_content_empleado_sin_correo='Por este medio se notifica que los siguientes empleados no cuentan con correo empresarial registrado: \n\n' 

                        text_content_empleado_sin_correo = text_content_empleado_sin_correo + str_empleados_sin_correo                 
                        from_email_empleado_sin_correo= settings.EMAIL_HOST_USER
                        to_email_empleado_sin_correo = empleado_responsable[0]['correo_empresarial']
                        try:
                            msg_empleado_sin_correo = EmailMultiAlternatives(subject_empleado_sin_correo, text_content_empleado_sin_correo, from_email_empleado_sin_correo, [to_email_empleado_sin_correo])
                            msg_empleado_sin_correo.send()
                            #print('CORREO ENVIADO CON EXITO')
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)

                    #print ("usuario",usuario)
            if empleados_sin_usuario:
                #envio de correo al responsable 
                usuario_responsable= Clima_Campaña.objects.filter(id=campaña_id).values('responsable')
                for a in usuario_responsable:
                    usuario=User.objects.filter(id=a['responsable']).values('username')
                    empleado_responsable=Funcional_empleado.objects.filter(codigo__icontains=usuario).values('correo_empresarial')
                    if empleado_responsable.count()!=0:
                        #aqui proceder a enviar correo
                        str_empleados_sin_usuario=str(empleados_sin_usuario)
                        str_empleados_sin_usuario=str_empleados_sin_usuario.replace(", ",",")
                        str_empleados_sin_usuario=str_empleados_sin_usuario.replace("[","")
                        str_empleados_sin_usuario=str_empleados_sin_usuario.replace("{","")
                        str_empleados_sin_usuario=str_empleados_sin_usuario.replace("'","")
                        str_empleados_sin_usuario=str_empleados_sin_usuario.replace("]","")
                        str_empleados_sin_usuario=str_empleados_sin_usuario.replace("}","")
                        str_empleados_sin_usuario=str_empleados_sin_usuario.replace(": ",":")
                        str_empleados_sin_usuario=str_empleados_sin_usuario.replace(",","\n")
                        subject_empleado_sin_usuario='AURORA - CLIMA LABORAL CAMPAÑA ' + campaña_nombre + ' EMPLEADOS SIN USUARIO REGISTRADO EN AURORA'
                        text_content_empleado_sin_usuario='Por este medio se notifica que los siguientes empleados no cuentan con un usuario registrado para poder acceder a AURORA: \n\n' 

                        text_content_empleado_sin_usuario = text_content_empleado_sin_usuario + str_empleados_sin_usuario                 
                        from_email_empleado_sin_usuario= settings.EMAIL_HOST_USER
                        to_email_empleado_sin_usuario = empleado_responsable[0]['correo_empresarial']
                        try:
                            msg_empleado_sin_usuario = EmailMultiAlternatives(subject_empleado_sin_usuario, text_content_empleado_sin_usuario, from_email_empleado_sin_usuario, [to_email_empleado_sin_usuario])
                            msg_empleado_sin_usuario.send()
                            #print('CORREO ENVIADO CON EXITO')
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)

                        #print ("usuario",usuario)     
            #print("cantidad empleados: ",empleados.count())
            #print("empleados sin correo:" , empleados.filter(correo_empresarial='').count())
            listas.append(objeto)
            data={"Listas":listas}
            dataempleados= {"filtros":listas,"empleados":empleados}
            #print (dataempleados)
        
        return Response(dataempleados,status= status.HTTP_200_OK)

class Clima_Encuesta_CheckListViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Clima_Encuesta.objects.all()
    serializer_class = Clima_Encuestaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = Clima_Encuesta.objects.all()
        serializer = Clima_Encuestaserializer(queryset, many=True)
        filter=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')
        else:
            return Response({"mensaje":"Faltan parámetros para el filtro"},status= status.HTTP_404_NOT_FOUND)

        queryset =  Clima_Encuesta.objects.filter(usuario__username__icontains=filter,fecha_llenado=None).distinct().order_by('campaña__fecha_fin')
        serializer = Clima_Encuestaserializer(queryset, many=True)
        
        return Response({"data":serializer.data,"count":queryset.count()})

class Reporte_ultima_sessionViewset(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Usuario_Log.objects.all()
    serializer_class = Usuario_Logserializer
    def get(self, request):
        queryset = Usuario_Log.objects.all()
        serializer = Usuario_Logserializer(queryset, many=True)
        inicio = self.request.query_params.get('inicio',None)
        fin = self.request.query_params.get('fin',None)
        limit = self.request.query_params.get('limit',None)
        offset = self.request.query_params.get('offset',None)


        if  limit and offset:
            offset=int(offset)
            limit=int(limit)
            
            if inicio and fin: 
                queryset = Usuario_Log.objects.filter(fecha_creacion__range=[inicio,fin]).order_by('-id')[offset:offset+limit]
                queryset2 = Usuario_Log.objects.filter(fecha_creacion__range=[inicio,fin]).order_by('-id')
                serializer = Usuario_Logserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Usuario_Log.objects.filter().order_by('-id')[offset:offset+limit]
                queryset2 = Usuario_Log.objects.filter().order_by('-id')
                serializer = Usuario_Logserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
        else:
            if inicio and fin: 
                queryset = Usuario_Log.objects.filter(fecha_creacion__range=[inicio,fin]).order_by('-id')
                queryset2 = Usuario_Log.objects.filter(fecha_creacion__range=[inicio,fin]).order_by('-id')
                serializer = Usuario_Logserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})
            else:
                queryset = Usuario_Log.objects.filter().order_by('-id')
                queryset2 = Usuario_Log.objects.filter().order_by('-id')
                serializer = Usuario_Logserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset2.count()})

class LLenar_Log_SessionViewset(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Usuario_Log.objects.all()
    serializer_class = Usuario_Logserializer
    
    def post(self, request):
        usuario=request.user
        Usuario_Log.objects.create(usuario=usuario,actividad='login')
        return Response({"mensaje":"La operacion fue exitosa"},status= status.HTTP_200_OK)

class Funciona_listado_hijos_nohijos_unidad(APIView):
    def get(self, request):
        unidad=self.request.query_params.get('unidad')
        yourdata= list(Funcional_Unidad_Organizativa.objects.filter(id=unidad).values_list('unidad_organizativa_jeraquia',flat=True))
       #print(yourdata)
        hijos=Funcional_Unidad_Organizativa.objects.filter(id__in=yourdata).exclude(id=unidad)
        no_hijos=Funcional_Unidad_Organizativa.objects.exclude(id__in=yourdata).exlude(id=unidad)
        hijos_serializer =funcional_unidad_organizativabasicoserializer(hijos,many=True)
        no_hijos_serializer =funcional_unidad_organizativabasicoserializer(no_hijos,many=True)


        return Response({"hijos":hijos_serializer.data,"no_hijos":no_hijos_serializer.data},status= status.HTTP_200_OK)


class Funciona_listado_hijos_nohijos_unidad(APIView):
    def get(self, request):
        unidad=self.request.query_params.get('unidad')
        yourdata= list(Funcional_Unidad_Organizativa.objects.filter(id=unidad).values_list('unidad_organizativa_jeraquia',flat=True))
       #print(yourdata)
        hijos=Funcional_Unidad_Organizativa.objects.filter(id__in=yourdata)
        no_hijos=Funcional_Unidad_Organizativa.objects.exclude(id__in=yourdata)
        hijos_serializer =funcional_unidad_organizativabasicoserializer(hijos,many=True)
        no_hijos_serializer =funcional_unidad_organizativabasicoserializer(no_hijos,many=True)


        return Response({"hijos":hijos_serializer.data,"no_hijos":no_hijos_serializer.data},status= status.HTTP_200_OK)

# class Funcionas_unidad_agregar_hijos(APIView):
#     def post(self, request):
#         padre=request.data['padre']
#         hijos=request.data['hijos']
#         papa=Funcional_Unidad_Organizativa.objects.get(id=padre) if Funcional_Unidad_Organizativa.objects.filter(id=padre) else None
#         if papa ==None:
#             return Response({"mensaje":"No existe el padre"},status= status.HTTP_404_NOT_FOUND)
       
#         yourdata= list(Funcional_Unidad_Organizativa.objects.filter(id=padre).values_list('unidad_organizativa_jeraquia',flat=True))
        
#         hijos=Funcional_Unidad_Organizativa.objects.filter(id__in=yourdata)
#         no_hijos=Funcional_Unidad_Organizativa.objects.exclude(id__in=yourdata)
#         hijos_serializer =funcional_unidad_organizativabasicoserializer(hijos,many=True)
#         no_hijos_serializer =funcional_unidad_organizativabasicoserializer(no_hijos,many=True)


#         return Response({"hijos":hijos_serializer.data,"no_hijos":no_hijos_serializer.data},status= status.HTTP_200_OK)
        
        


#         return Response(status= status.HTTP_200_OK)

class Funcionas_unidad_quitar_hijos(APIView):
    def post(self, request):
        unidad=Funcional_Unidad_Organizativa.objects.get(id=self.request.data['unidad']) if Funcional_Unidad_Organizativa.objects.filter(id=self.request.data['unidad']) else None
        hijos_lista=self.request.data['hijos']
        if unidad ==None:
            return Response({"mensaje":"Faltan parámetros para el filtro"},status= status.HTTP_404_NOT_FOUND)

        unidad.unidad_organizativa_jeraquia.remove(*hijos_lista)
        yourdata= list(Funcional_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('unidad_organizativa_jeraquia',flat=True))
        hijos=Funcional_Unidad_Organizativa.objects.filter(id__in=yourdata)

        no_hijos=Funcional_Unidad_Organizativa.objects.exclude(id__in=yourdata)
        hijos_serializer =funcional_unidad_organizativabasicoserializer(hijos,many=True)
        no_hijos_serializer =funcional_unidad_organizativabasicoserializer(no_hijos,many=True)


        return Response({"hijos":hijos_serializer.data,"no_hijos":no_hijos_serializer.data},status= status.HTTP_200_OK)

class Funcionas_unidad_agregar_hijos(APIView):
    def post(self, request):
        unidad=Funcional_Unidad_Organizativa.objects.get(id=self.request.data['unidad']) if Funcional_Unidad_Organizativa.objects.filter(id=self.request.data['unidad']) else None
        hijos_lista=self.request.data['hijos']
        if unidad ==None:
            return Response({"mensaje":"Faltan parámetros para el filtro"},status= status.HTTP_404_NOT_FOUND)
        
        for x in hijos_lista:
            padre_anterior=Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id__in=[x]) if Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id__in=[x]) else None
            if padre_anterior!=None:
                for y in padre_anterior:
                    y.unidad_organizativa_jeraquia.remove(x)

        unidad.unidad_organizativa_jeraquia.add(*hijos_lista)
        yourdata= list(Funcional_Unidad_Organizativa.objects.filter(id=unidad.id).values_list('unidad_organizativa_jeraquia',flat=True))
        hijos=Funcional_Unidad_Organizativa.objects.filter(id__in=yourdata)

        no_hijos=Funcional_Unidad_Organizativa.objects.exclude(id__in=yourdata)
        hijos_serializer =funcional_unidad_organizativabasicoserializer(hijos,many=True)
        no_hijos_serializer =funcional_unidad_organizativabasicoserializer(no_hijos,many=True)


        return Response({"hijos":hijos_serializer.data,"no_hijos":no_hijos_serializer.data},status= status.HTTP_200_OK)

class Clima_generacion_enlace_encuestas(APIView):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    def get(self,request):
        campaña_id=0
        username=''
        cuestionario_id=''
        if self.request.query_params.get('campaña_id'):
            campaña_id = self.request.query_params.get('campaña_id')
        else:
            return Response({"mensaje":"Falta parámetro de Campaña"},status= status.HTTP_404_NOT_FOUND)
        if self.request.query_params.get('username'):
            username = self.request.query_params.get('username')
        else:
            return Response({"mensaje":"Falta parámetros de username"},status= status.HTTP_404_NOT_FOUND)
        if campaña_id==0 or username=='':
            return Response({"mensaje":"Falta parámetros"},status= status.HTTP_404_NOT_FOUND)
        else:
            campaña_vigente= Clima_Campaña.objects.filter(Q(fecha_inicio__lte=datetime.now().date()),Q(fecha_fin__gte=datetime.now().date()),id=campaña_id).values('cuestionario_id') if Clima_Campaña.objects.filter(Q(fecha_inicio__lte=datetime.now().date()),Q(fecha_fin__gte=datetime.now().date()),id=campaña_id) else None
            if campaña_vigente==None:
                return Response({"mensaje":"Falta parámetro campaña"},status= status.HTTP_404_NOT_FOUND)
            else:
                cuestionario_id= campaña_vigente[0]['cuestionario_id']
            userr= User.objects.filter(username=username).values('id')
            user_id= userr[0]['id']
            encuesta_id= Clima_Encuesta.objects.filter(usuario=user_id,campaña=campaña_id,cuestionario=cuestionario_id).values('id') if Clima_Encuesta.objects.filter(usuario=user_id,campaña=campaña_id,cuestionario=cuestionario_id) else None
            if encuesta_id==None:
                return Response({"mensaje":"Falta parámetro encuesta"},status= status.HTTP_404_NOT_FOUND)

            enlace_encuesta= settings.URL_CLIMA_ENVIO_ENCUESTA + str(cuestionario_id) + '/' + str(encuesta_id[0]['id']) + '/' + str(campaña_id)

            return Response({"enlace_evaluacion":enlace_encuesta},status=status.HTTP_200_OK)

class Formal_Checkear_Check_list_Empleado(APIView):    
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    def post(self,request):
        #print(request.data)
        for empleado_lista in request.data['Hoja1']:
            if empleado_lista['activo']==1:
                Formal_Empleado_Check_List.objects.filter(checklist=empleado_lista['documento'],empleado=empleado_lista['codigo']).update(activo=True)
        
        #return Response(r2,status= status.HTTP_200_OK)
        return Response(status= status.HTTP_200_OK)

class Funcional_Checkear_Check_list_Empleado(APIView):    
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    def post(self,request):
        #print(request.data)
        for empleado_lista in request.data['Hoja2']:
            if empleado_lista['activo']==1:
                Funcional_Empleado_Check_List.objects.filter(checklist=empleado_lista['documento'],empleado=empleado_lista['codigo']).update(activo=True)
        
        #return Response(r2,status= status.HTTP_200_OK)
        return Response(status= status.HTTP_200_OK)
        #comentario solo para subir cambios

class Actualizacion_Datos_Excel_cambio_estado(APIView):
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    def post(self,request):
        tipo=''
        lista_id=[]

        if self.request.data['tipo_actualizacion']:
            tipo = self.request.data['tipo_actualizacion']
        else:
            return Response({"mensaje":"Falta parámetro de tipo de actualizacion"},status= status.HTTP_404_NOT_FOUND)
        
        if self.request.data['lista']:
            for ids in self.request.data['lista']:
                lista_id.append(ids['id'])
            #print('lista',lista_id)
            if tipo=='contacto':
                Actualizacion_Contacto.objects.filter(cargado=False,id__in=lista_id).update(cargado=True)
                return Response(status= status.HTTP_200_OK)
            elif tipo=='dependiente':
                Actualizacion_Dependiente.objects.filter(cargado=False,id__in=lista_id).update(cargado=True)
                return Response(status= status.HTTP_200_OK)
            elif tipo=='domicilio':
                Actualizacion_Domicilio.objects.filter(cargado=False,id__in=lista_id).update(cargado=True)
                return Response(status= status.HTTP_200_OK)
            elif tipo=='educacion':
                Actualizacion_Educacion.objects.filter(cargado=False,id__in=lista_id).update(cargado=True)
                return Response(status= status.HTTP_200_OK)
            elif tipo=='estado_civil':
                Actualizacion_Estado_Civil.objects.filter(cargado=False,id__in=lista_id).update(cargado=True)
                return Response(status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"No existe el tipo enviado"},status= status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"No hay datos que actualizar"},status= status.HTTP_404_NOT_FOUND)


class archivos_gestorViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = archivos_gestor.objects.all()
    serializer_class = archivos_gestorserializer
    def list(self, request):
        queryset = archivos_gestor.objects.all()
        objeto= archivos_gestor.objects.all()
        serializer = archivos_gestorserializer(queryset, many=True)
        id_empleado=0
        tipo_documento=''
        if self.request.query_params.get('id_empleado'):
            id_empleado = self.request.query_params.get('id_empleado')
        else:
            return Response({"mensaje":"Falta parámetro de id_empleado"},status= status.HTTP_404_NOT_FOUND)
        
        if self.request.query_params.get('tipo_documento'):
            tipo_documento = self.request.query_params.get('tipo_documento')
        else:
            return Response({"mensaje":"Falta parámetro de tipo_documento"},status= status.HTTP_404_NOT_FOUND)

        if id_empleado!=0 and tipo_documento!='':
            queryset = archivos_gestor.objects.filter(tipo_documento=tipo_documento,id_empleado=id_empleado).order_by('-id')
            serializer = archivos_gestorserializer(queryset, many=True)
            return Response({"data":serializer.data})
        else:
            return Response({"mensaje":"Falta parámetros"},status= status.HTTP_404_NOT_FOUND)




class archivos_gestor_postViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none() 
    def post(self,request):
        url =  settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CarpetaDetalle'
        emp=Funcional_empleado.objects.filter(id=self.request.data['id_empleado'])[0] if Funcional_empleado.objects.filter(id=self.request.data['id_empleado']) else None
        if emp==None:
            return Response({"resultado":"No Existe el empleado funcional indicado"},status= status.HTTP_404_NOT_FOUND)
        existe_carpeta=False
        exitoso=False
        myobj = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado']}

        x = requests.post(url, data = myobj)
        response_dict = x.json()
        
        cdid=0
        if len(response_dict)>0:
            for y in response_dict:
                if y['descripcion']=='CODIGO EMPLEADO':
                    cdid=y['id']         
        else:
            
            return Response({"resultado":"No se puede verificar el contenido el detalle de la carpeta"},status= status.HTTP_404_NOT_FOUND)
        

        if cdid !=0:
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/MantenimientoSubniveles'
            objeto = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado'],'cdid':cdid}
            x = requests.post(enlace, data = objeto)
            resultado = x.json()
            
            for carpeta in resultado:
                if carpeta['descripcion']==emp.codigo:
                    existe_carpeta=True
        if existe_carpeta==False:
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CrearMantenimientoSubniveles'
            objeto = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado'],'cdid':cdid,'descripcion':emp.codigo}
            
            x = requests.post(enlace, data = objeto)
            resultado = x.json()

        
        enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CrearDocumento'
        
        fecha=format = '%Y%m%d'
        # convert from string format to datetime format
        fecha = datetime.today().strftime('%Y%m%d')

        llave = str(self.request.data['empresa']) +'-'+ str(self.request.data['zona']) +'-'+ str(self.request.data['tipo_documento_GD'])+'-'+ str(self.request.data['descripcion'])+'-'+ str(emp.codigo) +'-'+ fecha
        
        objeto = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado'],'cdid':cdid,'descripcion':emp.codigo,'llave':llave,'origen':self.request.data['origen'],'documento':self.request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}
        x = requests.post(enlace, data = objeto)
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
        empleado=Funcional_empleado.objects.filter(codigo=emp.codigo) if Funcional_empleado.objects.filter(codigo=emp.codigo).count()>0 else None
        if empleado==None:
            return Response({"resultado":"No existe como Empleado Funcional"},status= status.HTTP_404_NOT_FOUND)
        archivos_gestor.objects.filter(id_empleado=empleado[0],tipo_documento='estado_civil').update(tipo_documento='otros_documentos')
        doc=archivos_gestor.objects.create(id_documento=id_gestor, llave=llave,id_area=self.request.data['id_area'],id_carpeta_encabezado=self.request.data['id_carpeta_encabezado'],empresa=self.request.data['empresa'],zona=self.request.data['zona'],tipo_documento_GD=self.request.data['tipo_documento_GD'],descripcion=self.request.data['descripcion'],id_empleado=empleado[0],tipo_documento=self.request.data['tipo_documento'],origen=self.request.data['origen'],extension=self.request.data['extension'],id_registro=self.request.data['id_registro'],contentTypeGD=self.request.data['contentTypeGD'])
        

        return Response({"resultado": archivos_gestorserializer(doc).data},status= status.HTTP_200_OK)

    def get_object(self, pk):
        try:
            return archivos_gestor.objects.get(pk=pk)
        except archivos_gestor.DoesNotExist:
            raise Http404
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = archivos_gestorserializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/ModificarDocumento'
            objeto = {'id':post.id_documento,'ceid':post.id_carpeta_encabezado,'llave':post.llave,'origen':post.origen,'documento':request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}
            #print('objeto',objeto)
            x = requests.post(enlace, data = objeto)
            resultado = x.json()
            for result in resultado:
               #print('resultado',result)
                if result['response'].find('Correctamente')==-1:
                        return Response({"resultado":result['response']},status= status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class archivos_gestor_formatos_oficialesViewSet(viewsets.ModelViewSet):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    queryset = archivos_gestor_formatos_oficiales.objects.all()
    serializer_class = archivos_gestor_formatos_oficialesserializer
    def list(self, request):
        queryset = archivos_gestor_formatos_oficiales.objects.all()
        objeto= archivos_gestor_formatos_oficiales.objects.all()
        serializer = archivos_gestor_formatos_oficialesserializer(queryset, many=True)
        tipo_documento=''

        if self.request.query_params.get('tipo_documento'):
            tipo_documento = self.request.query_params.get('tipo_documento')

        if tipo_documento:
            queryset = archivos_gestor_formatos_oficiales.objects.filter(tipo_documento=tipo_documento).order_by('-id')
            serializer = archivos_gestor_formatos_oficialesserializer(queryset, many=True)
            return Response({"data":serializer.data})
        else:
            queryset = archivos_gestor_formatos_oficiales.objects.filter().order_by('-id')
            serializer = archivos_gestor_formatos_oficialesserializer(queryset, many=True)
            return Response({"data":serializer.data})

class archivos_gestor_formatos_oficiales_postViewSet(APIView):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none() 
    def post(self,request):
        url =  settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CarpetaDetalle'
       #print('entro')
        myobj = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado']}

        x = requests.post(url, data = myobj)
        response_dict = x.json()
        

        if len(response_dict)>0:
           #print(response_dict)
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/CrearDocumento'

            llave = str(self.request.data['subnivel1']) +"-"+ str(self.request.data['subnivel2'])
            
            objeto = {'areaid': self.request.data['id_area'],'ceid':self.request.data['id_carpeta_encabezado'],'llave':llave,'origen':self.request.data['origen'],'documento':self.request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}
            x = requests.post(enlace, data = objeto)
            resultado = x.json()
           #print(resultado)
            if x.status_code==400:
                return Response({"resultado":resultado},status= status.HTTP_404_NOT_FOUND)

            for error in resultado:
                if error['response'].find('creado')==-1:
                    return Response({"resultado":resultado},status= status.HTTP_404_NOT_FOUND)
                    
            for result in resultado:
                indice1=result['response'].index(':')+1
                indice2=result['response'].index(',')
                id_gestor=result['response'][indice1:indice2] if indice1 and indice2 else None

            doc=archivos_gestor_formatos_oficiales.objects.create(id_documento=id_gestor, llave=llave,id_area=self.request.data['id_area'],id_carpeta_encabezado=self.request.data['id_carpeta_encabezado'],medidas_disciplinarias=self.request.data['medidas_disciplinarias'],tipo_documento=self.request.data['tipo_documento'],origen=self.request.data['origen'],extension=self.request.data['extension'],contentTypeGD=self.request.data['contentTypeGD'],subnivel1=self.request.data['subnivel1'],subnivel2=self.request.data['subnivel2'])
            
            return Response({"resultado": archivos_gestor_formatos_oficialesserializer(doc).data},status= status.HTTP_200_OK)
        else:
            return Response({"resultado":"No se puede verificar el contenido el detalle de la carpeta"},status= status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return archivos_gestor_formatos_oficiales.objects.get(pk=pk)
        except archivos_gestor_formatos_oficiales.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = archivos_gestor_formatos_oficialesserializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            enlace = settings.URL_GESTOR_DOCUMENTAL + '/api/IGDAPI/ModificarDocumento'
            objeto = {'id':post.id_documento,'ceid':post.id_carpeta_encabezado,'llave':post.llave,'origen':post.origen,'documento':request.data['archivo'],'email':settings.EMAIL_GESTOR_DOCCUMENTAL}
            #print('objeto',objeto)
            x = requests.post(enlace, data = objeto)
            resultado = x.json()
            for result in resultado:
               #print('resultado',result)
                if result['response'].find('Correctamente')==-1:
                        return Response({"resultado":result['response']},status= status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,pk):
        existe= archivos_gestor_formatos_oficiales.objects.filter(id=pk).count()
        if existe!=0:
            get = self.get_object(pk)
            #get =  on_off_bording_bienvenida.objects.filter(id=id) if on_off_bording_bienvenida.objects.filter(id=id) else None 
            serializer=archivos_gestor_formatos_oficialesserializer(get)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)



def funcion(lista):
    for x in lista:
        formal_cl=Formal_Check_List.objects.get(id=4)
        formal_emp=Formal_empleado.objects.get(codigo=x['codigo']) if Formal_empleado.objects.filter(codigo=x['codigo']) else None
        if formal_emp:
            obj, created = Formal_Empleado_Check_List.objects.update_or_create(
                checklist=formal_cl, empleado=formal_emp,activo=1,
                defaults={},
            )
        funcional_cl=Funcional_Check_List.objects.get(id=1)
        funcional_emp=Funcional_empleado.objects.get(codigo=x['codigo']) if Funcional_empleado.objects.filter(codigo=x['codigo']) else None 

        if funcional_emp:
            obj, created = Funcional_Empleado_Check_List.objects.update_or_create(
                checklist=funcional_cl, empleado=funcional_emp,activo=1,
                defaults={},
            )
    return True


class Funcional_empleado_lista_sencillaviewsets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = Funcional_empleado_jerarquiaserializer

    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = Funcional_empleado.objects.all()
        serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
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
                   #print('entro aqui1')
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter

            
                queryset =  Funcional_empleado.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  Funcional_empleado.objects.filter(**filter_kwargs).count()
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
               #print('entro aqui1.2')
                queryset =  Funcional_empleado.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  Funcional_empleado.objects.filter().count()
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                
                if tipo_busqueda:
                   #print('entro aqui2')
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter

                queryset =  Funcional_empleado.objects.filter(**filter_kwargs).order_by('id')
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('entro aqui2.1')
                queryset =  Funcional_empleado.objects.filter().order_by('id')
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class Funcional_empleado_activos_lista_sencillaviewsets(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Funcional_empleado.objects.all()
    serializer_class = Funcional_empleado_jerarquiaserializer

    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = Funcional_empleado.objects.all()
        serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
        fecha_actual= datetime.today().strftime('%Y-%m-%d')
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
                   #print('entro aqui1')
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter

            
                queryset =  Funcional_empleado.objects.filter(**filter_kwargs).filter(Q(fecha_baja__isnull=True)| Q(fecha_baja__gte=fecha_actual)).order_by('id')[offset:offset+limit]
                conteo =  Funcional_empleado.objects.filter(**filter_kwargs).count()
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
               #print('entro aqui1.2')
                queryset =  Funcional_empleado.objects.filter().filter(Q(fecha_baja__isnull=True)| Q(fecha_baja__gte=fecha_actual)).order_by('id')[offset:offset+limit]
                conteo =  Funcional_empleado.objects.filter().count()
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                
                if tipo_busqueda:
                   #print('entro aqui2')
                    if tipo_busqueda =='nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda =='codigo':
                        filter_kwargs['codigo__icontains'] = filter

                queryset =  Funcional_empleado.objects.filter(**filter_kwargs).filter(Q(fecha_baja__isnull=True)| Q(fecha_baja__gte=fecha_actual)).order_by('id')
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
               #print('entro aqui2.1')
                queryset =  Funcional_empleado.objects.filter().filter(Q(fecha_baja__isnull=True)| Q(fecha_baja__gte=fecha_actual)).order_by('id')
                serializer = Funcional_empleado_jerarquiaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})



        
class Funcional_Funciones_filtrado_unidad_organizativaViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = Funcional_Funciones.objects.all()
    serializer_class = Funcional_Funcionesserializer
    def list(self, request):
        queryset = Funcional_Funciones.objects.all()
        serializer_class = Funcional_Funcionesserializer(queryset, many=True)
        filter=''
        unidad_organizativa=''
        usuario = request.user
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        lista_funciones=[]
        
        
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
            # listado.extend(hermanos)
        equipo = Funcional_Unidad_Organizativa.objects.filter(id=unidad_organizativa).values_list('unidad_organizativa_jeraquia__id',flat=True)
        equipo =Funcional_Unidad_Organizativa.objects.filter(id__in=listado)
        
        lista_permiso=list(request.user.groups.all().values_list('name',flat=True))
       

        serializer_unidad = funcional_arbol_padre_serializer(uni[0])
        serializer_padre = funcional_arbol_padre_serializer(padre[0]).data if padre else []
        print('serializer_unidad',uni[0].codigo)
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

        listado_funciones_empleados=''
        if empleados!=None:
            listado_funciones_empleados = empleados.values_list('posicion',flat=True)

        empleados_con_jefe_inmediato= Funcional_empleado.objects.filter(jefe_inmediato=usuario).values_list('posicion',flat=True).exclude(fecha_baja__lt=datetime.now().date())
        lista_funciones.extend(empleados_con_jefe_inmediato)    
        if listado_funciones_empleados!='':
            lista_funciones.extend(listado_funciones_empleados)
        
        
        
        
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
                filter = self.request.query_params.get('filter')


        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
            

        if 'jefe' in grupos:
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
                        if tipo_busqueda =='codigo':
                            filter_kwargs['codigo'] = filter
                        if tipo_busqueda =='nombre':
                            filter_kwargs['nombre'] = filter
                        if tipo_busqueda =='id':
                            filter_kwargs['id'] = filter
                    
                    # funciones_list= Funcional_empleado.objects.filter(unidad_organizativa__id=unidad_organizativa).values_list('posicion',flat=True)
                    queryset =  Funcional_Funciones.objects.filter(**filter_kwargs,id__in=lista_funciones).order_by('id')[offset:offset+limit]
                    conteo = Funcional_Funciones.objects.filter(**filter_kwargs,id__in=lista_funciones).count()
                    serializer = Funcional_Funcionesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else:
                    # funciones_list= Funcional_empleado.objects.filter(unidad_organizativa__id=unidad_organizativa).values_list('posicion',flat=True) 
                    queryset =  Funcional_Funciones.objects.filter(id__in=lista_funciones).order_by('id')[offset:offset+limit]
                    conteo = Funcional_Funciones.objects.filter(id__in=lista_funciones).count()
                    serializer = Funcional_Funcionesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
            else:
                if filter!='' and tipo_busqueda!='':
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='descripcion':
                            filter_kwargs['descripcion__icontains'] = filter
                        if tipo_busqueda =='codigo':
                            filter_kwargs['codigo'] = filter
                        if tipo_busqueda =='nombre':
                            filter_kwargs['nombre'] = filter
                        if tipo_busqueda =='id':
                            filter_kwargs['id'] = filter
                            
                    # funciones_list= Funcional_empleado.objects.filter(unidad_organizativa__id=unidad_organizativa).values_list('posicion',flat=True)
                    queryset =  Funcional_Funciones.objects.filter(**filter_kwargs,id__in=lista_funciones).order_by('id')
                    conteo =Funcional_Funciones.objects.filter(**filter_kwargs,id__in=lista_funciones).count()
                    serializer = Funcional_Funcionesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else:
                    # funciones_list= Funcional_empleado.objects.filter(unidad_organizativa__id=unidad_organizativa).values_list('posicion',flat=True) 
                    queryset =  Funcional_Funciones.objects.filter(id__in=lista_funciones).order_by('id')
                    ##print('')

                    conteo =Funcional_Funciones.objects.filter(id__in=lista_funciones).count()
                    serializer = Funcional_Funcionesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})
        else:
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
                        if tipo_busqueda =='codigo':
                            filter_kwargs['codigo'] = filter
                        if tipo_busqueda =='nombre':
                            filter_kwargs['nombre'] = filter
                        if tipo_busqueda =='id':
                            filter_kwargs['id'] = filter
                            
                    queryset =  Funcional_Funciones.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                    conteo = Funcional_Funciones.objects.filter(**filter_kwargs).count()
                    serializer = Funcional_Funcionesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo}) 
                else: 
                    queryset =  Funcional_Funciones.objects.filter().order_by('id')[offset:offset+limit]
                    conteo= Funcional_Funciones.objects.filter().count()
                    serializer = Funcional_Funcionesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":conteo})
            else:
                if filter!='' and tipo_busqueda!='':
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='descripcion':
                            filter_kwargs['descripcion__icontains'] = filter
                        if tipo_busqueda =='codigo':
                            filter_kwargs['codigo'] = filter
                        if tipo_busqueda =='nombre':
                            filter_kwargs['nombre'] = filter
                        if tipo_busqueda =='id':
                            filter_kwargs['id'] = filter
                            
                    queryset =  Funcional_Funciones.objects.filter(**filter_kwargs).order_by('id')
                    serializer = Funcional_Funcionesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()}) 
                else: 
                    queryset =  Funcional_Funciones.objects.filter().order_by('id')
                    
                    serializer = Funcional_Funcionesserializer(queryset, many=True)
                    return Response({"data":serializer.data,"count":queryset.count()})



def puestos(usuario):
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
        empleados_dados_de_baja = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()) else None
        puestos = Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None) if Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None) else None
        
        if lider!=None:
            empleados_activos = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado).exclude(id__in=lideres).exclude(fecha_baja__lt=datetime.now().date()) else None
            empleados_dados_de_baja = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()).exclude(id__in=lideres) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id__in=listado,fecha_baja__lt=datetime.now().date()).exclude(id__in=lideres) else None
            puestos = Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None).exclude(id__in=lideres) if Funcional_Puesto.objects.filter(unidad_organizativa__id__in=listado,funcional_empleado=None).exclude(id__in=lideres) else None
        
        #Empleados que pertenecen a determinado jefe encontrados mediante la unidad organizativa
        listado_puestos_empleados_activos=[]
        lista_emple= empleados_activos.values_list('puesto__codigo',flat=True)
        listado_puestos_empleados_activos.extend(lista_emple)
        #No activos encontrados mediante la unidad organizativa en la tabla de empleados y la fecha de baja
        if empleados_dados_de_baja!=None:
            lista_puestos.extend(empleados_dados_de_baja.values_list('puesto__codigo',flat=True))
        #No activos encontrados mediante la unidad organizativa
        if puestos!=None:
            lista_puestos.extend( puestos.values_list('codigo',flat=True))
        
        #activos encontrados mediante el jefe inmediato
        empleados_con_jefe_inmediato= Funcional_empleado.objects.filter(jefe_inmediato=usuario).values_list('puesto__codigo',flat=True) if Funcional_empleado.objects.filter(jefe_inmediato=usuario) else None
        #inactivos encontrados mediante el jefe inmediato
        empleados_dados_baja_jefe_inmediato= Funcional_empleado.objects.filter(jefe_inmediato=usuario,fecha_baja__lt=datetime.now().date()).values_list('puesto__codigo',flat=True) if Funcional_empleado.objects.filter(jefe_inmediato=usuario,fecha_baja__lt=datetime.now().date()) else None

        #puestos dirigido por vacantes
        # lista_puesto_dirigido_por=[]
        puesto_dirigido_por_vacantes=Funcional_Puesto.objects.filter(unidad_organizativa__Dirigido_por=usuario,funcional_empleado=None).values_list('codigo',flat=True) if Funcional_Puesto.objects.filter(unidad_organizativa__Dirigido_por=usuario,funcional_empleado=None).values_list('codigo') else None  
        if puesto_dirigido_por_vacantes!=None:
            lista_puestos.extend(puesto_dirigido_por_vacantes)


        #puestos dirigido por activos
        puesto_dirigido_por_activos=Funcional_Puesto.objects.filter(unidad_organizativa__Dirigido_por=usuario).exclude(funcional_empleado=None).values_list('codigo',flat=True) if Funcional_Puesto.objects.filter(unidad_organizativa__Dirigido_por=usuario).exclude(funcional_empleado=None).values_list('codigo') else None  
        if puesto_dirigido_por_activos!=None:
            listado_puestos_empleados_activos.extend(puesto_dirigido_por_activos)




        #nuevo llenado de lista activos 
        if empleados_con_jefe_inmediato!=None:
            listado_puestos_empleados_activos.extend(empleados_con_jefe_inmediato) 
             
        #nuevo llenado de lista inactivos
        if empleados_dados_baja_jefe_inmediato!=None:
            lista_puestos.extend(empleados_dados_baja_jefe_inmediato)


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

        data={'plazas_vacantes':nueva_lista_plaza_vacantes,'plazas_activas':nueva_lista_plazas_activas,'total_plazas_vacantes':len(nueva_lista_plaza_vacantes),'total_plazas_activas':len(nueva_lista_plazas_activas)}
        # print(data)
        return data


