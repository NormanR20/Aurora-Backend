

from decimal import MIN_EMIN
from distutils.cygwinccompiler import Mingw32CCompiler
from django.db.models.functions import ExtractYear

from re import sub
from django.contrib.auth.models import User,Group
from django.http.response import Http404
from django.shortcuts import render
from calendar import monthrange

from rest_framework.generics import get_object_or_404
from ..models import on_off_bording_workflow,on_off_bording_tarea,on_off_bording_bloque
from ..models import on_off_bording_workflow_plantilla, on_off_bording_bloque_plantilla,on_off_bording_tarea_plantilla
from ..models import on_off_bording_bienvenida
from ..models import Funcional_empleado,Funcional_Unidad_Organizativa,Funcional_Organizacion,Funcional_Puesto
from ..serializers import on_off_bording_workflowserializer,on_off_bording_bloqueserializer,on_off_bording_tareaserializer
from ..serializers import on_off_bording_workflow_plantillaserializer,on_off_bording_bloque_plantillaserializer,on_off_bording_tarea_plantillaserializer
from ..serializers import on_off_bording_bienvenidaserializer
##############################################################################################

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
from ..models.modelos_nucleo import *
from ..serializers.serializers_nucleo import *
from django.apps import apps
from datetime import datetime,timedelta
from django.core.exceptions import ObjectDoesNotExist

import sys
sys.setrecursionlimit(100000000)                                                        
from rest_framework import viewsets




class On_off_bording_workflowViewSet(viewsets.ModelViewSet):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    queryset = on_off_bording_workflow.objects.all()
    serializer_class = on_off_bording_workflowserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        print(json.loads(self.request.query_params.get('tipo_workflow')))
        queryset = on_off_bording_workflow.objects.all()
        serializer = on_off_bording_workflowserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        tipo_wf=0
        print(self.request.query_params.get('tipo_workflow'))
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        if self.request.query_params.get('tipo_workflow'):
            tipo_wf = json.loads(self.request.query_params.get('tipo_workflow'))
        else:
            return Response({"mensaje":"Falta parámetro de tipo workflow"},status= status.HTTP_404_NOT_FOUND)

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'empleado':
                        filter_kwargs['empleado__username__icontains'] = filter
                    if tipo_busqueda == 'responsable':
                        filter_kwargs['responsable__username__icontains'] = filter
            
                filter_kwargs['tipo_workflow__in'] = tipo_wf
                queryset =  on_off_bording_workflow.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_workflow.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_workflowserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                filter_kwargs={}
                filter_kwargs['tipo_workflow__in'] = tipo_wf
                queryset =  on_off_bording_workflow.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_workflow.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_workflowserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda == 'descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'empleado':
                        filter_kwargs['empleado__username__icontains'] = filter
                    if tipo_busqueda == 'responsable':
                        filter_kwargs['responsable__username__icontains'] = filter

                filter_kwargs['tipo_workflow__in'] = tipo_wf
                queryset =  on_off_bording_workflow.objects.filter(**filter_kwargs).order_by('id')
                serializer = on_off_bording_workflowserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                filter_kwargs={}
                filter_kwargs['tipo_workflow__in'] = tipo_wf
                print('filtros',filter_kwargs)
                queryset =  on_off_bording_workflow.objects.filter(**filter_kwargs).order_by('id')
                serializer = on_off_bording_workflowserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class On_off_bording_bloqueViewSet(viewsets.ModelViewSet):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    queryset = on_off_bording_bloque.objects.all()
    serializer_class = on_off_bording_bloqueserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = on_off_bording_bloque.objects.all()
        serializer = on_off_bording_bloqueserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        id_workflow=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('id_workflow'):
            id_workflow = self.request.query_params.get('id_workflow')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'workflow':
                        filter_kwargs['workflow__nombre__icontains'] = filter
            
                if id_workflow:
                    filter_kwargs['workflow__id']=id_workflow

                queryset =  on_off_bording_bloque.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_bloque.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_bloqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 

            elif id_workflow:
                filter_kwargs={}
                if id_workflow:
                    filter_kwargs['workflow__id']=id_workflow

                queryset =  on_off_bording_bloque.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_bloque.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_bloqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 

            else: 
                queryset =  on_off_bording_bloque.objects.all().order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_bloque.objects.all().count()
                serializer = on_off_bording_bloqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda == 'descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'workflow':
                        filter_kwargs['workflow__nombre__icontains'] = filter
                
                if id_workflow:
                    filter_kwargs['workflow__id']=id_workflow

                queryset =  on_off_bording_bloque.objects.filter(**filter_kwargs).order_by('id')
                serializer = on_off_bording_bloqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            
            elif id_workflow:
                filter_kwargs={}
                if id_workflow:
                    filter_kwargs['workflow__id']=id_workflow

                queryset =  on_off_bording_bloque.objects.filter(**filter_kwargs).order_by('id')
                conteo =  on_off_bording_bloque.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_bloqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})

            else:
                queryset =  on_off_bording_bloque.objects.all().order_by('id')
                serializer = on_off_bording_bloqueserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class On_off_bording_tareaViewSet(viewsets.ModelViewSet):
    # authentication_classes=[TokenAuthentication]
    # permission_classes=[DjangoModelPermissions]
    queryset = on_off_bording_tarea.objects.all()
    serializer_class = on_off_bording_tareaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = on_off_bording_tarea.objects.all()
        serializer = on_off_bording_tareaserializer(queryset, many=True)
        filter=''
        id_bloque=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('id_bloque'):
            id_bloque = self.request.query_params.get('id_bloque')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'bloque':
                        filter_kwargs['bloque__nombre__icontains'] = filter
                    if tipo_busqueda == 'compa_guia':
                        filter_kwargs['compa_guia__username__icontains'] = filter
                
                if id_bloque:
                    filter_kwargs['bloque__id']=id_bloque
            
                queryset =  on_off_bording_tarea.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_tarea.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_tareaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  

            elif id_bloque:
                filter_kwargs={}
                if id_bloque:
                    filter_kwargs['bloque__id']=id_bloque
            
                queryset =  on_off_bording_tarea.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_tarea.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_tareaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 

            else: 
                queryset =  on_off_bording_tarea.objects.all().order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_tarea.objects.all().count()
                serializer = on_off_bording_tareaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda == 'descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'bloque':
                        filter_kwargs['bloque__nombre__icontains'] = filter
                    if tipo_busqueda == 'compa_guia':
                        filter_kwargs['compa_guia__username__icontains'] = filter

                if id_bloque:
                    filter_kwargs['bloque__id']=id_bloque

                queryset =  on_off_bording_tarea.objects.filter(**filter_kwargs).order_by('id')
                serializer = on_off_bording_tareaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

            elif id_bloque:
                filter_kwargs={}
                if id_bloque:
                    filter_kwargs['bloque__id']=id_bloque
            
                queryset =  on_off_bording_tarea.objects.filter(**filter_kwargs).order_by('nombre')
                conteo =  on_off_bording_tarea.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_tareaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo}) 

            else:
                queryset =  on_off_bording_tarea.objects.all().order_by('id')
                serializer = on_off_bording_tareaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


class Copia_workflowviewset(APIView):
    def post(self,request):
        #print('este es el request',request.data)    
        try:
            empleados=request.data['empleados']
            workflow=request.data['workflow']
            respuesta=[]
           #print("este es el request",request)
           #print("estos son los empleados",empleados)
           #print("este es el workflow",workflow)

            for x in empleados:
                
               #print("ciclo para empleado",x)
                workf=on_off_bording_workflow_plantilla.objects.get(id=workflow) if  on_off_bording_workflow_plantilla.objects.filter(id=workflow) else None
                
                if workf:
                    tipo_workflow=workf.tipo_workflow

                    
                    empleado=User.objects.get(id=x['empleado']) if User.objects.filter(id=x['empleado']) else None
                    if empleado==None:
                        return Response({"mensaje":"Ha Sucedido un error,Empleado enviado no existe"},status= status.HTTP_404_NOT_FOUND)

                    if  on_off_bording_workflow.objects.filter(empleado=empleado,tipo_workflow=workf.tipo_workflow,estado=False).count() > 0:
                        return Response({"mensaje":"El empleado ya esta en un proceso de este tipo"},status= status.HTTP_404_NOT_FOUND)


                    responsable=User.objects.get(id=x['responsable']) if User.objects.filter(id=x['responsable']) else None
                    if responsable==None:
                        return Response({"mensaje":"Ha Sucedido un error,Responsable enviado no existe"},status= status.HTTP_404_NOT_FOUND)
                   #print('empleado',empleado)
                   #print('responsable',responsable)


                    #comentario
                    wf=on_off_bording_workflow.objects.create(descripcion=workf.descripcion,nombre=workf.nombre,fecha_inicio=workf.fecha_inicio,fecha_fin=workf.fecha_fin,estado=workf.estado,empleado=empleado,responsable=responsable,tipo_workflow=workf.tipo_workflow)
                    
                    respuesta.append({"empleado":empleado.id,"workflow":wf.id})
                    wfbloques=on_off_bording_bloque_plantilla.objects.filter(workflow=workf.id) if  on_off_bording_bloque_plantilla.objects.filter(workflow=workf.id) else None
                    
                    if wfbloques:                    
                        for wb in wfbloques:
                            
                            nwfb= on_off_bording_bloque.objects.create(descripcion=wb.descripcion, nombre=wb.nombre,fecha_inicio=wb.fecha_inicio,fecha_fin=wb.fecha_fin,estado=wb.estado,posicion=wb.posicion,workflow=wf)
                            wftareas = on_off_bording_tarea_plantilla.objects.filter(bloque=wb.id) if  on_off_bording_tarea_plantilla.objects.filter(bloque=wb.id) else None
                            if wftareas:
                                for wft in wftareas:
                                    
                                    #compa=User.objects.get(id=wft.compa_guia.id) if User.objects.filter(id=wft.compa_guia.id) else None
                                    #if compa==None:
                                    #    return Response({"mensaje":"Ha Sucedido un error,Compañero guia no existe"},status= status.HTTP_404_NOT_FOUND)

                                    
                                    on_off_bording_tarea.objects.create(descripcion=wft.descripcion ,nombre=wft.nombre ,fecha_inicio=wft.fecha_inicio ,fecha_fin=wft.fecha_fin ,evaluable=wft.evaluable,calificacion=wft.calificacion,posicion=wft.posicion,estado=wft.estado,archivo_bajar=wft.archivo_bajar,subir_archivo=wft.subir_archivo,enlace_evaluacion=wft.enlace_evaluacion,bloque=nwfb,archivos_gestor=wft.archivos_gestor)
                            
                    rr=on_off_bording_workflow.objects.get(id=wf.id)
                    serializer = on_off_bording_workflowserializer(rr)
                    #print('llego al final')
                    #return Response(status= status.HTTP_200_OK)
                    if tipo_workflow==1:#on
                        on_off_notificaciones_envio_correo('Jefe Inmediato - Inicio On',wf.id)
                        on_off_notificaciones_envio_correo('Empleado - Inicio On',wf.id)
                        on_off_notificaciones_envio_correo('Responsable - Inicio On',wf.id)
                    elif tipo_workflow==2:#off 
                        on_off_notificaciones_envio_correo('Responsable - Inicio Off',wf.id)
                        on_off_notificaciones_envio_correo('Jefe Inmediato - Inicio Off',wf.id)

                else :
                    
                    return Response({"mensaje":"Ha Sucedido un error,contacta al administrador"},status= status.HTTP_404_NOT_FOUND)
                


            return Response({"resultado":respuesta},status= status.HTTP_200_OK)
        except BadHeaderError:
                return Response({"mensaje":"Ha Sucedido un error,contacta al administrador"},status= status.HTTP_404_NOT_FOUND)


