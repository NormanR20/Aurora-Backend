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

class descriptor_perfil_datos_generalesserializer(serializers.ModelSerializer):
    
    list_empresa = serializers.SerializerMethodField()
    def get_list_empresa(self, obj):
        
        organizcion = Funcional_Organizacion.objects.filter(id=obj.empresa_id) if Funcional_Organizacion.objects.filter(id=obj.empresa_id)  else None
        if organizcion == None:
           return None
        return Funcional_Organizacionserializer(organizcion, many=True).data
    
    list_division = serializers.SerializerMethodField()
    def get_list_division(self, obj):
        division = Funcional_Division.objects.filter(id=obj.division_id) if Funcional_Division.objects.filter(id=obj.division_id)  else None
        if division == None:
           return None
        return Funcional_Divisionserializer(division, many=True).data
    
    list_proposito_general = serializers.SerializerMethodField()
    def get_list_proposito_general(self, obj):
        proposito_general = descriptor_perfil_proposito.objects.filter(id=obj.proposito_general_id) if descriptor_perfil_proposito.objects.filter(id=obj.proposito_general_id)  else None
        if proposito_general == None:
           return None
        return descriptor_perfil_propositoserializer(proposito_general, many=True).data
    
    list_clasificacion_empleado = serializers.SerializerMethodField()
    def get_list_clasificacion_empleado(self, obj):
        clasificacion = Funcional_Clasificacion.objects.filter(id=obj.clasificacion_empleado_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_empleado_id)  else None
        if clasificacion == None:
           return None
        return Funcional_Clasificacionserializer(clasificacion, many=True).data
    
    list_posicion = serializers.SerializerMethodField()
    def get_list_posicion(self, obj):
        posicion = Funcional_Funciones.objects.filter(id=obj.posicion_id) if Funcional_Funciones.objects.filter(id=obj.posicion_id)  else None
        if posicion == None:
           return None
        return Funcional_Funcionesserializer(posicion, many=True).data
    
    list_posiciones_sustitutas = serializers.SerializerMethodField()
    def get_list_posiciones_sustitutas(self, obj):
        # print(obj.posiciones_sustitutas.values_list)
        posiciones_sustitutas = obj.posiciones_sustitutas.values('id')
        # print(posiciones_sustitutas)
        lista_posiciones = []
        for x in posiciones_sustitutas:
            lista_posiciones.append(x['id'])
        # print('lista',lista_posiciones)
        funciones = Funcional_Funciones.objects.filter(id__in=lista_posiciones) if Funcional_Funciones.objects.filter(id__in=lista_posiciones)  else None
        if funciones == None:
           return None
        return Funcional_Funcionessserializer(funciones, many=True).data
    
    list_unidad_organizativa=serializers.SerializerMethodField()
    def get_list_unidad_organizativa(self, obj):
        # print(obj.posiciones_sustitutas.values_list)
        unidad = Funcional_Unidad_Organizativa.objects.filter(id=obj.unidad_organizativa_id) if Funcional_Unidad_Organizativa.objects.filter(id=obj.unidad_organizativa_id)  else None
        if unidad == None:
           return None
        return funcional_unidad_organizativabasicoserializer(unidad, many=True).data
        


    
    
  
    class Meta:
        model = descriptor_perfil_datos_generales
        fields = '__all__'


class descriptor_perfil_tipo_competenciaserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_tipo_competencia
        fields = '__all__'




class descriptor_perfil_competencia_totalserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_competencia_total
        fields = '__all__'

class descriptor_perfil_competenciaserializer(serializers.ModelSerializer):
    list_archivo  = serializers.SerializerMethodField()
    def get_list_archivo(self, obj):
        
        archivo = archivos_gestor_competencia.objects.filter(id=obj.archivo_id) if archivos_gestor_competencia.objects.filter(id=obj.archivo_id)  else None
        if archivo == None:
            return None
        return archivos_gestor_competenciaserializer(archivo, many=True).data

    list_tipo_competencia = serializers.SerializerMethodField()
    def get_list_tipo_competencia(self, obj):
        tipo_competencia = descriptor_perfil_tipo_competencia.objects.filter(id=obj.tipo_competencia_id) if descriptor_perfil_tipo_competencia.objects.filter(id=obj.tipo_competencia_id)  else None
        if tipo_competencia == None:
           return None
        return descriptor_perfil_tipo_competenciaserializer(tipo_competencia, many=True).data
    

    list_clasificacion = serializers.SerializerMethodField()
    def get_list_clasificacion(self, obj):
        clasificacion = Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id)  else None
        if clasificacion == None:
           return None
        return Funcional_Clasificacionserializer(clasificacion, many=True).data


    class Meta:
        model = descriptor_perfil_competencia
        fields = '__all__'

