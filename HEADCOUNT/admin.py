from django.contrib import admin

from HEADCOUNT.views import views_sanciones
from .models import *
# Register your models here.


admin.site.register(Formal_Estado_civil)
admin.site.register(Formal_Check_List)
admin.site.register(Formal_Empleado_Check_List)
admin.site.register(Formal_empleado)
admin.site.register(sanciones_accion_disciplinaria)
admin.site.register(sanciones_accion_disciplinaria_correos)
admin.site.register(sanciones_casos_disciplinarios)
admin.site.register(sanciones_medidas_disciplinarias)
admin.site.register(sanciones_motivo_accion_disciplinaria)
admin.site.register(sanciones_tipo_falta)
admin.site.register(sanciones_categoria_desvinculacion)
admin.site.register(modelos_sanciones.sanciones_plantilla_formatos_oficiales)
admin.site.register(Funcional_empleado)
admin.site.register(sanciones_estatus)
admin.site.register(descriptor_perfil_proposito)
admin.site.register(descriptor_perfil_datos_generales)
admin.site.register(descriptor_perfil_datos_unidad_medida)
admin.site.register(descriptor_perfil_proposito_descriptor)
admin.site.register(descriptor_perfil_tipo_competencia)
admin.site.register(descriptor_perfil_competencia)
admin.site.register(descriptor_perfil_area)
admin.site.register(archivos_gestor_competencia)
admin.site.register(descriptor_perfil_competencia_descriptor)
#admin.site.register(descriptor_perfil_competencia_descriptor_archivo)
admin.site.register(descriptor_perfil_politicas_procedimientos)
admin.site.register(descriptor_perfil_indicador)
admin.site.register(descriptor_perfil_indicador_descriptor)
admin.site.register(descriptor_perfil_funcion)
admin.site.register(descriptor_perfil_experiencia)
admin.site.register(descriptor_perfil_formacion)
admin.site.register(descriptor_perfil_preparacion)
admin.site.register(descriptor_perfil_conocimiento_tecnico_adquirido)
admin.site.register(Funcional_Clasificacion)
admin.site.register(descriptor_perfil_formacion_area_conocimiento)
admin.site.register(descriptor_perfil_formacion_nivel_educativo)
admin.site.register(descriptor_perfil_titulo)
admin.site.register(descriptor_perfil_cursos_diplomados_seminario_pasantia)
admin.site.register(descriptor_perfil_conocimiento_tecnico)
admin.site.register(categoria_desempeno)
admin.site.register(evaluacion_frecuencia)    
admin.site.register(evaluacion_tipo_plan_accion)
admin.site.register(evaluacion_archivo_plan_accion_gestor)
admin.site.register(evaluacion_tipo_evaluacion)
admin.site.register(evaluacion_metrica_competencia)
admin.site.register(evaluacion_factor)
admin.site.register(evaluacion_competencia)
admin.site.register(evaluacion_metrica_factor)
admin.site.register(evaluacion_periodicidad)
admin.site.register(evaluacion_configuracion_periodo)
admin.site.register(evaluacion_plantilla_competencia)
admin.site.register(evaluacion_plantilla_factor)
admin.site.register(evaluacion_encabezado)
admin.site.register(detalle_evaluacion_competencia)
admin.site.register(detalle_evaluacion_factor)
admin.site.register(evaluacion_factor_plantilla_encabezado)
admin.site.register(evaluacion_competencia_plantilla_encabezado)
admin.site.register(notificacion_aurora)
admin.site.register(on_off_bording_workflow_plantilla)
admin.site.register(on_off_bording_bloque_plantilla)
admin.site.register(on_off_bording_tarea_plantilla)
admin.site.register(on_off_bording_workflow)
admin.site.register(on_off_bording_bloque)
admin.site.register(on_off_bording_tarea)
admin.site.register(on_off_bording_bienvenida)



admin.site.register(capacitacion_tipo_capacitacion)
admin.site.register(capacitacion_modalidad)
admin.site.register(capacitacion_matriz_9_cajas)
admin.site.register(capacitacion_evento_capacitacion)
admin.site.register(capacitacion_motivo_inasistencia)
admin.site.register(capacitacion_enfoque)
admin.site.register(capacitacion_origen)
admin.site.register(capacitacion_estado)
admin.site.register(capacitacion_curso)
admin.site.register(capacitacion_factor_evaluacion)
admin.site.register(capacitacion_escala_evaluacion_factor)
admin.site.register(capacitacion_metrica_educacion_formal)
admin.site.register(capacitacion_metrica_experiencia_puesto)
admin.site.register(capacitacion_metrica_evaluacion_factor)
admin.site.register(capacitacion_campania)
admin.site.register(capacitacion_asistencia)
admin.site.register(Funcional_Instituto)
admin.site.register(Funcional_Formacion)
admin.site.register(Funcional_Titulo)
admin.site.register(Funcional_Especialidad)
admin.site.register(capacitacion_metrica_9_cajas)
















