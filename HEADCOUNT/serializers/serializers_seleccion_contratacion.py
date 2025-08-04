from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields import files
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import models
from rest_framework.utils import field_mapping
#from ..serializers import *
from ..models import *
from django.contrib.auth.models import User,Group
from django.db.models import Count
from ..serializers import *

class seleccion_contratacion_motivoserializer(serializers.ModelSerializer):
    class Meta:
        model = seleccion_contratacion_motivo
        fields = '__all__'


class seleccion_contratacion_postulante_plazaserializer(serializers.ModelSerializer):
    list_plaza = serializers.SerializerMethodField()
    def get_list_plaza(self, obj):
        
        plaza = seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=obj.plaza_id) if seleccion_contratacion_solicitud_plaza_vacante.objects.filter(id=obj.plaza_id) else None
        if plaza == None:
           return None
        return seleccion_contratacion_solicitud_plaza_vacanteserializer(plaza, many=True).data
    
    list_estado = serializers.SerializerMethodField()
    def get_list_estado(self, obj):
      
        estado = seleccion_contratacion_estado.objects.filter(id=obj.estado_id) if seleccion_contratacion_estado.objects.filter(id=obj.estado_id) else None
        if estado == None:
           return None
        return seleccion_contratacion_estadoserializer(estado, many=True).data
    
    list_preparacion = serializers.SerializerMethodField()
    def get_list_preparacion(self, obj):
    
        # print(dir(obj))
        preparacion = descriptor_perfil_titulo.objects.filter(id=obj.profesion_id) if descriptor_perfil_titulo.objects.filter(id=obj.profesion_id) else None
        if preparacion == None:
           return None
        return descriptor_perfil_tituloserializer(preparacion, many=True).data
        
    class Meta:
        model = seleccion_contratacion_postulante_plaza
        fields = '__all__'

class seleccion_contratacion_paisserializer(serializers.ModelSerializer):
    
    class Meta:
        model = seleccion_contratacion_pais
        fields = '__all__'

class seleccion_contratacion_estadoserializer(serializers.ModelSerializer):
    
    class Meta:
        model = seleccion_contratacion_estado
        fields = '__all__'



class seleccion_contratacion_solicitud_plaza_vacanteserializer(serializers.ModelSerializer):
    list_creador_plaza = serializers.SerializerMethodField()
    def get_list_creador_plaza(self, obj):
        
        creador = User.objects.filter(id=obj.creador_plaza_id) if User.objects.filter(id=obj.creador_plaza_id) else None
        if creador == None:
           return None
        return UsuariosSerializer(creador, many=True).data
        

    list_pais = serializers.SerializerMethodField()
    def get_list_pais(self, obj):
      
        pais = seleccion_contratacion_pais.objects.filter(id=obj.pais_id) if seleccion_contratacion_pais.objects.filter(id=obj.pais_id) else None
        if pais == None:
           return None
        return seleccion_contratacion_paisserializer(pais, many=True).data
    
    list_estado = serializers.SerializerMethodField()
    def get_list_estado(self, obj):
      
        estado = seleccion_contratacion_estado.objects.filter(id=obj.estado_id) if seleccion_contratacion_estado.objects.filter(id=obj.estado_id) else None
        if estado == None:
           return None
        return seleccion_contratacion_estadoserializer(estado, many=True).data

    list_motivo = serializers.SerializerMethodField()
    def get_list_motivo(self, obj):
        motivo = seleccion_contratacion_motivo.objects.filter(id=obj.motivo_id) if seleccion_contratacion_motivo.objects.filter(id=obj.motivo_id) else None
        if motivo == None:
           return None
        return seleccion_contratacion_motivoserializer(motivo, many=True).data
    
    list_departamento = serializers.SerializerMethodField()
    def get_list_departamento(self, obj):
        departamento = Funcional_Division.objects.filter(id=obj.departamento_id) if Funcional_Division.objects.filter(id=obj.departamento_id) else None
        if departamento == None:
           return None
        return Funcional_Divisionserializer(departamento, many=True).data

    list_puesto = serializers.SerializerMethodField()
    def get_list_puesto(self, obj):
        posicion = Funcional_Puesto.objects.filter(id=obj.posicion_id) if Funcional_Puesto.objects.filter(id=obj.posicion_id) else None
        if posicion == None:
           return None
        return funcional_puestoserializer(posicion, many=True).data

    list_genero = serializers.SerializerMethodField()
    def get_list_genero(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=obj.funcion_id)   if descriptor_perfil_datos_generales.objects.filter(posicion=obj.funcion_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_descriptor_generoserializer(descriptor, many=True).data
    
    # list_division = serializers.SerializerMethodField()
    # def get_list_division(self, obj):
        
    #     descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=obj.funcion_id).values_list('division_id',flat=True) if descriptor_perfil_datos_generales.objects.filter(posicion=obj.funcion_id) else None
    #     if descriptor == None:
    #        return None
    #     division= Funcional_Division.objects.filter(id__in=descriptor) if Funcional_Division.objects.filter(id__in=descriptor) else None
    #     if division == None:
    #        return None
    #     return Funcional_Divisionserializer(division, many=True).data
    #     return 0
    
  
        
    list_experiencia = serializers.SerializerMethodField()
    def get_list_experiencia(self, obj):
        
        experiencia = descriptor_perfil_experiencia.objects.filter(descriptor__posicion=obj.funcion_id) if descriptor_perfil_experiencia.objects.filter(descriptor__posicion=obj.funcion_id)  else None
        if experiencia == None:
           return None
        return descriptor_perfil_experiencia_seleccion_serializer(experiencia, many=True).data

    list_formacion = serializers.SerializerMethodField()
    def get_list_formacion(self, obj):
        
        formacion = descriptor_perfil_formacion.objects.filter(descriptor__posicion=obj.funcion_id) if descriptor_perfil_formacion.objects.filter(descriptor__posicion=obj.funcion_id)  else None
        if formacion == None:
           return None
        return descriptor_perfil_formacion_seleccionserializer(formacion, many=True).data
    
    list_funcion = serializers.SerializerMethodField()
    def get_list_funcion(self, obj):
        
        funcion = Funcional_Funciones.objects.filter(id=obj.funcion_id) if Funcional_Funciones.objects.filter(id=obj.funcion_id)  else None
        if funcion == None:
           return None
        return Funcional_Funcionesserializer(funcion, many=True).data

    list_responsable_seguimiento_plaza = serializers.SerializerMethodField()
    def get_list_responsable_seguimiento_plaza(self, obj):
        
        creador = User.objects.filter(id=obj.responsable_seguimiento_plaza_id) if User.objects.filter(id=obj.responsable_seguimiento_plaza_id) else None
        if creador == None:
           return None
        return UsuariosSerializer(creador, many=True).data
        
    class Meta:
        model = seleccion_contratacion_solicitud_plaza_vacante
        fields = '__all__'



