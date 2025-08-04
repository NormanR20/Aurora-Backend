from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields import files
from HEADCOUNT.models.modelos_sanciones import sanciones_casos_disciplinarios
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import models
from rest_framework.utils import field_mapping
from ..models import Formal_Puesto, Formal_Salud, Formal_empleado,Funcional_Puesto,Formal_plaza,Funcional_Plaza,Formal_Unidad_Organizativa, Funcional_Unidad_Organizativa
from ..models import Formal_Relacion_Laboral,Funcional_Relacion_Laboral,Formal_Division,Formal_Division_Personal
from ..models import Formal_Estado_civil,Funcional_Estado_civil,Formal_Organizacion
from ..models import Formal_empleado,Funcional_empleado,Formal_Centro_Costo,Funcional_Division,Funcional_Division_Personal,Funcional_Centro_Costo,Funcional_Organizacion
from ..models import Formal_Parentesco,Funcional_Parentesco,Formal_Genero,Funcional_Genero,Formal_Funciones,Funcional_Funciones
from ..models import Formal_Situacion_Actual,Funcional_Situacion_Actual,Funcional_Compañia,Formal_Compañia,Formal_Especialidad,Funcional_Especialidad
from ..models import Formal_Contacto_Emergencia,Funcional_Contacto_Emergencia,Formal_Dependientes_Economico,Funcional_Dependientes_Economico
from ..models import Funcional_Beneficiario_Seguro,Formal_Beneficiario_Seguro,Formal_Formacion,Funcional_Formacion,Formal_Equipo, Funcional_Equipo
from ..models import Funcional_Historial_Laboral,Formal_Historial_Laboral
from ..models import Formal_Titulo,Funcional_Titulo,Formal_Instituto,Funcional_Instituto,Formal_Diagnostico,Funcional_Diagnostico
from ..models import Formal_Salud,Funcional_Salud,Formal_Educacion,Funcional_Educacion
from ..models import Actualizacion_Contacto,Actualizacion_Dependiente,Actualizacion_Domicilio,Actualizacion_Educacion
from ..models import Actualizacion_Estado_Civil
from ..models import Funcional_Check_List,Funcional_Empleado_Check_List,Formal_Check_List,Formal_Empleado_Check_List
from ..models import Configuracion_Actualizacion_Empleado
from ..models import Funcional_Laboratorio,Funcional_Vacuna,Funcional_Empleado_Vacuna
from ..models import Formal_Laboratorio,Formal_Vacuna,Formal_Empleado_Vacuna
from ..models import Funcional_Relacion_Laboral_Anterior,Formal_Relacion_Laboral_Anterior
from ..models import Funcional_Clasificacion,Formal_Clasificacion
from ..models import Tiempos_Empleado,Absentismo_Empleado,Dias_Laborados_Empleado,head_clima_pais,head_clima_departamento,head_clima_municipio
from ..models import Usuario_Log
#Segunda Etapa Clima Laboral
from ..models import Clima_Objeto,Clima_Sub_Objeto,Clima_Tipo_Pregunta,Clima_Tipo_Herramienta
from ..models import Clima_Plantilla, Clima_Plantilla_Preguntas,Clima_Plantilla_Opciones,Clima_Segmento
from ..models import Clima_Cuestionario,Clima_Cuestionario_Preguntas,Clima_Cuestionario_Opciones,Clima_Campaña
from ..models import Clima_Encuesta,Clima_Respuestas,archivos_gestor,archivos_gestor_formatos_oficiales
####################################################################################################
from ..models import descriptor_perfil_formacion_area_conocimiento,genero,descriptor_perfil_datos_unidad_medida
from ..models import descriptor_perfil_cursos_diplomados_seminario_pasantia
from ..models import descriptor_perfil_formacion_area_conocimiento,descriptor_perfil_formacion_nivel_educativo,descriptor_perfil_titulo,descriptor_perfil_conocimiento_tecnico
#####################################################################################################
from django.contrib.auth.models import User,Group
from django.db.models import Count
from django.contrib.auth.hashers import make_password
from ..serializers import *
from ..models import descriptor_perfil_datos_generales


class head_clima_paisserializer(serializers.ModelSerializer):
    class Meta:
        model = head_clima_pais
        fields = '__all__'

class head_clima_departamentoserializer(serializers.ModelSerializer):
    list_pais = serializers.SerializerMethodField()
    def get_list_pais(self, obj):
        if obj.pais:
            pais = head_clima_pais.objects.filter(id=obj.pais_id) if head_clima_pais.objects.filter(id=obj.pais_id)  else None
            if pais == None:
                return None
            return head_clima_paisserializer(pais, many=True).data   

    class Meta:
        model = head_clima_departamento
        fields = '__all__'

class head_clima_municipioserializer(serializers.ModelSerializer):
    list_departamento = serializers.SerializerMethodField()
    def get_list_departamento(self, obj):
        if obj.departamento:
               
            depto= head_clima_departamento.objects.filter(id=obj.departamento_id) if head_clima_departamento.objects.filter(id=obj.departamento_id)  else None
            if depto == None:
                return None
            return head_clima_departamentoserializer(depto, many=True).data   
    class Meta:
        model = head_clima_municipio
        fields = '__all__'



class descriptor_perfil_datos_unidad_medidasserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_datos_unidad_medida
        fields = '__all__'

class formal_puestoserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Puesto
        fields = '__all__'
class funcional_puestoserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Puesto
        fields = '__all__'

class formal_plazaserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_plaza
        fields = '__all__'

class funcional_plazaserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Plaza
        fields = '__all__'


class AutorizarSerializer(serializers.Serializer):
    autorizar = serializers.IntegerField()
    usuario =serializers.CharField()
    class Meta:
        fields =['autorizar','usuario']


class PadreSerializer(serializers.Serializer):
    padre = serializers.IntegerField()
    class Meta:
        fields =['padre']


class LogoutSerializer(serializers.Serializer):
    token =serializers.CharField()
    class Meta:
        fields =['token']

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    #validate_password = make_password
    def create(self, validated_data):
        password = validated_data.pop('password')
        groupss= validated_data.pop('groups')
       #print('la variable self ', password)
        #print('la variable password ', password)
        #print (groupss)
        #print ('Validated ', validated_data)

        user = super().create(validated_data)
        #user.set_password(validated_data['password'])
        #user.save()
        #validated_data['password'] = make_password(validated_data['password'])
        #user = User.objects.create(**validated_data)
        #user.set_password(password)
        #user.groups.set(groupss)
        #user.save()
       #print('la variable self2 ', password)
        #user = super().create(validated_data)
        
        #user.set_password(self.data['password'])
        #user.password=password
        user.groups.set(groupss)

        user.save()
       #print('la variable self3 ', password)
        user.set_password(password)
        usuario = User.objects.get(username=validated_data.pop('username'))
        usuario.set_password(password)
        usuario.save()
       #print(usuario)
        return user

    # def validate_password(self, value: str) -> str:
    #     return make_password(value)
    #     # user = self.model(
    #     #     email=self.normalize_email(email),
    #     #     name=name
    #     # )

    #     # user.set_password(password)
    #     # user.save()

    #     #return super(UserSerializer, self).create(validated_data)



class Formal_Relacion_Laboral_Anteriorserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Relacion_Laboral_Anterior
        fields = '__all__'

class Formal_Historial_Laboralserializer(serializers.ModelSerializer):
    puesto_list=serializers.SerializerMethodField()
    def get_puesto_list(self, obj):
        if obj.puesto == None:
            return None
        pto=Formal_Relacion_Laboral_Anterior.objects.filter(id=obj.puesto.id) if Formal_Relacion_Laboral_Anterior.objects.filter(id=obj.puesto.id) else None
        if pto == None:
           return None
        return Formal_Relacion_Laboral_Anteriorserializer(pto, many=True).data
    class Meta:
        model = Formal_Historial_Laboral
        fields = '__all__'

class Formal_Tituloserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Titulo
        fields ='__all__'

class Formal_Institutoserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Instituto
        fields='__all__'

class Formal_Diagnosticoserializer(serializers.ModelSerializer):
    class Meta:
        model=Formal_Diagnostico
        fields='__all__'
class Formal_Saludserializer(serializers.ModelSerializer):
    diagnostico_list = serializers.SerializerMethodField()

    def get_diagnostico_list(self,obj):
        if obj ==None:
            return None

        if obj.diagnostico ==None:
            return None
        diagnostico=Formal_Diagnostico.objects.filter(id=obj.diagnostico.id) if Formal_Diagnostico.objects.filter(id=obj.diagnostico.id) else None
        
        if diagnostico==None:
            return None
        return Formal_Diagnosticoserializer(diagnostico, many=True).data


    class Meta:
        model = Formal_Salud
        fields='__all__'

