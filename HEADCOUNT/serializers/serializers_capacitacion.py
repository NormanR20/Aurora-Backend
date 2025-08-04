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

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class capacitacion_archivo_gestorserializer(serializers.ModelSerializer):
    class Meta:
        model = capacitacion_archivo_gestor
        fields = '__all__'

class capacitacion_tipo_capacitacionserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
        
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data

    class Meta:
        model = capacitacion_tipo_capacitacion
        fields = '__all__'

class capacitacion_modalidadserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
        
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data

    class Meta:
        model = capacitacion_modalidad
        fields = '__all__'


class capacitacion_enfoqueserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data


    class Meta:
        model = capacitacion_enfoque
        fields = '__all__'


class capacitacion_motivo_inasistenciaserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data


    class Meta:
        model = capacitacion_motivo_inasistencia
        fields = '__all__'

class capacitacion_origenserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
        
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data

    class Meta:
        model = capacitacion_origen
        fields = '__all__'

class capacitacion_estadoserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
        
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data

    class Meta:
        model = capacitacion_estado
        fields = '__all__'



class capacitacion_cursoserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data


    class Meta:
        model = capacitacion_curso
        fields = '__all__'


class capacitacion_metrica_evaluacion_factorserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
        
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data


    class Meta:
        model = capacitacion_metrica_evaluacion_factor
        fields = '__all__'
        

class capacitacion_metrica_9_cajasserializer(serializers.ModelSerializer):
    class Meta:
        model = capacitacion_metrica_9_cajas
        fields = '__all__'

class capacitacion_campaniaserializer(serializers.ModelSerializer):
    
    list_estado = serializers.SerializerMethodField()
    def get_list_estado(self, obj):
        
        estado = capacitacion_estado.objects.filter(id=obj.estado_id) if capacitacion_estado.objects.filter(id=obj.estado_id)  else None
        if estado == None:
           return None
        return capacitacion_estadoserializer(estado, many=True).data

    class Meta:
        model = capacitacion_campania
        fields = '__all__'


class capacitacion_metrica_experiencia_puestoserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
        
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data


    class Meta:
        model = capacitacion_metrica_experiencia_puesto
        fields = '__all__'



class capacitacion_matriz_9_cajaserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
        
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data


    class Meta:
        model = capacitacion_matriz_9_cajas
        fields = '__all__'
        

class capacitacion_metrica_educacion_formalserializer(serializers.ModelSerializer):
    class Meta:
        model = capacitacion_metrica_educacion_formal
        fields = '__all__'