class archivos_gestor_competenciaserializer(serializers.ModelSerializer):
    class Meta:
        model = archivos_gestor_competencia
        fields = '__all__'


class descriptor_perfil_competencia_descriptorserializer(serializers.ModelSerializer):

    list_archivo  = serializers.SerializerMethodField()
    def get_list_archivo(self, obj):
        
        archivo = archivos_gestor_competencia.objects.filter(id=obj.archivo_id) if archivos_gestor_competencia.objects.filter(id=obj.archivo_id)  else None
        if archivo == None:
            return None
        return archivos_gestor_competenciaserializer(archivo, many=True).data
    
    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data

    list_competencia = serializers.SerializerMethodField()
    def get_list_competencia(self, obj):
        competencia = descriptor_perfil_competencia.objects.filter(id=obj.competencia_id) if descriptor_perfil_competencia.objects.filter(id=obj.competencia_id)  else None
        if competencia == None:
           return None
        return descriptor_perfil_competenciaserializer(competencia, many=True).data

    list_tipo_competencia = serializers.SerializerMethodField()
    def get_list_tipo_competencia(self, obj):
        tipo_competencia = descriptor_perfil_tipo_competencia.objects.filter(id=obj.tipo_competencia_id) if descriptor_perfil_tipo_competencia.objects.filter(id=obj.tipo_competencia_id)  else None
        if tipo_competencia == None:
           return None
        return descriptor_perfil_tipo_competenciaserializer(tipo_competencia, many=True).data
    
    list_area = serializers.SerializerMethodField()
    def get_list_area(self, obj):
        area = descriptor_perfil_area.objects.filter(id=obj.area_id) if descriptor_perfil_area.objects.filter(id=obj.area_id)  else None
        if area == None:
           return None
        return descriptor_perfil_areaserializer(area, many=True).data

    list_division = serializers.SerializerMethodField()
    def get_list_division(self, obj):
        division = Funcional_Division.objects.filter(id=obj.division_id) if Funcional_Division.objects.filter(id=obj.division_id)  else None
        if division == None:
           return None
        return Funcional_Divisionserializer(division, many=True).data
    
    list_Clasificacion = serializers.SerializerMethodField()
    def get_list_Clasificacion(self, obj):
        division = Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id)  else None
        if division == None:
           return None
        return Funcional_Clasificacionserializer(division, many=True).data
    
    
    

    class Meta:
        model = descriptor_perfil_competencia_descriptor
        fields = '__all__'


# class descriptor_perfil_competencia_descriptor_archivoserializer(serializers.ModelSerializer):
#     list_archivo  =serializers.SerializerMethodField()
#     def get_list_archivo(self,obj):
        
#         if obj ==None:
#             return None
#         if obj.archivo==None:
#             return None
#         Archivo_gestor=archivos_gestor.objects.filter(id=obj.archivo.id) if archivos_gestor.objects.filter(id=obj.archivo.id) else None
        
#         if Archivo_gestor==None:
#             return None
#         return archivos_gestorserializer(Archivo_gestor, many=True).data

#     list_competencia_descriptor = serializers.SerializerMethodField()
#     def get_list_competencia_descriptor(self, obj):
#         competencia_descriptor = descriptor_perfil_competencia_descriptor.objects.filter(id=obj.competencia_descriptor_id) if descriptor_perfil_competencia_descriptor.objects.filter(id=obj.competencia_descriptor_id)  else None
#         if competencia_descriptor == None:
#            return None
#         return descriptor_perfil_competencia_descriptorserializer(competencia_descriptor, many=True).data
#     class Meta:
#         model = descriptor_perfil_competencia_descriptor_archivo
#         fields = '__all__'



class descriptor_perfil_datos_unidad_medidaserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_datos_unidad_medida
        fields = '__all__'


class descriptor_perfil_areaserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_area
        fields = '__all__'


        

class descriptor_perfil_propositoserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_proposito
        fields = '__all__'


class descriptor_perfil_politicas_procedimientosserializer(serializers.ModelSerializer):
    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data
    
    list_archivo  =serializers.SerializerMethodField()
    def get_list_archivo(self,obj):
        if obj ==None:
            return None
        if obj.archivo==None:
            return None
        Archivo_gestor=archivos_gestor.objects.filter(id=obj.archivo.id) if archivos_gestor.objects.filter(id=obj.archivo.id) else None
        
        if Archivo_gestor==None:
            return None
        return archivos_gestorserializer(Archivo_gestor, many=True).data

    class Meta:
        model = descriptor_perfil_politicas_procedimientos
        fields = '__all__'


class descriptor_perfil_indicadorserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_indicador
        fields = '__all__'

