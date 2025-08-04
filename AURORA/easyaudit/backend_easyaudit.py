import logging
from easyaudit.models import RequestEvent, CRUDEvent, LoginEvent
from django.db.models.signals import pre_save
logger = logging.getLogger(__name__)

# ----------------------------------------
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password

class ModelBackend(ObtainAuthToken):
  fila=0 
  

  def request(self, request_info,**request):
    global fila
    creacion = RequestEvent.objects.create(**request_info)
    fila= creacion
    return creacion

  def crud(self, crud_info):
    return CRUDEvent.objects.create(**crud_info)

  def login(self, login_info):
    return LoginEvent.objects.create(**login_info)


  def post(self, request, *args, **kwargs):
      global fila
      serializer = self.serializer_class(data=request.data,
                                          context={'request': request})
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data['user']
      token, created = Token.objects.get_or_create(user=user)
      fila_id=0
      fila_id=fila
      username=request.data['username']
      password = request.data['password']
      query_string = 'username:'+username+'&'+'password:'+make_password(password)
      RequestEvent.objects.filter(id=fila_id.pk).update(query_string=query_string,user_id=user.pk)
     
      
      return Response({
          'token': token.key,
          # 'user_id': user.pk,
          # 'email': user.email
      })
   