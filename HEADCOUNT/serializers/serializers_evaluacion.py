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
from django.db.models import F
from decimal import Decimal, ROUND_HALF_UP



class evaluacion_frecuenciaserializer(serializers.ModelSerializer):
    class Meta:
        model = evaluacion_frecuencia
        fields = '__all__'

class evaluacion_tipo_plan_accionserializer(serializers.ModelSerializer):
    class Meta:
        model = evaluacion_tipo_plan_accion
        fields = '__all__'        



class evaluacion_competenciaserializer(serializers.ModelSerializer):
    list_competencia=serializers.SerializerMethodField()
    def get_list_competencia(self, obj):
        competencia = descriptor_perfil_competencia.objects.filter(id=obj.competencia_id) if descriptor_perfil_competencia.objects.filter(id=obj.competencia_id)  else None
        if competencia == None:
            return None
        return descriptor_perfil_competenciaserializer(competencia, many=True).data

    list_clasificacion=serializers.SerializerMethodField()
    def get_list_clasificacion(self, obj):
        clasificacion = Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id)  else None
        if clasificacion == None:
            return None
        return Funcional_Clasificacionserializer(clasificacion, many=True).data



    class Meta:
        model = evaluacion_competencia
        fields = '__all__'

class evaluacion_metrica_competenciaserializer(serializers.ModelSerializer):
    list_periodicidad  = serializers.SerializerMethodField()
    def get_list_periodicidad(self, obj):
        periodicidad = evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id)  else None
        if periodicidad == None:
            return None
        return evaluacion_periodicidadserializer(periodicidad, many=True).data
    class Meta:
        model = evaluacion_metrica_competencia
        fields = '__all__'
        

class evaluacion_factorserializer(serializers.ModelSerializer):
    
    list_clasificacion=serializers.SerializerMethodField()
    def get_list_clasificacion(self, obj):
        clasificacion = Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id)  else None
        if clasificacion == None:
            return None
        return Funcional_Clasificacionserializer(clasificacion, many=True).data

    list_periodicidad  = serializers.SerializerMethodField()
    def get_list_periodicidad(self, obj):
        periodicidad = evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id)  else None
        if periodicidad == None:
            return None
        return evaluacion_periodicidadserializer(periodicidad, many=True).data
    
    class Meta:
        model = evaluacion_factor
        fields = '__all__'


class evaluacion_tipo_evaluacionserializer(serializers.ModelSerializer):
    class Meta:
        model = evaluacion_tipo_evaluacion
        fields = '__all__'

class evaluacion_metrica_factorserializer(serializers.ModelSerializer):

    list_factor  = serializers.SerializerMethodField()
    def get_list_factor(self, obj):
        
        factor = evaluacion_factor.objects.filter(id=obj.factor_id) if evaluacion_factor.objects.filter(id=obj.factor_id)  else None
        if factor == None:
            return None
        return evaluacion_factorserializer(factor, many=True).data
    
    list_periodicidad  = serializers.SerializerMethodField()
    def get_list_periodicidad(self, obj):
        periodicidad = evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id)  else None
        if periodicidad == None:
            return None
        return evaluacion_periodicidadserializer(periodicidad, many=True).data
        
    class Meta:
        model = evaluacion_metrica_factor
        fields = '__all__'

class evaluacion_periodicidadserializer(serializers.ModelSerializer):
    list_empresa  = serializers.SerializerMethodField()
    def get_list_empresa(self, obj):
        empresa = Funcional_Organizacion.objects.filter(id=obj.empresa_id) if Funcional_Organizacion.objects.filter(id=obj.empresa_id)  else None
        if empresa == None:
            return None
        return Funcional_Organizacionserializer(empresa, many=True).data
    
    list_frecuencia  = serializers.SerializerMethodField()
    def get_list_frecuencia(self, obj):
        
        frecuencia = evaluacion_frecuencia.objects.filter(id=obj.frecuencia_id) if evaluacion_frecuencia.objects.filter(id=obj.frecuencia_id)  else None
        if frecuencia == None:
            return None
        return evaluacion_frecuenciaserializer(frecuencia, many=True).data

    list_evaluacion_configuracion_periodo = serializers.SerializerMethodField()
    def get_list_evaluacion_configuracion_periodo(self, obj):
        
        periodo = evaluacion_configuracion_periodo.objects.filter(periodicidad=obj.id) if evaluacion_configuracion_periodo.objects.filter(periodicidad=obj.id)  else None
        if periodo == None:
            return None
        return evaluacion_configuracion_periodossserializer(periodo, many=True).data

    


    class Meta:
        model = evaluacion_periodicidad
        fields = '__all__'
        



class evaluacion_archivo_plan_accion_gestorserializer(serializers.ModelSerializer):
    class Meta:
        model = evaluacion_archivo_plan_accion_gestor
        fields = '__all__'


class categoria_desempenoserializer(serializers.ModelSerializer):
    list_periodicidad  = serializers.SerializerMethodField()
    def get_list_periodicidad(self, obj):
        periodicidad = evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id)  else None
        if periodicidad == None:
            return None
        return evaluacion_periodicidadserializer(periodicidad, many=True).data
    class Meta:
        model = categoria_desempeno
        fields = '__all__'

class evaluacion_configuracion_periodossserializer(serializers.ModelSerializer):
    
    class Meta:
        model = evaluacion_configuracion_periodo
        fields = '__all__'