class Copia_masiva_workflowviewset(APIView):
    def post(self,request):

        #print('este es el request',request.data)
        try:
            empleados=request.data['empleados']
            workflow=request.data['workflow']
            for x in empleados:
                

                workf=on_off_bording_workflow.objects.get(id=workflow) if  on_off_bording_workflow.objects.filter(id=workflow) else None
                
                if workf:
                    empleado=User.objects.get(id=x['empleado']) if User.objects.filter(id=x['empleado']) else None

                    if empleado==None:
                        return Response({"mensaje":"Ha Sucedido un error,Empleado enviado no existe"},status= status.HTTP_404_NOT_FOUND)

                                        
                    
                    if  on_off_bording_workflow.objects.filter(empleado=empleado,tipo_workflow=workf.tipo_workflow,estado=False).count() > 0:
                        return Response({"mensaje":"El empleado ya esta en un proceso de este tipo"},status= status.HTTP_404_NOT_FOUND)

                    responsable=User.objects.get(id=x['responsable']) if User.objects.filter(id=x['responsable']) else None
                    
                    if responsable==None:
                        return Response({"mensaje":"Ha Sucedido un error,Responsable enviado no existe"},status= status.HTTP_404_NOT_FOUND)
                    
                    wf=on_off_bording_workflow.objects.create(descripcion=workf.descripcion,nombre=workf.nombre,fecha_inicio=workf.fecha_inicio,fecha_fin=workf.fecha_fin,empleado=empleado,responsable=responsable,tipo_workflow=workf.tipo_workflow)
                    wfbloques=on_off_bording_bloque.objects.filter(workflow=workf.id) if  on_off_bording_bloque.objects.filter(workflow=workf.id) else None
                    if wfbloques:
                        for wb in wfbloques:
                            
                            nwfb= on_off_bording_bloque.objects.create(descripcion=wb.descripcion, nombre=wb.nombre,fecha_inicio=wb.fecha_inicio,fecha_fin=wb.fecha_fin,posicion=wb.posicion,workflow=wf)
                            wftareas = on_off_bording_tarea.objects.filter(bloque=wb.id) if  on_off_bording_tarea.objects.filter(bloque=wb.id) else None
                            
                            if wftareas:
                                for wft in wftareas:
                                    
                                    #compa=User.objects.get(id=wft.compa_guia.id) if User.objects.filter(id=wft.compa_guia.id) else None
                                    #if compa==None:
                                    #    return Response({"mensaje":"Ha Sucedido un error,Compañero guia no existe"},status= status.HTTP_404_NOT_FOUND)

                                    
                                    on_off_bording_tarea.objects.create(descripcion=wft.descripcion ,nombre=wft.nombre ,fecha_inicio=wft.fecha_inicio ,fecha_fin=wft.fecha_fin ,evaluable=wft.evaluable,calificacion=wft.calificacion,posicion=wft.posicion,archivo_bajar=wft.archivo_bajar,subir_archivo=wft.subir_archivo,enlace_evaluacion=wft.enlace_evaluacion,bloque=nwfb,compa_guia=wft.compa_guia,archivos_gestor=wft.archivos_gestor)
                    rr=on_off_bording_workflow.objects.get(id=wf.id)
                    serializer = on_off_bording_workflowserializer(rr)
                    #return Response({"datos":serializer.data},status= status.HTTP_200_OK)
                    #print('llego al final')
                    #return Response(status= status.HTTP_200_OK)
                
                else :
                    
                    return Response({"mensaje":"Ha Sucedido un error,contacta al administrador"},status= status.HTTP_404_NOT_FOUND)
                


            return Response(status= status.HTTP_200_OK)
        except BadHeaderError:
                return Response({"mensaje":"Ha Sucedido un error,contacta al administrador"},status= status.HTTP_404_NOT_FOUND)

class On_off_bording_workflow_plantillaViewSet(viewsets.ModelViewSet):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    queryset = on_off_bording_workflow_plantilla.objects.all()
    serializer_class = on_off_bording_workflow_plantillaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = on_off_bording_workflow_plantilla.objects.all()
        serializer = on_off_bording_workflow_plantillaserializer(queryset, many=True)
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
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'creador_codigo':
                        filter_kwargs['creador__username__icontains'] = filter
                    if tipo_busqueda == 'creador_nombre':
                        filter_kwargs['creador__first_name__icontains'] = filter
            
                queryset =  on_off_bording_workflow_plantilla.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_workflow_plantilla.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_workflow_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  on_off_bording_workflow_plantilla.objects.all().order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_workflow_plantilla.objects.all().count()
                serializer = on_off_bording_workflow_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda == 'descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'creador_codigo':
                        filter_kwargs['creador__username__icontains'] = filter
                    if tipo_busqueda == 'creador_nombre':
                        filter_kwargs['creador__first_name__icontains'] = filter

                queryset =  on_off_bording_workflow_plantilla.objects.filter(**filter_kwargs).order_by('id')
                serializer = on_off_bording_workflow_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  on_off_bording_workflow_plantilla.objects.all().order_by('id')
                serializer = on_off_bording_workflow_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class On_off_bording_bloque_plantillaViewSet(viewsets.ModelViewSet):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    queryset = on_off_bording_bloque_plantilla.objects.all()
    serializer_class = on_off_bording_bloque_plantillaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = on_off_bording_bloque_plantilla.objects.all()
        serializer = on_off_bording_bloque_plantillaserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        id_workflow=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('id_workflow'):
            id_workflow = self.request.query_params.get('id_workflow')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'workflow':
                        filter_kwargs['workflow__nombre__icontains'] = filter

                if id_workflow:
                    filter_kwargs['workflow__id']=id_workflow

                queryset =  on_off_bording_bloque_plantilla.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_bloque_plantilla.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_bloque_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  

            elif id_workflow:
                filter_kwargs={}
                if id_workflow:
                    filter_kwargs['workflow__id']=id_workflow

                queryset =  on_off_bording_bloque_plantilla.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_bloque_plantilla.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_bloque_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  

            else: 
                queryset =  on_off_bording_bloque_plantilla.objects.all().order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_bloque_plantilla.objects.all().count()
                serializer = on_off_bording_bloque_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda == 'descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'workflow':
                        filter_kwargs['workflow__nombre__icontains'] = filter

                if id_workflow:
                    filter_kwargs['workflow__id']=id_workflow
                
                queryset =  on_off_bording_bloque_plantilla.objects.filter(**filter_kwargs).order_by('id')
                serializer = on_off_bording_bloque_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

            elif id_workflow:
                filter_kwargs={}
                if id_workflow:
                    filter_kwargs['workflow__id']=id_workflow

                queryset =  on_off_bording_bloque_plantilla.objects.filter(**filter_kwargs).order_by('id')
                conteo =  on_off_bording_bloque_plantilla.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_bloque_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  

            else:
                queryset =  on_off_bording_bloque_plantilla.objects.all().order_by('id')
                serializer = on_off_bording_bloque_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class On_off_bording_tarea_plantillaViewSet(viewsets.ModelViewSet):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    queryset = on_off_bording_tarea_plantilla.objects.all()
    serializer_class = on_off_bording_tarea_plantillaserializer
    def list(self, request):
        #print(self.request.query_params.get('filter'))
        queryset = on_off_bording_tarea_plantilla.objects.all()
        serializer = on_off_bording_tarea_plantillaserializer(queryset, many=True)
        filter=''
        id_bloque=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')
        
        if self.request.query_params.get('id_bloque'):
            id_bloque = self.request.query_params.get('id_bloque')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'bloque':
                        filter_kwargs['bloque__nombre__icontains'] = filter

                if id_bloque:
                    filter_kwargs['bloque__id']=id_bloque
            
                queryset =  on_off_bording_tarea_plantilla.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_tarea_plantilla.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_tarea_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  

            elif id_bloque:
                filter_kwargs={}
                if id_bloque:
                    filter_kwargs['bloque__id']=id_bloque
            
                queryset =  on_off_bording_tarea_plantilla.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_tarea_plantilla.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_tarea_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  

            else: 
                queryset =  on_off_bording_tarea_plantilla.objects.all().order_by('id')[offset:offset+limit]
                conteo =  on_off_bording_tarea_plantilla.objects.all().count()
                serializer = on_off_bording_tarea_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda == 'descripcion':
                        filter_kwargs['descripcion__icontains'] = filter
                    if tipo_busqueda == 'nombre':
                        filter_kwargs['nombre__icontains'] = filter
                    if tipo_busqueda == 'bloque':
                        filter_kwargs['bloque__nombre__icontains'] = filter

                if id_bloque:
                    filter_kwargs['bloque__id']=id_bloque

                queryset =  on_off_bording_tarea_plantilla.objects.filter(**filter_kwargs).order_by('id')
                serializer = on_off_bording_tarea_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

            elif id_bloque:
                filter_kwargs={}
                if id_bloque:
                    filter_kwargs['bloque__id']=id_bloque
            
                queryset =  on_off_bording_tarea_plantilla.objects.filter(**filter_kwargs).order_by('id')
                conteo =  on_off_bording_tarea_plantilla.objects.filter(**filter_kwargs).count()
                serializer = on_off_bording_tarea_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  

            else:
                queryset =  on_off_bording_tarea_plantilla.objects.all().order_by('id')
                serializer = on_off_bording_tarea_plantillaserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class On_off_bording_bienvenida_postViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    # queryset = on_off_bording_bienvenida.objects.all()
    # serializer_class = on_off_bording_bienvenidaserializer
    def get(self,request):
        get =  on_off_bording_bienvenida.objects.all().values('id','texto_json')
        serializer = on_off_bording_bienvenidaserializer(get,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    def post (self,request):

        existe= on_off_bording_bienvenida.objects.all().count()
        if existe == 0:
            serializer= on_off_bording_bienvenidaserializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset= on_off_bording_bienvenida.objects.all().values('id','texto_json')
            serializer= on_off_bording_bienvenidaserializer(queryset, many=True)
            #serializer= on_off_bording_bienvenidaserializer(data=request.data)
            return Response (serializer.data,status= status.HTTP_200_OK)

class On_off_bording_bienvenidaViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    # queryset = on_off_bording_bienvenida.objects.all()
    # serializer_class = on_off_bording_bienvenidaserializer
    
    def get_object(self,id):
        return on_off_bording_bienvenida.objects.get(id=id)
        # try:
        #     return on_off_bording_bienvenida.objects.get(id=id)
        # except on_off_bording_bienvenida.DoesNotExist:
        #     raise http404

    def get(self,request,id):
        existe= on_off_bording_bienvenida.objects.filter(id=id).count()
        if existe!=0:
            get = self.get_object(id)
            #get =  on_off_bording_bienvenida.objects.filter(id=id) if on_off_bording_bienvenida.objects.filter(id=id) else None 
            serializer=on_off_bording_bienvenidaserializer(get)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self,requets,id):
        existe= on_off_bording_bienvenida.objects.filter(id=id).count()
        if existe!=0:
            put = self.get_object(id)
            serializer= on_off_bording_bienvenidaserializer(put,data=requets.data)
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

