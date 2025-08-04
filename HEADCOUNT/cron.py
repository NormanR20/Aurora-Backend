from django.db.models.functions import ExtractYear

from re import sub
from django.contrib.auth.models import User,Group
from django.http.response import Http404
from django.shortcuts import render
from django.db.models import Value
from django.db import connection
import psycopg2

from rest_framework.generics import get_object_or_404
from .serializers import  UserSerializer, formal_puestoserializer, formal_unidad_organizativa_jerarquiaserializer,funcional_puestoserializer,formal_plazaserializer,funcional_plazaserializer
from .serializers import AutorizarSerializer,LogoutSerializer
from .serializers import groupserializer,funcional_unidad_organizativaserializer,formal_unidad_organizativaserializer
from .serializers import Funcional_Relacion_Laboralserializer,Formal_Relacion_Laboralserializer
from .serializers import Formal_empleadoserializer,Funcional_empleadoserializer
from .models import Formal_Diagnostico, Formal_Division, Formal_Division_Personal,Funcional_Division_Personal, Formal_Equipo, Formal_Especialidad, Formal_Estado_civil, Formal_Formacion, Formal_Historial_Laboral, Formal_Puesto, Formal_Salud, Formal_Situacion_Actual, Formal_empleado, Funcional_Diagnostico,Funcional_Puesto,Formal_plaza,Funcional_Plaza,seleccion_contratacion_puestos_vacante
from .serializers import Formal_empleadoserializer,Funcional_empleadoserializer,Formal_Divisionserializer,Formal_Organizacionserializer
from .serializers import Formal_Centro_Costoserializer,Formal_Estado_civilserializer,Funcional_Divisionserializer,Funcional_Centro_Costoserializer
from .serializers import Funcional_Organizacionserializer,Funcional_Estado_civilserializer,Formal_Parentescoserializer
from .serializers import Funcional_Parentescoserializer,Funcional_Generoserializer,Formal_Generoserializer
from .serializers import Formal_Funcionesserializer,Funcional_Funcionesserializer,Formal_Situacion_Actualserializer,Funcional_Situacion_Actualserializer
from .serializers import Formal_Compañiaserializer,Funcional_Compañiaserializer,Formal_Especialidadserializer,Funcional_Especialidadserializer,Funcional_Contacto_Emergenciaserializer,Formal_Contacto_Emergenciaserializer
from .serializers import Formal_Dependientes_Economicoserializer,Funcional_Dependientes_Economicoserializer,Funcional_Beneficiario_Seguroserializer,Formal_Beneficiario_Seguroserializer
from .serializers import Formal_Formacionserializer,Funcional_Formacionserializer,Funcional_Equiposerializer,Formal_Equiposerializer
from .serializers import Formal_Historial_Laboralserializer,Funcional_Historial_Laboralserializer,formal_unidad_organizativa_jerarquiaserializer
from .serializers import Formal_empleado_nodojerarquiaserializer,funcional_unidad_organizativa_jerarquiaserializer,Funcional_empleado_nodojerarquiaserializer
from .serializers import Formal_Tituloserializer,Formal_Institutoserializer,Formal_Diagnosticoserializer,Formal_Saludserializer
from .serializers import Formal_Educacionserializer
from .serializers import Funcional_Tituloserializer,Funcional_Institutoserializer,Funcional_Diagnosticoserializer,Funcional_Saludserializer
from .serializers import Funcional_Educacionserializer,Data_userserializer,Formal_Division_Personalserializer,Funcional_Division_Personalserializer
from .serializers import Formal_Division_Personalserializer,Funcional_Division_Personalserializer
from .serializers import Formal_empleado_jerarquiaserializer,Funcional_empleado_jerarquiaserializer
from .serializers import formal_unidad_organizativabasicoserializer,funcional_unidad_organizativabasicoserializer
from .serializers import Actualizacion_Contactoserializer,Actualizacion_Dependienteserializer,Actualizacion_Domicilioserializer,Actualizacion_Educacionserializer,Actualizacion_Estado_Civilserializer
from .serializers import Funcional_Check_Listserializer,Funcional_Empleado_Check_Listserializer
from .serializers import Formal_Check_Listserializer,Formal_Empleado_Check_Listserializer
from .serializers import Configuracion_Actualizacion_Empleadoserializer
from .serializers import Funcional_Relacion_Laboral_Anteriorserializer,Formal_Relacion_Laboral_Anteriorserializer
from .models import Formal_Estado_civil, Formal_Puesto, Formal_empleado,Funcional_Puesto,Formal_plaza,Funcional_Plaza
from .models import Formal_Unidad_Organizativa,Funcional_Unidad_Organizativa
from .models import Funcional_Relacion_Laboral,Formal_Relacion_Laboral,Funcional_Organizacion
from .models import Funcional_empleado,Formal_empleado,Formal_Division,Formal_Organizacion,Formal_Centro_Costo,Funcional_Division,Funcional_Centro_Costo
from .models import Funcional_Estado_civil,Formal_Parentesco,Funcional_Parentesco,Funcional_Genero,Formal_Genero
from .models import Formal_Funciones,Funcional_Funciones,Formal_Situacion_Actual,Funcional_Situacion_Actual
from .models import Formal_Compañia,Funcional_Compañia,Formal_Especialidad,Funcional_Especialidad,Funcional_Contacto_Emergencia,Formal_Contacto_Emergencia
from .models import Formal_Dependientes_Economico,Funcional_Dependientes_Economico,Funcional_Beneficiario_Seguro,Formal_Beneficiario_Seguro
from .models import Formal_Formacion,Funcional_Formacion,Funcional_Equipo,Formal_Equipo,Formal_Historial_Laboral,Funcional_Historial_Laboral
from .models import Funcional_Salud,Formal_Salud,Funcional_Diagnostico,Formal_Diagnostico,Formal_Educacion,Funcional_Educacion
from .models import Formal_Titulo,Formal_Instituto,Funcional_Instituto,Funcional_Titulo
from .models import Formal_Division_Personal,Funcional_Division_Personal
from .models import Formal_Asignacion_Equipo,Funcional_Asignacion_Equipo
from .models import Actualizacion_Contacto,Actualizacion_Dependiente,Actualizacion_Domicilio,Actualizacion_Educacion
from .models import Actualizacion_Estado_Civil,capacitacion_campania,capacitacion_estado,capacitacion_asistencia,capacitacion_evento_capacitacion
from .models import Funcional_Check_List,Funcional_Empleado_Check_List,Formal_Check_List,Formal_Empleado_Check_List
from .models import Configuracion_Actualizacion_Empleado
from .models import Funcional_Relacion_Laboral_Anterior, Formal_Relacion_Laboral_Anterior
from .models import Crjob_Log,Crjob_log_empledo,Crjob_log_complementaria
from .models import evaluacion_configuracion_periodo,descriptor_perfil_datos_generales, evaluacion_encabezado,evaluacion_tipo_evaluacion,evaluacion_periodicidad
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
from datetime import datetime
from .views.views_capacitacion import *
from .views.views_generar_archivo import *
import sys
sys.setrecursionlimit(100000000)

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