class capacitacion_monitor_colaboradoresserializer(serializers.ModelSerializer):
    
    empresa=serializers.SerializerMethodField()
    def get_empresa(self, obj):
        empresa=Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__sociedad_financiera__nombre',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if empresa == None:
           return None
        
        return empresa

    List_campanias=serializers.SerializerMethodField()
    def get_List_campanias(self,obj):
        capa= Funcional_empleado.objects.filter(id=obj.id).values_list('empleado_capacitacion_asistencia__evento_capacitacion__campania__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id).values('empleado_capacitacion_asistencia__evento_capacitacion__campania__nombre_campania') else None
        if capa== None:
            return None

        print('assssssssssssssssssssssssssssss',capa)
        campaniass=capacitacion_campania.objects.filter(id__in=capa) if capacitacion_campania.objects.filter(id__in=capa) else None
        if campaniass==None:
            return None
        return capacitacion_campaniaserializer(campaniass,many=True).data

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

    list_capacitaciones_completadas=serializers.SerializerMethodField()
    def get_list_capacitaciones_completadas(self,obj):
        contador=0
        capacitaciones=Funcional_empleado.objects.filter(id=obj.id).values_list('empleado_capacitacion_asistencia','empleado_capacitacion_asistencia__recibidas')
        cantidad=capacitaciones.count()
        for capacitacion_id,horas_recibidas in capacitaciones:
            duracion_horas=(Funcional_empleado.objects.filter(id=capacitacion_id).values_list('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas',flat=True))[0]['empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas'] if Funcional_empleado.objects.filter(id=capacitacion_id).values('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas') else None
            if horas_recibidas==duracion_horas:
                contador+=1
        string= str(contador) + '/' + str(cantidad)
        return string
    
    list_capacitaciones_completadas_porcentaje=serializers.SerializerMethodField()
    def get_list_capacitaciones_completadas_porcentaje(self,obj):
        contador=0
        capacitaciones=Funcional_empleado.objects.filter(id=obj.id).values_list('empleado_capacitacion_asistencia','empleado_capacitacion_asistencia__recibidas')
        cantidad=capacitaciones.count()
        for capacitacion_id,horas_recibidas in capacitaciones:
            duracion_horas=(Funcional_empleado.objects.filter(id=capacitacion_id).values_list('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas',flat=True))[0]['empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas'] if Funcional_empleado.objects.filter(id=capacitacion_id).values('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas') else None
            if horas_recibidas==duracion_horas:
                contador+=1
        string= (int(contador)*100)/100
        return string
    
    list_estado_capacitacion=serializers.SerializerMethodField()
    def get_list_estado_capacitacion(self,obj):
        contador=0
        capacitaciones=Funcional_empleado.objects.filter(id=obj.id).values_list('empleado_capacitacion_asistencia','empleado_capacitacion_asistencia__recibidas')
        cantidad=capacitaciones.count()
        for capacitacion_id,horas_recibidas in capacitaciones:
            duracion_horas=(Funcional_empleado.objects.filter(id=capacitacion_id).values_list('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas',flat=True))[0]['empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas'] if Funcional_empleado.objects.filter(id=capacitacion_id).values('empleado_capacitacion_asistencia__evento_capacitacion__duracion_horas') else None
            if horas_recibidas==duracion_horas:
                contador+=1
        if contador==0:
            string='Abierto'

        if contador>0:
            string='En proceso'
        
        if contador==cantidad:
            string='Cerrado'
        return string

        
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
 
class capacitacion_evento_capacitacionserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data

    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data

    list_campania= serializers.SerializerMethodField()
    def get_list_campania(self, obj):
        
        campania = capacitacion_campania.objects.filter(id=obj.campania_id) if capacitacion_campania.objects.filter(id=obj.campania_id)  else None
        if campania == None:
           return None
        return capacitacion_campaniaserializer(campania, many=True).data

    list_capacitacion = serializers.SerializerMethodField()
    def get_list_capacitacion(self, obj):
        
        capacitacion = capacitacion_curso.objects.filter(id=obj.capacitacion_id) if capacitacion_curso.objects.filter(id=obj.capacitacion_id)  else None
        if capacitacion == None:
           return None
        return capacitacion_cursoserializer(capacitacion, many=True).data

    list_responsable=serializers.SerializerMethodField()
    def get_list_responsable(self,obj):
        responsable = Funcional_empleado.objects.filter(id=obj.responsable_id) if Funcional_empleado.objects.filter(id=obj.responsable_id) else None
        if responsable ==None:
            return None
        return Funcional_empleadoserializer(responsable,many=True).data 

    list_tipo_capacitacion = serializers.SerializerMethodField()
    def get_list_tipo_capacitacion(self, obj):
        
        tipo_capacitacion = capacitacion_tipo_capacitacion.objects.filter(id=obj.tipo_capacitacion_id) if capacitacion_tipo_capacitacion.objects.filter(id=obj.tipo_capacitacion_id)  else None
        if tipo_capacitacion == None:
           return None
        return capacitacion_tipo_capacitacionserializer(tipo_capacitacion, many=True).data

    list_origen = serializers.SerializerMethodField()
    def get_list_origen(self, obj):
        
        origen = capacitacion_origen.objects.filter(id=obj.origen_id) if capacitacion_origen.objects.filter(id=obj.origen_id)  else None
        if origen == None:
           return None
        return capacitacion_origenserializer(origen, many=True).data

    list_modalidad = serializers.SerializerMethodField()
    def get_list_modalidad(self, obj):
        
        modalidad = capacitacion_modalidad.objects.filter(id=obj.modalidad_id) if capacitacion_modalidad.objects.filter(id=obj.modalidad_id)  else None
        if modalidad == None:
           return None
        return capacitacion_modalidadserializer(modalidad, many=True).data
    
    list_nivel_formacion = serializers.SerializerMethodField()
    def get_list_nivel_formacion(self, obj):
        
        nivel_educativo = Funcional_Instituto.objects.filter(id=obj.nivel_formacion_id) if Funcional_Instituto.objects.filter(id=obj.nivel_formacion_id)  else None
        if nivel_educativo == None:
           return None
        return Funcional_Institutoserializer(nivel_educativo, many=True).data

    list_formacion = serializers.SerializerMethodField()
    def get_list_formacion(self, obj):
        
        formacion = Funcional_Formacion.objects.filter(id=obj.formacion_id) if Funcional_Formacion.objects.filter(id=obj.formacion_id)  else None
        if formacion == None:
           return None
        return Funcional_Formacionserializer(formacion, many=True).data

    list_titulo = serializers.SerializerMethodField()
    def get_list_titulo(self, obj):
        
        titulo = Funcional_Titulo.objects.filter(id=obj.titulo_id) if Funcional_Titulo.objects.filter(id=obj.titulo_id)  else None
        if titulo == None:
           return None
        return Funcional_Tituloserializer(titulo, many=True).data

    list_especialidad = serializers.SerializerMethodField()
    def get_list_especialidad(self, obj):
        
        especialidad = Funcional_Especialidad.objects.filter(id=obj.especialidad_id) if Funcional_Especialidad.objects.filter(id=obj.especialidad_id)  else None
        if especialidad == None:
           return None
        return Funcional_Especialidadserializer(especialidad, many=True).data

    list_enfoque= serializers.SerializerMethodField()
    def get_list_enfoque(self, obj):
        
        enfoque = capacitacion_enfoque.objects.filter(id=obj.enfoque_id) if capacitacion_enfoque.objects.filter(id=obj.enfoque_id)  else None
        if enfoque == None:
           return None
        return capacitacion_enfoqueserializer(enfoque, many=True).data

    list_estado = serializers.SerializerMethodField()
    def get_list_estado(self, obj):
        
        estado = capacitacion_estado.objects.filter(id=obj.estado_id) if capacitacion_estado.objects.filter(id=obj.estado_id)  else None
        if estado == None:
           return None
        return capacitacion_estadoserializer(estado, many=True).data


    class Meta:
        model = capacitacion_evento_capacitacion
        fields = '__all__'


class capacitacion_asistenciaserializer(serializers.ModelSerializer):
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):

        usuario = User.objects.filter(id=obj.creado_por_id) if User.objects.filter(id=obj.creado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data
        
    list_actualizado_por = serializers.SerializerMethodField()
    def get_list_actualizado_por(self, obj):
        
        usuario = User.objects.filter(id=obj.actualizado_por_id) if User.objects.filter(id=obj.actualizado_por_id)  else None
        if usuario == None:
           return None
        return UsuariosSerializer(usuario, many=True).data


    list_empleado = serializers.SerializerMethodField()
    def get_list_empleado(self, obj):
        
        empleado = Funcional_empleado.objects.filter(id=obj.empleado.id) if Funcional_empleado.objects.filter(id=obj.empleado.id)  else None
        if empleado == None:
           return None
        return Funcional_empleadoserializer(empleado, many=True).data

    list_evento_capacitacion = serializers.SerializerMethodField()
    def get_list_evento_capacitacion(self, obj):
        
        event_capacitacion = capacitacion_evento_capacitacion.objects.filter(id=obj.evento_capacitacion.id) if capacitacion_evento_capacitacion.objects.filter(id=obj.evento_capacitacion.id)  else None
        if event_capacitacion == None:
           return None
        return capacitacion_evento_capacitacionserializer(event_capacitacion, many=True).data

    
    list_motivo_inasistencia = serializers.SerializerMethodField()
    def get_list_motivo_inasistencia(self, obj):
        
        motivo_inasistencia = capacitacion_motivo_inasistencia.objects.filter(id=obj.motivo_inasistencia_id) if capacitacion_motivo_inasistencia.objects.filter(id=obj.motivo_inasistencia_id)  else None
        if motivo_inasistencia == None:
           return None
        return capacitacion_motivo_inasistenciaserializer(motivo_inasistencia, many=True).data 

    list_estado = serializers.SerializerMethodField()
    def get_list_estado(self, obj):
        
        estad = capacitacion_estado.objects.filter(id=obj.estado_id) if capacitacion_estado.objects.filter(id=obj.estado_id)  else None
        if estad == None:
           return None
        return capacitacion_estadoserializer(estad, many=True).data    
    
    total_asistencia = serializers.SerializerMethodField()
    def get_total_asistencia(self, obj):
        
        total_asistencia_f = capacitacion_asistencia.objects.filter(evento_capacitacion=obj.evento_capacitacion_id).filter(asistio=True).count() if capacitacion_asistencia.objects.filter(evento_capacitacion=obj.evento_capacitacion_id).filter(asistio=True) else None
        return total_asistencia_f

    total_inasistencia = serializers.SerializerMethodField()
    def get_total_inasistencia(self, obj):
        
        total_inasistencia_f = capacitacion_asistencia.objects.filter(evento_capacitacion=obj.evento_capacitacion_id).filter(asistio=False).count() if capacitacion_asistencia.objects.filter(evento_capacitacion=obj.evento_capacitacion_id).filter(asistio=False) else None
        return total_inasistencia_f    

    class Meta:
        model = capacitacion_asistencia
        fields = '__all__'