class Formal_Educacionserializer(serializers.ModelSerializer):
    formacion_list=serializers.SerializerMethodField()
    def get_formacion_list(self,obj):
        
        formacion=Formal_Formacion.objects.filter(id=obj.formacion.id) if Formal_Formacion.objects.filter(id=obj.formacion.id) else None
        
        if formacion==None:
            return None
        
        return Formal_Formacionserializer(formacion[0]).data


    especialidad_list=serializers.SerializerMethodField()
    def get_especialidad_list(self,obj):
            
        if not obj.especialidad:
            return None
        especialidad=Formal_Especialidad.objects.filter(id=obj.especialidad.id) if Formal_Especialidad.objects.filter(id=obj.especialidad.id) else None
        
        if especialidad==None:
            return None
        return Formal_Especialidadserializer(especialidad[0]).data


    instituto_list=serializers.SerializerMethodField()
    def get_instituto_list(self,obj):
            
        if not obj.instituto:
            return None
        instituto=Formal_Instituto.objects.filter(id=obj.instituto.id) if Formal_Instituto.objects.filter(id=obj.instituto.id) else None
        
        if instituto==None:
            return None
        return Formal_Institutoserializer(instituto[0]).data

    titulo_list=serializers.SerializerMethodField()
    def get_titulo_list(self,obj):
            
        if not obj.titulo:
            return None
        titulo=Formal_Titulo.objects.filter(id=obj.titulo.id) if Formal_Titulo.objects.filter(id=obj.titulo.id) else None
        
        if titulo==None:
            return None
        return Formal_Tituloserializer(titulo[0]).data

    class Meta:
        model = Formal_Educacion
        fields='__all__'



class Formal_empleadoserializer(serializers.ModelSerializer):
    Formacion_List = serializers.SerializerMethodField()
    #historial_list = Formal_Historial_Laboralserializer(many=True, read_only=True)
    #este es un campo many to many dentro de la tabla de formal_empleado


    def get_Formacion_List(self, obj):
        fe=Formal_empleado.objects.filter(id=obj.id).values_list('formacion__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe == None:
           return None

        ff = Formal_Formacion.objects.filter(id__in=fe)
        if not ff:
            return None
        return Formal_Formacionserializer(ff, many=True).data

    clasificacion_nombre = serializers.SerializerMethodField()
    def get_clasificacion_nombre(self,obj):
        if obj.clasificacion_empleado == None:
            return None
        clasificacion=Formal_Clasificacion.objects.filter(id=obj.clasificacion_empleado_id) if Formal_Clasificacion.objects.filter(id=obj.clasificacion_empleado_id) else None
        if clasificacion == None:
           return None
        return Formal_Clasificacionserializer(clasificacion, many=True).data
    


    #el empleado es una llava foranea en la tabla Formal_Historial_Laboral
    Historial_Laboral_List = serializers.SerializerMethodField()
    def get_Historial_Laboral_List(self, obj):
        fhl=Formal_Historial_Laboral.objects.filter(empleado=obj.id) if Formal_Historial_Laboral.objects.filter(empleado=obj.id) else None
        if fhl == None:
           return None
        return Formal_Historial_Laboralserializer(fhl, many=True).data

    #para dependientes económicos
    Dependientes_Economicos_List = serializers.SerializerMethodField()
    def get_Dependientes_Economicos_List(self,obj):
        fde=Formal_Dependientes_Economico.objects.filter(empleado=obj.id) if Formal_Dependientes_Economico.objects.filter(empleado=obj.id) else None
        if fde == None:
            return None
        return Formal_Dependientes_Economicoserializer(fde, many=True).data
    
    #para Beneficiario_Seguro
    Beneficiario_Seguro_List= serializers.SerializerMethodField()
    def get_Beneficiario_Seguro_List(self,obj):
        fbs= Formal_Beneficiario_Seguro.objects.filter(empleado=obj.id) if Formal_Beneficiario_Seguro.objects.filter(empleado=obj.id) else None
        if fbs == None:
            return None
        return Formal_Beneficiario_Seguroserializer(fbs, many=True).data

    #para Relacion Laboral
    Relacion_Laboral_List= serializers.SerializerMethodField()
    def get_Relacion_Laboral_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('relacion_laboral__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe == None:
            return fe
        frl= Formal_Relacion_Laboral.objects.filter(id__in=fe)
        if not frl:
            return None
        return Formal_Relacion_Laboralserializer(frl,many=True).data
        
    #para Division
    Division_List= serializers.SerializerMethodField()
    def get_Division_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('division__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fd=Formal_Division.objects.filter(id__in=fe) if Formal_Division.objects.filter(id__in=fe) else None
        if  fd==None:
            return None
        return Formal_Divisionserializer(fd, many=True).data

    Division_Personal_List= serializers.SerializerMethodField()
    def get_Division_Personal_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('division_personal__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fd=Formal_Division_Personal.objects.filter(id__in=fe) if Formal_Division_Personal.objects.filter(id__in=fe) else None
        if  fd==None:
            return None
        return Formal_Division_Personalserializer(fd, many=True).data
    
    #para Centro de Costo
    Centro_Costo_List=serializers.SerializerMethodField()
    def get_Centro_Costo_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('centro_costo__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fcc=Formal_Centro_Costo.objects.filter(id__in=fe) if Formal_Centro_Costo.objects.filter(id__in=fe) else None
        if fcc==None:
            return None
        return Formal_Centro_Costoserializer (fcc,many=True).data

    #para Estado Civil
    Estado_Civil_List=serializers.SerializerMethodField()
    def get_Estado_Civil_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('estado_civil__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fec=Formal_Estado_civil.objects.filter(id__in=fe) if Formal_Estado_civil.objects.filter(id__in=fe) else None
        if fec==None:
            return None
        return Formal_Estado_civilserializer(fec,many=True).data

    #para Puesto
    Puesto_List=serializers.SerializerMethodField()
    def get_Puesto_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('puesto__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fp=Formal_Puesto.objects.filter(id__in=fe) if Formal_Puesto.objects.filter(id__in=fe) else None
        if fp==None:
            return None
        return formal_puestoserializer(fp,many=True).data

    #para unidad organizativa
    Unidad_Organizativa_List=serializers.SerializerMethodField()
    def get_Unidad_Organizativa_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fuo=Formal_Unidad_Organizativa.objects.filter(id__in=fe) if Formal_Unidad_Organizativa.objects.filter(id__in=fe) else None
        if fuo==None:
            return None
        return formal_unidad_organizativabasicoserializer(fuo,many=True).data

    #para especialidad
    Especialidad_List=serializers.SerializerMethodField()
    def get_Especialidad_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('especialidad__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fel=Formal_Especialidad.objects.filter(id__in=fe) if Formal_Especialidad.objects.filter(id__in=fe) else None
        if fel==None:
            return None
        return Formal_Especialidadserializer(fel,many=True).data

    #para Contacto de emergencia
    Contacto_Emergencia_List=serializers.SerializerMethodField()
    def get_Contacto_Emergencia_List(self, obj):
        fce=Formal_Contacto_Emergencia.objects.filter(empleado=obj.id) if Formal_Contacto_Emergencia.objects.filter(empleado=obj.id) else None
        if fce == None:
           return None
        return Formal_Contacto_Emergenciaserializer(fce, many=True).data

    
    situacion_actual_list=serializers.SerializerMethodField()
    def get_situacion_actual_list(self, obj):
        if obj.situacion_actual == None:
            return None
        sit=Formal_Situacion_Actual.objects.filter(id=obj.situacion_actual.id) if Formal_Situacion_Actual.objects.filter(id=obj.situacion_actual.id) else None
        if sit == None:
           return None
        return Formal_Situacion_Actualserializer(sit, many=True).data
    
    empresa=serializers.SerializerMethodField()
    def get_empresa(self, obj):
        empresa=Formal_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__sociedad_financiera__nombre',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if empresa == None:
           return None
        
        return empresa

    Educacion_List=serializers.SerializerMethodField()
    def get_Educacion_List(self, obj):
        fe=Formal_Educacion.objects.filter(empleado=obj.id) if Formal_Educacion.objects.filter(empleado=obj.id) else None
        if fe == None:
           return None
        return Formal_Educacionserializer(fe, many=True).data

    Salud_List=serializers.SerializerMethodField()
    def get_Salud_List(self, obj):
        salud=Formal_Salud.objects.filter(empleado=obj.id) if Formal_Salud.objects.filter(empleado=obj.id) else None
        if salud == None:
           return None
        return Formal_Saludserializer(salud, many=True).data
    Salud_List=serializers.SerializerMethodField()
    def get_Salud_List(self, obj):
        salud=Formal_Salud.objects.filter(empleado=obj.id) if Formal_Salud.objects.filter(empleado=obj.id) else None
        if salud == None:
           return None
        return Formal_Saludserializer(salud, many=True).data
   
    jefe=serializers.SerializerMethodField()
    def get_jefe(self, obj):
        jefe=Formal_empleado.objects.filter(codigo=obj.jefe_inmediato) if Formal_empleado.objects.filter(codigo=obj.jefe_inmediato) else None
        if jefe == None:
           return None
        return Formal_empleado_jerarquiaserializer(jefe, many=True).data

    #para Funciones
    Funciones_List=serializers.SerializerMethodField()
    def get_Funciones_List(self,obj):
        fe= Formal_empleado.objects.filter(id=obj.id).values_list('posicion__id',flat=True) if Formal_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        ff=Formal_Funciones.objects.filter(id__in=fe) if Formal_Funciones.objects.filter(id__in=fe) else None
        if ff==None:
            return None
        return Formal_Funcionesserializer(ff,many=True).data

    class Meta:
        model = Formal_empleado
        fields = '__all__'

class formal_unidad_organizativabasicoserializer(serializers.ModelSerializer):
    class Meta:

        model = Formal_Unidad_Organizativa
        fields = '__all__'

class funcional_unidad_organizativabasicoserializer(serializers.ModelSerializer):
    class Meta:

        model = Funcional_Unidad_Organizativa
        fields = '__all__'

class formal_unidad_organizativaserializer(serializers.ModelSerializer):
    #count = serializers.SerializerMethodField()
    #def get_count(self, obj):
    #return Formal_Unidad_Organizativa.objects.all().count()
    lider = serializers.SerializerMethodField()
    hijos = serializers.SerializerMethodField()

    
    def get_hijos(self,obj):
        hijos=Formal_Unidad_Organizativa.objects.filter(id=obj.id,unidad_organizativa_jeraquia__isnull=False).values_list("unidad_organizativa_jeraquia",flat=True) if Formal_Unidad_Organizativa.objects.filter(id=obj.id) else None
        if hijos!=None:
            h = Formal_Unidad_Organizativa.objects.filter(id__in=hijos,codigo__isnull=False)
                
            if h ==None:
                return None
            else:
              return  formal_unidad_organizativaserializer(h,many=True).data
       
        return  None

    def get_lider(self, obj):
        lider = Formal_empleado.objects.filter(codigo=obj.Dirigido_por) if Formal_empleado.objects.filter(codigo=obj.Dirigido_por) else None
        if lider==None:   
            return None
        return Formal_empleadoserializer(lider, many=True).data

    class Meta:

        model = Formal_Unidad_Organizativa
        fields = '__all__'

class Funcional_empleado_jerarquiaserializer(serializers.ModelSerializer):

    class Meta:

        model = Funcional_empleado
        fields = ['nombre','foto','id','codigo']
        

class Funcional_empleado_arbol_jerarquiaserializer(serializers.ModelSerializer):
    padre = serializers.SerializerMethodField()
    puesto_nombre= serializers.SerializerMethodField()
    def get_padre(self,obj):
        
        if obj.puesto.all().count()==0:
            return None

        return obj.puesto.all().values_list('unidad_organizativa__id',flat=True)[0]

    def get_puesto_nombre(self,obj):
        
        if obj.puesto.all().count()==0:
            return None

        return obj.puesto.all().values_list('descripcion',flat=True)[0]


    class Meta:

        model = Funcional_empleado
        fields = ['nombre','foto','id','codigo','padre','puesto_nombre']

class Formal_empleado_jerarquiaserializer(serializers.ModelSerializer):

    class Meta:

        model = Formal_empleado
        fields = ['nombre','foto','id','codigo']

class Formal_empleado_foto_serializer(serializers.ModelSerializer):

    class Meta:

        model = Formal_empleado
        fields = ['foto']
        
class Formal_empleado_nodojerarquiaserializer(serializers.ModelSerializer):
    puesto = serializers.SerializerMethodField()
    padre = serializers.SerializerMethodField()

    def get_padre(self, obj):
        padre = Formal_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True)[:1][0] if Formal_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True) else None
        if padre==None:
            return None
        return padre
    def get_puesto(self, obj):
        padre = Formal_empleado.objects.filter(id=obj.id).values_list('puesto__descripcion',flat=True)[:1][0] if Formal_empleado.objects.filter(id=obj.id).values_list('puesto__descripcion',flat=True) else None
        if padre==None:
            return None
        return padre


    class Meta:

        model = Formal_empleado
        fields = ['id','codigo','nombre','foto','padre','puesto']

class Funcional_empleado_nodojerarquiaserializer(serializers.ModelSerializer):
    puesto = serializers.SerializerMethodField()
    padre = serializers.SerializerMethodField()

    def get_padre(self, obj):
        padre = Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True)[:1][0] if Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True) else None
        if padre==None:
            return None
        return padre
    def get_puesto(self, obj):
        padre = Funcional_empleado.objects.filter(id=obj.id).values_list('puesto__descripcion',flat=True)[:1][0] if Funcional_empleado.objects.filter(id=obj.id).values_list('puesto__descripcion',flat=True) else None
        if padre==None:
            return None
        return padre


    class Meta:

        model = Funcional_empleado
        fields = ['id','codigo','nombre','foto','padre','puesto']        

class formal_unidad_organizativa_jerarquiaserializer(serializers.ModelSerializer):
    lider = serializers.SerializerMethodField()
    padre = serializers.SerializerMethodField()
    conteo_empleado = serializers.SerializerMethodField()

    def get_lider(self, obj):
        lider = Formal_empleado.objects.filter(codigo=obj.Dirigido_por) if Formal_empleado.objects.filter(codigo=obj.Dirigido_por) else None
        if lider==None:
            lider = Formal_empleado.objects.filter(puesto__unidad_organizativa__codigo=obj.codigo) if Formal_empleado.objects.filter(puesto__unidad_organizativa__codigo=obj.codigo) else None
            #print('este es el empleado',lider[0])
            if lider ==None:
                return None
            if lider.count()==0:
                return None
            lider = lider[0].jefe_inmediato if lider != None else None
            if lider!= None:
                #print('este es el codigo del jefe',lider)
                lider = Formal_empleado.objects.filter(codigo=lider)
            else:    
                return None
        if lider.count()==0:
            return None

        return Formal_empleado_jerarquiaserializer(lider[0]).data

    def get_padre(self, obj):
        padre = Formal_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia=obj.id).values_list('id',flat=True)[:1][0] if Formal_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia=obj.id) else None
        if padre==None:
            return None
        return padre

    def get_conteo_empleado(self, obj):
        conteo = Formal_empleado.objects.filter(unidad_organizativa__id=obj.id) if Formal_empleado.objects.filter(unidad_organizativa__id=obj.id) else None
        if conteo==None:
            return None
        return conteo.count()



    class Meta:

        model = Formal_Unidad_Organizativa
        fields = ['id','nombre','codigo','principal','padre','lider','conteo_empleado']


class funcional_unidad_organizativa_jerarquiaserializer(serializers.ModelSerializer):
    lider = serializers.SerializerMethodField()
    padre = serializers.SerializerMethodField()
    conteo_empleado = serializers.SerializerMethodField()

    def get_lider(self, obj):
        lider = Funcional_empleado.objects.filter(codigo=obj.Dirigido_por) if Funcional_empleado.objects.filter(codigo=obj.Dirigido_por) else None
        if lider==None:
            lider = Funcional_empleado.objects.filter(puesto__unidad_organizativa__codigo=obj.codigo) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__codigo=obj.codigo) else None
            if lider ==None:
                return None
            if lider.count()==0:
                return None
            lider = lider[0].jefe_inmediato if lider != None else None
            if lider!= None:
               #print('este es el codigo del jefe',lider)
                lider = Funcional_empleado.objects.filter(codigo=lider)
            else:    
                return None
        if lider.count()==0:
            return None
        
        return Funcional_empleado_jerarquiaserializer(lider[0]).data

    def get_padre(self, obj):
        padre = Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia=obj.id).values_list('id',flat=True)[:1][0] if Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia=obj.id) else None
        if padre==None:
            return None
        return padre

    def get_conteo_empleado(self, obj):
        conteo = Funcional_empleado.objects.filter(unidad_organizativa__id=obj.id) if Funcional_empleado.objects.filter(unidad_organizativa__id=obj.id) else None
        if conteo==None:
            return None
        return conteo.count()



    class Meta:

        model = Funcional_Unidad_Organizativa
        fields = ['id','nombre','codigo','principal','padre','lider','conteo_empleado']