class descriptor_perfil_indicador_descriptorserializer(serializers.ModelSerializer):
    list_indicador = serializers.SerializerMethodField()
    def get_list_indicador(self, obj):
              
        indicador = descriptor_perfil_indicador.objects.filter(id=obj.indicador_id) if descriptor_perfil_indicador.objects.filter(id=obj.indicador_id)  else None
        if indicador == None:
           return None
        return descriptor_perfil_indicadorserializer(indicador, many=True).data
    
    list_unidad_medida= serializers.SerializerMethodField()
    def get_list_unidad_medida(self, obj):
               
        unidad = descriptor_perfil_datos_unidad_medida.objects.filter(id=obj.unidad_medida_id) if descriptor_perfil_datos_unidad_medida.objects.filter(id=obj.unidad_medida_id)  else None
        if unidad == None:
           return None
        return descriptor_perfil_datos_unidad_medidaserializer(unidad, many=True).data  
    

    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data

    class Meta:
        model = descriptor_perfil_indicador_descriptor
        fields = '__all__'
        

class descriptor_perfil_preparacionserializer(serializers.ModelSerializer):
    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data

    list_curso = serializers.SerializerMethodField()
    def get_list_curso(self, obj):
        
        curso = descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter(id=obj.curso_id) if descriptor_perfil_cursos_diplomados_seminario_pasantia.objects.filter(id=obj.curso_id)  else None
        if curso == None:
           return None
        return descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(curso, many=True).data

        
    class Meta:
        model = descriptor_perfil_preparacion
        fields = '__all__'

class descriptor_perfil_formacionserializer(serializers.ModelSerializer):
    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data
    
    list_formacion = serializers.SerializerMethodField()
    def get_list_formacion(self, obj):
        
        formacion = descriptor_perfil_titulo.objects.filter(id=obj.formacion_id) if descriptor_perfil_titulo.objects.filter(id=obj.formacion_id)  else None
        if formacion == None:
           return None
        return descriptor_perfil_tituloserializer(formacion, many=True).data

    class Meta:
        model = descriptor_perfil_formacion
        fields = '__all__'


class descriptor_perfil_conocimiento_tecnico_adquiridoserializer(serializers.ModelSerializer):
    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data
    
    list_conocimiento = serializers.SerializerMethodField()
    def get_list_conocimiento(self, obj):
        
        conocimiento = descriptor_perfil_conocimiento_tecnico.objects.filter(id=obj.conocimiento_id) if descriptor_perfil_conocimiento_tecnico.objects.filter(id=obj.conocimiento_id)  else None
        if conocimiento == None:
           return None
        return descriptor_perfil_conocimiento_tecnicoserializer(conocimiento, many=True).data

    class Meta:
        model = descriptor_perfil_conocimiento_tecnico_adquirido
        fields = '__all__'

class descriptor_perfil_funcionserializer(serializers.ModelSerializer):
    list_unidad_medida = serializers.SerializerMethodField()
    def get_list_unidad_medida(self, obj):
        
        unidad = descriptor_perfil_datos_unidad_medida.objects.filter(id=obj.unidad_medida_id) if descriptor_perfil_datos_unidad_medida.objects.filter(id=obj.unidad_medida_id)  else None
        if unidad == None:
           return None
        return descriptor_perfil_datos_unidad_medidaserializer(unidad, many=True).data

    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data

    class Meta:
        model = descriptor_perfil_funcion
        fields = '__all__'

class descriptor_perfil_proposito_descriptorserializer(serializers.ModelSerializer):
    list_proposito = serializers.SerializerMethodField()
    def get_list_proposito(self, obj):
        
        proposito = descriptor_perfil_proposito.objects.filter(id=obj.proposito_id) if descriptor_perfil_proposito.objects.filter(id=obj.proposito_id)  else None
        if proposito == None:
           return None
        return descriptor_perfil_propositoserializer(proposito, many=True).data

    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data
    class Meta:
        model = descriptor_perfil_proposito_descriptor
        fields = '__all__'


class descriptor_perfil_experienciaserializer(serializers.ModelSerializer):
    list_descriptor = serializers.SerializerMethodField()
    def get_list_descriptor(self, obj):
        
        descriptor = descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id) if descriptor_perfil_datos_generales.objects.filter(id=obj.descriptor_id)  else None
        if descriptor == None:
           return None
        return descriptor_perfil_datos_generalesserializer(descriptor, many=True).data
        
    class Meta:
        model = descriptor_perfil_experiencia
        fields = '__all__'

class descriptor_perfil_experiencia_seleccion_serializer(serializers.ModelSerializer):
        
    class Meta:
        model = descriptor_perfil_experiencia
        fields = '__all__'

class descriptor_perfil_descriptor_generoserializer(serializers.ModelSerializer):
        
    class Meta:
        model = descriptor_perfil_datos_generales
        fields = ['genero']