class On_off_bording_bienvenida_embebidaViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    # queryset = on_off_bording_bienvenida.objects.all()
    # serializer_class = on_off_bording_bienvenidaserializer
    def get(self,request):
        usuario = request.user
        id_bienvenida=''
        codigo_empleado=usuario.username
        codigo_empleado=codigo_empleado.zfill(8)
        texto_json=''
        bienvenida =  on_off_bording_bienvenida.objects.all().values('id','texto_json')[0]
        cempleado=''
        if self.request.query_params.get('cempleado'):
            cempleado = self.request.query_params.get('cempleado')
        if bienvenida:
            texto_json = bienvenida['texto_json']
            texto_json= json.dumps(texto_json)
            empleado= Funcional_empleado.objects.filter(codigo=codigo_empleado).values('unidad_organizativa__sociedad_financiera__nombre','nombre','unidad_organizativa__Dirigido_por')
            if empleado:
                codigo_jefe= empleado[0]['unidad_organizativa__Dirigido_por']
                nombre_empleado= empleado[0]['nombre']
                nombre_compania= empleado[0]['unidad_organizativa__sociedad_financiera__nombre']
                if nombre_compania:               
                    texto_json=texto_json.replace('@compania',nombre_compania)
                else: 
                    texto_json=texto_json.replace('@compania','NOMBRE DE ORGANIZACION')
                texto_json=texto_json.replace('@nombre_empleado',nombre_empleado)
                if codigo_jefe:
                    empleado_jefe= Funcional_empleado.objects.filter(codigo=codigo_jefe).values('nombre','puesto__descripcion')
                    if empleado_jefe:
                        nombre_jefe = empleado_jefe[0]['nombre']
                        nombre_puesto = empleado_jefe[0]['puesto__descripcion']
                        if nombre_jefe:
                            texto_json=texto_json.replace('@nombre_jefe',nombre_jefe)
                        else:
                            texto_json=texto_json.replace('@nombre_jefe','NOMBRE DEL JEFE')
                        if nombre_puesto:
                            texto_json=texto_json.replace('@nombre_puesto',nombre_puesto)
                        else:
                            texto_json=texto_json.replace('@nombre_puesto','PUESTO DEL JEFE')
                    else:
                        texto_json=texto_json.replace('@nombre_jefe','NOMBRE DEL JEFE')
                        texto_json=texto_json.replace('@nombre_puesto','PUESTO DEL JEFE')
                else:
                    texto_json=texto_json.replace('@nombre_jefe','NOMBRE DEL JEFE')
                    texto_json=texto_json.replace('@nombre_puesto','PUESTO DEL JEFE')
                    
                fecha=datetime.now().date()
                fecha_str= fecha.strftime('%Y/%m/%d')
                texto_json=texto_json.replace('@fecha',fecha_str)
                texto_json= json.loads(texto_json)
                return Response({"data":texto_json})
                
            else:
                 return Response({"mensaje":"El empleado no existe"},status=status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response({"mensaje":"No hay una Bienvenida cargada"},status=status.HTTP_400_BAD_REQUEST) 


class On_off_bording_envio_correoViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    # queryset = on_off_bording_bienvenida.objects.all()
    # serializer_class = on_off_bording_bienvenidaserializer
    def get(self,request):
        #print ('hola')
        workflow_id=0
        bloque_id=0
        tarea_id=0
        modulo='ON/OFF BOARDING'
        tipo_mensaje = ''
        if self.request.query_params.get('workflow_id'):
            workflow_id = self.request.query_params.get('workflow_id')
        if self.request.query_params.get('bloque_id'):
            bloque_id = self.request.query_params.get('bloque_id')
        if self.request.query_params.get('tarea_id'):
            tarea_id = self.request.query_params.get('tarea_id')
        if  self.request.query_params.get('tipo_mensaje'):
            tipo_mensaje=self.request.query_params.get('tipo_mensaje')
        
        if bloque_id!=0 and workflow_id!=0 and tarea_id!=0 and tipo_mensaje!='':
            if (tipo_mensaje == 'Responsable - Nota Evaluacion'):
                
                tarea_valida_evaluable = on_off_bording_tarea.objects.filter(id=tarea_id,evaluable=True,estado=False).count()
                
                if tarea_valida_evaluable==0:
                    return Response({"mensaje":"Tarea no evaluable o tarea ya realizada"},status=status.HTTP_400_BAD_REQUEST)

                workflow=on_off_bording_workflow.objects.filter(id=workflow_id).values()
                empleado= workflow[0]['empleado_id']
                responsable= workflow[0]['responsable_id']

                configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
                if configuracion_correo:
                    asunto=configuracion_correo[0]['asunto']
                    mensaje=configuracion_correo[0]['mensaje']
                    #print('MENSAJE SIN SETEAR',mensaje)
                    variables_envio_correo= nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
                    if variables_envio_correo:
                        for vec in variables_envio_correo:
                            variable= vec.variable
                            app= vec.app
                            modelos= vec.modelos
                            valores= vec.valores
                            modelo_tb= apps.get_model(app,modelos)
                            valor_a_sustituir=modelo_tb.objects.filter(bloque__workflow__empleado__id=empleado,id=tarea_id).values(valores)[0]
                            if valor_a_sustituir:
                                valor_a_sustituir_str = valor_a_sustituir[valores]
                                #texto_json=texto_json.replace('@fecha',fecha_str)
                                mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                                asunto= asunto.replace(variable,valor_a_sustituir_str)
                                #print ('MENSAJES CON CAMBIOS',mensaje)

                        username_responsable= User.objects.filter(id=responsable).values('username')[0]
                        username_responsable = username_responsable['username']
                        responsable= Funcional_empleado.objects.filter(codigo=username_responsable).values('correo_empresarial')[0]
                        correo_responsable= responsable['correo_empresarial']
                        # for res in workflow: 
                        #     username_responsable= User.objects.filter(id=res['responsable_id']).values('username')
                        #     responsables= Funcional_empleado.objects.filter(codigo=username_responsable).values('correo_empresarial')
                        #     responsables= responsables[0]['correo_empresarial']
                        #     correo_responsable=responsables
                        if correo_responsable:
                            from_email_responsable_nota = settings.EMAIL_HOST_USER
                            try:
                                msg_responsable_nota = EmailMultiAlternatives(asunto, mensaje, from_email_responsable_nota, [correo_responsable])
                                msg_responsable_nota.send()
                                #print('CORREO ENVIADO CON EXITO')
                            except BadHeaderError:
                                return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
                            return Response({"asunto": asunto ,"mensaje":mensaje},status=status.HTTP_200_OK) 
                        else:
                            return Response({"mensaje":"el responsable no tiene correo empresarial registrado"},status= status.HTTP_404_NOT_FOUND)    
                    else:
                        return Response({"mensaje":"No existen variables cargadas para esta notificacion"},status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"mensaje":"No existe una configuracion de correo para esta notificacion"},status=status.HTTP_400_BAD_REQUEST)
            
            elif tipo_mensaje == 'Companero Guia - Notificacion acompanamiento':
                #compañiero_guia = on_off_bording_tarea.
                #print('Companero Guia - Notificacion acompanamiento')
                validacion_compa_guia = on_off_bording_tarea.objects.filter(Q(id=tarea_id),Q(estado=False),~Q(compa_guia=None)).count()
                if validacion_compa_guia==0:
                    return Response({"mensaje":"Tarea sin compañero guia o tarea ya realizada"},status=status.HTTP_400_BAD_REQUEST)

                tarea = on_off_bording_tarea.objects.filter(id= tarea_id).values() if on_off_bording_tarea.objects.filter(id= tarea_id).values() else None
                if tarea:
                    workflow=on_off_bording_tarea.objects.filter(id=tarea_id).values('bloque__workflow__empleado__id','compa_guia')
                    empleado= workflow[0]['bloque__workflow__empleado__id']
                    compa_guia= workflow[0]['compa_guia']
                    # print (compa_guia)
                    # print('empleado', empleado)
                    configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
                    
                    if configuracion_correo:
                        asunto=configuracion_correo[0]['asunto']
                        mensaje=configuracion_correo[0]['mensaje']
                        #print('MENSAJE SIN SETEAR',mensaje)
                        variables_envio_correo= nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
                        #print (variables_envio_correo)
                        if variables_envio_correo:
                            for vec in variables_envio_correo:
                                variable= vec.variable
                                app= vec.app
                                modelos= vec.modelos
                                valores= vec.valores
                                modelo_tb= apps.get_model(app,modelos)
                                valor_a_sustituir=modelo_tb.objects.filter(id=tarea_id).values(valores)[0]
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir[valores]
                                    #texto_json=texto_json.replace('@fecha',fecha_str)
                                    mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                                    asunto= asunto.replace(variable,valor_a_sustituir_str)
                                    #print ('MENSAJES CON CAMBIOS',mensaje)
                                
                            tipo_workflow= on_off_bording_workflow.objects.filter(id=workflow_id).values('tipo_workflow')[0]
                            tipo_workflow=tipo_workflow['tipo_workflow']
                            if tipo_workflow==1:
                                #print('ON')
                                on_off_notificaciones_envio_correo('Empleado - Notificacion compaguia On',tarea_id)
                            elif tipo_workflow==2:
                                #print('OFF')
                                on_off_notificaciones_envio_correo('Empleado - Notificacion compaguia Off',tarea_id)
                            
                            username_compa_guia= User.objects.filter(id=compa_guia).values('username')[0]
                            username_compa_guia = username_compa_guia['username']
                            compa_guia= Funcional_empleado.objects.filter(codigo=username_compa_guia).values('correo_empresarial')[0]
                            correo_compa_guia= compa_guia['correo_empresarial']
                            if correo_compa_guia:
                                from_email_compa_guia = settings.EMAIL_HOST_USER
                                try:
                                    msg_compa_guia = EmailMultiAlternatives(asunto, mensaje, from_email_compa_guia, [correo_compa_guia])
                                    msg_compa_guia.send()
                                    #print('CORREO ENVIADO CON EXITO')
                                except BadHeaderError:
                                    return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
                                return Response({"asunto": asunto ,"mensaje":mensaje},status=status.HTTP_200_OK) 
                            else:
                                return Response({"mensaje":"el compañero guia no tiene correo empresarial registrado"},status= status.HTTP_404_NOT_FOUND)
                        else:
                            return Response({"mensaje":"No existen variables cargadas para esta notificacion"},status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({"mensaje":"No existe una configuracion de correo para esta notificacion"},status=status.HTTP_400_BAD_REQUEST)
                    
            elif tipo_mensaje == 'Jefe - Retraso en Tareas':
                #print ('Jefe - Retraso en Tareas')
                validacion_jefe=on_off_bording_tarea.objects.filter(id=tarea_id,fecha_fin__lt=datetime.now().date(),estado=False).count()
                
                if validacion_jefe==0:
                    return Response({"mensaje":"Tarea a tiempo o tarea ya realizada"},status=status.HTTP_400_BAD_REQUEST)
                
                workflow=on_off_bording_tarea.objects.filter(id=tarea_id).values('bloque__workflow__empleado__id','compa_guia')
                empleado= workflow[0]['bloque__workflow__empleado__id']
                cod_empleado= User.objects.filter(id=empleado).values('username')
                codigo_empleado= cod_empleado[0]['username']
                #print(empleado)
                jefe_empleado=Funcional_empleado.objects.filter(codigo=codigo_empleado).values('unidad_organizativa__Dirigido_por')
                if jefe_empleado:
                    jefe_codigo=jefe_empleado[0]['unidad_organizativa__Dirigido_por']
                    #print(jefe_codigo)
                    configuracion_correo = nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') if nucleo_configuracion_correos.objects.filter(tipo_mensaje__nombre=tipo_mensaje,tipo_mensaje__modulo__nombre=modulo,tipo_mensaje__modulo__activo=True).values('asunto','mensaje') else None
                    if configuracion_correo:
                        asunto=configuracion_correo[0]['asunto']
                        mensaje=configuracion_correo[0]['mensaje']
                        #print('MENSAJE SIN SETEAR',mensaje)
                        variables_envio_correo= nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) if nucleo_variables_envio_correos.objects.filter (tipo_mensaje__nombre=tipo_mensaje) else None
                        if variables_envio_correo:
                            for vec in variables_envio_correo:
                                variable= vec.variable
                                app= vec.app
                                modelos= vec.modelos
                                valores= vec.valores
                                modelo_tb= apps.get_model(app,modelos)
                                valor_a_sustituir=modelo_tb.objects.filter(bloque__workflow__empleado__id=empleado,id=tarea_id).values(valores)[0]
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir[valores]
                                    #texto_json=texto_json.replace('@fecha',fecha_str)
                                    mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                                    asunto= asunto.replace(variable,valor_a_sustituir_str)
                                    #print ('MENSAJES CON CAMBIOS',mensaje)
                            jefe_emp= Funcional_empleado.objects.filter(codigo=jefe_codigo).values('correo_empresarial')
                            if jefe_emp:
                                correo_jefe= jefe_emp[0]['correo_empresarial']
                                if correo_jefe:
                                    from_email_jefe = settings.EMAIL_HOST_USER
                                    try:
                                        msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_jefe])
                                        msg_jefe.send()
                                        #print('CORREO ENVIADO CON EXITO')
                                    except BadHeaderError:
                                        return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
                                    return Response({"asunto": asunto ,"mensaje":mensaje},status=status.HTTP_200_OK) 
                                else:
                                    return Response({"mensaje":"el jefe no tiene correo empresarial registrado"},status= status.HTTP_404_NOT_FOUND)
                            else:
                                return Response({"mensaje":"el jefe no existe"},status= status.HTTP_404_NOT_FOUND)

                           
                        else:
                            return Response({"mensaje":"No existen variables cargadas para esta notificacion"},status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response({"mensaje":"No existe una configuracion de correo para esta notificacion"},status=status.HTTP_400_BAD_REQUEST)
                else:
                     return Response({"mensaje":"no hay un jefe asignado a la unidad organizativa del empleado"},status=status.HTTP_400_BAD_REQUEST)  
            else:
                return Response({"mensaje":"La tarea no cumple con los requerimientos para ser enviado un correo"},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"mensaje":"No hemos recibido los valores completos"},status= status.HTTP_404_NOT_FOUND)