class funcional_unidad_organizativaserializer(serializers.ModelSerializer):
#    count = serializers.SerializerMethodField()
#    def get_count(self, obj):
#       return Formal_Unidad_Organizativa.objects.all().count()
    lider = serializers.SerializerMethodField()
    hijos = serializers.SerializerMethodField()

    
    def get_hijos(self,obj):
        hijos=Funcional_Unidad_Organizativa.objects.filter(id=obj.id,unidad_organizativa_jeraquia__isnull=False).values_list("unidad_organizativa_jeraquia",flat=True) if Funcional_Unidad_Organizativa.objects.filter(id=obj.id) else None
        if hijos!=None:
            h = Funcional_Unidad_Organizativa.objects.filter(id__in=hijos,codigo__isnull=False)
                
            if h ==None:
                return None
            else:
              return  funcional_unidad_organizativaserializer(h,many=True).data
       
        return  None

    def get_lider(self, obj):
        lider = Funcional_empleado.objects.filter(codigo=obj.Dirigido_por) if Funcional_empleado.objects.filter(codigo=obj.Dirigido_por) else None
        if lider==None:
            return None
        return Funcional_empleadoserializer(lider, many=True).data

    class Meta:

        model = Funcional_Unidad_Organizativa
        fields = '__all__'




class groupserializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class Formal_Relacion_Laboralserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Relacion_Laboral
        fields = '__all__'

class Formal_Check_Listserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Check_List
        fields = '__all__'

class Formal_Empleado_Check_Listserializer(serializers.ModelSerializer):
    check_name = serializers.SerializerMethodField()

    def get_check_name(self,obj):
        if obj.checklist ==None:
            return None
        nombre=Formal_Check_List.objects.filter(id=obj.checklist.id)[0] if Formal_Check_List.objects.filter(id=obj.checklist.id) else None
        if nombre ==None :
            return None
        nombre=nombre.nombre
        return nombre

    class Meta:        
        model = Formal_Empleado_Check_List
        fields = '__all__'

