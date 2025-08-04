from re import T
from django.db import models
from django.db.models import base
from django.db.models.deletion import CASCADE
from django.db.models.functions.datetime import TruncHour
from django.utils.timezone import now
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User, Group

# Estructura formal
class head_clima_pais(models.Model):
    codigo= models.CharField(max_length=8,null=True,blank=True)
    nombre= models.CharField(max_length=200,null=True,blank=True)

class head_clima_departamento(models.Model):
    codigo= models.CharField(max_length=8,null=True,blank=True)
    nombre= models.CharField(max_length=200,null=True,blank=True)
    pais = models.ForeignKey("head_clima_pais", on_delete=models.CASCADE)

class head_clima_municipio(models.Model):
    codigo= models.CharField(max_length=8,null=True,blank=True)
    nombre= models.CharField(max_length=200,null=True,blank=True)
    departamento = models.ForeignKey("head_clima_departamento", on_delete=models.CASCADE)



class Formal_Estado_civil(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)

class Formal_Parentesco(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
class Formal_Genero(models.Model):
    nombre = models.CharField(max_length=200,null=True,blank=True)
class Formal_Organizacion(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
    tipo = models.IntegerField(default=1,null=True,blank=True)
class Formal_Unidad_Organizativa(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
    Dirigido_por = models.CharField(max_length=100,null=True,blank=True)
    unidad_organizativa_jeraquia = models.ManyToManyField('self',null=True,blank=True,symmetrical=False)
    sociedad_financiera = models.ManyToManyField(Formal_Organizacion,related_name='sociedad_financiera',null=True,blank=True)
    sociedad_pagadora = models.ManyToManyField(Formal_Organizacion,related_name='sociedad_pagadora',null=True,blank=True)
    principal= models.BooleanField(default=False,null=True,blank=True)

class Formal_Funciones(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre=models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    
class Formal_Puesto(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    unidad_organizativa = models.ManyToManyField(Formal_Unidad_Organizativa,null=True,blank=True)
    descripcion_larga=models.CharField(max_length=200,null=True,blank=True)
    sap= models.BooleanField(default=False,null=True,blank=False)

class Formal_Centro_Costo(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    organizacion = models.ForeignKey(Formal_Organizacion,blank=True,null=True,on_delete=models.CASCADE)


class Formal_Situacion_Actual(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=30,null=True,blank=True)
class Formal_Relacion_Laboral(models.Model):
    codigo = models.CharField(max_length=10,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)
class Formal_Compañia(models.Model):
    codigo = models.CharField(max_length=10,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)
class Formal_Division(models.Model):
    codigo = models.CharField(max_length=10,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)

class Formal_Division_Personal(models.Model):
    codigo = models.CharField(max_length=10,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)

class Formal_Formacion(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    documento = models.FileField(null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    
    

class Formal_Instituto(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)

class Formal_Especialidad(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    documento = models.FileField(null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    universidad=models.ManyToManyField(Formal_Instituto,null=True,blank=True)

class Formal_Titulo(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    universidad=models.ManyToManyField(Formal_Instituto,null=True,blank=True)


class Formal_Diagnostico(models.Model):
    codigo = models.CharField(max_length=4,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)

class Formal_Equipo (models.Model):
    codigo= models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=200,null=True,blank=True)
    service_tag= models.CharField(max_length=100,null=True,blank=True)
    estado = models.BooleanField(default=True,null=True,blank=True)
    sociedad = models.ForeignKey(Formal_Organizacion,null = True,blank=True,on_delete=models.CASCADE)
    
class Formal_Clasificacion(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)

class Formal_empleado(models.Model):
    foto=models.ImageField(upload_to='media',null=True,blank=True)
    identidad = models.CharField(max_length=200,null=True,blank=True)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    codigo =models.CharField(max_length=200,null=True,blank=True)
    telefono = models.CharField(max_length=200,null=True,blank=True)
    celular =models.CharField(max_length=200,null=True,blank=True)
    relacion_laboral = models.ForeignKey(Formal_Relacion_Laboral,null=True,blank=True,on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_baja= models.DateField(null=True,blank=True)
    division = models.ForeignKey(Formal_Division,null=True,blank=True, on_delete=models.CASCADE)
    division_personal = models.ForeignKey(Formal_Division_Personal,null=True,blank=True, on_delete=models.CASCADE)
    centro_costo = models.ForeignKey(Formal_Centro_Costo,null=True,blank=True, on_delete=models.CASCADE)
    antiguedad_laboral = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    correo_empresarial = models.EmailField(max_length=254,null=True,blank=True)
    correo_personal = models.EmailField(max_length=254,null=True,blank=True)
    fecha_cumpleaños = models.DateField(null=True,blank=True)
    edad = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    saldo_vacaciones =models.DecimalField(max_digits=10, decimal_places=3,null=True,blank=True)
    absentismo =models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True,default=0.00)
    domicilio =models.CharField(max_length=200,null=True,blank=True)
    historial_laboral=models.CharField(max_length=500,null=True,blank=True)
    #clasificacion  =models.CharField(max_length=500,null=True,blank=True)
    estado_civil = models.ForeignKey(Formal_Estado_civil, on_delete=models.CASCADE,null=True,blank=True)
    puesto=models.ManyToManyField(Formal_Puesto,null=True,blank=True)
    posicion=models.ManyToManyField(Formal_Funciones,null=True,blank=True)
    unidad_organizativa = models.ManyToManyField(Formal_Unidad_Organizativa,null=True,blank=True)
    formacion = models.ManyToManyField(Formal_Formacion,null=True,blank=True)
    especialidad =models.ManyToManyField(Formal_Especialidad,null=True,blank=True)
    tipo_sangre = models.CharField(max_length=5,null=True,blank=True)
    genero = models.CharField(max_length=1,null=True,blank=True)
    situacion_actual=models.ForeignKey(Formal_Situacion_Actual, on_delete=models.CASCADE,null=True,blank=True)
    enfermedad =models.ManyToManyField(Formal_Diagnostico,null=True,blank=True)
    jefe_inmediato = models.CharField(max_length=12,null=True,blank=True)
    clasificacion_empleado = models.ForeignKey(Formal_Clasificacion, on_delete=models.CASCADE,null=True,blank=True)
    updated_at = models.DateField(auto_now=True)
    clase_medida=models.CharField(max_length=500,null=True,blank=True)
    descripcion_clase_medida=models.CharField(max_length=500,null=True,blank=True)
    motivo_clase_medida=models.CharField(max_length=500,null=True,blank=True)
    descripcion_motivo_clase_medida=models.CharField(max_length=500,null=True,blank=True)
    es_jefe=models.BooleanField(null=True,blank=True,default=False)

    @property
    def find_age(self):
        return datetime.date.today().year - self.fecha_ingreso.year

class Formal_Asignacion_Equipo(models.Model):
    empleado = models.ForeignKey(Formal_empleado,null=True,blank=True,on_delete=models.CASCADE)
    equipo = models.ForeignKey(Formal_Equipo,null=True,blank=True,on_delete=models.CASCADE)

class Formal_Salud(models.Model): 
    diagnostico = models.ForeignKey(Formal_Diagnostico,null=True,blank=True,on_delete=models.CASCADE)
    empleado = models.ForeignKey(Formal_empleado,null=True,blank=True,on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True,null=True,blank=True)
    enfermedad = models.CharField(max_length=8,null=True,blank=True)

class Formal_Educacion(models.Model):
    formacion = models.ForeignKey(Formal_Formacion,null=True,blank=True,on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Formal_Especialidad,null=True,blank=True,on_delete=models.CASCADE)
    instituto = models.ForeignKey(Formal_Instituto,null=True,blank=True,on_delete=models.CASCADE)
    nombre_instituto=models.CharField(max_length=200,null=True,blank=True)
    titulo = models.ForeignKey(Formal_Titulo,null=True,blank=True,on_delete=models.CASCADE)
    empleado= models.ForeignKey(Formal_empleado,null=True,blank=True,on_delete=models.CASCADE)
    fecha_inicio = models.DateField(now,null=True,blank=True)
    fecha_fin = models.DateField(now,null=True,blank=True)
    subtipo = models.CharField(max_length=4,null=True,blank=True)
    clave_pais= models.CharField(default='HN',max_length=100,null=True,blank=True)
    
    


class Formal_Contacto_Emergencia(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    apellido = models.CharField(max_length=100,null=True,blank=True)
    segundo_apellido = models.CharField(max_length=100,null=True,blank=True)
    identidad = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=100,null=True,blank=True)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    correo = models.CharField(max_length=100,null=True,blank=True)
    anotaciones = models.CharField(max_length=200,null=True,blank=True)
    #genero = models.ForeignKey(Formal_Genero,null=True,blank=True,on_delete=models.CASCADE)
    genero = models.CharField(max_length=100,null=True,blank=True)
    parentesco = models.ForeignKey(Formal_Parentesco,null = True,blank=True,on_delete=models.CASCADE) 
    empleado = models.ForeignKey(Formal_empleado,null = True,blank=True,on_delete=models.CASCADE)  
    subtipo = models.CharField(max_length=200,null=True,blank=True)
    de=models.DateField(auto_now_add=True,null=True,blank=True)
    hasta=models.DateField(default=datetime.now().date(),null=True,blank=True)  
    apellido_soltera =models.CharField(max_length=100,null=True,blank=True)
    fecha_nacimiento = models.DateField(default=now,null=True,blank=True)
    ciudad_nacimiento=models.CharField(max_length=200,null=True,blank=True)
    pais_nacimiento=models.CharField(max_length=200,null=True,blank=True)
    nacionalidad = models.CharField(max_length=200,null=True,blank=True)
    dependiente = models.CharField(max_length=1,null=True,blank=True)
    


class Formal_Dependientes_Economico(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    primer_apellido = models.CharField(max_length=100,null=True,blank=True)
    segundo_apellido = models.CharField(max_length=100,null=True,blank=True)
    identidad = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=100,null=True,blank=True)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    anotaciones = models.CharField(max_length=200,null=True,blank=True)
    genero = models.ForeignKey(Formal_Genero,null=True,blank=True,on_delete=models.CASCADE)
    fecha_nacimiento = models.DateField(default=now,null=True,blank=True)
    parentesco = models.ForeignKey(Formal_Parentesco,null = True,blank=True,on_delete=models.CASCADE) 
    empleado = models.ForeignKey(Formal_empleado,null = True,blank=True,on_delete=models.CASCADE)  
    subtipo = models.CharField(max_length=4,null=True,blank=True)
    secuencia = models.CharField(max_length=2,null=True,blank=True)
    dependiente = models.CharField(max_length=1,null=True,blank=True)
    apellido_soltera =models.CharField(max_length=100,null=True,blank=True)
    de=models.DateField(auto_now_add=True,null=True,blank=True)
    hasta=models.DateField(default=datetime.now().date(),null=True,blank=True)
    ciudad_nacimiento=models.CharField(max_length=200,null=True,blank=True)
    pais_nacimiento=models.CharField(max_length=200,null=True,blank=True)
    nacionalidad = models.CharField(max_length=200,null=True,blank=True)

    
class Formal_Beneficiario_Seguro(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    identidad = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=100,null=True,blank=True)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    anotaciones = models.CharField(max_length=200,null=True,blank=True)
    #genero = models.ForeignKey(Formal_Genero,null=True,blank=True,on_delete=models.CASCADE)
    genero = models.CharField(max_length=100,null=True,blank=True)
    fecha_nacimiento = models.DateField()
    parentesco = models.ForeignKey(Formal_Parentesco,null = True,blank=True,on_delete=models.CASCADE) 
    empleado = models.ForeignKey(Formal_empleado,null = True,blank=True,on_delete=models.CASCADE)  

    



class Formal_plaza(models.Model):
    serie= models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=200,null=True,blank=True)
    puesto = models.ForeignKey(Formal_Puesto,null = True,blank=True,on_delete=models.CASCADE)  

class Formal_Relacion_Laboral_Anterior(models.Model):
    codigo = models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)

class Formal_Historial_Laboral(models.Model):
    descripcion= models.CharField(max_length=100,null=True,blank=True)
    empleado=models.ForeignKey(Formal_empleado, on_delete=models.CASCADE,null=True,blank=True)
    puesto = models.ForeignKey(Formal_Relacion_Laboral_Anterior, on_delete=models.CASCADE,null=True,blank=True)



class Actualizacion_Contacto(models.Model):
    codigo_empleado = models.CharField(max_length=100,null=True,blank=True)
    subtipo = models.CharField(max_length=4,null=True,blank=True)
    valor= models.CharField(max_length=100,null=True,blank=True)
    cargado=models.BooleanField(default=False,null=True,blank=True)
    fecha=models.DateField(auto_now=True,null=True,blank=True)


class Actualizacion_Dependiente(models.Model):
    codigo_empleado = models.CharField(max_length=100,null=True,blank=True)
    subtipo = models.CharField(max_length=4,null=True,blank=True)
    secuencia= models.CharField(max_length=4,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
    primer_apellido= models.CharField(max_length=100,null=True,blank=True)
    segundo_apellido =models.CharField(max_length=100,null=True,blank=True)
    apellido_soltera =models.CharField(max_length=100,null=True,blank=True)
    identidad=models.CharField(max_length=100,null=True,blank=True)
    dependiente = models.CharField(max_length=100,null=True,blank=True)
    cargado=models.BooleanField(default=False,null=True,blank=True)
    de=models.DateField(auto_now_add=True,null=True,blank=True)
    hasta=models.DateField(default=datetime.now().date(),null=True,blank=True)
    genero=models.CharField(max_length=100,null=True,blank=True)
    fecha_nacimiento=models.DateField(default=datetime.now().date(),null=True,blank=True)
    ciudad_nacimiento=models.CharField(max_length=200,null=True,blank=True)
    pais_nacimiento=models.CharField(max_length=200,null=True,blank=True)
    nacionalidad = models.CharField(max_length=200,null=True,blank=True)
    fecha=models.DateField(auto_now=True,null=True,blank=True)

# class Actualizacion_Domicilio_Region(models.Model):
#     codigo = models.CharField(max_length=100,null=True,blank=True)
#     nombre = models.CharField(max_length=300,null=True,blank=True)

class Actualizacion_Domicilio(models.Model):
    codigo_empleado = models.CharField(max_length=100,null=True,blank=True)
    subtipo = models.CharField(max_length=4,null=True,blank=True)
    domicilio = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=20,null=True,blank=True)
    cargado=models.BooleanField(default=False,null=True,blank=True)
    fecha=models.DateField(auto_now=True,null=True,blank=True)
    de=models.DateField(auto_now_add=True,null=True,blank=True)
    hasta=models.DateField(default=datetime.now().date(),null=True,blank=True)
    colonia = models.CharField(max_length=300,null=True,blank=True)
    region= models.CharField(max_length=20,null=True,blank=True)
    tipo_residencia=models.CharField(max_length=100,null=True,blank=True)


class Actualizacion_Educacion(models.Model):
    codigo_empleado = models.CharField(max_length=100,null=True,blank=True)
    subtipo = models.CharField(default='50',max_length=4,null=True,blank=True)
    formacion = models.CharField(max_length=200,null=True,blank=True)
    instituto = models.CharField(max_length=200,null=True,blank=True)
    clave_pais= models.CharField(max_length=100,null=True,blank=True)   
    titulo =models.CharField(max_length=200,null=True,blank=True)
    especialidad= models.CharField(max_length=200,null=True,blank=True)
    cargado=models.BooleanField(default=False,null=True,blank=True)
    fecha_inicio=models.DateField(null=True,blank=True)
    fecha_fin=models.DateField(null=True,blank=True)
    fecha=models.DateField(auto_now=True,null=True,blank=True)

class Actualizacion_Estado_Civil(models.Model):
    codigo_empleado = models.CharField(max_length=100,null=True,blank=True)
    estado_civil = models.CharField(max_length=10,null=True,blank=True)
    cargado=models.BooleanField(default=False,null=True,blank=True)
    fecha=models.DateField(auto_now=True,null=True,blank=True)


class Formal_Check_List(models.Model):
    nombre=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion = models.DateField(default=datetime.now,null=True,blank=True)
    activo = models.BooleanField(default=False,blank=True,null=True)

class Formal_Empleado_Check_List(models.Model):
    checklist = models.ForeignKey(Formal_Check_List,blank=True,null=True,on_delete=models.CASCADE)
    empleado = models.ForeignKey(Formal_empleado,blank=True,null=True,on_delete=models.CASCADE)
    fecha= models.DateField(default=datetime.now,null=True,blank=True)
    activo = models.BooleanField(default=False,blank=True,null=True)

class Formal_Laboratorio(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    fecha = models.DateField(default=datetime.now,null=True,blank=True)

class Formal_Vacuna(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    fecha = models.DateField(default=datetime.now,null=True,blank=True)
    laboratorio =  models.ForeignKey(Formal_Laboratorio,blank=True,null=True,on_delete=models.CASCADE)
    covid = models.BooleanField(default=False,blank=True,null=True)


class Formal_Empleado_Vacuna(models.Model):
    vacuna =  models.ForeignKey(Formal_Vacuna,blank=True,null=True,on_delete=models.CASCADE)
    empleado =  models.ForeignKey(Formal_empleado,blank=True,null=True,on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now,null=True,blank=True)

#Estructura funcional

class genero(models.Model):
    nombre=models.CharField(max_length=100,null=True,blank=True)

#se agrego para hacer realaciones con el empleado funcional
class descriptor_perfil_datos_unidad_medida(models.Model):
    descripcion=models.CharField(max_length=500,null=False,blank=False)
    abreviatura=models.CharField(max_length=500,null=True,blank=True)
    magnitud=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class descriptor_perfil_formacion_area_conocimiento(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class descriptor_perfil_formacion_nivel_educativo(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class descriptor_perfil_titulo(models.Model):
    nivel_academico=models.ForeignKey(descriptor_perfil_formacion_nivel_educativo,null=True,blank=True,on_delete=models.CASCADE)
    titulo=models.CharField(max_length=500,null=True,blank=True)
    area_conocimiento=models.ForeignKey(descriptor_perfil_formacion_area_conocimiento,null=True,blank=True,on_delete=models.CASCADE)

class descriptor_perfil_cursos_diplomados_seminario_pasantia(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    duracion = models.DecimalField(max_digits=20, decimal_places=2)
    unidad_medida=models.ForeignKey(descriptor_perfil_datos_unidad_medida,null=True,blank=True,on_delete=models.CASCADE)

class descriptor_perfil_conocimiento_tecnico(models.Model):
    nombre=models.CharField(max_length=500,null=True,blank=True)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)





class Funcional_Estado_civil(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
class Funcional_Parentesco(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
class Funcional_Genero(models.Model):
    nombre = models.CharField(max_length=200,null=True,blank=True)
class Funcional_Organizacion(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
    tipo = models.IntegerField(default=1,null=True,blank=True)
class Funcional_Unidad_Organizativa(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre = models.CharField(max_length=100,null=True,blank=True)
    Dirigido_por = models.CharField(max_length=100,null=True,blank=True)
    unidad_organizativa_jeraquia = models.ManyToManyField('self',null=True,blank=True,symmetrical=False)
    sociedad_financiera = models.ManyToManyField(Funcional_Organizacion,related_name='sociedad_financiera',null=True,blank=True)
    sociedad_pagadora = models.ManyToManyField(Funcional_Organizacion,related_name='sociedad_pagadora',null=True,blank=True)
    principal= models.BooleanField(default=False,null=True,blank=True)



class Funcional_Funciones(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    nombre=models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
class Funcional_Puesto(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    unidad_organizativa = models.ManyToManyField(Funcional_Unidad_Organizativa,null=True,blank=True)
    descripcion_larga=models.CharField(max_length=200,null=True,blank=True)
    sap= models.BooleanField(default=False,null=True,blank=False)
    activo=models.BooleanField(default=True,null=True,blank=False)

class Funcional_Centro_Costo(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    organizacion = models.ForeignKey(Funcional_Organizacion,blank=True,null=True,on_delete=models.CASCADE)

class Funcional_Situacion_Actual(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=30,null=True,blank=True)
class Funcional_Relacion_Laboral(models.Model):
    codigo = models.CharField(max_length=10,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)
class Funcional_Compañia(models.Model):
    codigo = models.CharField(max_length=10,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)
class Funcional_Division(models.Model):
    codigo = models.CharField(max_length=10,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)

class Funcional_Division_Personal(models.Model):
    codigo = models.CharField(max_length=10,null=True,blank=True)
    descripcion= models.CharField(max_length=100,null=True,blank=True)


class Funcional_Formacion(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    documento = models.FileField(null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)

    
class Funcional_Instituto(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)

class Funcional_Especialidad(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    documento = models.FileField(null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    universidad=models.ManyToManyField(Funcional_Instituto,null=True,blank=True)

class Funcional_Titulo(models.Model):
    codigo = models.CharField(max_length=20,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    universidad=models.ManyToManyField(Funcional_Instituto,null=True,blank=True)

class Funcional_Diagnostico(models.Model):
    codigo = models.CharField(max_length=4,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)

class Funcional_Equipo (models.Model):
    codigo= models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=200,null=True,blank=True)
    service_tag= models.CharField(max_length=100,null=True,blank=True)
    estado = models.BooleanField(default=True,null=True,blank=True)
    sociedad = models.ForeignKey(Funcional_Organizacion,null = True,blank=True,on_delete=models.CASCADE)

class Funcional_Clasificacion(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
#empleados funcionales
class Funcional_empleado(models.Model):
    foto=models.ImageField(upload_to='media',null=True,blank=True)
    identidad = models.CharField(max_length=200,null=True,blank=True)
    nombre = models.CharField(max_length=200,null=True,blank=True)
    codigo =models.CharField(max_length=200,null=True,blank=True)
    telefono = models.CharField(max_length=200,null=True,blank=True)
    celular =models.CharField(max_length=200,null=True,blank=True)
    relacion_laboral = models.ForeignKey(Funcional_Relacion_Laboral,null=True,blank=True,on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_baja = models.DateField(null=True,blank=True)
    division = models.ForeignKey(Funcional_Division,null=True,blank=True, on_delete=models.CASCADE)
    division_personal = models.ForeignKey(Funcional_Division_Personal,null=True,blank=True, on_delete=models.CASCADE)
    centro_costo = models.ForeignKey(Funcional_Centro_Costo,null=True,blank=True, on_delete=models.CASCADE)
    antiguedad_laboral = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    correo_empresarial = models.EmailField(max_length=254,null=True,blank=True)
    correo_personal = models.EmailField(max_length=254,null=True,blank=True)
    fecha_cumpleaños = models.DateField(null=True,blank=True)
    edad = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    saldo_vacaciones =models.DecimalField(max_digits=10, decimal_places=3,null=True,blank=True)
    absentismo =models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True,default=0.00)
    domicilio =models.CharField(max_length=200,null=True,blank=True)
    historial_laboral=models.CharField(max_length=500,null=True,blank=True)
    #clasificacion  =models.CharField(max_length=500,null=True,blank=True)
    estado_civil = models.ForeignKey(Funcional_Estado_civil, on_delete=models.CASCADE,null=True,blank=True)
    puesto=models.ManyToManyField(Funcional_Puesto,null=True,blank=True)
    posicion=models.ManyToManyField(Funcional_Funciones,null=True,blank=True)
    unidad_organizativa = models.ManyToManyField(Funcional_Unidad_Organizativa,null=True,blank=True)
    formacion = models.ManyToManyField(Funcional_Formacion,null=True,blank=True)
    especialidad =models.ManyToManyField(Funcional_Especialidad,null=True,blank=True)
    tipo_sangre = models.CharField(max_length=5,null=True,blank=True)
    genero = models.CharField(max_length=1,null=True,blank=True)
    situacion_actual=models.ForeignKey(Funcional_Situacion_Actual, on_delete=models.CASCADE,null=True,blank=True)
    jefe_inmediato = models.CharField(max_length=12,null=True,blank=True)
    clasificacion_empleado = models.ForeignKey(Funcional_Clasificacion, on_delete=models.CASCADE,null=True,blank=True)
    updated_at = models.DateField(auto_now=True)
    clase_medida=models.CharField(max_length=500,null=True,blank=True)
    descripcion_clase_medida=models.CharField(max_length=500,null=True,blank=True)
    motivo_clase_medida=models.CharField(max_length=500,null=True,blank=True)
    descripcion_motivo_clase_medida=models.CharField(max_length=500,null=True,blank=True)
    es_jefe=models.BooleanField(null=True,blank=True,default=False)
    municipio =models.ForeignKey(head_clima_municipio,null=True,blank=True,on_delete=models.CASCADE)
    sap= models.BooleanField(default=False,null=True,blank=False)



class  archivos_gestor(models.Model):
    id_area= models.IntegerField(null=False,blank=False)
    id_carpeta_encabezado= models.IntegerField(null=False,blank=False)
    empresa= models.CharField(max_length=200,null=True,blank=True)
    zona= models.CharField(max_length=200,null=True,blank=True)
    tipo_documento_GD = models.CharField(max_length=200,null=True,blank=True)
    descripcion =models.CharField(max_length=200,null=True,blank=True)
    id_empleado =models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.CASCADE)
    tipo_documento=models.CharField(max_length=200,null=True,blank=True)
    fecha= models.DateField(default=datetime.now().date(),null=True,blank=True)
    origen =models.CharField(max_length=300,null=True,blank=True)
    extension=models.CharField(max_length=20,null=True,blank=True)
    id_registro= models.IntegerField(default=0,null=False,blank=False)
    id_documento= models.IntegerField(default=0,null=False,blank=False)
    llave= models.CharField(max_length=300,null=True,blank=True)
    fecha_creacion= models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion= models.DateField(auto_now=True,null=True,blank=True)
    contentTypeGD = models.CharField(max_length=255,null=True,blank=True)

class Funcional_Asignacion_Equipo(models.Model):
    empleado = models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.CASCADE)
    equipo = models.ForeignKey(Funcional_Equipo,null=True,blank=True,on_delete=models.CASCADE)

class Funcional_Salud(models.Model): 
    diagnostico = models.ForeignKey(Funcional_Diagnostico,null=True,blank=True,on_delete=models.CASCADE)
    empleado = models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True,null=True,blank=True)
    enfermedad = models.CharField(max_length=8,null=True,blank=True)
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE)

class Funcional_Educacion(models.Model):
    formacion = models.ForeignKey(Funcional_Formacion,null=True,blank=True,on_delete=models.CASCADE)
    especialidad = models.ForeignKey(Funcional_Especialidad,null=True,blank=True,on_delete=models.CASCADE)
    instituto = models.ForeignKey(Funcional_Instituto,null=True,blank=True,on_delete=models.CASCADE)
    nombre_instituto=models.CharField(max_length=200,null=True,blank=True)
    titulo = models.ForeignKey(Funcional_Titulo,null=True,blank=True,on_delete=models.CASCADE)
    empleado= models.ForeignKey(Funcional_empleado,null=True,blank=True,on_delete=models.CASCADE)
    fecha_inicio = models.DateField(now,null=True,blank=True)
    fecha_fin = models.DateField(now,null=True,blank=True)
    subtipo = models.CharField(max_length=4,null=True,blank=True)
    clave_pais= models.CharField(default='HN',max_length=100,null=True,blank=True)
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE)

class Funcional_Contacto_Emergencia(models.Model):
        nombre = models.CharField(max_length=100,null=True,blank=True)
        apellido = models.CharField(max_length=100,null=True,blank=True)
        segundo_apellido = models.CharField(max_length=100,null=True,blank=True)
        identidad = models.CharField(max_length=100,null=True,blank=True)
        telefono = models.CharField(max_length=100,null=True,blank=True)
        direccion = models.CharField(max_length=100,null=True,blank=True)
        correo = models.CharField(max_length=100,null=True,blank=True)
        anotaciones = models.CharField(max_length=200,null=True,blank=True)
        #genero = models.ForeignKey(Formal_Genero,null=True,blank=True,on_delete=models.CASCADE)
        genero = models.CharField(max_length=100,null=True,blank=True)
        parentesco = models.ForeignKey(Funcional_Parentesco,null = True,blank=True,on_delete=models.CASCADE) 
        empleado = models.ForeignKey(Funcional_empleado,null = True,blank=True,on_delete=models.CASCADE)  
        subtipo = models.CharField(max_length=200,null=True,blank=True)
        de=models.DateField(auto_now_add=True,null=True,blank=True)
        hasta=models.DateField(default=datetime.now().date(),null=True,blank=True)  
        apellido_soltera =models.CharField(max_length=100,null=True,blank=True)
        fecha_nacimiento = models.DateField(default=now,null=True,blank=True)
        ciudad_nacimiento=models.CharField(max_length=200,null=True,blank=True)
        pais_nacimiento=models.CharField(max_length=200,null=True,blank=True)
        nacionalidad = models.CharField(max_length=200,null=True,blank=True)
        dependiente = models.CharField(max_length=1,null=True,blank=True)
        archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE)
    


class Funcional_Dependientes_Economico(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    primer_apellido = models.CharField(max_length=100,null=True,blank=True)
    segundo_apellido = models.CharField(max_length=100,null=True,blank=True)
    identidad = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=100,null=True,blank=True)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    anotaciones = models.CharField(max_length=200,null=True,blank=True)
    #genero = models.ForeignKey(Funcional_Genero,null=True,blank=True,on_delete=models.CASCADE)
    genero = models.CharField(max_length=100,null=True,blank=True)
    fecha_nacimiento = models.DateField(default=now,null=True,blank=True)
    parentesco = models.ForeignKey(Funcional_Parentesco,null = True,blank=True,on_delete=models.CASCADE) 
    empleado = models.ForeignKey(Funcional_empleado,null = True,blank=True,on_delete=models.CASCADE)  
    subtipo = models.CharField(max_length=4,null=True,blank=True)
    secuencia = models.CharField(max_length=2,null=True,blank=True)
    dependiente = models.CharField(max_length=1,null=True,blank=True)
    apellido_soltera =models.CharField(max_length=100,null=True,blank=True)
    de=models.DateField(auto_now_add=True,null=True,blank=True)
    hasta=models.DateField(default=datetime.now().date(),null=True,blank=True)
    ciudad_nacimiento=models.CharField(max_length=200,null=True,blank=True)
    pais_nacimiento=models.CharField(max_length=200,null=True,blank=True)
    nacionalidad = models.CharField(max_length=200,null=True,blank=True)
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE)

    
class Funcional_Beneficiario_Seguro(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    identidad = models.CharField(max_length=100,null=True,blank=True)
    telefono = models.CharField(max_length=100,null=True,blank=True)
    direccion = models.CharField(max_length=100,null=True,blank=True)
    anotaciones = models.CharField(max_length=200,null=True,blank=True)
    #genero = models.ForeignKey(Funcional_Genero,null=True,blank=True,on_delete=models.CASCADE)
    genero = models.CharField(max_length=100,null=True,blank=True)
    fecha_nacimiento = models.DateField()
    parentesco = models.ForeignKey(Funcional_Parentesco,null = True,blank=True,on_delete=models.CASCADE )
    empleado = models.ForeignKey(Funcional_empleado,null = True,blank=True,on_delete=models.CASCADE)  
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE)

    

    
class Funcional_Plaza(models.Model):
    serie= models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=200,null=True,blank=True)
    puesto = models.ForeignKey(Funcional_Puesto,null = True,blank=True,on_delete=models.CASCADE) 
 


class Funcional_Relacion_Laboral_Anterior(models.Model):
    codigo = models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)

class Funcional_Historial_Laboral(models.Model):
    descripcion= models.CharField(max_length=100,null=True,blank=True)
    empleado=models.ForeignKey(Funcional_empleado, on_delete=models.CASCADE,null=True,blank=True)
    puesto = models.ForeignKey(Funcional_Relacion_Laboral_Anterior, on_delete=models.CASCADE,null=True,blank=True)
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE)



class Funcional_Check_List(models.Model):
    nombre=models.CharField(max_length=100,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    activo = models.BooleanField(default=False,blank=True,null=True)
    

class Funcional_Empleado_Check_List(models.Model):
    checklist = models.ForeignKey(Funcional_Check_List,blank=True,null=True,on_delete=models.CASCADE)
    empleado = models.ForeignKey(Funcional_empleado,blank=True,null=True,on_delete=models.CASCADE)
    fecha= models.DateField(auto_now_add=True,null=True,blank=True)
    activo = models.BooleanField(default=False,blank=True,null=True)
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE)


class Funcional_Laboratorio(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    fecha = models.DateField(auto_now_add=True,null=True,blank=True)

class Funcional_Vacuna(models.Model):
    nombre = models.CharField(max_length=100,null=True,blank=True)
    fecha = models.DateField(auto_now_add=True,null=True,blank=True)
    laboratorio =  models.ForeignKey(Funcional_Laboratorio,blank=True,null=True,on_delete=models.CASCADE)
    covid = models.BooleanField(default=False,blank=True,null=True)


class Funcional_Empleado_Vacuna(models.Model):
    vacuna =  models.ForeignKey(Funcional_Vacuna,blank=True,null=True,on_delete=models.CASCADE)
    empleado =  models.ForeignKey(Funcional_empleado,blank=True,null=True,on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now().date(),null=True,blank=True)
    archivos_gestor=models.ForeignKey(archivos_gestor,null=True,blank=True,on_delete=models.CASCADE)


class Configuracion_Actualizacion_Empleado(models.Model):
    fecha_inicio = models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_fin =models.DateField(default=datetime.now().date(),null=True,blank=True)
    activo = models.BooleanField(default=True,null=True,blank=True)

#log cronjobs
class Crjob_Log(models.Model):
    descripcion = models.CharField(max_length=100)
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)
class Crjob_log_empledo(models.Model):
    empleado = models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)

class Crjob_log_complementaria(models.Model):
    data = models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True,null=True,blank=True)


class Tiempos_Empleado(models.Model):
    empleado = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    incapacidad_enfermedad_anual= models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)
    tiempo_compensatorio = models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)
    vacaciones = models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)

class Absentismo_Empleado(models.Model):
    empleado = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    codigo = models.CharField(max_length=100,null=True,blank=True)
    descripcion = models.CharField(max_length=100,null=True,blank=True)
    dias = models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)
    anio = models.CharField(max_length=4,null=True,blank=True)

class Dias_Laborados_Empleado(models.Model):
    empleado = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    anio= models.CharField(max_length=4,null=True,blank=True)
    mes= models.CharField(max_length=4,null=True,blank=True)
    dias= models.CharField(max_length=4,null=True,blank=True)
    dias_asuentes = models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)
    dias_laborados = models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)

class Usuario_Log(models.Model):
    usuario = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)
    actividad = models.CharField(max_length=2500)



#Segunda Etapa Clima Laboral
##########################################TABLAS PARA CLIMA LABORAL#################################################################################
class Clima_Objeto(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)

class Clima_Sub_Objeto(models.Model):
    nombre = models.CharField(max_length=100)
    objeto = models.ForeignKey(Clima_Objeto,null=True,blank=True,on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)

class Clima_Tipo_Pregunta(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)

class Clima_Plantilla(models.Model):
    nombre_plantilla = models.CharField(max_length=100)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)

class Clima_Plantilla_Preguntas(models.Model):
    pregunta = models.CharField(max_length=500)
    plantilla =models.ForeignKey(Clima_Plantilla,on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)
    tipo=models.ForeignKey(Clima_Tipo_Pregunta, on_delete=models.CASCADE)

class Clima_Plantilla_Opciones(models.Model):
    respuesta = models.CharField(max_length=500)
    pregunta = models.ForeignKey(Clima_Plantilla_Preguntas,null=True,blank=True,on_delete=models.CASCADE)
    valor= models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)

class Clima_Cuestionario(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=10000)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)
    objeto = models.ForeignKey(Clima_Objeto,null=True,blank=True,on_delete=models.CASCADE)

class Clima_Cuestionario_Preguntas(models.Model):
    pregunta = models.CharField(max_length=500)
    cuestionario =models.ForeignKey(Clima_Cuestionario,on_delete=models.CASCADE)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)
    sub_objeto = models.ForeignKey(Clima_Sub_Objeto,null=True,blank=True,on_delete=models.CASCADE)
    tipo = models.ForeignKey(Clima_Tipo_Pregunta, on_delete=models.CASCADE)
    posicion = models.IntegerField(blank=True,null=True,default=0)