class On_off_bording_estadoViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    # queryset = on_off_bording_bienvenida.objects.all()
    # serializer_class = on_off_bording_bienvenidaserializer
    def get(self,request):
        get =  on_off_bording_tarea.objects.all().values('id','texto_json')
        serializer = on_off_bording_bienvenidaserializer(get,many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    def post (self,request):

        existe= on_off_bording_tarea.objects.filter(id=request.data['tarea']) if on_off_bording_tarea.objects.filter(id=request.data['tarea']) else None
        if existe == None:
            
            return Response ({"mensaje":"No existe la tarea enviada"},status=status.HTTP_400_BAD_REQUEST)
        else:
            tarea=existe[0]
            if tarea.evaluable == True and tarea.subir_archivo == True:
                if tarea.calificacion >= 80 and tarea.archivos_gestor != None:
                    tarea.estado=True
                    tarea.save()
                    tipo_workflow= on_off_bording_tarea.objects.filter(id=tarea.id).values('bloque__workflow__tipo_workflow')[0]
                    tipo_workflow=tipo_workflow['bloque__workflow__tipo_workflow']
                    if tipo_workflow==1:
                        on_off_notificaciones_envio_correo('Empleado - Fin Actividad On',tarea.id)
                        on_off_notificaciones_envio_correo('Jefe Inmediato - Fin Actividad On',tarea.id)
                    if tipo_workflow==2:
                        on_off_notificaciones_envio_correo('Jefe - Fin Actividad Off',tarea.id)
                    
                else:
                    return Response ({"mensaje":"calificacion insuficiente o archivo a cargar vacio"},status=status.HTTP_400_BAD_REQUEST)

            elif tarea.evaluable == True:
                if tarea.calificacion >= 80:
                    tarea.estado=True
                    tarea.save()
                    tipo_workflow= on_off_bording_tarea.objects.filter(id=tarea.id).values('bloque__workflow__tipo_workflow')[0]
                    tipo_workflow=tipo_workflow['bloque__workflow__tipo_workflow']
                    if tipo_workflow==1:
                        on_off_notificaciones_envio_correo('Empleado - Fin Actividad On',tarea.id)
                        on_off_notificaciones_envio_correo('Jefe Inmediato - Fin Actividad On',tarea.id)
                    if tipo_workflow==2:
                        on_off_notificaciones_envio_correo('Jefe - Fin Actividad Off',tarea.id)

                else:
                    return Response ({"mensaje":"calificacion insuficiente"},status=status.HTTP_400_BAD_REQUEST)

            elif tarea.subir_archivo==True:
                if tarea.archivos_gestor!=None:
                    tarea.estado=True
                    tarea.save()
                    tipo_workflow= on_off_bording_tarea.objects.filter(id=tarea.id).values('bloque__workflow__tipo_workflow')[0]
                    tipo_workflow=tipo_workflow['bloque__workflow__tipo_workflow']
                    if tipo_workflow==1:
                        on_off_notificaciones_envio_correo('Empleado - Fin Actividad On',tarea.id)
                        on_off_notificaciones_envio_correo('Jefe Inmediato - Fin Actividad On',tarea.id)
                    if tipo_workflow==2:
                        on_off_notificaciones_envio_correo('Jefe - Fin Actividad Off',tarea.id)


            elif tarea.evaluable == False:
                tarea.estado=True
                tarea.save()
                tipo_workflow= on_off_bording_tarea.objects.filter(id=tarea.id).values('bloque__workflow__tipo_workflow')[0]
                tipo_workflow=tipo_workflow['bloque__workflow__tipo_workflow']
                if tipo_workflow==1:
                    on_off_notificaciones_envio_correo('Empleado - Fin Actividad On',tarea.id)
                    on_off_notificaciones_envio_correo('Jefe Inmediato - Fin Actividad On',tarea.id)
                if tipo_workflow==2:
                    on_off_notificaciones_envio_correo('Jefe - Fin Actividad Off',tarea.id)
            
            tareas= on_off_bording_tarea.objects.filter(bloque=tarea.bloque.id).count() if on_off_bording_tarea.objects.filter(bloque=tarea.bloque.id) else 0
            tareas_terminadas= on_off_bording_tarea.objects.filter(bloque=tarea.bloque.id,estado=True).count() if on_off_bording_tarea.objects.filter(bloque=tarea.bloque.id,estado=True) else 0
            if tareas == tareas_terminadas:
                on_off_bording_bloque.objects.filter(id=tarea.bloque.id).update(estado=True)
            
            bloques_total= on_off_bording_bloque.objects.filter(workflow=tarea.bloque.workflow.id).count() if on_off_bording_bloque.objects.filter(workflow=tarea.bloque.workflow.id) else 0
            bloques_terminados= on_off_bording_bloque.objects.filter(workflow=tarea.bloque.workflow.id,estado=True).count() if on_off_bording_bloque.objects.filter(workflow=tarea.bloque.workflow.id,estado=True) else 0
            if bloques_total==bloques_terminados:
                on_off_bording_workflow.objects.filter(id=tarea.bloque.workflow.id).update(estado=True)
                if tarea.bloque.workflow.tipo_workflow==1:
                    on_off_notificaciones_envio_correo('Responsable - Fin On',tarea.bloque.workflow.id)
                    on_off_notificaciones_envio_correo('Empleado - Fin On',tarea.bloque.workflow.id)
                    on_off_notificaciones_envio_correo('Jefe Inmediato - Fin On',tarea.bloque.workflow.id)
                elif tarea.bloque.workflow.tipo_workflow==2:
                    on_off_notificaciones_envio_correo('Jefe Inmediato - Fin Off',tarea.bloque.workflow.id)
                    on_off_notificaciones_envio_correo('Responsable - Fin Off',tarea.bloque.workflow.id)
            return Response ({"mensaje":"Operacion Exitosa"},status= status.HTTP_200_OK)

#prueba
class On_off_bording_monitorViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    # queryset = on_off_bording_bienvenida.objects.all()
    # serializer_class = on_off_bording_bienvenidaserializer
    
    def get(self,request):
        tipo_wf=0
        filter=''
        tipo_busqueda=''

        if self.request.query_params.get('tipo_workflow'):
            tipo_wf = json.loads(self.request.query_params.get('tipo_workflow'))
            #tipo_wf = int(self.request.query_params.get('tipo_workflow'))
        else:
            return Response({"mensaje":"Falta parámetros de tipo workflow"},status= status.HTTP_404_NOT_FOUND)
        
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        # if request.data['tipo_workflow']:
        #     tipo_wf= request.data['tipo_workflow']
        # else:
        #     return Response({"mensaje":"Falta parámetros de tipo workflow"},status= status.HTTP_404_NOT_FOUND)

        #request.data['tarea']
        usuario = request.user
        username =usuario.username
        username = username.zfill(8)
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        #print (usuario)
        #print (grupos)
        if 'jefe' in grupos:
            #print('jefe')
            empleados = Funcional_empleado.objects.filter(unidad_organizativa__Dirigido_por=username).values('codigo')
            lista_codigos_empleados=[]
            for x in empleados:
                lista_codigos_empleados.append(x['codigo'])
            if lista_codigos_empleados:
                if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))

                    if filter!='' and tipo_busqueda!='':
                        filter_kwargs={}
                        if tipo_busqueda:
                            if tipo_busqueda =='descripcion_wf':
                                filter_kwargs['descripcion__icontains'] = filter
                            if tipo_busqueda == 'nombre_wf':
                                filter_kwargs['nombre__icontains'] = filter
                            if tipo_busqueda == 'codigo_empleado':
                                filter_kwargs['empleado__username__icontains'] = filter
                            if tipo_busqueda == 'nombre_empleado':
                                filter_kwargs['empleado__first_name__icontains'] = filter
                        

                        filter_kwargs['empleado__username__in'] = lista_codigos_empleados
                        filter_kwargs['tipo_workflow__in'] = tipo_wf
                        #print (filter_kwargs)
                        resultado = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').order_by('id')[offset:offset+limit]
                        conteo = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)    
                        
                    else:
                        resultado = on_off_bording_workflow.objects.filter(empleado__username__in=lista_codigos_empleados,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').order_by('id')[offset:offset+limit]
                        conteo = on_off_bording_workflow.objects.filter(empleado__username__in=lista_codigos_empleados,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                else:
                    if filter!='' and tipo_busqueda!='':
                        filter_kwargs={}
                        if tipo_busqueda:
                            if tipo_busqueda =='descripcion_wf':
                                filter_kwargs['descripcion__icontains'] = filter
                            if tipo_busqueda == 'nombre_wf':
                                filter_kwargs['nombre__icontains'] = filter
                            if tipo_busqueda == 'codigo_empleado':
                                filter_kwargs['empleado__username__icontains'] = filter
                            if tipo_busqueda == 'nombre_empleado':
                                filter_kwargs['empleado__first_name__icontains'] = filter
                            
                        filter_kwargs['empleado__username__in'] = lista_codigos_empleados
                        filter_kwargs['tipo_workflow__in'] = tipo_wf
                        resultado = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')
                        conteo = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                    else:
                        resultado = on_off_bording_workflow.objects.filter(empleado__username__in=lista_codigos_empleados,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')
                        conteo = on_off_bording_workflow.objects.filter(empleado__username__in=lista_codigos_empleados,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
        elif 'Responsable_OnBoarding' in grupos and 'Responsable_OffBoarding' in grupos:
            if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                offset=int(self.request.query_params.get('offset'))
                limit=int(self.request.query_params.get('limit'))

                if filter!='' and tipo_busqueda!='':
                        filter_kwargs={}
                        if tipo_busqueda:
                            if tipo_busqueda =='descripcion_wf':
                                filter_kwargs['descripcion__icontains'] = filter
                            if tipo_busqueda == 'nombre_wf':
                                filter_kwargs['nombre__icontains'] = filter
                            if tipo_busqueda == 'codigo_empleado':
                                filter_kwargs['empleado__username__icontains'] = filter
                            if tipo_busqueda == 'nombre_empleado':
                                filter_kwargs['empleado__first_name__icontains'] = filter
                        

                        filter_kwargs['responsable__id'] = usuario.id
                        filter_kwargs['tipo_workflow__in'] = tipo_wf
                        resultado = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')[offset:offset+limit]
                        conteo = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                else:
                    resultado = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')[offset:offset+limit]
                    conteo = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                    return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
            else:
                if filter!='' and tipo_busqueda!='':
                    filter_kwargs={}
                    if tipo_busqueda:
                        if tipo_busqueda =='descripcion_wf':
                            filter_kwargs['descripcion__icontains'] = filter
                        if tipo_busqueda == 'nombre_wf':
                            filter_kwargs['nombre__icontains'] = filter
                        if tipo_busqueda == 'codigo_empleado':
                            filter_kwargs['empleado__username__icontains'] = filter
                        if tipo_busqueda == 'nombre_empleado':
                            filter_kwargs['empleado__first_name__icontains'] = filter
                    

                    filter_kwargs['responsable__id'] = usuario.id
                    filter_kwargs['tipo_workflow__in'] = tipo_wf
                    resultado = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')
                    conteo = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                    return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                else:
                    resultado = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')
                    conteo = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                    return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
        elif 'Responsable_OnBoarding' in grupos:
            if 1 in tipo_wf:
                if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))

                    if filter!='' and tipo_busqueda!='':
                            filter_kwargs={}
                            if tipo_busqueda:
                                if tipo_busqueda =='descripcion_wf':
                                    filter_kwargs['descripcion__icontains'] = filter
                                if tipo_busqueda == 'nombre_wf':
                                    filter_kwargs['nombre__icontains'] = filter
                                if tipo_busqueda == 'codigo_empleado':
                                    filter_kwargs['empleado__username__icontains'] = filter
                                if tipo_busqueda == 'nombre_empleado':
                                    filter_kwargs['empleado__first_name__icontains'] = filter
                            

                            filter_kwargs['responsable__id'] = usuario.id
                            filter_kwargs['tipo_workflow__in'] = tipo_wf
                            resultado = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')[offset:offset+limit]
                            conteo = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                            return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                    else:
                        resultado = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')[offset:offset+limit]
                        conteo = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                else:
                    if filter!='' and tipo_busqueda!='':
                        filter_kwargs={}
                        if tipo_busqueda:
                            if tipo_busqueda =='descripcion_wf':
                                filter_kwargs['descripcion__icontains'] = filter
                            if tipo_busqueda == 'nombre_wf':
                                filter_kwargs['nombre__icontains'] = filter
                            if tipo_busqueda == 'codigo_empleado':
                                filter_kwargs['empleado__username__icontains'] = filter
                            if tipo_busqueda == 'nombre_empleado':
                                filter_kwargs['empleado__first_name__icontains'] = filter
                        

                        filter_kwargs['responsable__id'] = usuario.id
                        filter_kwargs['tipo_workflow__in'] = tipo_wf
                        resultado = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')
                        conteo = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                    else:
                        resultado = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')
                        conteo = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"su perfil no puede visualizar los OnBoarding"},status=status.HTTP_200_OK)
        elif 'Responsable_OffBoarding' in grupos:
            if 2 in tipo_wf:
                if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
                    offset=int(self.request.query_params.get('offset'))
                    limit=int(self.request.query_params.get('limit'))

                    if filter!='' and tipo_busqueda!='':
                            filter_kwargs={}
                            if tipo_busqueda:
                                if tipo_busqueda =='descripcion_wf':
                                    filter_kwargs['descripcion__icontains'] = filter
                                if tipo_busqueda == 'nombre_wf':
                                    filter_kwargs['nombre__icontains'] = filter
                                if tipo_busqueda == 'codigo_empleado':
                                    filter_kwargs['empleado__username__icontains'] = filter
                                if tipo_busqueda == 'nombre_empleado':
                                    filter_kwargs['empleado__first_name__icontains'] = filter
                            

                            filter_kwargs['responsable__id'] = usuario.id
                            filter_kwargs['tipo_workflow__in'] = tipo_wf
                            resultado = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')[offset:offset+limit]
                            conteo = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                            return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                    else:
                        resultado = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')[offset:offset+limit]
                        conteo = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                else:
                    if filter!='' and tipo_busqueda!='':
                        filter_kwargs={}
                        if tipo_busqueda:
                            if tipo_busqueda =='descripcion_wf':
                                filter_kwargs['descripcion__icontains'] = filter
                            if tipo_busqueda == 'nombre_wf':
                                filter_kwargs['nombre__icontains'] = filter
                            if tipo_busqueda == 'codigo_empleado':
                                filter_kwargs['empleado__username__icontains'] = filter
                            if tipo_busqueda == 'nombre_empleado':
                                filter_kwargs['empleado__first_name__icontains'] = filter
                        

                        filter_kwargs['responsable__id'] = usuario.id
                        filter_kwargs['tipo_workflow__in'] = tipo_wf
                        resultado = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')
                        conteo = on_off_bording_workflow.objects.filter(**filter_kwargs).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
                    else:
                        resultado = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje')
                        conteo = on_off_bording_workflow.objects.filter(responsable__id=usuario.id,tipo_workflow__in=tipo_wf).annotate(num_ok=Count(Case(When(on_off_bording_bloque__on_off_bording_tarea__estado=True, then=1),output_field=IntegerField()))).annotate(num_fail=Count('id')).annotate(num_bloques=Count('on_off_bording_bloque__id',distinct=True)).annotate(porcentaje=(F('num_ok')*100/F('num_fail'))).values('id','descripcion','nombre','fecha_inicio','fecha_fin','estado','empleado_id','empleado__first_name','empleado__last_name','empleado__username','responsable_id','responsable__username','responsable__first_name','responsable__last_name','num_ok','num_fail','num_bloques','porcentaje').count()
                        return Response ({"mensaje":resultado,"count":conteo},status= status.HTTP_200_OK)
            else:
                return Response({"mensaje":"su perfil no puede visualizar los OffBoarding"},status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"no entra en los grupos para visualizar"},status=status.HTTP_200_OK)
    
        #return Response ({"mensaje":"ejemplo"},status= status.HTTP_200_OK)
        



