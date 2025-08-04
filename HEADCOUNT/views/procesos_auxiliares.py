from decimal import MIN_EMIN
from distutils.cygwinccompiler import Mingw32CCompiler
from email import message
from email.policy import HTTP
from urllib import response
from django.db.models.functions import ExtractYear
import ast
from re import sub
from django.contrib.auth.models import User,Group
from django.http.response import Http404
from django.shortcuts import render
from calendar import monthrange
from HEADCOUNT.serializers.serializers_evaluacion import evaluacion_periodicidadserializer, evaluacion_plantilla_competenciaserializer
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
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
from pyrfc import *
from datetime import date,datetime,timedelta
import json
from ..serializers import *
from ..models import *
from ..models import evaluacion_archivo_plan_accion_gestor
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist
import sys
from rest_framework import generics
import io
import string
import csv
sys.setrecursionlimit(100000000)                                                        
from rest_framework import viewsets
import requests
from datetime import datetime
from rest_framework import status
from dateutil.relativedelta import relativedelta

class cargar_posicion_empleado(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[DjangoModelPermissions]   
    queryset = User.objects.none() 

    def post(self,request):
        print(request.data)
        entrada=request.data['Hoja1']
        for x in entrada:
            clasificacion=Funcional_Clasificacion.objects.get(nombre=x["clasificacion"])
            Funciones=Funcional_Funciones.objects.filter(codigo=x["codigo"])
            if Funciones:
                for y in Funciones:
                    Funcional_empleado.objects.filter(posicion__codigo=x["codigo"]).update(clasificacion_empleado=clasificacion)

        return Response({"resultado": ""},status= status.HTTP_200_OK)