class Funcional_Relacion_Laboralserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Relacion_Laboral
        fields = '__all__'

class Formal_Estado_civilserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Estado_civil
        fields = '__all__'


#class Formal_Estado_civilserializer(serializers.ModelSerializer):
#    class Meta:
#        model = Formal_Estado_civil
#        fields = '__all__'

# class Formal_empleadoserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Formal_empleado
#         fields = '__all__'


class archivos_gestorserializer(serializers.ModelSerializer):
    class Meta:
        model = archivos_gestor
        fields ='__all__'


class Funcional_Tituloserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Titulo
        fields ='__all__'


class Funcional_Institutoserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Instituto
        fields='__all__'


class Funcional_Diagnosticoserializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Funcional_Diagnostico
        fields='__all__'




class Funcional_Saludserializer(serializers.ModelSerializer):
    diagnostico_list = serializers.SerializerMethodField()
    archivo_gestor  =serializers.SerializerMethodField()

    def get_diagnostico_list(self,obj):
        if obj ==None:
            return None
        if obj.diagnostico==None:
            return None
        diagnostico=Funcional_Diagnostico.objects.filter(id=obj.diagnostico.id) if Funcional_Diagnostico.objects.filter(id=obj.diagnostico.id) else None
        
        if diagnostico==None:
            return None
        return Funcional_Diagnosticoserializer(diagnostico, many=True).data

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
        model = Funcional_Salud
        fields='__all__'        
class Funcional_Educacionserializer(serializers.ModelSerializer):
    formacion_list=serializers.SerializerMethodField()
    def get_formacion_list(self,obj):
        
        formacion=Funcional_Formacion.objects.filter(id=obj.formacion.id) if Funcional_Formacion.objects.filter(id=obj.formacion.id) else None
        
        if formacion==None:
            return None
        
        return Funcional_Formacionserializer(formacion[0]).data



    especialidad_list=serializers.SerializerMethodField()
    def get_especialidad_list(self,obj):
            
        if not obj.especialidad:
            return None
        especialidad=Funcional_Especialidad.objects.filter(id=obj.especialidad.id) if Funcional_Especialidad.objects.filter(id=obj.especialidad.id) else None
        
        if especialidad==None:
            return None
        return Funcional_Especialidadserializer(especialidad[0]).data


    instituto_list=serializers.SerializerMethodField()
    def get_instituto_list(self,obj):
            
        if not obj.instituto:
            return None
        instituto=Funcional_Instituto.objects.filter(id=obj.instituto.id) if Funcional_Instituto.objects.filter(id=obj.instituto.id) else None
        
        if instituto==None:
            return None
        return Funcional_Institutoserializer(instituto[0]).data

    titulo_list=serializers.SerializerMethodField()
    def get_titulo_list(self,obj):
            
        if not obj.titulo:
            return None
        titulo=Funcional_Titulo.objects.filter(id=obj.titulo.id) if Funcional_Titulo.objects.filter(id=obj.titulo.id) else None
        
        if titulo==None:
            return None
        return Funcional_Tituloserializer(titulo[0]).data

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
        model = Funcional_Educacion
        fields='__all__'



class archivos_gestor_formatos_oficialesserializer(serializers.ModelSerializer):
    class Meta:
        model = archivos_gestor_formatos_oficiales
        fields ='__all__'

class generoserializer(serializers.ModelSerializer):
    class Meta:
        model = genero
        fields = '__all__'

class descriptor_perfil_formacion_area_conocimientoserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_formacion_area_conocimiento
        fields = '__all__'


class descriptor_perfil_cursos_diplomados_seminario_pasantiaserializer(serializers.ModelSerializer):
    
    list_unidad_medida = serializers.SerializerMethodField()
    def get_list_unidad_medida(self, obj):
        
        unidad = descriptor_perfil_datos_unidad_medida.objects.filter(id=obj.unidad_medida_id) if descriptor_perfil_datos_unidad_medida.objects.filter(id=obj.unidad_medida_id)  else None
        if unidad == None:
           return None
        return descriptor_perfil_datos_unidad_medidasserializer(unidad, many=True).data

    class Meta:
        model = descriptor_perfil_cursos_diplomados_seminario_pasantia
        fields = '__all__'
  
class descriptor_perfil_formacion_nivel_educativoserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_formacion_nivel_educativo
        fields = '__all__'

class descriptor_perfil_tituloserializer(serializers.ModelSerializer):
    list_nivel_academico = serializers.SerializerMethodField()
    def get_list_nivel_academico(self, obj):
        
        nivel_educativo = descriptor_perfil_formacion_nivel_educativo.objects.filter(id=obj.nivel_academico_id) if descriptor_perfil_formacion_nivel_educativo.objects.filter(id=obj.nivel_academico_id)  else None
        if nivel_educativo == None:
           return None
        return descriptor_perfil_formacion_nivel_educativoserializer(nivel_educativo, many=True).data
    
    list_area_conocimiento = serializers.SerializerMethodField()
    def get_list_area_conocimiento(self, obj):
        
        area_conocimiento = descriptor_perfil_formacion_area_conocimiento.objects.filter(id=obj.area_conocimiento_id) if descriptor_perfil_formacion_area_conocimiento.objects.filter(id=obj.area_conocimiento_id)  else None
        if area_conocimiento == None:
           return None
        return descriptor_perfil_formacion_area_conocimientoserializer(area_conocimiento, many=True).data
    

    class Meta:
        model = descriptor_perfil_titulo
        fields = '__all__'

class descriptor_perfil_conocimiento_tecnicoserializer(serializers.ModelSerializer):
    class Meta:
        model = descriptor_perfil_conocimiento_tecnico
        fields = '__all__'


class funcional_funciones_descriptorserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Funciones
        fields = ['id','codigo']