class On_off_bording_posicionViewSet(APIView):
    authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    # queryset = on_off_bording_bienvenida.objects.all()
    # serializer_class = on_off_bording_bienvenidaserializer
    
    def post (self,request):
        primero=request.data['primero']
        arreglo=[]
        conteo=0

        #aqui empieza        
        for x in primero:
            tarea=on_off_bording_tarea_plantilla.objects.get(id=x['id'])
            if  x['posicion'] != tarea.posicion:
                tarea2 = on_off_bording_tarea_plantilla.objects.get(posicion=x['posicion'],bloque=tarea.bloque.id)
                pt1_fecha_fin = tarea.fecha_fin 
                pt1_fecha_inicio = tarea.fecha_inicio 
                pt1_posicion = tarea.posicion
                tarea.fecha_inicio=tarea2.fecha_inicio
                tarea.fecha_fin=tarea2.fecha_fin
                tarea.posicion=tarea2.posicion
                tarea.save()

                tarea2.fecha_inicio=pt1_fecha_inicio
                tarea2.fecha_fin=pt1_fecha_fin
                tarea2.posicion=pt1_posicion
                tarea2.save()



        # primer_tarea =  on_off_bording_tarea_plantilla.objects.get(id=primero)
        # segunda_tarea =  on_off_bording_tarea_plantilla.objects.get(id=segundo)
        # pt1_fecha_inicio = primer_tarea.fecha_inicio
        # pt1_fecha_fin = primer_tarea.fecha_fin 
        # pt1_posicion = primer_tarea.posicion
        # on_off_bording_tarea_plantilla.objects.filter(id=primero).update(fecha_inicio=segunda_tarea.fecha_inicio,fecha_fin=segunda_tarea.fecha_fin,posicion=segunda_tarea.posicion)
        # on_off_bording_tarea_plantilla.objects.filter(id=segundo).update(fecha_inicio=pt1_fecha_inicio,fecha_fin=pt1_fecha_fin,posicion=pt1_posicion)
    
        return Response ({"mensaje":"Proceso exitoso"},status= status.HTTP_200_OK)


class On_off_boarding_Control_FechasViewSet(APIView):
    authentication_classes=[TokenAuthentication]

    def post(self,request):
        tarea_id = request.data['tarea']
        if not on_off_bording_tarea_plantilla.objects.filter(id=tarea_id):
            return Response ({"mensaje":"la tarea no existe"},status=status.HTTP_400_BAD_REQUEST)
        tarea =  on_off_bording_tarea_plantilla.objects.get(id=tarea_id)
        bloque = on_off_bording_bloque_plantilla.objects.get(id=tarea.bloque.id)
        workflow = on_off_bording_workflow_plantilla.objects.get(id=bloque.workflow.id)
        fecha_inicio=on_off_bording_tarea_plantilla.objects.filter(bloque=bloque.id).aggregate(Min('fecha_inicio'))['fecha_inicio__min']
        fecha_fin=on_off_bording_tarea_plantilla.objects.filter(bloque=bloque.id).aggregate(Max('fecha_fin'))['fecha_fin__max']
       #print(fecha_inicio)
       #print(fecha_fin)
        bloque.fecha_inicio=fecha_inicio
        bloque.fecha_fin=fecha_fin
        bloque.save()
        #on_off_bording_bloque_plantilla.objects.filter(id=tarea.bloque.id).update(fecha_fin=fecha_fin,fecha_inicio=fecha_inicio)

        fecha_inicio_bloque=on_off_bording_bloque_plantilla.objects.filter(workflow=workflow.id).aggregate(Min('fecha_inicio'))['fecha_inicio__min']
        fecha_fin_bloque=on_off_bording_bloque_plantilla.objects.filter(workflow=workflow.id).aggregate(Max('fecha_fin'))['fecha_fin__max']

        workflow.fecha_inicio=fecha_inicio_bloque
        workflow.fecha_fin=fecha_fin_bloque
        workflow.save()
        return Response ({"mensaje":"Proceso exitoso"},status= status.HTTP_200_OK)


class On_off_boarding_workflow_Control_FechasViewSet(APIView):
    authentication_classes=[TokenAuthentication]

    def post(self,request):
        tarea_id = request.data['tarea']
        if not on_off_bording_tarea.objects.filter(id=tarea_id):
            return Response ({"mensaje":"la tarea no existe"},status=status.HTTP_400_BAD_REQUEST)
        tarea =  on_off_bording_tarea.objects.get(id=tarea_id)
        bloque = on_off_bording_bloque.objects.get(id=tarea.bloque.id)
        workflow = on_off_bording_workflow.objects.get(id=bloque.workflow.id)
        fecha_inicio=on_off_bording_tarea.objects.filter(bloque=bloque.id).aggregate(Min('fecha_inicio'))['fecha_inicio__min']
        fecha_fin=on_off_bording_tarea.objects.filter(bloque=bloque.id).aggregate(Max('fecha_fin'))['fecha_fin__max']
       #print(fecha_inicio)
       #print(fecha_fin)
        bloque.fecha_inicio=fecha_inicio
        bloque.fecha_fin=fecha_fin
        bloque.save()
        #on_off_bording_bloque_plantilla.objects.filter(id=tarea.bloque.id).update(fecha_fin=fecha_fin,fecha_inicio=fecha_inicio)

        fecha_inicio_bloque=on_off_bording_bloque.objects.filter(workflow=workflow.id).aggregate(Min('fecha_inicio'))['fecha_inicio__min']
        fecha_fin_bloque=on_off_bording_bloque.objects.filter(workflow=workflow.id).aggregate(Max('fecha_fin'))['fecha_fin__max']

        workflow.fecha_inicio=fecha_inicio_bloque
        workflow.fecha_fin=fecha_fin_bloque
        workflow.save()
        return Response ({"mensaje":"Proceso exitoso"},status= status.HTTP_200_OK)

class On_off_boarding_paso_actual(APIView):
    authentication_classes=[TokenAuthentication]

    def post(self,request):
        tarea_id = request.data['tarea']

        return Response ({"mensaje":"Proceso exitoso"},status= status.HTTP_200_OK)



class On_off_bording_mostrar_bienvenida(APIView):
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[DjangoModelPermissions]
    def get(self,request):
        username=''
        workflow_id=0
        existe_wf=0
        if self.request.query_params.get('username'):
            username = self.request.query_params.get('username')
        else:
            return Response({"mensaje":"Falta parámetros de username"},status= status.HTTP_404_NOT_FOUND)

        if self.request.query_params.get('workflow_id'):
            workflow_id = self.request.query_params.get('workflow_id')
        else:
            return Response({"mensaje":"Falta parámetros de workflow_id"},status= status.HTTP_404_NOT_FOUND)

        existe_wf=on_off_bording_workflow.objects.filter(empleado__username=username,tipo_workflow=1,id=workflow_id,estado=False).count()
        if existe_wf==0:
            mostrar=False
            return Response ({'mostrar':mostrar},status= status.HTTP_404_NOT_FOUND)
        else:
            existe_false=on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username=username,estado=True,bloque__workflow__id=workflow_id) if on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username=username,estado=True,bloque__workflow__id=workflow_id) else None
            if existe_false:
                mostrar= False
                return Response ({'mostrar':mostrar},status= status.HTTP_404_NOT_FOUND)
            else:
                mostrar=True
                return Response ({'mostrar':mostrar},status= status.HTTP_200_OK)

class On_off_bording_navegacion(APIView):
    def post(self,request):
        if 'workflow' in request.data:
            workflow=request.data['workflow']
            bloque_actual=None
            bloques_activos=on_off_bording_bloque.objects.filter(estado=True,workflow=workflow).order_by('posicion')
            bloques_inactivos=on_off_bording_bloque.objects.filter(estado=False,workflow=workflow).order_by('posicion')
            if bloques_activos.count()>0:
                bloques_resultado=on_off_bording_bloque.objects.filter(estado=True,workflow=workflow).order_by('-posicion')
                bloque_actual=bloques_resultado[0]
                posicion_actual=bloque_actual.posicion + 1 
                bloque_actual=on_off_bording_bloque.objects.filter(estado=False,posicion=posicion_actual,workflow=workflow).order_by('-posicion')[0]
            elif bloques_activos.count()==0:
                bloque_actual=bloques_inactivos[0]

            posicion_anterior = bloque_actual.posicion -1
            posicion_siguiente = bloque_actual.posicion + 1
            bloque_anterior=on_off_bording_bloque.objects.filter(posicion=posicion_anterior,workflow=workflow)[0] if on_off_bording_bloque.objects.filter(posicion=posicion_anterior,workflow=workflow) else None
            bloque_siguiente=on_off_bording_bloque.objects.filter(posicion=posicion_siguiente,workflow=workflow)[0] if on_off_bording_bloque.objects.filter(posicion=posicion_siguiente,workflow=workflow) else None
            
            b_actual=on_off_bording_bloqueserializer(bloque_actual).data
            b_anterior=on_off_bording_bloqueserializer(bloque_anterior).data if bloque_anterior !=None else None
            b_siguiente=on_off_bording_bloqueserializer(bloque_siguiente).data if bloque_siguiente!=None else None
            return Response ({'bloque_actual':b_actual,'bloque_anterior':b_anterior,'bloque_siguiente':b_siguiente},status= status.HTTP_200_OK)
        else:
            return Response ({'mensaje':'Debe enviar el parametro workflow'},status= status.HTTP_404_NOT_FOUND)
        return Response (status= status.HTTP_200_OK)