def Formal_RFC_Carga_Masiva_Complementaria():
    Crjob_Log.objects.create(descripcion="Inicio job Formal_RFC_Carga_Masiva_Complementaria")
    with Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300') as conx:
    #with Connection(user='INTERFACESAP', passwd='1nt3rf4c3sF4r!n73r',ashost='172.10.0.6', sysnr='00', client='300') as conx:
        #r2 = conx.call('ZRFC_HEADCOUNT_AURORA',IRG_PERNR=IRG_PERNR)
        r2 = conx.call('ZRFC_SUPPL_TABLES_AURORA')
        Crjob_log_complementaria.objects.create(data=str(r2))
        
       #print('este es el resultado',r2)
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
            
        Crjob_Log.objects.create(descripcion="Inicio job Formal_RFC_Carga_Masiva_Complementaria")
        return True


def Formal_RFC_Carga_Masiva():
    Crjob_Log.objects.create(descripcion="Inicio job Formal_RFC_Carga_Masiva")
    # IRG_PERNR=[{
    # "LOW":"00501134",
    # "OPTION":"",
    # "SIGN":"",
    #     }]
    with Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300') as conx:
    #with Connection(user='INTERFACESAP', passwd='1nt3rf4c3sF4r!n73r',ashost='172.10.0.6', sysnr='00', client='300') as conx:
        #r2 = conx.call('ZRFC_HEADCOUNT_AURORA',IRG_PERNR=IRG_PERNR)
        r2 = conx.call('ZRFC_HEADCOUNT_AURORA')
        #for empleado in r2['ET_HEADCOUNT']:
        #    relacion_laboral=Formal_Estado_civil.objects.get(relacion_laboral=empleado['PERSG'])
        #    puesto = Formal_Puesto.objects.get(codigo=empleado['STELL'])
        #    formal_empleado = Formal_empleado(identidad=empleado['ICNUM'], nombre=empleado['ENAME'], codigo=empleado['PERNR'], fecha_ingreso=empleado['INDAT'], division=empleado['WERKS'], centro_costo=empleado['KOSTL'], antiguedad_laboral=empleado['ANTLAB'], fecha_cumpleaños=empleado['GBDAT'], edad=empleado["EDAD"], saldo_vacaciones=empleado["ANZHL"], absentismo=empleado["AWART"], domicilio=empleado["ORT01"], historial_laboral=empleado["ARBGB"])
        #    if  relacion_laboral:
        #        formal_empleado.relacion_laboral=relacion_laboral.codigo
        #    if  puesto:
        #        formal_empleado.puesto.add(relacion_laboral)

        empleado_formal=Formal_empleado.objects.filter(fecha_baja__lt=datetime.now().date())
        for colaborador in empleado_formal:
            colaborador.puesto.remove(*colaborador.puesto.all())  

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
                obj.puesto.remove(*obj.puesto.all())
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
        
            
        Crjob_Log.objects.create(descripcion="Final job Formal_RFC_Carga_Masiva")
        return True


