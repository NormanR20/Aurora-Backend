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


#from ..serializers_head_clima import archivos_gestor_formatos_oficialesserializer

class sanciones_categoria_desvinculacionserializer(serializers.ModelSerializer):
    class Meta:
        model = sanciones_categoria_desvinculacion
        fields = '__all__'

class sanciones_motivo_accion_disciplinariaserializer(serializers.ModelSerializer):
    class Meta:
        model = sanciones_motivo_accion_disciplinaria
        fields = '__all__'

class sanciones_tipo_accion_disciplinariaserializer(serializers.ModelSerializer):
    class Meta:
        model = sanciones_tipo_accion_disciplinaria
        fields = '__all__'

class sanciones_medidas_disciplinariasserializer(serializers.ModelSerializer):
    class Meta:
        model = sanciones_medidas_disciplinarias
        fields = '__all__'

class sanciones_tipo_faltaserializer(serializers.ModelSerializer):
    class Meta:
        model = sanciones_tipo_falta
        fields = '__all__'

class sanciones_estatusserializer(serializers.ModelSerializer):
    class Meta:
        model = sanciones_estatus
        fields = '__all__'

class sanciones_casos_disciplinariosserializer(serializers.ModelSerializer):

    list_accion_disciplinaria = serializers.SerializerMethodField()
    def get_list_accion_disciplinaria(self, obj):
        accion_disciplinaria = sanciones_tipo_accion_disciplinaria.objects.filter(id=obj.id_accion_disciplinaria.id) if sanciones_tipo_accion_disciplinaria.objects.filter(id=obj.id_accion_disciplinaria.id)  else None
        if accion_disciplinaria == None:
           return None
        return sanciones_tipo_accion_disciplinariaserializer(accion_disciplinaria, many=True).data

    # id_motivo = models.ForeignKey(sanciones_motivo_accion_disciplinaria,on_delete=models.CASCADE)
    list_id_motivo = serializers.SerializerMethodField()
    def get_list_id_motivo(self, obj):
        id_motivo = sanciones_motivo_accion_disciplinaria.objects.filter(id=obj.id_motivo.id) if sanciones_motivo_accion_disciplinaria.objects.filter(id=obj.id_motivo.id)  else None

        if id_motivo == None:
           return None
        return sanciones_motivo_accion_disciplinariaserializer(id_motivo, many=True).data

    # id_encargado = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    list_id_encargado = serializers.SerializerMethodField()
    def get_list_id_encargado(self, obj):
        if obj ==None:
            return None
        if obj.id_encargado==None:
            return None
        id_encargado = User.objects.filter(id=obj.id_encargado.id) if User.objects.filter(id=obj.id_encargado.id)  else None

        if id_encargado == None:
           return None

        return UserSerializer(id_encargado, many=True).data

    # id_tipo_falta = models.ForeignKey(sanciones_tipo_falta,on_delete=models.CASCADE)
    list_id_tipo_falta = serializers.SerializerMethodField()
    def get_list_id_tipo_falta(self, obj):
        id_tipo_falta = sanciones_tipo_falta.objects.filter(id=obj.id_tipo_falta.id) if sanciones_tipo_falta.objects.filter(id=obj.id_tipo_falta.id)  else None

        if id_tipo_falta == None:
           return None

        return sanciones_tipo_faltaserializer(id_tipo_falta, many=True).data
    # codigo_empleado = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE ,related_name='codigo_empleado')
    list_codigo_empleado = serializers.SerializerMethodField()
    def get_list_codigo_empleado(self, obj):
        if obj ==None:
            return None
        if obj.codigo_empleado==None:
            return None
        codigo_empleado = Funcional_empleado.objects.filter(id=obj.codigo_empleado.id) if Funcional_empleado.objects.filter(id=obj.codigo_empleado.id)  else None

        if codigo_empleado == None:
           return None

        return Funcional_empleadoserializer(codigo_empleado, many=True).data
    # creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE ,related_name='creado_por')
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):
        if obj ==None:
            return None
        if obj.creado_por==None:
            return None
        creado_por = User.objects.filter(id=obj.creado_por.id) if User.objects.filter(id=obj.creado_por.id)  else None

        if creado_por == None:
           return None

        return UserSerializer(creado_por, many=True).data
    #estatus = models.ForeignKey(sanciones_estatus,on_delete=models.CASCADE)
    list_estatus = serializers.SerializerMethodField()
    def get_list_estatus(self, obj):
        estatus = sanciones_estatus.objects.filter(id=obj.estatus.id) if sanciones_estatus.objects.filter(id=obj.estatus.id)  else None

        if estatus == None:
           return None

        return sanciones_estatusserializer(estatus, many=True).data

    list_id_usuario = serializers.SerializerMethodField()
    def get_list_id_usuario(self, obj):
        if obj.codigo_empleado==None:
            return None
        Usuario = User.objects.filter(username=obj.codigo_empleado.codigo) if User.objects.filter(username=obj.codigo_empleado.codigo)  else None

        if Usuario == None:
           return None
        
        return UsuariosSerializer(Usuario, many=True).data


    list_workflow = serializers.SerializerMethodField()
    def get_list_workflow(self, obj):
        if obj.off_bording==None:
            return None

        salida = on_off_bording_workflow.objects.filter(id=obj.off_bording.id) if on_off_bording_workflow.objects.filter(id=obj.off_bording.id)  else None

        if salida == None:
           return None

        return on_off_bording_workflowserializer(salida, many=True).data


    list_categoria_desvinculacion = serializers.SerializerMethodField()
    def get_list_categoria_desvinculacion(self, obj):
        if obj.categoria_desvinculacion==None:
            return None
        categoria_desvinculacion = sanciones_categoria_desvinculacion.objects.filter(id=obj.categoria_desvinculacion.id) if sanciones_categoria_desvinculacion.objects.filter(id=obj.categoria_desvinculacion.id)  else None

        if categoria_desvinculacion == None:
           return None

        return sanciones_categoria_desvinculacionserializer(categoria_desvinculacion, many=True).data


    class Meta:
        model = sanciones_casos_disciplinarios
        fields = '__all__'