class Clima_Cuestionario_Opciones(models.Model):
    respuesta = models.CharField(max_length=500)
    pregunta = models.ForeignKey(Clima_Cuestionario_Preguntas,null=True,blank=True,on_delete=models.CASCADE)
    valor= models.DecimalField(null=True,decimal_places=2,blank=True,default=0,max_digits=5)
    posicion = models.IntegerField(blank=True,null=True,default=0)

class Clima_Segmento(models.Model):
    nombre = models.CharField(max_length=200)
    empresas=models.ManyToManyField(Funcional_Organizacion,null=True,blank=True,symmetrical=False)
    unidades=models.ManyToManyField(Funcional_Unidad_Organizativa,null=True,blank=True,symmetrical=False)
    puestos=models.ManyToManyField(Funcional_Puesto,null=True,blank=True,symmetrical=False)
    edad_inicio=models.IntegerField(blank=True,null=True,default=18)
    edad_fin=models.IntegerField(blank=True,null=True,default=18)
    genero =models.CharField(max_length=10,blank=True,null=True)
    antiguedad_inicio=models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=5)
    antiguedad_fin=models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=5)

class Clima_Tipo_Herramienta(models.Model):
    nombre=models.CharField(max_length=100)
    fecha_creacion=models.DateField(auto_now_add=True,null=True,blank=True)