def Funcional_RFC_Carga_Masiva():
    Crjob_Log.objects.create(descripcion="Inicio job Funcional_RFC_Carga_Masiva")
    # IRG_PERNR=[{
    # "LOW":"00508155",
    # "OPTION":"",
    # "SIGN":"",
    #     }]
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
            
        empleado_funcional=Funcional_empleado.objects.filter(fecha_baja__lt=datetime.now().date())
        for colaborador in empleado_funcional:
            colaborador.puesto.remove(*colaborador.puesto.all())
            

        for empleado in r2['ET_HEADCOUNT']:

            Crjob_log_empledo.objects.create(empleado=str(empleado))
            val=Funcional_empleado.objects.filter(codigo=empleado['PERNR']).count()
            
            

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
            #temporal=datetime.strptime(empleado['INDAT'], '%Y%m%d').date() if empleado['INDAT']!='' else None
            ##print('dato con formato',temporal)
            ##print('dato sin formato',empleado['INDAT'])
            ##print('codigo de empleado',empleado['PERNR'])
            
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
                    #'jefe_inmediato':empleado["PERNR_JEFE"],
                    'estado_civil':estado_civil[0] if estado_civil!=None else None,
                    'clase_medida':empleado["MASSN"],
                    'descripcion_clase_medida':empleado["MASSN_DESC"],
                    'motivo_clase_medida':empleado["MASSG_IN"],
                    'descripcion_motivo_clase_medida':empleado["MASSG_IN_DESC"],
                    'sap':True,
                }
            )

           #print('objecto creado',obj.fecha_ingreso)
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
                
            #este bloque se descomenta para atualizar puestos
            if val==0:
                # 'jefe_inmediato':empleado["PERNR_JEFE"],
                obj.jefe_inmediato=empleado["PERNR_JEFE"]
                obj.save()
                if puesto!=None:
                    obj.puesto.remove(*obj.puesto.all())
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
            
            #este bloque se descommenta para actualizar unidades

            if val==0:
                if unidad!=None:
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
        Crjob_Log.objects.create(descripcion="Fimal job Funcional_RFC_Carga_Masiva")
        return True




def Funcional_RFC_Carga_Masiva_Complementaria():
    Crjob_Log.objects.create(descripcion="Inicio job Funcional_RFC_Carga_Masiva_Complementaria")
    with Connection(user=settings.SAP['sap_user'], passwd=settings.SAP['sap_pass'],ashost=settings.SAP['ambiente_sap'], sysnr='00', client='300') as conx:
    #with Connection(user='INTERFACESAP', passwd='1nt3rf4c3sF4r!n73r',ashost='172.10.0.6', sysnr='00', client='300') as conx:
        #r2 = conx.call('ZRFC_HEADCOUNT_AURORA',IRG_PERNR=IRG_PERNR)
        r2 = conx.call('ZRFC_SUPPL_TABLES_AURORA')
        Crjob_log_complementaria.objects.create(data=str(r2))
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
            codigo_lista=[]
            #Funcional_Puesto.objects.filter(sap=True).delete()
            for puesto in r2['ET_PUESTOS']:                
                obj, created = Funcional_Puesto.objects.update_or_create(
                    codigo=puesto['PLANS'],         
                    defaults={
                        'codigo':puesto['PLANS'], 
                        'descripcion':puesto['PLSTX'],         
                        'descripcion_larga':puesto['PLSTX2'], 
                        'sap':True,
                        'activo':True,    
                                  

                    }
                )
                codigo_lista.append(puesto['PLANS'])
            #verificando puestos inactivos
            Funcional_Puesto.objects.exclude(codigo__in=codigo_lista).filter(sap=True).update(activo=False)
          
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
                        #'Dirigido_por':unidad_organizativa['PERNR_D'], #comentado para evitar modificar la estructura
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
                        #descomentar para actualizar 
                        #'Dirigido_por':unidad_organizativa['PERNR_D'], #comentado para evitar modificar la estructura
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
# Descomentarse para realizar 
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
        Crjob_Log.objects.create(descripcion="Final job Funcional_RFC_Carga_Masiva_Complementaria")
        return True

