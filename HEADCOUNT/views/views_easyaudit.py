

from django.db.models.functions import ExtractYear

from django.contrib.auth.models import User,Group
from django.http.response import Http404
from django.shortcuts import render

from HEADCOUNT.serializers.serializers_descriptor_perfil import descriptor_perfil_competenciaserializer
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
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
from django.db.models import Q,F,Count,Sum,FloatField,ExpressionWrapper, query,Case ,When,IntegerField,Max,Min
from django.utils.crypto import get_random_string
import string
from django.contrib.auth import authenticate
from datetime import datetime,timedelta
import json
from ..serializers import *
from ..models import *
from django.apps import apps
from datetime import datetime,timedelta
import io
import csv
                                                     
from rest_framework import viewsets
import requests
from datetime import datetime
from easyaudit.models import RequestEvent, CRUDEvent, LoginEvent


class easyaudit_RequestEventViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = RequestEvent.objects.all()
    serializer_class = easyaudit_RequestEventserializer
    def list(self, request):
        print(self.request.query_params.get('filter'))
        queryset = RequestEvent.objects.all()
        serializer = easyaudit_RequestEventserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='url':
                        filter_kwargs['url__icontains'] = filter
                    if tipo_busqueda =='metodo':
                        filter_kwargs['method__icontains'] = filter
                    if tipo_busqueda =='query':
                        filter_kwargs['query_string__icontains'] = filter
                    if tipo_busqueda =='datetime':
                        filter_kwargs['datetime__icontains'] = filter
                    if tipo_busqueda =='user_id':
                        filter_kwargs['user_id'] = filter
                

                queryset =  RequestEvent.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  RequestEvent.objects.filter(**filter_kwargs).count()
                serializer = easyaudit_RequestEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  RequestEvent.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  RequestEvent.objects.filter().count()
                serializer = easyaudit_RequestEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='url':
                        filter_kwargs['url__icontains'] = filter
                    if tipo_busqueda =='metodo':
                        filter_kwargs['method__icontains'] = filter
                    if tipo_busqueda =='query':
                        filter_kwargs['query_string__icontains'] = filter
                    if tipo_busqueda =='datetime':
                        filter_kwargs['datetime__icontains'] = filter
                    if tipo_busqueda =='user_id':
                        filter_kwargs['user_id'] = filter

                        
                queryset =  RequestEvent.objects.filter(**filter_kwargs).order_by('id')
                serializer = easyaudit_RequestEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  RequestEvent.objects.filter().order_by('id')
                serializer = easyaudit_RequestEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})

class easyaudit_CRUDEventViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = CRUDEvent.objects.all()
    serializer_class = easyaudit_CRUDEventserializer
    def list(self, request):
        print(self.request.query_params.get('filter'))
        queryset = CRUDEvent.objects.all()
        serializer = easyaudit_CRUDEventserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='login':
                        filter_kwargs['event_type'] = filter # 1=POST,2=PUT, 3=DELETE 
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='json_crud':
                        filter_kwargs['object_json_repr__icontains'] = filter
                    if tipo_busqueda =='user_id':
                        filter_kwargs['user_id'] = filter
                   
                

                queryset =  CRUDEvent.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  CRUDEvent.objects.filter(**filter_kwargs).count()
                serializer = easyaudit_CRUDEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  CRUDEvent.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  CRUDEvent.objects.filter().count()
                serializer = easyaudit_CRUDEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='url':
                        filter_kwargs['url__icontains'] = filter
                    if tipo_busqueda =='metodo':
                        filter_kwargs['method__icontains'] = filter
                    if tipo_busqueda =='query':
                        filter_kwargs['query_string__icontains'] = filter
                    if tipo_busqueda =='datetime':
                        filter_kwargs['datetime__icontains'] = filter
                    if tipo_busqueda =='user_id':
                        filter_kwargs['user_id'] = filter

                        
                queryset =  CRUDEvent.objects.filter(**filter_kwargs).order_by('id')
                serializer = easyaudit_CRUDEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  CRUDEvent.objects.filter().order_by('id')
                serializer = easyaudit_CRUDEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})


class easyaudit_LoginEventViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]
    queryset = LoginEvent.objects.all()
    serializer_class = easyaudit_LoginEventserializer
    def list(self, request):
        print(self.request.query_params.get('filter'))
        queryset = LoginEvent.objects.all()
        serializer = easyaudit_LoginEventserializer(queryset, many=True)
        filter=''
        tipo_busqueda=''
        if self.request.query_params.get('filter'):
            filter = self.request.query_params.get('filter')

        if self.request.query_params.get('tipo_busqueda'):
            tipo_busqueda = self.request.query_params.get('tipo_busqueda')

        if self.request.query_params.get('limit') and self.request.query_params.get('offset'):
            offset=int(self.request.query_params.get('offset'))
            limit=int(self.request.query_params.get('limit'))

            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='login':
                        filter_kwargs['login_type'] = filter #0=inicio session, 1=cierre session, 2 =fallo session
                    if tipo_busqueda =='username':
                        filter_kwargs['username'] = filter
                    if tipo_busqueda =='user_id':
                        filter_kwargs['user_id'] = filter
                    if tipo_busqueda =='fecha':
                        filter_kwargs['datetime__icontains'] = filter
                

                queryset =  LoginEvent.objects.filter(**filter_kwargs).order_by('id')[offset:offset+limit]
                conteo =  LoginEvent.objects.filter(**filter_kwargs).count()
                serializer = easyaudit_LoginEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})  
            else: 
                queryset =  LoginEvent.objects.filter().order_by('id')[offset:offset+limit]
                conteo =  LoginEvent.objects.filter().count()
                serializer = easyaudit_LoginEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":conteo})
        else:
            if filter!='' and tipo_busqueda!='':
                filter_kwargs={}
                if tipo_busqueda:
                    if tipo_busqueda =='id':
                        filter_kwargs['id'] = filter
                    if tipo_busqueda =='login':
                        filter_kwargs['login_type'] = filter #0=inicio session, 1=cierre session, 2 =fallo session
                    if tipo_busqueda =='username':
                        filter_kwargs['username'] = filter
                    if tipo_busqueda =='user_id':
                        filter_kwargs['user_id'] = filter
                    if tipo_busqueda =='fecha':
                        filter_kwargs['datetime__icontains'] = filte

                        
                queryset =  LoginEvent.objects.filter(**filter_kwargs).order_by('id')
                serializer = easyaudit_LoginEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
            else:
                queryset =  LoginEvent.objects.filter().order_by('id')
                serializer = easyaudit_LoginEventserializer(queryset, many=True)
                return Response({"data":serializer.data,"count":queryset.count()})