class Clima_Campaña(models.Model):
    nombre_campaña = models.CharField(max_length=100)
    responsable = models.ManyToManyField(User,null=True,blank=True)
    cuestionario = models.ForeignKey(Clima_Cuestionario,on_delete=models.CASCADE,null=True,blank=True)    
    segmento = models.ForeignKey(Clima_Segmento,on_delete=models.CASCADE,null=True,blank=True)   
    fecha_inicio=models.DateField(default=datetime.now().date(),null=True,blank=True)
    fecha_fin = models.DateField(default=datetime.now().date(),null=True,blank=True)
    activa = models.BooleanField(default=True,blank=True,null=False)
    tipo_herramienta = models.ForeignKey(Clima_Tipo_Herramienta,on_delete=models.CASCADE,null=True,blank=True)

class Clima_Encuesta(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    campaña = models.ForeignKey(Clima_Campaña,on_delete=models.CASCADE,null=True,blank=True)
    cuestionario = models.ForeignKey(Clima_Cuestionario,on_delete=models.CASCADE,null=True,blank=True)
    fecha_aplicacion = models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_llenado = models.DateField(null=True,blank=True)

class Clima_Respuestas(models.Model):
    encuesta = models.ForeignKey(Clima_Encuesta,on_delete=models.CASCADE,null=True,blank=True)
    pregunta = models.ForeignKey(Clima_Cuestionario_Preguntas,on_delete=models.CASCADE,null=True,blank=True)
    opcion = models.ManyToManyField(Clima_Cuestionario_Opciones,null=True,blank=True,symmetrical=False)
    respuesta = models.CharField(max_length=500,null=True,blank=True) 
    fecha_ingreso = models.DateField(auto_now_add=True,null=True,blank=True)

class archivos_gestor_formatos_oficiales(models.Model):
    id_area = models.IntegerField(null=False,blank=False)
    id_carpeta_encabezado = models.IntegerField(null=False,blank=False)
    subnivel1 = models.CharField(max_length=200,null=True,blank=True) 
    subnivel2 = models.CharField(max_length=200,null=True,blank=True)
    medidas_disciplinarias = models.CharField(max_length=200,null=True,blank=True)
    tipo_documento = models.CharField(max_length=200,null=True,blank=True) 
    origen = models.CharField(max_length=300,null=True,blank=True)
    extension = models.CharField(max_length=20,null=True,blank=True)
    id_documento = models.IntegerField(default=0,null=False,blank=False)
    llave = models.CharField(max_length=300,null=True,blank=True)
    fecha_creacion = models.DateField(auto_now_add=True,null=True,blank=True)
    fecha_actualizacion = models.DateField(auto_now=True,null=True,blank=True)
    contentTypeGD = models.CharField(max_length=255,null=True,blank=True)