def Formal_checklist():
    
    checklist_activo=Formal_Empleado_Check_List.objects.filter(activo=True)
    empleado_activos = Formal_empleado.objects.filter(situacion_actual__id=1).exclude(fecha_baja=None)

    for empleado in empleado_activos:
        check_list = Formal_Check_List.objects.filter(activo=True)
        for check in check_list:
            empleado_check, created = Formal_Empleado_Check_List.objects.update_or_create(
            empleado=empleado,
            checklist=check,
            defaults={
                'empleado':empleado,
                'checklist':check,
            }
            )
    checklist_inactivo=Formal_Check_List.objects.filter(activo=False)
    for check in check_list:
        if check.activo==False:
            Formal_Empleado_Check_List.filter(checklist=check).delete()


    return True  

def Funcional_checklist():
    
    checklist_inactivo=Funcional_Empleado_Check_List.objects.filter(activo=False)
    empleado_activos = Funcional_empleado.objects.filter(situacion_actual__id=1).exclude(fecha_baja=None)

    for empleado in empleado_activos:
        check_list = Funcional_Check_List.objects.filter(activo=True)
        for check in check_list:
            empleado_check, created = Funcional_Empleado_Check_List.objects.update_or_create(
            empleado=empleado,
            checklist=check,
            defaults={
                'empleado':empleado,
                'checklist':check,
            }
            )
    checklist_inactivo=Funcional_Check_List.objects.filter(activo=False)
    for check in check_list:
        if check.activo==False:
            Funcional_Empleado_Check_List.filter(checklist=check).delete()

    return True  



def Creacion_Usuario():
    usuarios=list(User.objects.filter().values_list('username',flat=True))
    empleados_sin_usuario=Funcional_empleado.objects.exclude(codigo__in=usuarios).filter(codigo='00503816')

    for empleado in empleados_sin_usuario:
        subject = 'Nueva Cuenta AURORA'
        message = 'Bienvenido a AURORA, Hemos configurado tu cuenta y acceso, podras cambiar la contraseña temporal al ingresar a tu perfil'
        from_email = settings.EMAIL_HOST_USER
        to=empleado.correo_personal
        text_content=''
        text_content = text_content + '\nSu usuario es:'+ empleado.codigo
        text_content ='Su contraseña es la siguiente:'
        code = get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
        text_content = text_content + ': '+code + '\nSe recomienda hacer el cambio de contraseña ya que la misma es temporal'
        password=code
        user = User.objects.create_user(username=empleado.codigo,password=password,first_name=empleado.nombre,email=empleado.correo_personal)
        user.save()
        subordinados=Funcional_empleado.objects.filter(jefe_inmediato=empleado.codigo).count()
        liderados=  Funcional_Unidad_Organizativa.objects.filter(Dirigido_por=empleado.codigo).count() 
        perfil_empleado = Group.objects.get(name='empleado') if Group.objects.filter(name='empleado') else None
        perfil_jefe = Group.objects.get(name='jefe') if Group.objects.filter(name='jefe') else None

        if subordinados>0 or liderados>0:
            if perfil_jefe !=None:
                user.groups.add(perfil_jefe) 
        else:
            if perfil_empleado !=None:
                user.groups.add(perfil_empleado)
        user.save()

    return True  

def jefes_inmediatos():
    
    jefes=Formal_empleado.objects.filter().values('jefe_inmediato').distinct()
    Formal_empleado.objects.filter(codigo__in=jefes).update(es_jefe=True)
    Funcional_empleado.objects.filter(codigo__in=jefes).update(es_jefe=True)

    return True  


    