class evaluacion_configuracion_periodoserializer(serializers.ModelSerializer):
    list_periodicidad  = serializers.SerializerMethodField()
    def get_list_periodicidad(self, obj):
        periodicidad = evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id)  else None
        if periodicidad == None:
            return None
        return evaluacion_periodicidadserializer(periodicidad, many=True).data
    
    list_tipo_evaluacion  = serializers.SerializerMethodField()
    def get_list_tipo_evaluacion(self, obj):
        
        tipo_evaluacion = evaluacion_tipo_evaluacion.objects.filter(id=obj.tipo_evaluacion_id) if evaluacion_tipo_evaluacion.objects.filter(id=obj.tipo_evaluacion_id)  else None
        if tipo_evaluacion == None:
            return None
        return evaluacion_tipo_evaluacionserializer(tipo_evaluacion, many=True).data

    class Meta:
        model = evaluacion_configuracion_periodo
        fields = '__all__'

class evaluacion_factor_plantilla_encabezadoserializer(serializers.ModelSerializer):
    list_plantilla_factor=serializers.SerializerMethodField()
    def get_list_plantilla_factor(self,obj):
        funcion = evaluacion_plantilla_factor.objects.filter(factor_plantilla_encabezado=obj.id) if evaluacion_plantilla_factor.objects.filter(factor_plantilla_encabezado=obj.id)  else None
        if funcion == None:
            return None
        return evaluacion_plantilla_factorserializer(funcion, many=True).data

    list_periodicidad =serializers.SerializerMethodField()
    def get_list_periodicidad(self,obj):
        periodicidad=evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) else None 
        if periodicidad==None:
            return None 
        return evaluacion_periodicidadserializer(periodicidad,many=True).data
        
    class Meta:
        model = evaluacion_factor_plantilla_encabezado
        fields = '__all__'
    

class evaluacion_competencia_plantilla_encabezadoserializer(serializers.ModelSerializer):
    list_periodicidad =serializers.SerializerMethodField()
    def get_list_periodicidad(self,obj):
        periodicidad=evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) else None 
        if periodicidad==None:
            return None 
        return evaluacion_periodicidadserializer(periodicidad,many=True).data
    
    list_plantilla_competencia=serializers.SerializerMethodField()
    def get_list_plantilla_competencia(self,obj):
        funcion = evaluacion_plantilla_competencia.objects.filter(competencia_plantilla_encabezado=obj.id) if evaluacion_plantilla_competencia.objects.filter(competencia_plantilla_encabezado=obj.id)  else None
        if funcion == None:
            return None
        return evaluacion_plantilla_competenciaserializer(funcion, many=True).data
    class Meta:
        model = evaluacion_competencia_plantilla_encabezado
        fields = '__all__'


class evaluacion_plantilla_competenciaserializer(serializers.ModelSerializer):
    list_funcion=serializers.SerializerMethodField()
    def get_list_funcion(self,obj):
        funcion = Funcional_Funciones.objects.filter(id=obj.posicion_id) if Funcional_Funciones.objects.filter(id=obj.posicion_id)  else None
        if funcion == None:
            return None
        return Funcional_Funcionesserializer(funcion, many=True).data

    list_competencia_descriptor=serializers.SerializerMethodField()
    def get_list_competencia_descriptor(self,obj):
        competencia = descriptor_perfil_competencia_descriptor.objects.filter(id=obj.competencia_descriptor_id) if descriptor_perfil_competencia_descriptor.objects.filter(id=obj.competencia_descriptor_id)  else None
        if competencia == None:
            return None
        return descriptor_perfil_competencia_descriptorserializer(competencia, many=True).data

    list_competencia=serializers.SerializerMethodField()
    def get_list_competencia(self,obj):
        competencia = descriptor_perfil_competencia.objects.filter(id=obj.competencia_id) if descriptor_perfil_competencia.objects.filter(id=obj.competencia_id)  else None
        if competencia == None:
            return None
        return descriptor_perfil_competenciaserializer(competencia, many=True).data


    list_clasificacion=serializers.SerializerMethodField()
    def get_list_clasificacion(self, obj):
        clasificacion = Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id)  else None
        if clasificacion == None:
            return None
        return Funcional_Clasificacionserializer(clasificacion, many=True).data

    list_periodicidad =serializers.SerializerMethodField()
    def get_list_periodicidad(self,obj):
        periodicidad=evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) else None 
        if periodicidad==None:
            return None 
        return evaluacion_periodicidadserializer(periodicidad,many=True).data

    class Meta:
        model = evaluacion_plantilla_competencia
        fields = '__all__'



