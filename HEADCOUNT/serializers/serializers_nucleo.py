from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields import files
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import models
from rest_framework.utils import field_mapping
from django.contrib.auth.models import User,Group
from django.db.models import Count
from django.contrib.auth.hashers import make_password
from ..models import *
from ..serializers import *

class nucleo_modulosserializer(serializers.ModelSerializer):

    class Meta:
        model = nucleo_modulos
        fields = '__all__'

class nucleo_tipo_mensajeserializer(serializers.ModelSerializer):
    modulos_lista = serializers.SerializerMethodField()
    def get_modulos_lista(self, obj):
        modulos = nucleo_modulos.objects.filter(id=obj.modulo.id) if nucleo_modulos.objects.filter(id=obj.modulo.id)  else None

        if modulos == None:
           return None

        return nucleo_modulosserializer(modulos, many=True).data

    class Meta:
        model = nucleo_tipo_mensaje
        fields = '__all__'

class nucleo_configuracion_correosserializer(serializers.ModelSerializer):

    tipo_mensajes_lista = serializers.SerializerMethodField()
    def get_tipo_mensajes_lista(self, obj):
        tipo_mensaje = nucleo_tipo_mensaje.objects.filter(id=obj.tipo_mensaje.id) if nucleo_tipo_mensaje.objects.filter(id=obj.tipo_mensaje.id)  else None

        if tipo_mensaje == None:
           return None

        return nucleo_tipo_mensajeserializer(tipo_mensaje, many=True).data

    datos_creador=   serializers.SerializerMethodField()
    def get_datos_creador(self, obj):
        usuario=None
        if obj.creador:
            usuario=User.objects.filter(id=obj.creador.id) if User.objects.filter(id=obj.creador.id) else None
            if usuario == None:
                return None

        return UserSerializer(usuario, many=True).data

    class Meta:
        model = nucleo_configuracion_correos
        fields = '__all__'

class nucleo_variables_envio_correosserializer(serializers.ModelSerializer):
    tipo_mensajes_lista = serializers.SerializerMethodField()
    def get_tipo_mensajes_lista(self, obj):
        tipo_mensaje = nucleo_tipo_mensaje.objects.filter(id=obj.tipo_mensaje.id) if nucleo_tipo_mensaje.objects.filter(id=obj.tipo_mensaje.id)  else None

        if tipo_mensaje == None:
           return None

        return nucleo_tipo_mensajeserializer(tipo_mensaje, many=True).data
    class Meta:
        model = nucleo_variables_envio_correos
        fields = '__all__'

class nucleo_pruebasserializer(serializers.ModelSerializer):

    class Meta:
        model = nucleo_pruebas
        fields = '__all__'