def informacin_powerBIviewsets():
    
    plazas_totales=[]
    puestos_vacios= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).annotate(estado_puesto= Value('Vacante'),funcional_empleado_codigo=F('funcional_empleado__codigo'),funcional_empleado_nombre=F('funcional_empleado__nombre'),unidad_organizativa_nombre=F('unidad_organizativa__nombre'),unidad_organizativa_codigo=F('unidad_organizativa__codigo')).values('codigo','descripcion','descripcion_larga','funcional_empleado_codigo','funcional_empleado_nombre','unidad_organizativa_nombre','unidad_organizativa_codigo' ,'estado_puesto')
    plazas_totales.extend(list(puestos_vacios))

    puestos_ocupados= Funcional_Puesto.objects.filter().exclude(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).annotate(estado_puesto= Value('No vacante'),funcional_empleado_codigo=F('funcional_empleado__codigo'),funcional_empleado_nombre=F('funcional_empleado__nombre'),unidad_organizativa_nombre=F('unidad_organizativa__nombre'),unidad_organizativa_codigo=F('unidad_organizativa__codigo')).values('codigo','descripcion','descripcion_larga','funcional_empleado_codigo','funcional_empleado_nombre','unidad_organizativa_nombre','unidad_organizativa_codigo' ,'estado_puesto')
    plazas_totales.extend(list(puestos_ocupados))
 
    # cursor = connection.cursor()
    # cursor.execute('TRUNCATE TABLE "HEADCOUNT_seleccion_contratacion_puestos_vacante" RESTART IDENTITY;')
    # print('tabla limpia')
    codigos=[]
    for plaza in plazas_totales:
        llenado= seleccion_contratacion_puestos_vacante.objects.create(**plaza)
        codigos.append(plaza['codigo'])
        # llenado= seleccion_contratacion_puestos_vacante.objects.create(**plaza)
        puestos, created = seleccion_contratacion_puestos_vacante.objects.update_or_create(
                codigo=plaza['codigo'],
                defaults={
                    'descripcion' : plaza['descripcion'],
                    'descripcion_larga' : plaza['descripcion_larga'],
                    'funcional_empleado_codigo' : plaza['funcional_empleado_codigo'],
                    'funcional_empleado_nombre' : plaza['funcional_empleado_nombre'],
                    'unidad_organizativa_nombre' : plaza['unidad_organizativa_nombre'],
                    'unidad_organizativa_codigo' : plaza['unidad_organizativa_codigo'],
                    'estado_puesto' : plaza['estado_puesto'],
                }
                )
    borrar = seleccion_contratacion_puestos_vacante.objects.exclude(codigo__in=codigos).delete()
    return 1