class sanciones_accion_disciplinariaserializer(serializers.ModelSerializer):
    list_caso_disciplinario= serializers.SerializerMethodField()
    def get_list_caso_disciplinario(self, obj):
        
        caso = sanciones_casos_disciplinarios.objects.filter(id=obj.caso_disciplinario.id) if sanciones_casos_disciplinarios.objects.filter(id=obj.caso_disciplinario.id)  else None

        if caso == None:
            return None

        return sanciones_casos_disciplinariosserializer(caso, many=True).data

    
    list_medida = serializers.SerializerMethodField()
    def get_list_medida(self, obj):
        medida = sanciones_medidas_disciplinarias.objects.filter(id=obj.medida_disciplinaria.id) if sanciones_medidas_disciplinarias.objects.filter(id=obj.medida_disciplinaria.id)  else None

        if medida == None:
           return None

        return sanciones_medidas_disciplinariasserializer(medida, many=True).data


    list_categoria_desvinculacion = serializers.SerializerMethodField()
    def get_list_categoria_desvinculacion(self, obj):
        if obj.categoria_desvinculacion==None:
            return None
        categoria_desvinculacion = sanciones_categoria_desvinculacion.objects.filter(id=obj.categoria_desvinculacion.id) if sanciones_categoria_desvinculacion.objects.filter(id=obj.categoria_desvinculacion.id)  else None

        if categoria_desvinculacion == None:
           return None

        return sanciones_categoria_desvinculacionserializer(categoria_desvinculacion, many=True).data

    list_off_bording = serializers.SerializerMethodField()
    def get_list_off_bording(self, obj):
        if obj.off_bording==None:
            return None
        off_bording = on_off_bording_workflow.objects.filter(id=obj.off_bording.id) if on_off_bording_workflow.objects.filter(id=obj.off_bording.id)  else None

        if off_bording == None:
           return None

        return on_off_bording_workflowserializer(off_bording, many=True).data

    list_archivo_evidencia = serializers.SerializerMethodField()
    def get_list_archivo_evidencia(self, obj):
        if obj.archivo_evidencia==None:
            return None
        ag = archivos_gestor.objects.filter(id=obj.archivo_evidencia.id) if archivos_gestor.objects.filter(id=obj.archivo_evidencia.id)  else None

        if ag == None:
           return None
        return archivos_gestorserializer(ag, many=True).data


    list_archivo_autorizacion = serializers.SerializerMethodField()
    def get_list_archivo_autorizacion(self, obj):
        if obj.archivo_autorizacion==None:
            return None
        ag = archivos_gestor.objects.filter(id=obj.archivo_autorizacion.id) if archivos_gestor.objects.filter(id=obj.archivo_autorizacion.id)  else None

        if ag == None:
           return None
        return archivos_gestorserializer(ag, many=True).data
    

    list_aplicada_por = serializers.SerializerMethodField()
    def get_list_aplicada_por(self, obj):
        if obj.aplicada_por==None:
            return None
        aplicada_por = User.objects.filter(id=obj.aplicada_por.id) if User.objects.filter(id=obj.aplicada_por.id)  else None
        if aplicada_por == None:
           return None
        return UserSerializer(aplicada_por, many=True).data   

    list_archivos_gestor_autorizacion = serializers.SerializerMethodField()
    def list_archivos_gestor_autorizacion(self, obj):
        if obj.archivos_gestor_autorizacion==None:
            return None
        ag = archivos_gestor.objects.filter(id=obj.archivos_gestor_autorizacion.id) if archivos_gestor.objects.filter(id=obj.archivos_gestor_autorizacion.id)  else None

        if ag == None:
           return None
        return archivos_gestorserializer(ag, many=True).data  
    class Meta:
        model = sanciones_accion_disciplinaria
        fields = '__all__'


