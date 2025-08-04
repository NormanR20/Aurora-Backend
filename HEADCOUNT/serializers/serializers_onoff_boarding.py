from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields import files
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import models
from rest_framework.utils import field_mapping
from ..models import on_off_bording_bloque,on_off_bording_tarea,on_off_bording_workflow
from ..models import on_off_bording_bloque_plantilla,on_off_bording_tarea_plantilla,on_off_bording_workflow_plantilla
from ..models import on_off_bording_bienvenida 
from ..models import archivos_gestor
from ..serializers import *
####################################################################################################
from django.contrib.auth.models import User,Group
from django.db.models import Count


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class on_off_bording_workflow_plantillaserializer(serializers.ModelSerializer):
    workflow_bloques = serializers.SerializerMethodField()
    #historial_list = Formal_Historial_Laboralserializer(many=True, read_only=True)
    #este es un campo many to many dentro de la tabla de formal_empleado


    def get_workflow_bloques(self, obj):

        bloque=on_off_bording_bloque_plantilla.objects.filter(workflow=obj.id) if on_off_bording_bloque_plantilla.objects.filter(workflow=obj.id) else None
        if bloque == None:
           return None

        return on_off_bording_bloque_plantillaserializer(bloque, many=True).data



    datos_creador=   serializers.SerializerMethodField()
    def get_datos_creador(self, obj):
        usuario=None
        if obj.creador:
            usuario=User.objects.filter(id=obj.creador.id) if User.objects.filter(id=obj.creador.id) else None
            if usuario == None:
                return None

        return UserSerializer(usuario, many=True).data

    class Meta:
        model = on_off_bording_workflow_plantilla
        fields = '__all__'





class on_off_bording_bloque_plantillaserializer(serializers.ModelSerializer):
    workflow_tareas = serializers.SerializerMethodField()
    #historial_list = Formal_Historial_Laboralserializer(many=True, read_only=True)
    #este es un campo many to many dentro de la tabla de formal_empleado


    def get_workflow_tareas(self, obj):
        tarea=on_off_bording_tarea_plantilla.objects.filter(bloque=obj.id) if on_off_bording_tarea_plantilla.objects.filter(bloque=obj.id)  else None
        if tarea == None:
           return None

        return on_off_bording_tarea_plantillaserializer(tarea, many=True).data
    class Meta:
        model = on_off_bording_bloque_plantilla
        fields = '__all__'

class on_off_bording_tarea_plantillaserializer(serializers.ModelSerializer):
    archivo_gestor  =serializers.SerializerMethodField()
    def get_archivo_gestor(self,obj):
        if obj ==None:
            return None
        if obj.archivos_gestor==None:
            return None
        Archivo_gestor=archivos_gestor.objects.filter(id=obj.archivos_gestor.id) if archivos_gestor.objects.filter(id=obj.archivos_gestor.id) else None
        
        if Archivo_gestor==None:
            return None
        return archivos_gestorserializer(Archivo_gestor, many=True).data
    class Meta:
        model = on_off_bording_tarea_plantilla
        fields = '__all__'





class on_off_bording_workflowserializer(serializers.ModelSerializer):
    workflow_bloques = serializers.SerializerMethodField()
    #historial_list = Formal_Historial_Laboralserializer(many=True, read_only=True)
    #este es un campo many to many dentro de la tabla de formal_empleado


    def get_workflow_bloques(self, obj):
        bloque=on_off_bording_bloque.objects.filter(workflow=obj.id) if on_off_bording_bloque.objects.filter(workflow=obj.id) else None
        if bloque == None:
           return None

        return on_off_bording_bloqueserializer(bloque, many=True).data


    datos_empleado=   serializers.SerializerMethodField()
    def get_datos_empleado(self, obj):
        usuario=None
        if obj.empleado:
            usuario=User.objects.filter(id=obj.empleado.id) if User.objects.filter(id=obj.empleado.id) else None
            if usuario == None:
                return None

        return UserSerializer(usuario, many=True).data

    datos_responsable=   serializers.SerializerMethodField()
    def get_datos_responsable(self, obj):
        usuario=None
        if obj.responsable:
            usuario=User.objects.filter(id=obj.responsable.id) if User.objects.filter(id=obj.responsable.id) else None
            if usuario == None:
                return None

        return UserSerializer(usuario, many=True).data



    class Meta:
        model = on_off_bording_workflow
        fields = '__all__'

class on_off_bording_bloqueserializer(serializers.ModelSerializer):
    workflow_tareas = serializers.SerializerMethodField()
    #historial_list = Formal_Historial_Laboralserializer(many=True, read_only=True)
    #este es un campo many to many dentro de la tabla de formal_empleado


    def get_workflow_tareas(self, obj):
        tarea=on_off_bording_tarea.objects.filter(bloque=obj.id) if on_off_bording_tarea.objects.filter(bloque=obj.id)  else None
        if tarea == None:
           return None

        return on_off_bording_tareaserializer(tarea, many=True).data
    class Meta:
        model = on_off_bording_bloque
        fields = '__all__'

class on_off_bording_tareaserializer(serializers.ModelSerializer):
    datos_compa_guia=   serializers.SerializerMethodField()
    def get_datos_compa_guia(self, obj):
        usuario=None
        if obj.compa_guia:
            usuario=User.objects.filter(id=obj.compa_guia.id) if User.objects.filter(id=obj.compa_guia.id) else None
            if usuario == None:
                return None

        return UserSerializer(usuario, many=True).data
    archivo_gestor  =serializers.SerializerMethodField()
    def get_archivo_gestor(self,obj):
        if obj ==None:
            return None
        if obj.archivos_gestor==None:
            return None
        Archivo_gestor=archivos_gestor.objects.filter(id=obj.archivos_gestor.id) if archivos_gestor.objects.filter(id=obj.archivos_gestor.id) else None
        
        if Archivo_gestor==None:
            return None
        return archivos_gestorserializer(Archivo_gestor, many=True).data

    class Meta:
        model = on_off_bording_tarea
        fields = '__all__'


class on_off_bording_bienvenidaserializer(serializers.ModelSerializer):
    class Meta:
        model = on_off_bording_bienvenida
        fields = '__all__'