#todo para dasboard onbording-----------------------------------------------------
class On_off_bording_Dashboard_jefe_responsable(APIView):
    authentication_classes = [TokenAuthentication]
    #permission_classes = [DjangoModelPermissions]
    def get(self,request):
        usuario = request.user
        grupos = list(usuario.groups.all().values_list('name',flat=True))
        user_id=usuario.id
        username =usuario.username
        username = username.zfill(8)
        fecha=''
        monitor_WF={}
        workflow_x_mes_al_año=[]
        labels=[]
        dataset=[]

        tipo_workflow=0
        if self.request.query_params.get('fecha'):
            fecha=self.request.query_params.get('fecha')
        else:
            return Response({"mensaje":"Faltan parámetros para el filtro"},status= status.HTTP_404_NOT_FOUND)

        if self.request.query_params.get('tipo_workflow'):
            tipo_workflow=self.request.query_params.get('tipo_workflow')
        else:
            return Response({"mensaje":"Faltan parámetros para el filtro"},status= status.HTTP_404_NOT_FOUND)
        
        tipo_workflow=int(tipo_workflow)
        fecha= datetime.strptime(fecha,"%Y-%m-%d")
        fecha=fecha.date()
        ff=On_off_bording_agregar_meses(fecha,1)
        lista_fecha_fin=ff- timedelta(days=1)
        lista_fecha_inicio= On_off_bording_agregar_meses(fecha,-11) #-11 porque el 12 es en el que esta
        cantidad_meses = On_off_bording_cantidad_meses_entre_fechas(datetime.strptime(str(lista_fecha_inicio),"%Y-%m-%d"),datetime.strptime(str(lista_fecha_fin),"%Y-%m-%d"))+1
        
        listas=On_off_bording_obtener_entre_mes(str(lista_fecha_inicio),str(lista_fecha_fin))
        
        objetoxmes=[]
        
        data_finalizado=[]
        data_atrazado=[]
        data_pendiente=[]
        mesfinalizado=[]
        mesatrazado=[]
        mespendiente=[]
        finalizado=0
        atrazado=0
        pendiente=0
        #x=x
        #para monitor WF
        hoy=datetime.now().date() 

        # actual_fecha_fin=On_off_bording_agregar_meses(hoy,12)
        # actual_fecha_fin=actual_fecha_fin.replace(month=1,day=1)
        # actual_fecha_fin=actual_fecha_fin - timedelta(days=1)
        actual_fecha_fin= hoy
        
        actual_fecha_inicio=actual_fecha_fin.replace(month=1,day=1)
        
        atras_fecha_fin = actual_fecha_inicio - timedelta(days=1)
        
        atras_fecha_inicio = atras_fecha_fin.replace(month=1,day=1)
        
        if 'jefe' in grupos:
            empleados = Funcional_empleado.objects.filter(unidad_organizativa__Dirigido_por=username).values('codigo')
            lista_codigos_empleados=[]
            for x in empleados:
                lista_codigos_empleados.append(x['codigo'])
            if lista_codigos_empleados:    
                #activos
                activos = on_off_bording_workflow.objects.filter(empleado__username__in=lista_codigos_empleados,estado=False,tipo_workflow=tipo_workflow,fecha_inicio__gte=actual_fecha_inicio).count()
                # activos = on_off_bording_workflow.objects.filter(empleado__username__in=lista_codigos_empleados,estado=False,tipo_workflow=tipo_workflow,fecha_fin__range=[actual_fecha_inicio,actual_fecha_fin]).count()
                #porcentaje_activos_vrs_año_pasado

                atras_activos = on_off_bording_workflow.objects.filter(empleado__username__in=lista_codigos_empleados,estado=False,tipo_workflow=tipo_workflow,fecha_fin__range=[atras_fecha_inicio,atras_fecha_fin]).count()
                if atras_activos!=0:
                    porcentaje_activos_vrs_anio_pasado=(activos/atras_activos)*100
                else:
                    porcentaje_activos_vrs_anio_pasado=0
                #inducciones_actuales_total
                inducciones_actuales_total = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,bloque__workflow__estado=False).count()
                # inducciones_actuales_total = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,bloque__workflow__fecha_fin__range=[actual_fecha_inicio,actual_fecha_fin]).count()

                #inducciones_actuales_finalizado
                inducciones_actuales_finalizado = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,estado=True,bloque__workflow__estado=False).count()
                # inducciones_actuales_finalizado = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,estado=True,bloque__workflow__fecha_fin__range=[actual_fecha_inicio,actual_fecha_fin]).count()
                
                #inducciones_actuales_atrasado
                inducciones_actuales_atrasadas = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,estado=False,fecha_fin__lt=datetime.now().date(),bloque__workflow__estado=False).count()
                # inducciones_actuales_atrasadas = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,estado=False,fecha_fin__lt=datetime.now().date(),bloque__workflow__fecha_fin__range=[actual_fecha_inicio,actual_fecha_fin]).count()
                
                #inducciones_actuales_pendiente
                inducciones_actuales_pendiente=inducciones_actuales_total-inducciones_actuales_finalizado-inducciones_actuales_atrasadas
                objeto= {"activos":activos,"porcentaje_activos_vrs_año_pasado":porcentaje_activos_vrs_anio_pasado,"inducciones_actuales_total":inducciones_actuales_total,"inducciones_actuales_finalizado":inducciones_actuales_finalizado,"inducciones_actuales_atrasadas":inducciones_actuales_atrasadas,"inducciones_actuales_pendiente":inducciones_actuales_pendiente}
                monitor_WF=objeto

                for mes in listas:
                    total = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                    finalizado = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,estado=True,bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                    atrazado = on_off_bording_tarea.objects.filter(bloque__workflow__empleado__username__in=lista_codigos_empleados,bloque__workflow__tipo_workflow=tipo_workflow,estado=False,fecha_fin__lt=datetime.now().date(),bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                    pendiente = total-finalizado-atrazado
                    mes_str=''
                    anio=''
                    if mes=='01':
                        mes_str='Enero'
                    elif mes=='02':
                        mes_str='Febrero'
                    elif mes=='03':
                        mes_str='Marzo'
                    elif mes=='04':
                        mes_str='Abril'
                    elif mes=='05':
                        mes_str='Mayo'
                    elif mes=='06':
                        mes_str='Junio'
                    elif mes=='07':
                        mes_str='Julio'
                    elif mes=='08':
                        mes_str='Agosto'
                    elif mes=='09':
                        mes_str='Septiembre'
                    elif mes=='10':
                        mes_str='Octubre'
                    elif mes=='11':
                        mes_str='Noviembre'
                    else:
                        mes_str='Diciembre'

                    anio = str(listas[mes][0])
                    anio = anio[0:4]
                    mesanio = mes_str + '-' + anio
                    objetoxmes.append(mesanio)
                    mesfinalizado.append(finalizado)
                    mesatrazado.append(atrazado)
                    mespendiente.append(pendiente)

                labels=objetoxmes
                data_finalizado=mesfinalizado
                data_atrazado=mesatrazado
                data_pendiente=mespendiente

                datagrande={}
                datadd1={}
                datadd2={}
                datadd3={}
                datadd1={'label':'finalizado','data':data_finalizado}
                datadd2={'label':'atrazados','data':data_atrazado}
                datadd3={'label':'pendiente','data':data_pendiente}
                dataset.append(datadd1)
                dataset.append(datadd2)
                dataset.append(datadd3)


            else:
                return Response({"mensaje":"Sin registro de empleados"},status= status.HTTP_404_NOT_FOUND)
            print('para jefes')
        elif 'Responsable_OnBoarding' in grupos and tipo_workflow==1:

            activos = on_off_bording_workflow.objects.filter(responsable__username=username,estado=False,tipo_workflow=tipo_workflow,fecha_inicio__gte=actual_fecha_inicio).count()
            #porcentaje_activos_vrs_año_pasado
            atras_activos = on_off_bording_workflow.objects.filter(responsable__username=username,estado=False,tipo_workflow=tipo_workflow,fecha_fin__range=[atras_fecha_inicio,atras_fecha_fin]).count()
            if atras_activos!=0:
                porcentaje_activos_vrs_anio_pasado=(activos/atras_activos)*100
            else:
                porcentaje_activos_vrs_anio_pasado=0
            
            #inducciones_actuales_total
            inducciones_actuales_total = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,bloque__workflow__estado=False).count()

            #inducciones_actuales_finalizado
            inducciones_actuales_finalizado = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=True,bloque__workflow__estado=False).count()
            
            #inducciones_actuales_atrasado
            inducciones_actuales_atrasadas = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=False,fecha_fin__lt=datetime.now().date(),bloque__workflow__estado=False).count()

            #inducciones_actuales_pendiente
            inducciones_actuales_pendiente=inducciones_actuales_total-inducciones_actuales_finalizado-inducciones_actuales_atrasadas
            objeto= {"activos":activos,"porcentaje_activos_vrs_año_pasado":porcentaje_activos_vrs_anio_pasado,"inducciones_actuales_total":inducciones_actuales_total,"inducciones_actuales_finalizado":inducciones_actuales_finalizado,"inducciones_actuales_atrasadas":inducciones_actuales_atrasadas,"inducciones_actuales_pendiente":inducciones_actuales_pendiente}
            monitor_WF=objeto
            
            for mes in listas:
                mes_str=''
                anio=''
                total = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                finalizado = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=True,bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                atrazado = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=False,fecha_fin__lt=datetime.now().date(),bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                pendiente = total-finalizado-atrazado
                if mes=='01':
                    mes_str='Enero'                    
                elif mes=='02':
                    mes_str='Febrero'
                elif mes=='03':
                    mes_str='Marzo'
                elif mes=='04':
                    mes_str='Abril'
                elif mes=='05':
                    mes_str='Mayo'
                elif mes=='06':
                    mes_str='Junio'
                elif mes=='07':
                    mes_str='Julio'
                elif mes=='08':
                    mes_str='Agosto'
                elif mes=='09':
                    mes_str='Septiembre'
                elif mes=='10':
                    mes_str='Octubre'
                elif mes=='11':
                    mes_str='Noviembre'
                else:
                    mes_str='Diciembre'

                anio = str(listas[mes][0])
                anio = anio[0:4]
                mesanio = mes_str + '-' + anio
                objetoxmes.append(mesanio)
                mesfinalizado.append(finalizado)
                mesatrazado.append(atrazado)
                mespendiente.append(pendiente)

            labels=objetoxmes
            data_finalizado=mesfinalizado
            data_atrazado=mesatrazado
            data_pendiente=mespendiente

            datagrande={}
            datadd1={}
            datadd2={}
            datadd3={}
            datadd1={'label':'finalizado','data':data_finalizado}
            datadd2={'label':'atrazados','data':data_atrazado}
            datadd3={'label':'pendiente','data':data_pendiente}
            dataset.append(datadd1)
            dataset.append(datadd2)
            dataset.append(datadd3)
        elif 'Responsable_OffBoarding' in grupos and tipo_workflow==2:
            activos = on_off_bording_workflow.objects.filter(responsable__username=username,estado=False,tipo_workflow=tipo_workflow,fecha_inicio__gte=actual_fecha_inicio).count()
            # activos = on_off_bording_workflow.objects.filter(responsable__username=username,estado=False,tipo_workflow=tipo_workflow,fecha_fin__range=[actual_fecha_inicio,actual_fecha_fin]).count()
            #porcentaje_activos_vrs_año_pasado
            atras_activos = on_off_bording_workflow.objects.filter(responsable__username=username,estado=False,tipo_workflow=tipo_workflow,fecha_fin__range=[atras_fecha_inicio,atras_fecha_fin]).count()
            if atras_activos!=0:
                porcentaje_activos_vrs_anio_pasado=(activos/atras_activos)*100
            else:
                porcentaje_activos_vrs_anio_pasado=0
            
            #inducciones_actuales_total
            inducciones_actuales_total = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,bloque__workflow__estado=False).count()
            # inducciones_actuales_total = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,bloque__workflow__fecha_fin__range=[actual_fecha_inicio,actual_fecha_fin]).count()

            #inducciones_actuales_finalizado
            inducciones_actuales_finalizado = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=True,bloque__workflow__estado=False).count()
            # inducciones_actuales_finalizado = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=True,bloque__workflow__fecha_fin__range=[actual_fecha_inicio,actual_fecha_fin]).count()

            #inducciones_actuales_atrasado
            inducciones_actuales_atrasadas = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=False,fecha_fin__lt=datetime.now().date(),bloque__workflow__estado=False).count()
            # inducciones_actuales_atrasadas = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=False,fecha_fin__lt=datetime.now().date(),bloque__workflow__fecha_fin__range=[actual_fecha_inicio,actual_fecha_fin]).count()

            #inducciones_actuales_pendiente
            inducciones_actuales_pendiente=inducciones_actuales_total-inducciones_actuales_finalizado-inducciones_actuales_atrasadas
            objeto= {"activos":activos,"porcentaje_activos_vrs_año_pasado":porcentaje_activos_vrs_anio_pasado,"inducciones_actuales_total":inducciones_actuales_total,"inducciones_actuales_finalizado":inducciones_actuales_finalizado,"inducciones_actuales_atrasadas":inducciones_actuales_atrasadas,"inducciones_actuales_pendiente":inducciones_actuales_pendiente}
            monitor_WF=objeto
            
            for mes in listas:
                mes_str=''
                anio=''
                total = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                finalizado = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=True,bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                atrazado = on_off_bording_tarea.objects.filter(bloque__workflow__responsable__username=username,bloque__workflow__tipo_workflow=tipo_workflow,estado=False,fecha_fin__lt=datetime.now().date(),bloque__workflow__fecha_fin__range=[listas[mes][0],listas[mes][1]]).count()
                pendiente = total-finalizado-atrazado
                if mes=='01':
                    mes_str='Enero'                    
                elif mes=='02':
                    mes_str='Febrero'
                elif mes=='03':
                    mes_str='Marzo'
                elif mes=='04':
                    mes_str='Abril'
                elif mes=='05':
                    mes_str='Mayo'
                elif mes=='06':
                    mes_str='Junio'
                elif mes=='07':
                    mes_str='Julio'
                elif mes=='08':
                    mes_str='Agosto'
                elif mes=='09':
                    mes_str='Septiembre'
                elif mes=='10':
                    mes_str='Octubre'
                elif mes=='11':
                    mes_str='Noviembre'
                else:
                    mes_str='Diciembre'

                anio = str(listas[mes][0])
                anio = anio[0:4]
                mesanio = mes_str + '-' + anio
                objetoxmes.append(mesanio)
                mesfinalizado.append(finalizado)
                mesatrazado.append(atrazado)
                mespendiente.append(pendiente)

            labels=objetoxmes
            data_finalizado=mesfinalizado
            data_atrazado=mesatrazado
            data_pendiente=mespendiente

            datagrande={}
            datadd1={}
            datadd2={}
            datadd3={}
            datadd1={'label':'finalizado','data':data_finalizado}
            datadd2={'label':'atrazados','data':data_atrazado}
            datadd3={'label':'pendiente','data':data_pendiente}
            dataset.append(datadd1)
            dataset.append(datadd2)
            dataset.append(datadd3)
        else:
            print('no esta en ninguno de los dos perfiles')
        
        data={"monitor_WF":monitor_WF,"labels": labels,'dataset':dataset}
        return Response (data,status= status.HTTP_200_OK)