class Funcional_empleadoserializer(serializers.ModelSerializer):
    Formacion_List = serializers.SerializerMethodField()
    #historial_list = Funcional_Historial_Laboralserializer(many=True, read_only=True)
    #este es un campo many to many dentro de la tabla de Funcional_empleado

    def get_Formacion_List(self, obj):
        fe=Funcional_empleado.objects.filter(id=obj.id).values_list('formacion__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe == None:
           return None

        ff = Funcional_Formacion.objects.filter(id__in=fe)
        if not ff:
            return None
        return Funcional_Formacionserializer(ff, many=True).data

    clasificacion_nombre = serializers.SerializerMethodField()
    def get_clasificacion_nombre(self,obj):
        if obj.clasificacion_empleado == None:
            return None
        clasificacion=Funcional_Clasificacion.objects.filter(id=obj.clasificacion_empleado_id) if Funcional_Clasificacion.objects.filter(id=obj.clasificacion_empleado_id) else None
        if clasificacion == None:
           return None
        return Funcional_Clasificacionserializer(clasificacion, many=True).data    

    Descriptor_listo = serializers.SerializerMethodField()
    def get_Descriptor_listo(self,obj):
        
        Funcion = Funcional_empleado.objects.filter(id=obj.pk).values_list('posicion',flat=True)
        funcion_2=Funcional_Funciones.objects.filter(id=Funcion[0]) if Funcional_Funciones.objects.filter(id=Funcion[0]) else None
        if funcion_2 == None:
           return None
        return funcional_funciones_descriptorserializer(funcion_2, many=True).data    


    #el empleado es una llava foranea en la tabla Funcional_Historial_Laboral
    Historial_Laboral_List = serializers.SerializerMethodField()
    def get_Historial_Laboral_List(self, obj):
        fhl=Funcional_Historial_Laboral.objects.filter(empleado=obj.id) if Funcional_Historial_Laboral.objects.filter(empleado=obj.id) else None
        if fhl == None:
           return None
        return Funcional_Historial_Laboralserializer(fhl, many=True).data

    #para dependientes económicos
    Dependientes_Economicos_List = serializers.SerializerMethodField()
    def get_Dependientes_Economicos_List(self,obj):
        fde=Funcional_Dependientes_Economico.objects.filter(empleado=obj.id) if Funcional_Dependientes_Economico.objects.filter(empleado=obj.id) else None
        if fde == None:
            return None
        return Funcional_Dependientes_Economicoserializer(fde, many=True).data
    
    #para Beneficiario_Seguro
    Beneficiario_Seguro_List= serializers.SerializerMethodField()
    def get_Beneficiario_Seguro_List(self,obj):
        fbs= Funcional_Beneficiario_Seguro.objects.filter(empleado=obj.id) if Funcional_Beneficiario_Seguro.objects.filter(empleado=obj.id) else None
        if fbs == None:
            return None
        return Funcional_Beneficiario_Seguroserializer(fbs, many=True).data

    #para Relacion Laboral
    Relacion_Laboral_List= serializers.SerializerMethodField()
    def get_Relacion_Laboral_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('relacion_laboral__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe == None:
            return fe
        frl= Funcional_Relacion_Laboral.objects.filter(id__in=fe)
        if not frl:
            return None
        return Funcional_Relacion_Laboralserializer(frl,many=True).data
        
    #para Division
    Division_List= serializers.SerializerMethodField()
    def get_Division_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('division__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fd=Funcional_Division.objects.filter(id__in=fe) if Funcional_Division.objects.filter(id__in=fe) else None
        if  fd==None:
            return None
        return Funcional_Divisionserializer(fd, many=True).data

    Division_Personal_List= serializers.SerializerMethodField()
    def get_Division_Personal_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('division_personal__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fd=Funcional_Division_Personal.objects.filter(id__in=fe) if Funcional_Division_Personal.objects.filter(id__in=fe) else None
        if  fd==None:
            return None
        return Funcional_Division_Personalserializer(fd, many=True).data
    
    #para Centro de Costo
    Centro_Costo_List=serializers.SerializerMethodField()
    def get_Centro_Costo_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('centro_costo__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fcc=Funcional_Centro_Costo.objects.filter(id__in=fe) if Funcional_Centro_Costo.objects.filter(id__in=fe) else None
        if fcc==None:
            return None
        return Funcional_Centro_Costoserializer (fcc,many=True).data

    #para Estado Civil
    Estado_Civil_List=serializers.SerializerMethodField()
    def get_Estado_Civil_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('estado_civil__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fec=Funcional_Estado_civil.objects.filter(id__in=fe) if Funcional_Estado_civil.objects.filter(id__in=fe) else None
        if fec==None:
            return None
        return Funcional_Estado_civilserializer(fec,many=True).data

    #para Puesto
    Puesto_List=serializers.SerializerMethodField()
    def get_Puesto_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('puesto__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fp=Funcional_Puesto.objects.filter(id__in=fe) if Funcional_Puesto.objects.filter(id__in=fe) else None
        if fp==None:
            return None
        return funcional_puestoserializer(fp,many=True).data

    #para unidad organizativa
    Unidad_Organizativa_List=serializers.SerializerMethodField()
    def get_Unidad_Organizativa_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fuo=Funcional_Unidad_Organizativa.objects.filter(id__in=fe) if Funcional_Unidad_Organizativa.objects.filter(id__in=fe) else None
        if fuo==None:
            return None
        return funcional_unidad_organizativabasicoserializer(fuo,many=True).data

    #para especialidad
    Especialidad_List=serializers.SerializerMethodField()
    def get_Especialidad_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('especialidad__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        fel=Funcional_Especialidad.objects.filter(id__in=fe) if Funcional_Especialidad.objects.filter(id__in=fe) else None
        if fel==None:
            return None
        return Funcional_Especialidadserializer(fel,many=True).data

    #para Contacto de emergencia
    Contacto_Emergencia_List=serializers.SerializerMethodField()
    def get_Contacto_Emergencia_List(self, obj):
        fce=Funcional_Contacto_Emergencia.objects.filter(empleado=obj.id) if Funcional_Contacto_Emergencia.objects.filter(empleado=obj.id) else None
        if fce == None:
           return None
        return Funcional_Contacto_Emergenciaserializer(fce, many=True).data

    
    situacion_actual_list=serializers.SerializerMethodField()
    def get_situacion_actual_list(self, obj):
        if obj.situacion_actual == None:
            return None
        sit=Funcional_Situacion_Actual.objects.filter(id=obj.situacion_actual.id) if Funcional_Situacion_Actual.objects.filter(id=obj.situacion_actual.id) else None
        if sit == None:
           return None
        return Funcional_Situacion_Actualserializer(sit, many=True).data
    
    empresa=serializers.SerializerMethodField()
    def get_empresa(self, obj):
        empresa=Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__sociedad_financiera__nombre',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if empresa == None:
           return None
        
        return empresa
    
    empresa_id=serializers.SerializerMethodField()
    def get_empresa_id(self, obj):
        empresa=Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__sociedad_financiera',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if empresa == None:
           return None
        
        return empresa

    Educacion_List=serializers.SerializerMethodField()
    def get_Educacion_List(self, obj):
        fe=Funcional_Educacion.objects.filter(empleado=obj.id) if Funcional_Educacion.objects.filter(empleado=obj.id) else None
        if fe == None:
           return None
        return Funcional_Educacionserializer(fe, many=True).data

    Salud_List=serializers.SerializerMethodField()
    def get_Salud_List(self, obj):
        salud=Funcional_Salud.objects.filter(empleado=obj.id) if Funcional_Salud.objects.filter(empleado=obj.id) else None
        if salud == None:
           return None
        return Funcional_Saludserializer(salud, many=True).data
    Salud_List=serializers.SerializerMethodField()
    def get_Salud_List(self, obj):
        salud=Funcional_Salud.objects.filter(empleado=obj.id) if Funcional_Salud.objects.filter(empleado=obj.id) else None
        if salud == None:
           return None
        return Funcional_Saludserializer(salud, many=True).data
   
    jefe=serializers.SerializerMethodField()
    def get_jefe(self, obj):
        jefe=Funcional_empleado.objects.filter(codigo=obj.jefe_inmediato) if Funcional_empleado.objects.filter(codigo=obj.jefe_inmediato) else None
        if jefe == None:
           return None
        return Funcional_empleado_jerarquiaserializer(jefe, many=True).data

    #para Funciones
    Funciones_List=serializers.SerializerMethodField()
    def get_Funciones_List(self,obj):
        fe= Funcional_empleado.objects.filter(id=obj.id).values_list('posicion__id',flat=True) if Funcional_empleado.objects.filter(id=obj.id) else None
        if fe==None:
            return None
        ff=Funcional_Funciones.objects.filter(id__in=fe) if Funcional_Funciones.objects.filter(id__in=fe) else None
        if ff==None:
            return None
        return Funcional_Funcionesserializer(ff,many=True).data

    croquis  =serializers.SerializerMethodField()
    def get_croquis(self,obj):
        if obj ==None:
            return None
        #if obj.archivos_gestor==None:
        #    return None
        Archivo_gestor=archivos_gestor.objects.filter(tipo_documento='direccion',id_empleado=obj.id) if archivos_gestor.objects.filter(tipo_documento='direccion',id_empleado=obj.id) else None
        
        if Archivo_gestor==None:
            return None
        return archivos_gestorserializer(Archivo_gestor, many=True).data
    estado_civil_archivo  =serializers.SerializerMethodField()
    def get_estado_civil_archivo(self,obj):
        if obj ==None:
            return None
        #if obj.archivos_gestor==None:
        #    return None
        Archivo_gestor=archivos_gestor.objects.filter(tipo_documento='estado_civil',id_empleado=obj.id).order_by('-id')[0] if archivos_gestor.objects.filter(tipo_documento='estado_civil',id_empleado=obj.id) else None
        
        if Archivo_gestor==None:
            return None
        return archivos_gestorserializer([Archivo_gestor], many=True).data

    # list_casos_disciplinarios  =serializers.SerializerMethodField()
    # def get_list_casos_disciplinarios(self,obj):
    #     if obj ==None:
    #         return None
    #     #if obj.archivos_gestor==None:
    #     #    return None
    #     casos_disciplinarios=sanciones_casos_disciplinarios.objects.filter(codigo_empleado__id=obj.id).order_by('-id') if sanciones_casos_disciplinarios.objects.filter(codigo_empleado__id=obj.id) else None
        
    #     if casos_disciplinarios==None:
    #         return None
    #     return sanciones_casos_disciplinariosserializer(casos_disciplinarios, many=True).data
    conteo_casos= serializers.SerializerMethodField()
    def get_conteo_casos(self,obj):
        conteo = sanciones_casos_disciplinarios.objects.filter(codigo_empleado__id=obj.id).count() if sanciones_casos_disciplinarios.objects.filter(codigo_empleado__id=obj.id) else 0
    
        return conteo


    descriptor_List = serializers.SerializerMethodField()
    def get_descriptor_List(self, obj):
        if obj.posicion:
            ##ff=Funcional_Funciones.objects.filter(id=obj.posicion.id).order_by('-id')
            ff=1
            if ff:
                descriptor=descriptor_perfil_datos_generales.objects.filter(posicion__in=obj.posicion.all()).order_by('-id')
                #descriptor={"puesto":123,"puesto2":"123"}
                if descriptor:
                    #serializado=descriptor_perfil_datos_generalesserializer(descriptor)
                    respuesta=descriptor
                    respuesta={"nombre_posicion":descriptor[0].nombre_posicion,"descripcion_larga":descriptor[0].descripcion_larga,'id':descriptor[0].id}
                    return respuesta
                else: 
                   respuesta=None
            else:
                respuesta=None
        return None
    
    list_municipio=serializers.SerializerMethodField()
    def get_list_municipio(self, obj):
        municipio=head_clima_municipio.objects.filter(id=obj.municipio_id) if head_clima_municipio.objects.filter(id=obj.municipio_id) else None
        if municipio == None:
           return None
        return head_clima_municipioserializer(municipio, many=True).data


    list_username = serializers.SerializerMethodField()
    def get_list_username(self, obj):
        
        user = User.objects.filter(username=obj.codigo) if User.objects.filter(username=obj.codigo) else None
        if user == None:
           return None
        return UsuariosSerializer(user, many=True).data


    class Meta:
        
        model = Funcional_empleado
        fields = '__all__'


class Funcional_empleado_foto_serializer(serializers.ModelSerializer):

    class Meta:

        model = Funcional_empleado
        fields = ['foto']

#Agregado 
class Formal_Divisionserializer(serializers.ModelSerializer):
    class Meta:
        model= Formal_Division
        fields= '__all__'

class Formal_Division_Personalserializer(serializers.ModelSerializer):
    class Meta:
        model= Formal_Division_Personal
        fields= '__all__'

class Formal_Organizacionserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Organizacion
        fields = '__all__'

class Formal_Centro_Costoserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Centro_Costo
        fields = '__all__'

class Funcional_Divisionserializer(serializers.ModelSerializer):
    class Meta:
        model= Funcional_Division
        fields= '__all__'

class Funcional_Division_Personalserializer(serializers.ModelSerializer):
    class Meta:
        model= Funcional_Division_Personal
        fields= '__all__'


class Funcional_Centro_Costoserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Centro_Costo
        fields = '__all__'

class Funcional_Organizacionserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Organizacion
        fields = '__all__'

class Funcional_Estado_civilserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Estado_civil
        fields = '__all__'

#agregado 2
class Formal_Parentescoserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Parentesco
        fields = '__all__'

class Funcional_Parentescoserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Parentesco
        fields = '__all__'

class Formal_Generoserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Genero
        fields = '__all__'

class Funcional_Generoserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Genero
        fields = '__all__'

class Formal_Funcionesserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Funciones
        fields = '__all__'

class Funcional_Funcionesserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Funciones
        fields = '__all__'

class Funcional_Funcionessserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Funciones
        fields = ('id','nombre','codigo','descripcion',)

class Formal_Situacion_Actualserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Situacion_Actual
        fields = '__all__'

class Funcional_Situacion_Actualserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Situacion_Actual
        fields = '__all__'

class Formal_Compañiaserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Compañia
        fields = '__all__'

class Funcional_Compañiaserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Compañia
        fields = '__all__'

class Formal_Especialidadserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Especialidad
        fields = '__all__'

class Funcional_Especialidadserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Especialidad
        fields = '__all__'

class Formal_Contacto_Emergenciaserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Contacto_Emergencia
        fields = '__all__'

class Funcional_Contacto_Emergenciaserializer(serializers.ModelSerializer):
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
        model = Funcional_Contacto_Emergencia
        fields = '__all__'

class Formal_Dependientes_Economicoserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Dependientes_Economico
        fields = '__all__'

class Funcional_Dependientes_Economicoserializer(serializers.ModelSerializer):
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
        model = Funcional_Dependientes_Economico
        fields = '__all__'

class Formal_Beneficiario_Seguroserializer(serializers.ModelSerializer):
    parentesco_list = serializers.SerializerMethodField()

    def get_parentesco_list(self,obj):
        parentesco=Formal_Parentesco.objects.filter(id=obj.parentesco.id) if Formal_Parentesco.objects.filter(id=obj.parentesco.id) else None
        
        if parentesco==None:
            return None
        return Formal_Parentescoserializer(parentesco, many=True).data

    class Meta:
        model = Formal_Beneficiario_Seguro
        fields = '__all__'

class Funcional_Beneficiario_Seguroserializer(serializers.ModelSerializer):
    parentesco_list = serializers.SerializerMethodField()

    def get_parentesco_list(self,obj):
        parentesco=Funcional_Parentesco.objects.filter(id=obj.parentesco.id) if Funcional_Parentesco.objects.filter(id=obj.parentesco.id) else None
        
        if parentesco==None:
            return None
        return Funcional_Parentescoserializer(parentesco, many=True).data

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
        model = Funcional_Beneficiario_Seguro
        fields = '__all__'

class Formal_Formacionserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Formacion
        fields = '__all__'

class Funcional_Formacionserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Formacion
        fields = '__all__'


class Formal_Equiposerializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Equipo
        fields = '__all__'

class Funcional_Equiposerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Equipo
        fields = '__all__'

class Funcional_Relacion_Laboral_Anteriorserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Relacion_Laboral_Anterior
        fields = '__all__'

class Funcional_Historial_Laboralserializer(serializers.ModelSerializer):
    puesto_list=serializers.SerializerMethodField()
    def get_puesto_list(self, obj):
        if obj.puesto == None:
            return None
        pto=Funcional_Relacion_Laboral_Anterior.objects.filter(id=obj.puesto.id) if Funcional_Relacion_Laboral_Anterior.objects.filter(id=obj.puesto.id) else None
        if pto == None:
           return None
        return Funcional_Relacion_Laboral_Anteriorserializer(pto, many=True).data

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
        model = Funcional_Historial_Laboral
        fields = '__all__'


class Data_userserializer(serializers.Serializer):
    id_user = serializers.IntegerField()
    id = serializers.IntegerField()
    username =serializers.CharField()
    nombre  = serializers.CharField()
    grupo = serializers.ListField(child = serializers.CharField())
    foto = serializers.ImageField()
    actualizado=serializers.BooleanField()
    
    class Meta:
        fields =['id_user','id','username','nombre','grupo','foto','actualizado']


class Actualizacion_Contactoserializer(serializers.ModelSerializer):
    class Meta:
        model = Actualizacion_Contacto
        fields = '__all__'

class Actualizacion_Dependienteserializer(serializers.ModelSerializer):
    class Meta:
        model = Actualizacion_Dependiente
        fields = '__all__'

class Actualizacion_Domicilioserializer(serializers.ModelSerializer):
    class Meta:
        model = Actualizacion_Domicilio
        fields = '__all__'

class Actualizacion_Educacionserializer(serializers.ModelSerializer):
    class Meta:
        model = Actualizacion_Educacion
        fields = '__all__'

class Actualizacion_Estado_Civilserializer(serializers.ModelSerializer):
    class Meta:
        model = Actualizacion_Estado_Civil
        fields = '__all__'

class Funcional_Check_Listserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Check_List
        fields = '__all__'

class Funcional_Empleado_Check_Listserializer(serializers.ModelSerializer):

    check_name = serializers.SerializerMethodField()
    def get_check_name(self,obj):
        if obj.checklist ==None:
            return None
        nombre=Funcional_Check_List.objects.filter(id=obj.checklist.id)[0] if Funcional_Check_List.objects.filter(id=obj.checklist.id) else None
        if nombre ==None :
            return None
        nombre=nombre.nombre
        return nombre
    
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
        model = Funcional_Empleado_Check_List
        fields = '__all__'

class Configuracion_Actualizacion_Empleadoserializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracion_Actualizacion_Empleado
        fields = '__all__'


#Agregado Para manejo de Vacunas 
class Funcional_Laboratorioserializer(serializers.ModelSerializer):
    class Meta:
        model = Funcional_Laboratorio
        fields = '__all__'

class Funcional_Vacunaserializer(serializers.ModelSerializer):
    laboratorio_list = serializers.SerializerMethodField()

    def get_laboratorio_list(self,obj):
        laboratorio=Funcional_Laboratorio.objects.filter(id=obj.laboratorio.id) if Funcional_Laboratorio.objects.filter(id=obj.laboratorio.id) else None
        
        if laboratorio==None:
            return None
        return Funcional_Laboratorioserializer(laboratorio, many=True).data


    class Meta:
        model = Funcional_Vacuna
        fields='__all__'

class Funcional_Empleado_Vacunaserializer(serializers.ModelSerializer):
    vacuna_list = serializers.SerializerMethodField()

    def get_vacuna_list(self,obj):
        vacuna=Funcional_Vacuna.objects.filter(id=obj.vacuna.id) if Funcional_Vacuna.objects.filter(id=obj.vacuna.id) else None
        
        if vacuna==None:
            return None
        return Funcional_Vacunaserializer(vacuna, many=True).data

    empleado_list = serializers.SerializerMethodField()

    def get_empleado_list(self,obj):
        empleado=Funcional_empleado.objects.filter(id=obj.empleado.id) if Funcional_empleado.objects.filter(id=obj.empleado.id) else None
        
        if empleado==None:
            return None
        return Funcional_empleadoserializer(empleado, many=True).data


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
        model = Funcional_Empleado_Vacuna
        fields='__all__'

class Formal_Laboratorioserializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_Laboratorio
        fields = '__all__'

class Formal_Vacunaserializer(serializers.ModelSerializer):
    laboratorio_list = serializers.SerializerMethodField()

    def get_laboratorio_list(self,obj):
        laboratorio=Formal_Laboratorio.objects.filter(id=obj.laboratorio.id) if Formal_Laboratorio.objects.filter(id=obj.laboratorio.id) else None
        
        if laboratorio==None:
            return None
        return Formal_Laboratorioserializer(laboratorio, many=True).data


    class Meta:
        model = Formal_Vacuna
        fields='__all__'

class Formal_Empleado_Vacunaserializer(serializers.ModelSerializer):
    vacuna_list = serializers.SerializerMethodField()

    def get_vacuna_list(self,obj):
        vacuna=Formal_Vacuna.objects.filter(id=obj.vacuna.id) if Formal_Vacuna.objects.filter(id=obj.vacuna.id) else None
        
        if vacuna==None:
            return None
        return Formal_Vacunaserializer(vacuna, many=True).data

    empleado_list = serializers.SerializerMethodField()

    def get_empleado_list(self,obj):
        empleado=Formal_empleado.objects.filter(id=obj.empleado.id) if Formal_empleado.objects.filter(id=obj.empleado.id) else None
        
        if empleado==None:
            return None
        return Formal_empleadoserializer(empleado, many=True).data

    class Meta:
        model = Formal_Empleado_Vacuna
        fields='__all__'

class Formal_Clasificacionserializer (serializers.ModelSerializer):
    class Meta:
        model = Formal_Clasificacion
        fields = '__all__'


class Funcional_Clasificacionserializer (serializers.ModelSerializer):
    class Meta:
        model = Funcional_Clasificacion
        fields = '__all__'

class ApiJefesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    codigo = serializers.CharField()
    nombre =serializers.CharField()
    class Meta:
        fields =['id','codigo','nombre']


class Tiempos_Empleadoserializer (serializers.ModelSerializer):
    class Meta:
        model = Tiempos_Empleado
        fields = '__all__'

class Absentismo_Empleadoserializer (serializers.ModelSerializer):
    class Meta:
        model = Absentismo_Empleado
        fields = '__all__'

class Dias_Laborados_Empleadoserializer (serializers.ModelSerializer):
    class Meta:
        model = Dias_Laborados_Empleado
        fields = '__all__'

class Tiempos_Empleado_Unificadoserializer (serializers.ModelSerializer):
    absentismo = serializers.SerializerMethodField()

    def get_absentismo(self,obj):
        ab=Absentismo_Empleado.objects.filter(empleado=obj.empleado) if Absentismo_Empleado.objects.filter(empleado=obj.empleado) else None
        
        if ab==None:
            return None
        return Absentismo_Empleadoserializer(ab, many=True).data
    
    class Meta:
        model = Tiempos_Empleado
        fields = '__all__'
class funcional_arbol_padre_serializer(serializers.ModelSerializer):
    lider = serializers.SerializerMethodField()
    padre = serializers.SerializerMethodField()
    #sub_equipo = serializers.SerializerMethodField()
    conteo_empleado = serializers.SerializerMethodField()

    def get_lider(self, obj):
       #print('este es el objeto',obj)
        lider = Funcional_empleado.objects.filter(codigo=obj.Dirigido_por) if Funcional_empleado.objects.filter(codigo=obj.Dirigido_por) else None
       #print('primero este es el lider',lider)
        if lider==None:
            cod_uni= Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id__in=[obj.id]).values_list('id',flat=True)
            while lider == None and cod_uni.count()>0:
                unidad = Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id__in=cod_uni)
                lider = unidad[0].Dirigido_por if Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id__in=cod_uni) else None
               #print('este es el lider',lider)
                lider = Funcional_empleado.objects.filter(codigo=lider)
                if lider==None:
                    unidad_lista = Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia__id__in=cod_uni).values_list('codigo',flat=True)
                    cod_uni= unidad_lista
        if lider==None or lider.count()==0:
           #print('si entro a condicional')
            lider = Funcional_empleado.objects.filter(codigo=obj.Dirigido_por) if Funcional_empleado.objects.filter(codigo=obj.Dirigido_por) else None
            if lider==None:
                lider = Funcional_empleado.objects.filter(puesto__unidad_organizativa__codigo=obj.codigo) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__codigo=obj.codigo) else None
                if lider ==None:
                    return None
                if lider.count()==0:
                    return None
               #print('este es el jefe inmediato',lider[0])
                lider = lider[0].jefe_inmediato if lider != None else None
                if lider!= None:
                   #print('este es el codigo del jefe',lider)
                    lider = Funcional_empleado.objects.filter(codigo=lider)
                   #print('este es el fin',lider)
                else:    
                    return None
           #print('lider al final',lider)
            if lider.count()==0:
                return None
            else: 
                return Funcional_empleado_arbol_jerarquiaserializer(lider[0]).data
        else:
           #print('llego hasta el finalxxxxxxxxxxxxxxxxxxxxxxxxxx')
            return Funcional_empleado_arbol_jerarquiaserializer(lider[0]).data

    def get_padre(self, obj):
        padre = Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia=obj.id).values_list('id',flat=True)[:1][0] if Funcional_Unidad_Organizativa.objects.filter(unidad_organizativa_jeraquia=obj.id) else None
        if padre==None:
            return None
        return padre

    # def get_equipo(self, obj):
    #     lider=self.get_lider(obj)
    #     equipo = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id=obj.id) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id=obj.id) else None
    #     if lider!=None:
    #         equipo = Funcional_empleado.objects.filter(puesto__unidad_organizativa__id=obj.id).exclude(codigo=lider['codigo']) if Funcional_empleado.objects.filter(puesto__unidad_organizativa__id=obj.id).exclude(codigo=lider['codigo']) else None
    #     if equipo==None:
    #         return None
    #     return Funcional_empleado_jerarquiaserializer(equipo, many=True).data

    #def get_sub_equipo(self, obj):
    #    unidades=Funcional_Unidad_Organizativa.objects.filter(id=obj.id).values_list('unidad_organizativa_jeraquia__id',flat=True)
    #    unidades_resultantes=Funcional_Unidad_Organizativa.objects.filter(id__in=unidades)
    #    return funcional_arbol_serializer(unidades_resultantes, many=True).data

    def get_conteo_empleado(self, obj):
        conteo = Funcional_empleado.objects.filter(unidad_organizativa__id=obj.id) if Funcional_empleado.objects.filter(unidad_organizativa__id=obj.id) else None
        if conteo==None:
            return None
        return conteo.count()
    class Meta:
        model = Funcional_Unidad_Organizativa
        fields = ['id','nombre','principal','lider','padre','conteo_empleado']


class Funcional_empleado_nodojerarquiaserializer_mix(serializers.ModelSerializer):
    puesto = serializers.SerializerMethodField()
    padre = serializers.SerializerMethodField()

    def get_padre(self, obj):
        padre = Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True)[:1][0] if Funcional_empleado.objects.filter(id=obj.id).values_list('unidad_organizativa__id',flat=True) else None
        if padre==None:
            return None
        return padre
    def get_puesto(self, obj):
        padre = Funcional_empleado.objects.filter(id=obj.id).values_list('puesto__descripcion',flat=True)[:1][0] if Funcional_empleado.objects.filter(id=obj.id).values_list('puesto__descripcion',flat=True) else None
        if padre==None:
            return None
        return padre


    class Meta:

        model = Funcional_empleado
        fields = ['id','codigo','nombre','foto','padre','puesto']       

#Segunda Etapa Clima Laboral
##########################################PARA CLIMA LABORAL#################################################################################
class Clima_Objetoserializer (serializers.ModelSerializer):
    class Meta:
        model = Clima_Objeto
        fields = '__all__'

class Clima_Sub_Objetoserializer (serializers.ModelSerializer):
    objetos_list = serializers.SerializerMethodField()
    def get_objetos_list(self,obj):
        objetos=Clima_Objeto.objects.filter(id=obj.objeto.id) if Clima_Objeto.objects.filter(id=obj.objeto.id) else None

        if objetos==None:
            return None
        return Clima_Objetoserializer(objetos[0]).data

    class Meta:
        model = Clima_Sub_Objeto
        fields = '__all__'

class Clima_Tipo_Preguntaserializer (serializers.ModelSerializer):
    class Meta:
        model = Clima_Tipo_Pregunta
        fields = '__all__'

class Clima_Tipo_Herramientaserializer (serializers.ModelSerializer):
    class Meta:
        model = Clima_Tipo_Herramienta
        fields = '__all__'

class Clima_Plantillaserializer (serializers.ModelSerializer):
    class Meta:
        model = Clima_Plantilla
        fields = '__all__'

class Clima_Plantilla_Preguntasserializer (serializers.ModelSerializer):
    plantilla_list = serializers.SerializerMethodField()
    def get_plantilla_list(self,obj):
        plantilla=Clima_Plantilla.objects.filter(id=obj.plantilla.id) if Clima_Plantilla.objects.filter(id=obj.plantilla.id) else None

        if plantilla==None:
            return None
        return Clima_Plantillaserializer(plantilla[0]).data

    tipo_list = serializers.SerializerMethodField()
    def get_tipo_list(self,obj):
        tipo=Clima_Tipo_Pregunta.objects.filter(id=obj.tipo.id) if Clima_Tipo_Pregunta.objects.filter(id=obj.tipo.id) else None

        if tipo==None:
            return None
        return Clima_Tipo_Preguntaserializer(tipo[0]).data

    class Meta:
        model = Clima_Plantilla_Preguntas
        fields = '__all__'

class Clima_Plantilla_Opcionesserializer (serializers.ModelSerializer):
    pregunta_list = serializers.SerializerMethodField()
    def get_pregunta_list(self,obj):
        pregunta=Clima_Plantilla_Preguntas.objects.filter(id=obj.pregunta.id) if Clima_Plantilla_Preguntas.objects.filter(id=obj.pregunta.id) else None

        if pregunta==None:
            return None
        return Clima_Plantilla_Preguntasserializer(pregunta[0]).data

    class Meta:
        model = Clima_Plantilla_Opciones
        fields = '__all__'

class Clima_Segmentoserializer (serializers.ModelSerializer):
    empresas_list = serializers.SerializerMethodField()
    def get_empresas_list(self,obj):
        emp= Clima_Segmento.objects.filter(id=obj.id).values_list('empresas__id',flat=True) if Clima_Segmento.objects.filter(id=obj.id) else None
        if emp==None:
            return None
        empresas=Funcional_Organizacion.objects.filter(id__in=emp) if Funcional_Organizacion.objects.filter(id__in=emp) else None

        if empresas==None:
            return None
        return Funcional_Organizacionserializer(empresas,many=True).data
    
    unidades_list = serializers.SerializerMethodField()
    def get_unidades_list(self,obj):
        uni=Clima_Segmento.objects.filter(id=obj.id).values_list('unidades__id',flat=True) if Clima_Segmento.objects.filter(id=obj.id) else None
        if uni==None:
            return None
        unidades=Funcional_Unidad_Organizativa.objects.filter(id__in=uni) if Funcional_Unidad_Organizativa.objects.filter(id__in=uni) else None

        if unidades==None:
            return None
        return funcional_unidad_organizativabasicoserializer(unidades,many=True).data

    puestos_list = serializers.SerializerMethodField()
    def get_puestos_list(self,obj):
        pue=Clima_Segmento.objects.filter(id=obj.id).values_list('puestos__id',flat=True) if Clima_Segmento.objects.filter(id=obj.id) else None
        if pue==None:
            return None
        puestos=Funcional_Puesto.objects.filter(id__in=pue) if Funcional_Puesto.objects.filter(id__in=pue) else None

        if puestos==None:
            return None
        return funcional_puestoserializer(puestos,many=True).data

    class Meta:
        model = Clima_Segmento
        fields = '__all__'
    
class Clima_Cuestionarioserializer (serializers.ModelSerializer):
    objeto_list = serializers.SerializerMethodField()
    def get_objeto_list(self,obj):
        objeto=Clima_Objeto.objects.filter(id=obj.objeto.id) if Clima_Objeto.objects.filter(id=obj.objeto.id) else None

        if objeto==None:
            return None
        return Clima_Objetoserializer(objeto[0]).data

    class Meta:
        model = Clima_Cuestionario
        fields = '__all__'

class Clima_Cuestionario_Preguntasserializer (serializers.ModelSerializer):
    cuestionario_list = serializers.SerializerMethodField()
    def get_cuestionario_list(self,obj):
        cuestionario=Clima_Cuestionario.objects.filter(id=obj.cuestionario.id) if Clima_Cuestionario.objects.filter(id=obj.cuestionario.id) else None

        if cuestionario==None:
            return None
        return Clima_Cuestionarioserializer(cuestionario[0]).data

    subobjeto_list = serializers.SerializerMethodField()
    def get_subobjeto_list(self,obj):
        subobjeto=Clima_Sub_Objeto.objects.filter(id=obj.sub_objeto.id) if Clima_Sub_Objeto.objects.filter(id=obj.sub_objeto.id) else None

        if subobjeto==None:
            return None
        return Clima_Sub_Objetoserializer(subobjeto[0]).data
    
    tipo_list = serializers.SerializerMethodField()
    def get_tipo_list(self,obj):
        tipo=Clima_Tipo_Pregunta.objects.filter(id=obj.tipo.id) if Clima_Tipo_Pregunta.objects.filter(id=obj.tipo.id) else None

        if tipo==None:
            return None
        return Clima_Tipo_Preguntaserializer(tipo[0]).data

    class Meta:
        model = Clima_Cuestionario_Preguntas
        fields = '__all__'

class Clima_Cuestionario_Opcionesserializer (serializers.ModelSerializer):
    pregunta_list = serializers.SerializerMethodField()
    def get_pregunta_list(self,obj):
        pregunta=Clima_Cuestionario_Preguntas.objects.filter(id=obj.pregunta.id) if Clima_Cuestionario_Preguntas.objects.filter(id=obj.pregunta.id) else None

        if pregunta==None:
            return None
        return Clima_Cuestionario_Preguntasserializer(pregunta[0]).data

    class Meta:
        model = Clima_Cuestionario_Opciones
        fields = '__all__'

class Clima_Usuarios_ResponsablesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name= serializers.CharField()
    class Meta:
        fields =['id','username','first_name','last_name']   

class Clima_Campañaserializer (serializers.ModelSerializer):
    responsable_list = serializers.SerializerMethodField()
    def get_responsable_list(self,obj):
        res= Clima_Campaña.objects.filter(id=obj.id).values_list('responsable__id',flat=True) if Clima_Campaña.objects.filter(id=obj.id) else None
        if res==None:
            return None
        responsable= User.objects.filter(id__in=res) if User.objects.filter(id__in=res) else None

        if responsable==None:
            return None
        return Clima_Usuarios_ResponsablesSerializer(responsable,many=True).data

    cuestionario_list = serializers.SerializerMethodField()
    def get_cuestionario_list(self,obj):
        cuestionario=Clima_Cuestionario.objects.filter(id=obj.cuestionario.id) if Clima_Cuestionario.objects.filter(id=obj.cuestionario.id) else None

        if cuestionario==None:
            return None
        return Clima_Cuestionarioserializer(cuestionario[0]).data

    segmento_list = serializers.SerializerMethodField()
    def get_segmento_list(self,obj):
        segmento=Clima_Segmento.objects.filter(id=obj.segmento.id) if Clima_Segmento.objects.filter(id=obj.segmento.id) else None

        if segmento==None:
            return None
        return Clima_Segmentoserializer(segmento[0]).data

    tipo_herramienta_list = serializers.SerializerMethodField()
    def get_tipo_herramienta_list(self,obj):
        tipo_herramienta=Clima_Tipo_Herramienta.objects.filter(id=obj.tipo_herramienta.id) if Clima_Tipo_Herramienta.objects.filter(id=obj.tipo_herramienta.id) else None

        if tipo_herramienta==None:
            return None
        return Clima_Tipo_Herramientaserializer(tipo_herramienta[0]).data

    class Meta:
        model = Clima_Campaña
        fields = '__all__'

class Clima_Encuestaserializer (serializers.ModelSerializer):
    usuario_list = serializers.SerializerMethodField()
    def get_usuario_list(self,obj):
        usuario=User.objects.filter(id=obj.usuario.id) if User.objects.filter(id=obj.usuario.id) else None
        if usuario==None:
            return None
        return Clima_Usuarios_ResponsablesSerializer(usuario[0]).data

    campaña_list = serializers.SerializerMethodField()
    def get_campaña_list(self,obj):
        campaña=Clima_Campaña.objects.filter(id=obj.campaña.id) if Clima_Campaña.objects.filter(id=obj.campaña.id) else None

        if campaña==None:
            return None
        return Clima_Campañaserializer(campaña[0]).data

    cuestionario_list = serializers.SerializerMethodField()
    def get_cuestionario_list(self,obj):
        cuestionario=Clima_Cuestionario.objects.filter(id=obj.cuestionario.id) if Clima_Cuestionario.objects.filter(id=obj.cuestionario.id) else None

        if cuestionario==None:
            return None
        return Clima_Cuestionarioserializer(cuestionario[0]).data

    class Meta:
        model = Clima_Encuesta
        fields = '__all__'

class Clima_Respuestasserializer (serializers.ModelSerializer):
    encuesta_list = serializers.SerializerMethodField()
    def get_encuesta_list(self,obj):
        encuesta=Clima_Encuesta.objects.filter(id=obj.encuesta.id) if Clima_Encuesta.objects.filter(id=obj.encuesta.id) else None

        if encuesta==None:
            return None
        return Clima_Encuestaserializer(encuesta[0]).data

    pregunta_list = serializers.SerializerMethodField()
    def get_pregunta_list(self,obj):
        pregunta=Clima_Cuestionario_Preguntas.objects.filter(id=obj.pregunta.id) if Clima_Cuestionario_Preguntas.objects.filter(id=obj.pregunta.id) else None

        if pregunta==None:
            return None
        return Clima_Cuestionario_Preguntasserializer(pregunta[0]).data

    opcion_list = serializers.SerializerMethodField()
    def get_opcion_list(self,obj):
        op= Clima_Respuestas.objects.filter(id=obj.id).values_list('opcion__id',flat=True) if Clima_Respuestas.objects.filter(id=obj.id) else None
        if op==None:
            return None
        opcion= Clima_Cuestionario_Opciones.objects.filter(id__in=op) if Clima_Cuestionario_Opciones.objects.filter(id__in=op) else None

        if opcion==None:
            return None
        return Clima_Cuestionario_Opcionesserializer(opcion,many=True).data
    
    class Meta:
        model = Clima_Respuestas
        fields = '__all__'



class Usuario_Logserializer (serializers.ModelSerializer):
    nombre = serializers.SerializerMethodField()
    codigo=serializers.SerializerMethodField()
    ultimo_acceso=serializers.SerializerMethodField()
    correo = serializers.SerializerMethodField()
    def get_nombre(self,obj):
        nombre=Funcional_empleado.objects.filter(codigo=obj.usuario.username)[0].nombre if Funcional_empleado.objects.filter(codigo=obj.usuario.username) else None
        return nombre

    def get_codigo(self,obj):
        codigo=obj.usuario.username if obj.usuario else None
        return codigo

    def get_ultimo_acceso(self,obj):
        ultimo_acceso=obj.usuario.last_login if obj.usuario else None
        return ultimo_acceso

    def get_correo(self,obj):
        correo=Funcional_empleado.objects.filter(codigo=obj.usuario.username)[0].correo_empresarial if Funcional_empleado.objects.filter(codigo=obj.usuario.username) else None
        return correo


    class Meta:
        model = Usuario_Log
        fields = '__all__'


class archivos_gestor_formatos_oficialesserializer(serializers.ModelSerializer):
    class Meta:
        model = archivos_gestor_formatos_oficiales
        fields ='__all__'


