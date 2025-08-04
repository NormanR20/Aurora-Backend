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
from easyaudit.models import RequestEvent, CRUDEvent, LoginEvent



class easyaudit_RequestEventserializer(serializers.ModelSerializer):
        
    class Meta:
        model = RequestEvent
        fields = '__all__'


class easyaudit_CRUDEventserializer(serializers.ModelSerializer):
        
    class Meta:
        model = CRUDEvent
        fields = '__all__'

class easyaudit_LoginEventserializer(serializers.ModelSerializer):
        
    class Meta:
        model = LoginEvent
        fields = '__all__'

        