def Llenado_Encabezado():    
    hoy=datetime.now().date()
    anio_actual=datetime.now().date().year
    inicio_anio=datetime.now().date().replace(month=1, day=1)
    #periodicidad_actual=evaluacion_configuracion_periodo.objects.filter().values_list('periodicidad__empresa__id','tipo_evaluacion__id','tipo_evaluacion__nombre','periodicidad','periodo') if evaluacion_configuracion_periodo.objects.filter(fecha_inicio=hoy).values_list('periodicidad__empresa__id','tipo_evaluacion__id','periodicidad','periodo')  else None
    lista_empleados_sin_descriptor=[]
    lista_empleados_sin_funcion=[]
    comparacion=evaluacion_configuracion_periodo.objects.filter(periodicidad__anio=anio_actual,fecha_inicio__lte=hoy).values_list('periodicidad__empresa__id','tipo_evaluacion__id','tipo_evaluacion__nombre','periodicidad','periodo','fecha_inicio') if evaluacion_configuracion_periodo.objects.filter(periodicidad__anio=anio_actual,fecha_inicio__lte=hoy).values_list('periodicidad__empresa__id','tipo_evaluacion__id','tipo_evaluacion__nombre','periodicidad','periodo','fecha_inicio')  else None
    if comparacion==None:
        return 1
    for empresa_id, tipo_evaluacion,tipo_evaluacion_nombre,periodicidad,periodo,fecha_inicio in comparacion:
        if tipo_evaluacion_nombre=='0°':
            empleados = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=empresa_id,fecha_ingreso__lt=inicio_anio).filter(Q(fecha_baja__gt=hoy)|Q(fecha_baja=None)).values_list('codigo',flat=True)
            for empleado_codigo in empleados:
                # if empleado_codigo=='00500693':
                #     print('tipo_evaluacion_nombre',tipo_evaluacion_nombre)
                empleado= Funcional_empleado.objects.get(codigo=empleado_codigo) if Funcional_empleado.objects.filter(codigo=empleado_codigo) else None 
                ###########################################################################################
                # codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                id_funcion=Funcional_empleado.objects.get(codigo=empleado_codigo)
                posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0] if id_funcion.posicion.all().count()>0 else None
                if posicion==None:
                    lista_empleados_sin_funcion.append(empleado_codigo)
                    continue
                descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=posicion).order_by('-id').first() if descriptor_perfil_datos_generales.objects.filter(posicion=posicion) else None
                ###########################################################################################
                if descriptor==None:
                    lista_empleados_sin_descriptor.append(empleado_codigo)
                    continue
                # print('empleado_codigo',empleado_codigo)
                # jefe_inmediato
                # if empleado_codigo=='00500693':
                #         print('jefe_inmediato',jefe_inmediato)
                jefe_inmediato=''
                jefe_inmediato = Funcional_empleado.objects.get(codigo=empleado.jefe_inmediato) if Funcional_empleado.objects.filter(codigo=empleado.jefe_inmediato) else None
                if jefe_inmediato==None:
                    Dirigido_por=(Funcional_empleado.objects.values(codigo=empleado.codigo).values('unidad_organizativa__Dirigido_por'))[0]['unidad_organizativa__Dirigido_por'] if Funcional_empleado.objects.filter(codigo=empleado.jefe_inmediato) else None
                    jefe_inmediato = Funcional_empleado.objects.get(codigo=Dirigido_por) if Funcional_empleado.objects.filter(codigo=empleado.jefe_inmediato) else None
                    # if empleado_codigo=='00500693':
                    #     print('jefe_inmediato',jefe_inmediato)

                        
                te= evaluacion_tipo_evaluacion.objects.get(id=tipo_evaluacion) if evaluacion_tipo_evaluacion.objects.filter(id=tipo_evaluacion) else None
                p=evaluacion_periodicidad.objects.get(id=periodicidad) if evaluacion_periodicidad.objects.filter(id=periodicidad) else None
                print('jefe_inmediato',jefe_inmediato)

                if empleado!=None:
                    nuevo_encabezado_1= evaluacion_encabezado.objects.update_or_create(evaluado=empleado,
                                                                                    tipo_evaluacion=te,
                                                                                    periodicidad=p,
                                                                                    periodo=periodo,
                                                                                    tipo_evaluacion_encabezado=1,
                                                                                    descriptor_empleado=descriptor,
                                                                                    defaults={
                                                                                                'responsable_directo':jefe_inmediato, 
                                                                                                'evaluador':empleado,})
                    
                    nuevo_encabezado_2= evaluacion_encabezado.objects.update_or_create(evaluado=empleado,
                                                                                    tipo_evaluacion=te,
                                                                                    periodicidad=p,
                                                                                    descriptor_empleado=descriptor,
                                                                                    periodo=periodo,
                                                                                    tipo_evaluacion_encabezado=2,
                                                                                    defaults={
                                                                                                'responsable_directo':jefe_inmediato, 
                                                                                                'evaluador':empleado,})
        if tipo_evaluacion_nombre=='90°':
            empleados = Funcional_empleado.objects.filter(unidad_organizativa__sociedad_financiera__id=empresa_id,fecha_ingreso__lt=inicio_anio).filter(Q(fecha_baja__gt=hoy)|Q(fecha_baja=None)).values_list('codigo',flat=True)
            for empleado_codigo in empleados:
                empleado= Funcional_empleado.objects.get(codigo=empleado_codigo) if Funcional_empleado.objects.filter(codigo=empleado_codigo) else None 
                ###########################################################################################
                # codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                id_funcion=Funcional_empleado.objects.get(codigo=empleado_codigo)
                posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0] if id_funcion.posicion.all().count()>0 else None
                if posicion==None:
                    lista_empleados_sin_funcion.append(empleado_codigo)
                    continue
                descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=posicion).order_by('-id').first()
                if descriptor==None:
                    lista_empleados_sin_descriptor.append(empleado_codigo)
                    continue
                ###########################################################################################
                print('empleado_codigo',empleado_codigo)
                # jefe_inmediato
                jefe_inmediato=''
                jefe_inmediato = Funcional_empleado.objects.get(codigo=empleado.jefe_inmediato) if Funcional_empleado.objects.filter(codigo=empleado.jefe_inmediato) else None
                if jefe_inmediato==None:
                    Dirigido_por=(Funcional_empleado.objects.values(codigo=empleado.codigo).values('unidad_organizativa__Dirigido_por'))[0]['unidad_organizativa__Dirigido_por'] if Funcional_empleado.objects.filter(codigo=empleado.jefe_inmediato) else None
                    jefe_inmediato = Funcional_empleado.objects.get(codigo=Dirigido_por) if Funcional_empleado.objects.filter(codigo=empleado.jefe_inmediato) else None

                        
                te= evaluacion_tipo_evaluacion.objects.get(id=tipo_evaluacion) if evaluacion_tipo_evaluacion.objects.filter(id=tipo_evaluacion) else None
                p=evaluacion_periodicidad.objects.get(id=periodicidad) if evaluacion_periodicidad.objects.filter(id=periodicidad) else None
                print('jefe_inmediato',jefe_inmediato)

                if empleado!=None:
                    nuevo_encabezado_1= evaluacion_encabezado.objects.update_or_create(evaluado=empleado,                                                                                    
                                                                                    tipo_evaluacion=te,
                                                                                    periodicidad=p,
                                                                                    descriptor_empleado=descriptor,
                                                                                    periodo=periodo,
                                                                                    tipo_evaluacion_encabezado=1,
                                                                                    defaults={
                                                                                                'responsable_directo':jefe_inmediato, 
                                                                                                'evaluador':jefe_inmediato,})
                            
                    nuevo_encabezado_2= evaluacion_encabezado.objects.update_or_create(evaluado=empleado,                                                                                    
                                                                                    tipo_evaluacion=te,
                                                                                    periodicidad=p,
                                                                                    descriptor_empleado=descriptor,
                                                                                    periodo=periodo,
                                                                                    tipo_evaluacion_encabezado=2,
                                                                                    defaults={
                                                                                                'responsable_directo':jefe_inmediato, 
                                                                                                'evaluador':jefe_inmediato,})           
    
    if len(lista_empleados_sin_descriptor)>0:
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Evaluacion').values_list('username',flat=True)
        for responsable in usuarios_reponsables:
            correo_responsable=(Funcional_empleado.objects.filter(codigo=responsable).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=responsable).values('correo_empresarial') else None
            # id_responsable
            if correo_responsable==None:
                continue
            else:

                asunto='Códigos de empleados sin descriptor'
                codigoss = ','.join(str(x) for x in lista_empleados_sin_descriptor)
                mensaje= 'Hola, el siguiente listado de empleados no tienen descriptores y para realizar las evaluaciones es de forma obligatoria el tener un descriptor asignado, por favor tomar nota en el asunto y asignar los descriptores correspondientes, listado: ' + codigoss
                


                from_email_jefe= settings.EMAIL_HOST_USER
                try:
                    msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_responsable])
                    msg_jefe.send()
                    # notificacion=notificacion_aurora.objects.create(destinatario=id_responsable,asunto=asunto,mensaje=mensaje)
                except BadHeaderError:
                    print('Error de envio de correos')
    
    #######################################################
    if len(lista_empleados_sin_funcion)>0:
        usuarios_reponsables = User.objects.filter(groups__name='Responsable_Evaluacion').values_list('username',flat=True)
        for responsable in usuarios_reponsables:
            correo_responsable=(Funcional_empleado.objects.filter(codigo=responsable).values('correo_empresarial'))[0]['correo_empresarial'] if Funcional_empleado.objects.filter(codigo=responsable).values('correo_empresarial') else None
            # id_responsable
            if correo_responsable==None:
                continue
            else:

                asunto='Códigos de empleados sin funciones asignadas'
                codigoss = ','.join(str(x) for x in lista_empleados_sin_funcion)
                mensaje= 'Hola, el siguiente listado de empleados no tienen funciones y para realizar las evaluaciones es de forma obligatoria el tener una función asignada, por favor tomar nota en el asunto y asignar las funciones correspondientes, listado: ' + codigoss
                


                from_email_jefe= settings.EMAIL_HOST_USER
                try:
                    msg_jefe = EmailMultiAlternatives(asunto, mensaje, from_email_jefe, [correo_responsable])
                    msg_jefe.send()
                    # notificacion=notificacion_aurora.objects.create(destinatario=id_responsable,asunto=asunto,mensaje=mensaje)
                except BadHeaderError:
                    print('Error de envio de correos')
    
    return True   
    
        
        

    