class descriptor_perfil_descriptor_divisionserializer(serializers.ModelSerializer):
    list_departamento = serializers.SerializerMethodField()
    def get_list_departamento(self, obj):
        
        division = Funcional_Division.objects.filter(id=obj.division_id) if Funcional_Division.objects.filter(id=obj.division_id)  else None
        if division == None:
           return None
        return Funcional_Divisionserializer(division, many=True).data

    class Meta:
        model = descriptor_perfil_datos_generales
        fields = ['list_departamento']

class descriptor_perfil_formacion_seleccionserializer(serializers.ModelSerializer):
    
    list_formacion = serializers.SerializerMethodField()
    def get_list_formacion(self, obj):
        
        formacion = descriptor_perfil_titulo.objects.filter(id=obj.formacion_id) if descriptor_perfil_titulo.objects.filter(id=obj.formacion_id)  else None
        if formacion == None:
           return None
        return descriptor_perfil_tituloserializer(formacion, many=True).data

    class Meta:
        model = descriptor_perfil_formacion
        fields = '__all__'


class descriptor_perfil_datos_generalessserializer(serializers.ModelSerializer):
    
    list_empresa = serializers.SerializerMethodField()
    def get_list_empresa(self, obj):
        
        organizcion = Funcional_Organizacion.objects.filter(id=obj.empresa_id) if Funcional_Organizacion.objects.filter(id=obj.empresa_id)  else None
        if organizcion == None:
           return None
        return Funcional_Organizacionserializer(organizcion, many=True).data
    
    list_division = serializers.SerializerMethodField()
    def get_list_division(self, obj):
        division = Funcional_Division.objects.filter(id=obj.division_id) if Funcional_Division.objects.filter(id=obj.division_id)  else None
        if division == None:
           return None
        return Funcional_Divisionserializer(division, many=True).data
    
    list_proposito_general = serializers.SerializerMethodField()
    def get_list_proposito_general(self, obj):
        proposito_general = descriptor_perfil_proposito.objects.filter(id=obj.proposito_general_id) if descriptor_perfil_proposito.objects.filter(id=obj.proposito_general_id)  else None
        if proposito_general == None:
           return None
        return descriptor_perfil_propositoserializer(proposito_general, many=True).data
    
    list_clasificacion_empleado = serializers.SerializerMethodField()
    def get_list_clasificacion_empleado(self, obj):
        clasificacion = Funcional_Clasificacion.objects.filter(id=obj.clasificacion_empleado_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_empleado_id)  else None
        if clasificacion == None:
           return None
        return Funcional_Clasificacionserializer(clasificacion, many=True).data
    
    list_posicion = serializers.SerializerMethodField()
    def get_list_posicion(self, obj):
        
        posicion = Funcional_Funciones.objects.filter(id=obj.posicion_id) if Funcional_Funciones.objects.filter(id=obj.posicion_id)  else None
        if posicion == None:
           return None
        return Funcional_Funcionesserializer(posicion, many=True).data
    
    list_posiciones_sustitutas = serializers.SerializerMethodField()
    def get_list_posiciones_sustitutas(self, obj):
        # print(obj.posiciones_sustitutas.values_list)
        posiciones_sustitutas = obj.posiciones_sustitutas.values('id')
        # print(posiciones_sustitutas)
        lista_posiciones = []
        for x in posiciones_sustitutas:
            lista_posiciones.append(x['id'])
        # print('lista',lista_posiciones)
        funciones = Funcional_Funciones.objects.filter(id__in=lista_posiciones) if Funcional_Funciones.objects.filter(id__in=lista_posiciones)  else None
        if funciones == None:
           return None
        return Funcional_Funcionessserializer(funciones, many=True).data

    list_posicion = serializers.SerializerMethodField()
    def get_list_posicion(self, obj):
        
        posicion = Funcional_Funciones.objects.filter(id=obj.posicion_id) if Funcional_Funciones.objects.filter(id=obj.posicion_id)  else None
        if posicion == None:
           return None
        return Funcional_Funcionesserializer(posicion, many=True).data
    
    list_experiencia = serializers.SerializerMethodField()
    def get_list_experiencia(self, obj):
        
        experiencia = descriptor_perfil_experiencia.objects.filter(descriptor=obj.pk) if descriptor_perfil_experiencia.objects.filter(descriptor=obj.pk)  else None
        if experiencia == None:
           return None
        return descriptor_perfil_experiencia_seleccion_serializer(experiencia, many=True).data

    list_formacion = serializers.SerializerMethodField()
    def get_list_formacion(self, obj):
        
        formacion = descriptor_perfil_formacion.objects.filter(descriptor=obj.pk) if descriptor_perfil_formacion.objects.filter(descriptor=obj.pk)  else None
        if formacion == None:
           return None
        return descriptor_perfil_formacion_seleccionserializer(formacion, many=True).data
    
  
    class Meta:
        model = descriptor_perfil_datos_generales
        fields = '__all__'