class sanciones_accion_disciplinaria_correosserializer(serializers.ModelSerializer):
    list_sanciones_accion_disciplinaria_correos = serializers.SerializerMethodField()
    def get_list_sanciones_accion_disciplinaria_correos(self, obj):
        if obj.accion_disciplinaria==None:
            return None
        accion_disciplinaria = sanciones_accion_disciplinaria.objects.filter(id=obj.accion_disciplinaria.id) if sanciones_accion_disciplinaria.objects.filter(id=obj.accion_disciplinaria.id)  else None

        if accion_disciplinaria == None:
           return None
        return sanciones_accion_disciplinariaserializer(accion_disciplinaria, many=True).data  

    class Meta:
        model = sanciones_accion_disciplinaria_correos
        fields = '__all__'

class sanciones_plantilla_formatos_oficialesserializer(serializers.ModelSerializer):
    # creado_por = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE ,related_name='creado_por')
    list_creado_por = serializers.SerializerMethodField()
    def get_list_creado_por(self, obj):
        creado_por = User.objects.filter(id=obj.creado_por.id) if User.objects.filter(id=obj.creado_por.id)  else None

        if creado_por == None:
           return None

        return UserSerializer(creado_por, many=True).data

    #archivo = models.ForeignKey(archivos_gestor,on_delete=models.CASCADE)
    list_archivo = serializers.SerializerMethodField()
    def get_list_archivo(self, obj):
        archivo = archivos_gestor_formatos_oficiales.objects.filter(id=obj.archivo.id) if archivos_gestor_formatos_oficiales.objects.filter(id=obj.archivo.id)  else None
        print (archivo)
        if archivo == None:
           return None

        return archivos_gestor_formatos_oficialesserializer(archivo, many=True).data

    class Meta:
        model = sanciones_plantilla_formatos_oficiales
        fields = '__all__'