class evaluacion_encabezadoserializer(serializers.ModelSerializer):
    
    listado_evaluaciones=serializers.SerializerMethodField()
    def get_listado_evaluaciones(self,obj):
        evaluaciones_competencia = evaluacion_encabezado.objects.filter(periodicidad=obj.periodicidad_id,periodo=obj.periodo,tipo_evaluacion_encabezado=1,evaluado=obj.evaluado_id,tipo_evaluacion=obj.tipo_evaluacion).values_list('id') if evaluacion_encabezado.objects.filter(periodicidad=obj.periodicidad_id,periodo=obj.periodo,tipo_evaluacion_encabezado=1,evaluado=obj.evaluado_id).values_list('id') else None
        evaluaciones_factor = evaluacion_encabezado.objects.filter(periodicidad=obj.periodicidad_id,periodo=obj.periodo,tipo_evaluacion_encabezado=2,evaluado=obj.evaluado_id,tipo_evaluacion=obj.tipo_evaluacion).values_list('id') if evaluacion_encabezado.objects.filter(periodicidad=obj.periodicidad_id,periodo=obj.periodo,tipo_evaluacion_encabezado=1,evaluado=obj.evaluado_id).values_list('id') else None
        data={'evaluaciones_competencia':evaluaciones_competencia,'evaluaciones_factor':evaluaciones_factor}
        return data

    list_nota_total=serializers.SerializerMethodField()
    def get_list_nota_total(self,obj):
        nota= calculo_nota_puntuacion_total(obj.id)
        nota_f = Decimal(nota).quantize(0, ROUND_HALF_UP)  
        return nota_f

    list_nota_total_desempenio=serializers.SerializerMethodField()
    def get_list_nota_total_desempenio(self,obj):
        total_desempenio_f= calculo_nota_puntuacion_total(obj.id)
        total_desempenio= Decimal(total_desempenio_f).quantize(0, ROUND_HALF_UP) 
        desempenio = (categoria_desempeno.objects.filter(periodicidad=obj.periodicidad_id,valor_minimo__lte=total_desempenio, valor_maximo__gte=total_desempenio).values('descripcion'))[0]['descripcion'] if (categoria_desempeno.objects.filter(periodicidad=obj.periodicidad_id,valor_minimo__lte=total_desempenio, valor_maximo__gte=total_desempenio).values('descripcion')) else 'Sin categorizaciòn'
        return desempenio



    list_evaluado=serializers.SerializerMethodField()
    def get_list_evaluado(self,obj):
        evaluado = Funcional_empleado.objects.filter(id=obj.evaluado_id) if Funcional_empleado.objects.filter(id=obj.evaluado_id) else None
        if evaluado ==None:
            return None
        return Funcional_empleadoserializer(evaluado,many=True).data  

    list_responsable=serializers.SerializerMethodField()
    def get_list_responsable(self,obj):
        responsable = Funcional_empleado.objects.filter(id=obj.responsable_directo_id) if Funcional_empleado.objects.filter(id=obj.responsable_directo_id) else None
        if responsable ==None:
            return None
        return Funcional_empleadoserializer(responsable,many=True).data 

    list_evaluador=serializers.SerializerMethodField()
    def get_list_evaluador(self,obj):
        evaluador = Funcional_empleado.objects.filter(id=obj.evaluador_id) if Funcional_empleado.objects.filter(id=obj.evaluador_id) else None
        if evaluador ==None:
            return None
        return Funcional_empleadoserializer(evaluador,many=True).data 

    list_tipo_evaluacion =serializers.SerializerMethodField()
    def get_list_tipo_evaluacion(self,obj):
        tipo_evaluacion=evaluacion_tipo_evaluacion.objects.filter(id=obj.tipo_evaluacion_id) if evaluacion_tipo_evaluacion.objects.filter(id=obj.tipo_evaluacion_id) else None 
        if tipo_evaluacion==None:
            return None 
        return evaluacion_tipo_evaluacionserializer(tipo_evaluacion,many=True).data

    list_periodicidad =serializers.SerializerMethodField()
    def get_list_periodicidad(self,obj):
        periodicidad=evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) else None 
        if periodicidad==None:
            return None 
        return evaluacion_periodicidadserializer(periodicidad,many=True).data

    list_evaluacion_tipo_plan_accion=serializers.SerializerMethodField()
    def get_list_evaluacion_tipo_plan_accion(self,obj):
        tipo_plan_accion=evaluacion_tipo_plan_accion.objects.filter(id=obj.tipo_plan_accion_id) if evaluacion_tipo_plan_accion.objects.filter(id=obj.tipo_plan_accion_id) else None 
        if tipo_plan_accion==None:
            return None 
        return evaluacion_tipo_plan_accionserializer(tipo_plan_accion,many=True).data



    list_evaluacion_archivo_plan_accion_gestor=serializers.SerializerMethodField()
    def get_list_evaluacion_archivo_plan_accion_gestor(self,obj):
        
        archivo=evaluacion_archivo_plan_accion_gestor.objects.filter(id=obj.evaluacion_archivo_plan_accion_gestor_id) if evaluacion_archivo_plan_accion_gestor.objects.filter(id=obj.evaluacion_archivo_plan_accion_gestor_id) else None 
        if archivo==None:
            return None 
        return evaluacion_archivo_plan_accion_gestorserializer(archivo,many=True).data

    list_validacion_respuestas =serializers.SerializerMethodField()
    def get_list_validacion_respuestas(self,obj):
        if obj.tipo_evaluacion_encabezado==2:
            validacion=validacion_evaluacion_factor(obj.id)
        else: 
            validacion=validacion_evaluacion_competencia(obj.id) 
        return validacion

    list_evaluacion_configuracion_periodo = serializers.SerializerMethodField()
    def get_list_evaluacion_configuracion_periodo(self, obj):
        
        periodo = evaluacion_configuracion_periodo.objects.filter(periodicidad=obj.periodicidad_id,periodo=obj.periodo) if evaluacion_configuracion_periodo.objects.filter(periodicidad=obj.periodicidad_id,periodo=obj.periodo)  else None
        if periodo == None:
            return None
        return evaluacion_configuracion_periodossserializer(periodo, many=True).data

    class Meta:      
        model =evaluacion_encabezado
        fields = "__all__"