def On_off_bording_agregar_meses(dt,meses):
    mes= dt.month - 1 + meses
    año = dt.year + mes / 12
    año = int(año)
    mes = mes % 12 + 1
    dia = min(dt.day,monthrange(año,mes)[1])
    return dt.replace(year = año,month = mes,day = dia)

def On_off_bording_obtener_entre_mes(fecha_inicio,fecha_fin):
    lista_dias = {}
    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    while fecha_inicio <= fecha_fin:
        # fecha_str = fecha_inicio.strftime("%Y-%m")
        fecha_str = fecha_inicio.strftime("%m")
        lista_dias[fecha_str] = ['%d-%d-01'%(fecha_inicio.year, fecha_inicio.month),'%d-%d-%d'%(fecha_inicio.year, fecha_inicio.month, monthrange(fecha_inicio.year, fecha_inicio.month)[1])]
        fecha_inicio = On_off_bording_agregar_meses(fecha_inicio,1)

    return lista_dias

def On_off_bording_cantidad_meses_entre_fechas(fecha_inicio, fecha_fin):
    delta = 0
    while True:
        mdias = monthrange(fecha_inicio.year, fecha_inicio.month)[1]
        fecha_inicio += timedelta(days=mdias)
        if fecha_inicio <= fecha_fin:
            delta += 1
        else:
            break
    return delta

#------------------------------------------------------------------------------------

def reparar_posiciones_workflow():
    workflow=on_off_bording_workflow.objects.filter().order_by('-fecha_inicio')
    for w in workflow:
        bn=1
        bloque= on_off_bording_bloque.objects.filter(workflow=w.id).order_by('-fecha_inicio')
        for b in bloque:
            b.posicion=bn
            b.save()
            tarea = on_off_bording_tarea.objects.filter(bloque=b.id).order_by('-fecha_inicio')
            tr=1
            for t in tarea:
                t.posicion=tr
                t.save()
                tr=tr+1
            bn=bn + 1            
    return 1
            
class On_off_bording_eliminar_workflow(APIView):
    authentication_classes=[TokenAuthentication]

    def get_object(self,id):
        return on_off_bording_workflow.objects.get(id=id)
        
    def delete(self,request,id):
        try:
            eliminar = self.get_object(id)
        except ObjectDoesNotExist:
            return Response({"mensaje":"No existe un Workflow con ese id"},status=status.HTTP_400_BAD_REQUEST)
        
        tareas= on_off_bording_tarea.objects.filter(bloque__workflow__id=eliminar.id,estado=True).count()
        if tareas == 0:
            eliminar.delete()
            return Response({"mensaje":"Se elimino el Workflow"},status=status.HTTP_200_OK)
        else:
            return Response({"mensaje":"No se puede eliminar el Workflow porque ya tiene al menos una actividad realizada"},status=status.HTTP_400_BAD_REQUEST)


class On_off_bording_workflow_duplicar(APIView):
    authentication_classes=[TokenAuthentication]

    def post(self,request):
        plantilla=request.data['plantilla']
        wfp=on_off_bording_workflow_plantilla.objects.get(id=plantilla) if on_off_bording_workflow_plantilla.objects.filter(id=plantilla) else None
        if wfp==None:
            return Response({"mensaje":"La plantilla seleccionada no existe"},status=status.HTTP_400_BAD_REQUEST)

        copia = on_off_bording_workflow_plantilla.objects.create(descripcion= wfp.descripcion, nombre= wfp.nombre, fecha_inicio= wfp.fecha_inicio, fecha_fin=wfp.fecha_fin, estado=wfp.estado, creador= wfp.creador, tipo_workflow= wfp.tipo_workflow)
        
        bwp= on_off_bording_bloque_plantilla.objects.filter(workflow__id=plantilla) 
        for b in bwp:
            nbwf=on_off_bording_bloque_plantilla.objects.create(descripcion=b.descripcion,nombre=b.nombre,fecha_inicio=b.fecha_inicio,fecha_fin=b.fecha_fin,estado=b.estado,posicion=b.posicion,workflow=copia)
            twfp= on_off_bording_tarea_plantilla.objects.filter(bloque__workflow__id=plantilla,bloque__id=b.id)
            for t in twfp:
                ntwfp=on_off_bording_tarea_plantilla.objects.create(descripcion=t.descripcion,nombre=t.nombre,fecha_inicio=t.fecha_inicio,fecha_fin=t.fecha_fin,evaluable=t.evaluable,calificacion=t.calificacion,posicion=t.posicion,estado=t.estado,archivo_subir=t.archivo_subir,archivo_bajar=t.archivo_bajar,subir_archivo=t.subir_archivo,enlace_evaluacion=t.enlace_evaluacion,bloque=nbwf)


        resultado=on_off_bording_workflow_plantillaserializer(copia).data
        return Response({"mensaje":"Copia realizada con exito","resultado":resultado},status=status.HTTP_200_OK)
    

class On_off_bording_navegacion_anterior(APIView):
    def get(self,request):
         
        if  self.request.query_params.get('bloque'):
            bloque= self.request.query_params.get('bloque')
            bloque_obj=on_off_bording_bloque.objects.get(id=bloque)
            workflow=on_off_bording_workflow.objects.get(id=bloque_obj.workflow.id)
            bloque_recibido=on_off_bording_bloque.objects.get(id=bloque)
            bloque_actual=on_off_bording_bloque.objects.get(posicion=bloque_obj.posicion-1,workflow=bloque_recibido.workflow.id) if on_off_bording_bloque.objects.filter(posicion=bloque_obj.posicion-1,workflow=bloque_recibido.workflow.id) else None
            bloque_siguiente=on_off_bording_bloque.objects.get(posicion=bloque_obj.posicion,workflow=bloque_recibido.workflow.id) if on_off_bording_bloque.objects.filter(posicion=bloque_obj.posicion,workflow=bloque_recibido.workflow.id) else None
            bloque_anterior=on_off_bording_bloque.objects.get(posicion=bloque_obj.posicion-2,workflow=bloque_recibido.workflow.id) if on_off_bording_bloque.objects.filter(posicion=bloque_obj.posicion-2,workflow=bloque_recibido.workflow.id) else None



            return Response ({'bloque_actual':on_off_bording_bloqueserializer(bloque_actual).data,'bloque_anterior':on_off_bording_bloqueserializer(bloque_anterior).data,'bloque_siguiente':on_off_bording_bloqueserializer(bloque_siguiente).data},status= status.HTTP_200_OK)
        else:
            return Response ({'mensaje':'Debe enviar el parametro workflow'},status= status.HTTP_404_NOT_FOUND)
        return Response (status= status.HTTP_200_OK)