def informacin_powerBIviewsets():
    
    plazas_totales=[]
    puestos_vacios= Funcional_Puesto.objects.filter(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).filter(activo=True).annotate(estado_puesto= Value('Vacante'),funcional_empleado_codigo=F('funcional_empleado__codigo'),funcional_empleado_nombre=F('funcional_empleado__nombre'),unidad_organizativa_nombre=F('unidad_organizativa__nombre'),unidad_organizativa_codigo=F('unidad_organizativa__codigo')).values('codigo','descripcion','descripcion_larga','funcional_empleado_codigo','funcional_empleado_nombre','unidad_organizativa_nombre','unidad_organizativa_codigo' ,'estado_puesto')
    plazas_totales.extend(list(puestos_vacios))

    puestos_ocupados= Funcional_Puesto.objects.filter(activo=True).exclude(Q(funcional_empleado__isnull=True)|Q(funcional_empleado__fecha_baja__lt=datetime.now().date())).annotate(estado_puesto= Value('No vacante'),funcional_empleado_codigo=F('funcional_empleado__codigo'),funcional_empleado_nombre=F('funcional_empleado__nombre'),unidad_organizativa_nombre=F('unidad_organizativa__nombre'),unidad_organizativa_codigo=F('unidad_organizativa__codigo')).values('codigo','descripcion','descripcion_larga','funcional_empleado_codigo','funcional_empleado_nombre','unidad_organizativa_nombre','unidad_organizativa_codigo' ,'estado_puesto')
    plazas_totales.extend(list(puestos_ocupados))
 
    # cursor = connection.cursor()
    # cursor.execute('TRUNCATE TABLE "HEADCOUNT_seleccion_contratacion_puestos_vacante" RESTART IDENTITY;')
    # print('tabla limpia')
    codigos=[]
    for plaza in plazas_totales:
        llenado= seleccion_contratacion_puestos_vacante.objects.create(**plaza)
        codigos.append(plaza['codigo'])
        # llenado= seleccion_contratacion_puestos_vacante.objects.create(**plaza)
        puestos, created = seleccion_contratacion_puestos_vacante.objects.update_or_create(
                codigo=plaza['codigo'],
                defaults={
                    'descripcion' : plaza['descripcion'],
                    'descripcion_larga' : plaza['descripcion_larga'],
                    'funcional_empleado_codigo' : plaza['funcional_empleado_codigo'],
                    'funcional_empleado_nombre' : plaza['funcional_empleado_nombre'],
                    'unidad_organizativa_nombre' : plaza['unidad_organizativa_nombre'],
                    'unidad_organizativa_codigo' : plaza['unidad_organizativa_codigo'],
                    'estado_puesto' : plaza['estado_puesto'],
                }
                )
    borrar = seleccion_contratacion_puestos_vacante.objects.exclude(codigo__in=codigos).delete()
    return 1