class evaluacion_plantilla_factorserializer(serializers.ModelSerializer):

    list_posicion  = serializers.SerializerMethodField()
    def get_list_posicion(self, obj):
        
        posicion = Funcional_Funciones.objects.filter(id=obj.posicion_id) if Funcional_Funciones.objects.filter(id=obj.posicion_id)  else None
        if posicion == None:
            return None
        return Funcional_Funcionesserializer(posicion, many=True).data

    list_factor  = serializers.SerializerMethodField()
    def get_list_factor(self, obj):
        
        factor = evaluacion_factor.objects.filter(id=obj.factor_id) if evaluacion_factor.objects.filter(id=obj.factor_id)  else None
        if factor == None:
            return None
        return evaluacion_factorserializer(factor, many=True).data

    list_periodicidad =serializers.SerializerMethodField()
    def get_list_periodicidad(self,obj):
        periodicidad=evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) else None 
        if periodicidad==None:
            return None 
        return evaluacion_periodicidadserializer(periodicidad,many=True).data

    list_clasificacion=serializers.SerializerMethodField()
    def get_list_clasificacion(self, obj):
        clasificacion = Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_id)  else None
        if clasificacion == None:
            return None
        return Funcional_Clasificacionserializer(clasificacion, many=True).data


    class Meta:
        model = evaluacion_plantilla_factor
        fields = '__all__'