def on_off_notificaciones_envio_correo(tipo_mensaje,id_vario):
    modulo='ON/OFF BOARDING'
    print (tipo_mensaje,id_vario)
    if tipo_mensaje=='Jefe Inmediato - Inicio On':
        codigo_jefe=''
        codigo_empleado=''
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('empleado__id')
        empleado= workflow[0]['empleado__id']
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
                    if variable=='@@jefe_nombre':
                        codigo_empleado =  modelo_tb.objects.filter(empleado__id=empleado,id=id_vario).values(valores)[0]
                        if codigo_empleado:
                            codigo_jefe=Funcional_empleado.objects.filter(codigo=codigo_empleado['empleado__username']).values('unidad_organizativa__Dirigido_por')
                            if codigo_jefe:
                                valor_a_sustituir=Funcional_empleado.objects.filter(codigo=codigo_jefe[0]['unidad_organizativa__Dirigido_por']).values('nombre')
                                if valor_a_sustituir:
                                    valor_a_sustituir_str = valor_a_sustituir[0]['nombre']
                                    mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                                    asunto= asunto.replace(variable,valor_a_sustituir_str)
                                else:
                                    valor_a_sustituir_str =''
                                    mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                                    asunto= asunto.replace(variable,valor_a_sustituir_str)

                    else:
                        valor_a_sustituir=modelo_tb.objects.filter(empleado__id=empleado,id=id_vario).values(valores)[0]
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir[valores]
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                        else:
                            valor_a_sustituir_str =''
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                if codigo_jefe:
                    jefe= Funcional_empleado.objects.filter(codigo=codigo_jefe[0]['unidad_organizativa__Dirigido_por']).values('correo_empresarial')[0]
                    correo_jefe=jefe['correo_empresarial']
                    if correo_jefe:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_jefe])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)

    elif tipo_mensaje=='Empleado - Inicio On':
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('empleado__id')
        empleado= workflow[0]['empleado__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(empleado__id=empleado,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_empleado= User.objects.filter(id=empleado).values('username')[0]
                empleado_c=Funcional_empleado.objects.filter(codigo=codigo_empleado['username']).values('correo_empresarial')
                if empleado_c:
                    correo_empleado=empleado_c[0]['correo_empresarial']
                    if correo_empleado:
                        from_email_empleado= settings.EMAIL_HOST_USER
                        try:
                            msg_empleado = EmailMultiAlternatives(asunto, mensaje, from_email_empleado, [correo_empleado])
                            msg_empleado.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Responsable - Inicio Off':
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('responsable__id')
        responsable= workflow[0]['responsable__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(responsable__id=responsable,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_responsable= User.objects.filter(id=responsable).values('username')[0]
                responsable_c=Funcional_empleado.objects.filter(codigo=codigo_responsable['username']).values('correo_empresarial')
                if responsable_c:
                    correo_responsable=responsable_c[0]['correo_empresarial']
                    if correo_responsable:
                        from_email_responsable= settings.EMAIL_HOST_USER
                        try:
                            msg_responsable = EmailMultiAlternatives(asunto, mensaje, from_email_responsable, [correo_responsable])
                            msg_responsable.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Jefe Inmediato - Inicio Off':
        codigo_jefe=''
        codigo_empleado=''
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('empleado__id','empleado__username')
        empleado= workflow[0]['empleado__id']
        codigo_empleado=workflow[0]['empleado__username']
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


                    
                    if codigo_empleado:
                        codigo_jefe=Funcional_empleado.objects.filter(codigo=codigo_empleado).values('unidad_organizativa__Dirigido_por')
                    if variable=='@@fechainicio':
                        valor_a_sustituir=modelo_tb.objects.filter(empleado__id=empleado,id=id_vario).values(valores)[0]
                        print (valor_a_sustituir)
                        if valor_a_sustituir:
                            fecha= valor_a_sustituir[valores]
                            valor_a_sustituir_str=fecha.strftime('%d-%m-%Y')
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                        else:
                            valor_a_sustituir_str =''
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        # fecha=datetime.now().date()
                        # fecha_str= fecha.strftime('%Y/%m/%d')
                        # texto_json=texto_json.replace('@fecha',fecha_str)
                        # texto_json= json.loads(texto_json) 
                        valor_a_sustituir=modelo_tb.objects.filter(empleado__id=empleado,id=id_vario).values(valores)[0]
                        if valor_a_sustituir:
                            valor_a_sustituir_str = valor_a_sustituir[valores]
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                        else:
                            valor_a_sustituir_str =''
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                if codigo_jefe:
                    jefe= Funcional_empleado.objects.filter(codigo=codigo_jefe[0]['unidad_organizativa__Dirigido_por']).values('correo_empresarial')[0]
                    correo_jefe=jefe['correo_empresarial']
                    if correo_jefe:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_jefe])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Responsable - Fin On':
        print (tipo_mensaje)
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('responsable__id')
        responsable= workflow[0]['responsable__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(responsable__id=responsable,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_responsable= User.objects.filter(id=responsable).values('username')[0]
                responsable_c=Funcional_empleado.objects.filter(codigo=codigo_responsable['username']).values('correo_empresarial')
                if responsable_c:
                    correo_responsable=responsable_c[0]['correo_empresarial']
                    if correo_responsable:
                        from_email_responsable= settings.EMAIL_HOST_USER
                        try:
                            msg_responsable = EmailMultiAlternatives(asunto, mensaje, from_email_responsable, [correo_responsable])
                            msg_responsable.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Empleado - Fin On':
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('empleado__id')
        empleado= workflow[0]['empleado__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(empleado__id=empleado,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_empleado= User.objects.filter(id=empleado).values('username')[0]
                empleado_c=Funcional_empleado.objects.filter(codigo=codigo_empleado['username']).values('correo_empresarial')
                if empleado_c:
                    correo_empleado=empleado_c[0]['correo_empresarial']
                    if correo_empleado:
                        from_email_empleado= settings.EMAIL_HOST_USER
                        try:
                            msg_empleado = EmailMultiAlternatives(asunto, mensaje, from_email_empleado, [correo_empleado])
                            msg_empleado.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Jefe Inmediato - Fin Off':
        codigo_jefe=''
        codigo_empleado=''
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('empleado__id','empleado__username')
        empleado= workflow[0]['empleado__id']
        codigo_empleado=workflow[0]['empleado__username']
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
                    if codigo_empleado:
                        codigo_jefe=Funcional_empleado.objects.filter(codigo=codigo_empleado).values('unidad_organizativa__Dirigido_por')
                    valor_a_sustituir=modelo_tb.objects.filter(empleado__id=empleado,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                if codigo_jefe:
                    jefe= Funcional_empleado.objects.filter(codigo=codigo_jefe[0]['unidad_organizativa__Dirigido_por']).values('correo_empresarial')[0]
                    correo_jefe=jefe['correo_empresarial']
                    if correo_jefe:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_jefe])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Responsable - Fin Off':
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('responsable__id')
        responsable= workflow[0]['responsable__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(responsable__id=responsable,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_responsable= User.objects.filter(id=responsable).values('username')[0]
                responsable_c=Funcional_empleado.objects.filter(codigo=codigo_responsable['username']).values('correo_empresarial')
                if responsable_c:
                    correo_responsable=responsable_c[0]['correo_empresarial']
                    if correo_responsable:
                        from_email_responsable= settings.EMAIL_HOST_USER
                        try:
                            msg_responsable = EmailMultiAlternatives(asunto, mensaje, from_email_responsable, [correo_responsable])
                            msg_responsable.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Empleado - Notificacion compaguia On':
        workflow= on_off_bording_tarea.objects.filter(id=id_vario).values('bloque__workflow__empleado__id')
        empleado= workflow[0]['bloque__workflow__empleado__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(bloque__workflow__empleado__id=empleado,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_empleado= User.objects.filter(id=empleado).values('username')[0]
                empleado_c=Funcional_empleado.objects.filter(codigo=codigo_empleado['username']).values('correo_empresarial')
                if empleado_c:
                    correo_empleado=empleado_c[0]['correo_empresarial']
                    if correo_empleado:
                        from_email_empleado= settings.EMAIL_HOST_USER
                        try:
                            msg_empleado = EmailMultiAlternatives(asunto, mensaje, from_email_empleado, [correo_empleado])
                            msg_empleado.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Empleado - Notificacion compaguia Off':
        workflow= on_off_bording_tarea.objects.filter(id=id_vario).values('bloque__workflow__empleado__id')
        empleado= workflow[0]['bloque__workflow__empleado__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(bloque__workflow__empleado__id=empleado,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_empleado= User.objects.filter(id=empleado).values('username')[0]
                empleado_c=Funcional_empleado.objects.filter(codigo=codigo_empleado['username']).values('correo_empresarial')
                if empleado_c:
                    correo_empleado=empleado_c[0]['correo_empresarial']
                    if correo_empleado:
                        from_email_empleado= settings.EMAIL_HOST_USER
                        try:
                            msg_empleado = EmailMultiAlternatives(asunto, mensaje, from_email_empleado, [correo_empleado])
                            msg_empleado.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Empleado - Fin Actividad On':
        workflow= on_off_bording_tarea.objects.filter(id=id_vario).values('bloque__workflow__empleado__id')
        empleado= workflow[0]['bloque__workflow__empleado__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(bloque__workflow__empleado__id=empleado,id=id_vario).values(valores)[0]
                    print(valor_a_sustituir)
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        if valor_a_sustituir_str!=None:
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                        else:
                            valor_a_sustituir_str =''
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_empleado= User.objects.filter(id=empleado).values('username')[0]
                empleado_c=Funcional_empleado.objects.filter(codigo=codigo_empleado['username']).values('correo_empresarial')
                if empleado_c:
                    correo_empleado=empleado_c[0]['correo_empresarial']
                    if correo_empleado:
                        from_email_empleado= settings.EMAIL_HOST_USER
                        try:
                            msg_empleado = EmailMultiAlternatives(asunto, mensaje, from_email_empleado, [correo_empleado])
                            msg_empleado.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Jefe - Fin Actividad Off':
        codigo_jefe=''
        codigo_empleado=''
        workflow= on_off_bording_tarea.objects.filter(id=id_vario).values('bloque__workflow__empleado__id','bloque__workflow__empleado__username')
        empleado= workflow[0]['bloque__workflow__empleado__id']
        codigo_empleado=workflow[0]['bloque__workflow__empleado__username']
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
                    if codigo_empleado:
                        codigo_jefe=Funcional_empleado.objects.filter(codigo=codigo_empleado).values('unidad_organizativa__Dirigido_por')
                    valor_a_sustituir=modelo_tb.objects.filter(bloque__workflow__empleado__id=empleado,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        if valor_a_sustituir_str!=None:
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                        else:
                            valor_a_sustituir_str =''
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                if codigo_jefe:
                    jefe= Funcional_empleado.objects.filter(codigo=codigo_jefe[0]['unidad_organizativa__Dirigido_por']).values('correo_empresarial')[0]
                    correo_jefe=jefe['correo_empresarial']
                    if correo_jefe:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_jefe])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Responsable - Inicio On':
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('responsable__id')
        responsable= workflow[0]['responsable__id']
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
                    valor_a_sustituir=modelo_tb.objects.filter(responsable__id=responsable,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                codigo_responsable= User.objects.filter(id=responsable).values('username')[0]
                responsable_c=Funcional_empleado.objects.filter(codigo=codigo_responsable['username']).values('correo_empresarial')
                if responsable_c:
                    correo_responsable=responsable_c[0]['correo_empresarial']
                    if correo_responsable:
                        from_email_responsable= settings.EMAIL_HOST_USER
                        try:
                            msg_responsable = EmailMultiAlternatives(asunto, mensaje, from_email_responsable, [correo_responsable])
                            msg_responsable.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Jefe Inmediato - Fin On':
        codigo_jefe=''
        codigo_empleado=''
        workflow= on_off_bording_workflow.objects.filter(id=id_vario).values('empleado__id','empleado__username')
        empleado= workflow[0]['empleado__id']
        codigo_empleado=workflow[0]['empleado__username']
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
                    if codigo_empleado:
                        codigo_jefe=Funcional_empleado.objects.filter(codigo=codigo_empleado).values('unidad_organizativa__Dirigido_por')
                    valor_a_sustituir=modelo_tb.objects.filter(empleado__id=empleado,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                if codigo_jefe:
                    jefe= Funcional_empleado.objects.filter(codigo=codigo_jefe[0]['unidad_organizativa__Dirigido_por']).values('correo_empresarial')[0]
                    correo_jefe=jefe['correo_empresarial']
                    if correo_jefe:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_jefe])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)
    elif tipo_mensaje=='Jefe Inmediato - Fin Actividad On':
        codigo_jefe=''
        codigo_empleado=''
        workflow= on_off_bording_tarea.objects.filter(id=id_vario).values('bloque__workflow__empleado__id','bloque__workflow__empleado__username')
        empleado= workflow[0]['bloque__workflow__empleado__id']
        codigo_empleado=workflow[0]['bloque__workflow__empleado__username']
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
                    if codigo_empleado:
                        codigo_jefe=Funcional_empleado.objects.filter(codigo=codigo_empleado).values('unidad_organizativa__Dirigido_por')
                        if codigo_jefe[0]['unidad_organizativa__Dirigido_por']=='00000000':
                            return Response({"mensaje":"El empleado no tiene jefe asignado"},status= status.HTTP_404_NOT_FOUND)
                    valor_a_sustituir=modelo_tb.objects.filter(bloque__workflow__empleado__id=empleado,id=id_vario).values(valores)[0]
                    if valor_a_sustituir:
                        valor_a_sustituir_str = valor_a_sustituir[valores]
                        if valor_a_sustituir_str!=None:
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                        else:
                            valor_a_sustituir_str =''
                            mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                            asunto= asunto.replace(variable,valor_a_sustituir_str)
                    else:
                        valor_a_sustituir_str =''
                        mensaje= mensaje.replace(variable,valor_a_sustituir_str)
                        asunto= asunto.replace(variable,valor_a_sustituir_str)
                
                if codigo_jefe:
                    jefe= Funcional_empleado.objects.filter(codigo=codigo_jefe[0]['unidad_organizativa__Dirigido_por']).values('correo_empresarial')[0]
                    correo_jefe=jefe['correo_empresarial']
                    if correo_jefe:
                        from_email_jefe= settings.EMAIL_HOST_USER
                        try:
                            msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_jefe])
                            msg_jefe.send()
                        except BadHeaderError:
                            return Response({"mensaje":"la cuenta no existe favor verificar"},status= status.HTTP_404_NOT_FOUND)

    return 1