def cambio_estado_campanias():
    hoy=datetime.now().date()
    ###########En proceso
    campanias_en_proceso = capacitacion_campania.objects.all().values_list('id','fecha_inicio')
    for campania_id, fecha_inicio in campanias_en_proceso:
        if hoy >= fecha_inicio:
            estado_en_proceso_id=(capacitacion_estado.objects.filter(descripcion='En proceso').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='En proceso').values('id') else None
            
            if estado_en_proceso_id!=None:
                capacitacion_campania.objects.filter(id=campania_id).update(estado=estado_en_proceso_id)
                ####Envio de notificaciones#######################################################
                listado_empleados= capacitacion_asistencia.objects.filter(evento_capacitacion__campania__id=campania_id).values_list('empleado__codigo',flat=True)
               
                print('cantidad de empleados capacitacion',len(listado_empleados))
                for codigo_colaborador in listado_empleados:
                    funcion_envio_correo('Comienzo Ruta de Aprendizaje',campania_id,codigo_colaborador)



    ###########Cerrado
    campanias_cerradas = capacitacion_campania.objects.all().values_list('id','fecha_fin')
    for campania_id, fecha_fin in campanias_cerradas:
        if hoy >= fecha_fin:
            estado_cerrado=(capacitacion_estado.objects.filter(descripcion='Cerrado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Cerrado').values('id') else None
            if estado_cerrado!=None:
                capacitacion_campania.objects.filter(id=campania_id).update(estado=estado_cerrado)
                ####Envio de notificaciones#######################################################
                listado_empleados= capacitacion_asistencia.objects.filter(evento_capacitacion__campania__id=campania_id).values_list('empleado__codigo',flat=True)
                
                for codigo_colaborador in listado_empleados:
                    funcion_envio_correo('Fin Ruta de Aprendizaje',campania_id,codigo_colaborador)


def cambio_estado_evento_capacitacion():
    hoy=datetime.now().date()
    # print('hoy',hoy)
    ###########En proceso
    eventos_en_proceso = capacitacion_evento_capacitacion.objects.all().values_list('id','fecha_inicio')
    for evento_id, fecha_inicio in eventos_en_proceso:
        if hoy>=fecha_inicio:
            # print('fecha_inicio',fecha_inicio)
            # print('evento_id',evento_id)
            # print('fecha_inicio',fecha_inicio)
            estado_en_proceso_id=(capacitacion_estado.objects.filter(descripcion='En proceso').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='En proceso').values('id') else None
            if estado_en_proceso_id!=None:
                capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(estado=estado_en_proceso_id)
                ####Envio de notificaciones#######################################################
                colaborador_codigos= capacitacion_asistencia.objects.filter(evento_capacitacion__id=evento_id).values_list('empleado__codigo',flat=True)
                # print('colaborador_codigos',colaborador_codigos)
                # print('colaborador_codigos',len(colaborador_codigos))
                
                for cod_colaborador in colaborador_codigos:
                    # print('entro')
                    funcion_envio_correo('evaluación capacitacion:jefe',evento_id,cod_colaborador)

    ###########Cerrado
    eventos_cerrados = capacitacion_evento_capacitacion.objects.all().values_list('id','fecha_fin')
    for evento_id, fecha_fin in eventos_cerrados:
        if hoy>=fecha_fin:
            # print('fecha_fin',fecha_fin)
            estado_cerrado=(capacitacion_estado.objects.filter(descripcion='Cerrado').values('id'))[0]['id'] if capacitacion_estado.objects.filter(descripcion='Cerrado').values('id') else None
            if estado_cerrado!=None:
                capacitacion_evento_capacitacion.objects.filter(id=evento_id).update(estado=estado_cerrado)