class monitor_colaboradoresserializer(serializers.ModelSerializer):
    list_pruebas_realizadas  = serializers.SerializerMethodField()
    def get_list_pruebas_realizadas(self, obj):
        
        total_factor= evaluacion_encabezado.objects.filter(evaluado=obj.id).filter(tipo_evaluacion_encabezado=1).exclude(nota_total_porcentaje=None).count()
        total_competencia= evaluacion_encabezado.objects.filter(evaluado=obj.id).filter(tipo_evaluacion_encabezado=2).exclude(nota_total_porcentaje=None).count()
        return (int(total_factor) + int(total_competencia)) / 2

    total_pruebas = serializers.SerializerMethodField()
    def get_total_pruebas(self, obj):
        
        total_factor= evaluacion_encabezado.objects.filter(evaluado=obj.id).filter(tipo_evaluacion_encabezado=1).count()
       
        return total_factor

    empresa=serializers.SerializerMethodField()
    def get_empresa(self, obj):
        empresa=Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__sociedad_financiera__nombre',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if empresa == None:
           return None
        
        return empresa

    Division_List= serializers.SerializerMethodField()
    def get_Division_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('division__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fd=Funcional_Division.objects.filter(id__in=fe) if Funcional_Division.objects.filter(id__in=fe) else None
        if  fd==None:
            return None
        return Funcional_Divisionserializer(fd, many=True).data
    
    Unidad_Organizativa_List=serializers.SerializerMethodField()
    def get_Unidad_Organizativa_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fuo=Funcional_Unidad_Organizativa.objects.filter(id__in=fe) if Funcional_Unidad_Organizativa.objects.filter(id__in=fe) else None
        if fuo==None:
            return None
        return funcional_unidad_organizativabasicoserializer(fuo,many=True).data
    
    list_jefe_inmediato = serializers.SerializerMethodField()
    def get_list_jefe_inmediato(self,obj):
        jefe= Funcional_empleado.objects.filter(codigo=obj.jefe_inmediato) if Funcional_empleado.objects.filter(jefe_inmediato=obj.jefe_inmediato) else None
        if jefe==None:
            return None
        return Funcional_empleadoserializer(jefe, many=True).data

    
    list_puesto = serializers.SerializerMethodField()
    def get_list_puesto(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('puesto__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fp=Funcional_Puesto.objects.filter(id__in=fe) if Funcional_Puesto.objects.filter(id__in=fe) else None
        if fp==None:
            return None
        return funcional_puestoserializer(fp,many=True).data
    
    list_funcion=serializers.SerializerMethodField()
    def get_list_funcion(elf,obj):
        ff= Funcional_empleado.objects.filter(id=obj.id).values_list('posicion__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if ff==None:
            return None

        funcion = Funcional_Funciones.objects.filter(id__in=ff) if Funcional_Funciones.objects.filter(id__in=ff)  else None
        if funcion == None:
            return None
        return Funcional_Funcionesserializer(funcion, many=True).data
    
    empresa_id=serializers.SerializerMethodField()
    def get_empresa_id(self, obj):
        empresa=Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__sociedad_financiera',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if empresa == None:
           return None
        
        return empresa
    
    class Meta:
        model = Funcional_empleado
        fields = '__all__'

class detalle_evaluacion_factorserializer(serializers.ModelSerializer):

    list_encabezado  = serializers.SerializerMethodField()
    def get_list_encabezado(self, obj):
        
        encabezado = evaluacion_encabezado.objects.filter(id=obj.encabezado_id) if evaluacion_encabezado.objects.filter(id=obj.encabezado_id)  else None
        if encabezado == None:
            return None
        return evaluacion_encabezadoserializer(encabezado, many=True).data
    

    list_metrica_factor  = serializers.SerializerMethodField()
    def get_list_metrica_factor(self, obj):
        
        metrica_factor = evaluacion_metrica_factor.objects.filter(id=obj.metrica_factor_id) if evaluacion_metrica_factor.objects.filter(id=obj.metrica_factor_id)  else None
        if metrica_factor == None:
            return None
        return evaluacion_metrica_factorserializer(metrica_factor, many=True).data


    list_evaluacion_plantilla_competencia  = serializers.SerializerMethodField()
    def get_list_evaluacion_plantilla_competencia(self, obj):
        
        plantilla_competencia = evaluacion_plantilla_competencia.objects.filter(id=obj.evaluacion_plantilla_competencia_id) if evaluacion_plantilla_competencia.objects.filter(id=obj.evaluacion_plantilla_competencia_id)  else None
        if plantilla_competencia == None:
            return None
        return evaluacion_plantilla_competenciaserializer(factor, many=True).data


    class Meta:
        model = detalle_evaluacion_factor
        fields = '__all__'

class detalle_evaluacion_factor_indicadorserializer(serializers.ModelSerializer):

    list_encabezado  = serializers.SerializerMethodField()
    def get_list_encabezado(self, obj):
        
        encabezado = evaluacion_encabezado.objects.filter(id=obj.encabezado_id) if evaluacion_encabezado.objects.filter(id=obj.encabezado_id)  else None
        if encabezado == None:
            return None
        return evaluacion_encabezadoserializer(encabezado, many=True).data
    
    list_factor  = serializers.SerializerMethodField()
    def get_list_factor(self, obj):
        
        factor = evaluacion_factor.objects.filter(id=obj.factor_id) if evaluacion_factor.objects.filter(id=obj.factor_id)  else None
        if factor == None:
            return None
        return evaluacion_factorserializer(factor, many=True).data
    

    list_metrica_factor  = serializers.SerializerMethodField()
    def get_list_metrica_factor(self, obj):
        
        metrica_factor = evaluacion_metrica_factor.objects.filter(id=obj.metrica_factor_id) if evaluacion_metrica_factor.objects.filter(id=obj.metrica_factor_id)  else None
        if metrica_factor == None:
            return None
        return evaluacion_metrica_factorserializer(metrica_factor, many=True).data


    list_evaluacion_plantilla_competencia  = serializers.SerializerMethodField()
    def get_list_evaluacion_plantilla_competencia(self, obj):
        
        plantilla_competencia = evaluacion_plantilla_competencia.objects.filter(id=obj.evaluacion_plantilla_competencia_id) if evaluacion_plantilla_competencia.objects.filter(id=obj.evaluacion_plantilla_competencia_id)  else None
        if plantilla_competencia == None:
            return None
        return evaluacion_plantilla_competenciaserializer(factor, many=True).data

    class Meta:
        model = detalle_evaluacion_factor_indicador
        fields = '__all__'

# class evaluacion_factor_plantilla_encabezadoserializer(serializers.ModelSerializer):
    
#     list_periodicidad =serializers.SerializerMethodField()
#     def get_list_periodicidad(self,obj):
#         periodicidad=evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) else None 
#         if periodicidad==None:
#             return None 
#         return evaluacion_periodicidadserializer(periodicidad,many=True).data

#     class Meta:
#         model = evaluacion_factor_plantilla_encabezado
#         fields = '__all__' 

# class evaluacion_competencia_plantilla_encabezadoserializer(serializers.ModelSerializer):
    
#     list_periodicidad =serializers.SerializerMethodField()
#     def get_list_periodicidad(self,obj):
#         periodicidad=evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) if evaluacion_periodicidad.objects.filter(id=obj.periodicidad_id) else None 
#         if periodicidad==None:
#             return None 
#         return evaluacion_periodicidadserializer(periodicidad,many=True).data

#     class Meta:
#         model = evaluacion_competencia_plantilla_encabezado
#         fields = '__all__'



class detalle_evaluacion_competenciaserializer(serializers.ModelSerializer):
    list_encabezado  = serializers.SerializerMethodField()
    def get_list_encabezado(self, obj):
        
        encabezado = evaluacion_encabezado.objects.filter(id=obj.encabezado_id) if evaluacion_encabezado.objects.filter(id=obj.encabezado_id)  else None
        if encabezado == None:
            return None
        return evaluacion_encabezadoserializer(encabezado, many=True).data
    
    list_metrica_competencia  = serializers.SerializerMethodField()
    def get_list_metrica_competencia(self, obj):
        
        metrica_competencia = evaluacion_metrica_competencia.objects.filter(id=obj.metrica_competencia_id) if evaluacion_metrica_competencia.objects.filter(id=obj.metrica_competencia_id)  else None
        if metrica_competencia == None:
            return None
        return evaluacion_metrica_competenciaserializer(factor, many=True).data

    list_plantilla_competencia=serializers.SerializerMethodField()
    def get_list_plantilla_competencia(self,obj):
        funcion = evaluacion_plantilla_competencia.objects.filter(competencia_plantilla_encabezado=obj.id) if evaluacion_plantilla_competencia.objects.filter(competencia_plantilla_encabezado=obj.id)  else None
        if funcion == None:
            return None
        return evaluacion_plantilla_competenciaserializer(funcion, many=True).data
    
    class Meta:
        model = detalle_evaluacion_competencia
        fields = '__all__'


class detalle_evaluacion_competencia_preguntasserializer(serializers.ModelSerializer):
    list_plantilla_competencia=serializers.SerializerMethodField()
    def get_list_plantilla_competencia(self,obj):
        funcion = evaluacion_plantilla_competencia.objects.filter(competencia_plantilla_encabezado=obj.id) if evaluacion_plantilla_competencia.objects.filter(competencia_plantilla_encabezado=obj.id)  else None
        if funcion == None:
            return None
        return evaluacion_plantilla_competenciaserializer(funcion, many=True).data

    list_metrica_competencia  = serializers.SerializerMethodField()
    def get_list_metrica_competencia(self, obj):
        
        metrica_competencia = evaluacion_metrica_competencia.objects.filter(id=obj.metrica_competencia_id) if evaluacion_metrica_competencia.objects.filter(id=obj.metrica_competencia_id)  else None
        if metrica_competencia == None:
            return None
        return evaluacion_metrica_competenciaserializer(metrica_competencia, many=True).data

    class Meta:
        model = detalle_evaluacion_competencia
        fields = '__all__'

class evaluacion_encabezado_preguntasserializer(serializers.ModelSerializer):
    list_detalle_competencia  = serializers.SerializerMethodField()
    def get_list_detalle_competencia(self, obj):
        
        detalle_competencia = detalle_evaluacion_competencia.objects.filter(encabezado_id=obj.id) if detalle_evaluacion_competencia.objects.filter(encabezado_id=obj.id)  else None
        if detalle_competencia == None:
            return None
        return detalle_evaluacion_competencia_preguntasserializer(detalle_competencia, many=True).data
  
    class Meta:      
        model =evaluacion_encabezado
        fields = "__all__"

class detalle_evaluacion_factor_preguntasserializer(serializers.ModelSerializer):
    list_plantilla_factor=serializers.SerializerMethodField()
    def get_list_plantilla_factor(self,obj):
        factor = evaluacion_plantilla_factor.objects.filter(factor_plantilla_encabezado=obj.id) if evaluacion_plantilla_competencia.objects.filter(factor_plantilla_encabezado=obj.id)  else None
        if factor == None:
            return None
        return evaluacion_plantilla_factorserializer(factor, many=True).data

    list_metrica_factor  = serializers.SerializerMethodField()
    def get_list_metrica_factor(self, obj):
        
        metrica_factor = evaluacion_metrica_factor.objects.filter(id=obj.metrica_factor_id) if evaluacion_metrica_factor.objects.filter(id=obj.metrica_factor_id)  else None
        if metrica_factor == None:
            return None
        return evaluacion_metrica_factorserializer(metrica_factor, many=True).data

    class Meta:
        model = detalle_evaluacion_factor
        fields = '__all__'


class evaluacion_encabezado_preguntas_factorserializer(serializers.ModelSerializer):
    list_detalle_factor = serializers.SerializerMethodField()
    def get_list_detalle_factor(self, obj):
        
        detalle_factor = detalle_evaluacion_factor.objects.filter(encabezado_id=obj.id) if detalle_evaluacion_factor.objects.filter(encabezado_id=obj.id)  else None
        if detalle_factor == None:
            return None
        return detalle_evaluacion_factor_preguntasserializer(detalle_factor, many=True).data
  
    class Meta:      
        model =evaluacion_encabezado
        fields = "__all__"







##VALIDACION DE RESPUESTAS#################################################################


def validacion_evaluacion_factor(id):
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezado_preguntas_factorserializer(queryset, many=True)
 
    factores=[]
    periodicidad=''
    clasificacion=''
    preguntas=[]
    lista_factores=[]
    preguntas_tipo_0=[]
    preguntas_tipo_2=[]
    funcion=''
    listado=[]
    tipo_factores=[]
    data_factor={}
    contador_preguntas=0

    respuestas_factor_totales=0

    
    if id!='':
        codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
        id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
        posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
        #############################
        descriptor_encabezado = (evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado'))[0]['descriptor_empleado'] if evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado') else None
        
        if descriptor_encabezado==None:
            return 'Descriptor no existe en el encabezado'
        descriptor= descriptor_perfil_datos_generales.objects.get(id=descriptor_encabezado) if descriptor_perfil_datos_generales.objects.filter(id=descriptor_encabezado) else None
        
        #############################
        if descriptor!=None:
            clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
        else:
            return 'Descriptor no existe'
        #clasificacion=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id'))[0]['evaluado__clasificacion_empleado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id') else None
        # clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
        periodicidad=(evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id'))[0]['periodicidad__id'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id') else None
        factores.extend(evaluacion_factor.objects.filter(clasificacion_id=clasificacion,periodicidad=periodicidad).values_list('id', flat=True))
        
    
    if not None in factores:
        print('encontro factores')
        for factor in factores:
            print('id de factor iterando',factor)
            objeto_encabezado=evaluacion_encabezado.objects.get(id=id)
            objeto_factor=evaluacion_factor.objects.get(id=factor)

            if objeto_factor.tipo_factor!=None:
                if objeto_factor.tipo_factor==0:
                    respuesta_peso_encontrado=''
                    preguntas_tipo_factor=evaluacion_plantilla_factor.objects.filter(factor=factor,factor__tipo_factor=0, periodicidad=objeto_factor.periodicidad).values('pregunta',id_origen_pregunta=F('id'))
                    respuesta= detalle_evaluacion_factor.objects.filter(factor=factor,factor__tipo_factor=0, encabezado=id).values('id')
                    contador_preguntas+=preguntas_tipo_factor.count()
                    respuestas_factor_totales+=respuesta.count()
                    print('RESPUESTA_preguntas-contador_preguntas__0',respuestas_factor_totales)
                    print('contador_preguntas-contador_preguntas__0',contador_preguntas)
                    print('#########################################################')





                if objeto_factor.tipo_factor==1:
                    codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                    id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
                    e=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
                    descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=e).order_by('-id').first()
                    
                    
                    
                    preg=descriptor_perfil_funcion.objects.filter(descriptor_id=descriptor.id,fundamental=True).values('id','descripcion')
                    if preg.count()<=3:
                        contador_preguntas+=preg.count()
                    else:
                        contador_preguntas+=3
                    respuesta= detalle_evaluacion_factor.objects.filter(factor=factor,factor__tipo_factor=1, encabezado=id).values()
                    respuestas_factor_totales+=respuesta.count()
                    print('RESPUESTA_preguntas-contador_preguntas__0',respuestas_factor_totales)
                    print('contador_preguntas-contador_preguntas',contador_preguntas)
                    print('#########################################################')

                if objeto_factor.tipo_factor==2:
                    lista_preguntas_factor2=[]
                    codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
                    id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
                    e=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)
                    descriptor = descriptor_perfil_datos_generales.objects.filter(posicion__in=e).order_by('-id').first()
                    
                    
                    
                    preg=descriptor_perfil_indicador_descriptor.objects.filter(descriptor_id=descriptor.id).values_list('indicador','indicador__objetivo')
                    if preg.count()<=3:
                        contador_preguntas+=preg.count()
                    else:
                        contador_preguntas+=3
                    respuesta= detalle_evaluacion_factor.objects.filter(factor=factor,factor__tipo_factor=2, encabezado=id).values()
                    respuestas_factor_totales+=respuesta.count()
                    print('RESPUESTA_preguntas-contador_preguntas__0',respuestas_factor_totales)
                    print('contador_preguntas-contador_preguntas',contador_preguntas)
                    print('#########################################################')
            else:
                return "Tipo de factor no definido"

    else:
        return "Factores no encontrados"

    if respuestas_factor_totales == contador_preguntas:
        return True
    if respuestas_factor_totales > contador_preguntas:
        return 'Se encontro un problema, hay mas respuestas que preguntas en el sistema'
    
    if respuestas_factor_totales < contador_preguntas:
        return False



def validacion_evaluacion_competencia(id):
    queryset = evaluacion_encabezado.objects.all()
    serializer_class = evaluacion_encabezado_preguntas_factorserializer(queryset, many=True)
        
    clasificacion=''
    periodicidad=''
    pregunta=[]
    #competencias=[]
    estado_evaluacion=''
    tipo_evaluacion_encabezado=''
    contador_respuestas=0
    almacenamiento_cantidad_preguntas=0
   
    if id!='':
        codigo_empleado=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__codigo'))[0]['evaluado__codigo']
        id_funcion=Funcional_empleado.objects.get(codigo=codigo_empleado)
        posicion=id_funcion.posicion.all().order_by('-id').values_list('id',flat=True)[0]
        # descriptor = descriptor_perfil_datos_generales.objects.filter(posicion=posicion).order_by('-id').first()
        ##################################################
        descriptor_encabezado = (evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado'))[0]['descriptor_empleado'] if evaluacion_encabezado.objects.filter(id=id).values('descriptor_empleado') else None
        
        if descriptor_encabezado==None:
            return 'Descriptor no existe en el encabezado'
        descriptor= descriptor_perfil_datos_generales.objects.get(id=descriptor_encabezado) if descriptor_perfil_datos_generales.objects.filter(id=descriptor_encabezado) else None
        
        #############################
        if descriptor!=None:
            clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
        else:
            return 'Descriptor no existe'
        ##################################################
        # clasificacion=(descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado'))[0]['clasificacion_empleado'] if descriptor_perfil_datos_generales.objects.filter(id=descriptor.id).values('clasificacion_empleado') else None
        #clasificacion=(evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id'))[0]['evaluado__clasificacion_empleado__id'] if evaluacion_encabezado.objects.filter(id=id).values('evaluado__clasificacion_empleado__id') else None
        #competencias=evaluacion_competencia.objects.filter(clasificacion_id=clasificacion).values_list('id', flat=True)          
        periodicidad=(evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id'))[0]['periodicidad__id'] if evaluacion_encabezado.objects.filter(id=id).values('periodicidad__id') else None          
        tipo_evaluacion_encabezado=(evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion_encabezado'))[0]['tipo_evaluacion_encabezado'] if evaluacion_encabezado.objects.filter(id=id).values('tipo_evaluacion_encabezado') else None
        estado_evaluacion=(evaluacion_encabezado.objects.filter(id=id).values('estado'))[0]['estado'] if evaluacion_encabezado.objects.filter(id=id).values('estado') else None
        competencia_perfil_descriptor=descriptor_perfil_competencia_descriptor.objects.filter(descriptor_id=descriptor.id).values_list('id', flat=True)
        competencia_descriptor=evaluacion_competencia.objects.filter(periodicidad__id=periodicidad).filter(competencia__descriptor_perfil_competencia_descriptor__id__in=competencia_perfil_descriptor).distinct().values_list('id', flat=True)

    # print(competencias)
    # nueva_competencias=[]

    # if competencias==None:
    #     return Response({"Competencias no encontradas"},status= status.HTTP_404_NOT_FOUND)
    # else:
    #     if len(competencias)!=0:
    #         for item in competencias:
    #             if item not in nueva_competencias:
    #                 if item!=None:
    #                     nueva_competencias.append(item)

    data={}
    
    if clasificacion!=None:
        if periodicidad!=None:
            for competencia in competencia_descriptor:
                #print(competencia)
                
                listado_pregunta_competencia=list(evaluacion_plantilla_competencia.objects.filter(competencia__clasificacion=clasificacion).filter(competencia__id=competencia).filter(periodicidad__id=periodicidad).values('pregunta',idCompetencia=F('competencia__competencia__id'),nombreCompetencia=F('competencia__competencia__nombre'),descripcionCompetencia=F('competencia__competencia__descripcion'),idClasificacion=F('competencia__clasificacion'),idPlantilla=F('id')))
                conteo_preguntas=evaluacion_plantilla_competencia.objects.filter(competencia__clasificacion=clasificacion).filter(competencia__id=competencia).filter(periodicidad__id=periodicidad).values('pregunta',idCompetencia=F('competencia__competencia__id'),nombreCompetencia=F('competencia__competencia__nombre'),descripcionCompetencia=F('competencia__competencia__descripcion'),idClasificacion=F('competencia__clasificacion'),idPlantilla=F('id')).count()
                
                almacenamiento_cantidad_preguntas+=conteo_preguntas
                
                for lista in listado_pregunta_competencia:
                    metrica_competencia_id_x= detalle_evaluacion_competencia.objects.filter(evaluacion_plantilla_competencia=lista['idPlantilla']).filter(encabezado=id).values('metrica_competencia','metrica_competencia__grado')
                    contador_respuestas+=metrica_competencia_id_x.count()

    if almacenamiento_cantidad_preguntas==contador_respuestas:
        return True
    if almacenamiento_cantidad_preguntas>contador_respuestas:
        return False

    if almacenamiento_cantidad_preguntas<contador_respuestas:
        return 'Algo salio mal, hay mas respuestas que preguntas en el sistema'




#########NOTIFICACIONES EN AURORA#############################################################3#############################
class notificacion_auroraserializer(serializers.ModelSerializer):

    list_destinatario=serializers.SerializerMethodField()
    def get_list_destinatario(self,obj):
        destinatario = Funcional_empleado.objects.filter(id=obj.destinatario_id) if Funcional_empleado.objects.filter(id=obj.destinatario_id) else None
        if destinatario ==None:
            return None
        return Funcional_empleadoserializer(destinatario,many=True).data  
   
    class Meta:      
        model =notificacion_aurora
        fields = "__all__"








######################################################################3#############################

def calculo_nota_puntuacion_total(encabezado_id):
    encabezado_evaluado= (evaluacion_encabezado.objects.filter(id=encabezado_id).values('evaluado'))[0]['evaluado'] if evaluacion_encabezado.objects.filter(id=encabezado_id).values('evaluado') else None
    encabezado_periodicidad=  (evaluacion_encabezado.objects.filter(id=encabezado_id).values('periodicidad'))[0]['periodicidad'] if evaluacion_encabezado.objects.filter(id=encabezado_id).values('periodicidad') else None
    encabezado_periodo =  (evaluacion_encabezado.objects.filter(id=encabezado_id).values('periodicidad__evaluacion_configuracion_periodo__periodo'))[0]['periodicidad__evaluacion_configuracion_periodo__periodo'] if evaluacion_encabezado.objects.filter(id=encabezado_id).values('periodicidad__evaluacion_configuracion_periodo__periodo') else None
    encabezado_tipo_evaluacion =  (evaluacion_encabezado.objects.filter(id=encabezado_id).values('tipo_evaluacion__id'))[0]['tipo_evaluacion__id'] if evaluacion_encabezado.objects.filter(id=encabezado_id).values('tipo_evaluacion__id') else None
    #########################################################################################################################
    resultados_evaluaciones=list(evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion).values('id','tipo_evaluacion_encabezado')) if evaluacion_encabezado.objects.filter(evaluado=encabezado_evaluado,periodicidad=encabezado_periodicidad,periodicidad__evaluacion_configuracion_periodo__periodo=encabezado_periodo,tipo_evaluacion__id=encabezado_tipo_evaluacion).values('id','tipo_evaluacion_encabezado') else None
    if  resultados_evaluaciones!=None:
            for x in resultados_evaluaciones:
                id_encabezado = x['id']
                id_tipo_evaluacion=x['tipo_evaluacion_encabezado']
                
                if id_tipo_evaluacion==1:
                    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                    print('id_encabezado',id_encabezado)
                    print('id_tipo_evaluacion',id_tipo_evaluacion)
                    nota_competencia= evaluacion_encabezado.objects.filter(id=id_encabezado).values('nota_total_porcentaje_prorateo','nivel_resultado')
                    nota_total_competencia =nota_competencia[0]['nota_total_porcentaje_prorateo']
                    nota_total_competencia_desempeno=nota_competencia[0]['nivel_resultado']
                    encabezado_competencia_id=id_encabezado


                if id_tipo_evaluacion==2:
                    print('##################################')
                    print('id_encabezado',id_encabezado)
                    print('id_tipo_evaluacion',id_tipo_evaluacion)
                    nota_factor= evaluacion_encabezado.objects.filter(id=id_encabezado).values('nota_total_porcentaje','nivel_resultado')
                    nota_total_factor = nota_factor[0]['nota_total_porcentaje']
                    nota_total_factor_desempenio = nota_factor[0]['nivel_resultado']
                    

            if nota_total_competencia!=None and nota_total_factor!=None:
                total_desempenio= (int(nota_total_competencia)+int(nota_total_factor))/2
            else:
                return False 
            
            
    return total_desempenio

