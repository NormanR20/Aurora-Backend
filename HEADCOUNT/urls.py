from os import name
from django.urls import path,include
from rest_framework import routers
from .views import Formal_PuestoViewSet,Funcional_PuestoViewSet
from .views import Formal_PlazaViewSet,Funcional_PlazaViewSet,AutorizacionViewSet,UserViewSet,GroupViewSet
from .views import LogoutViewset,Funcional_unidadViewSet,Formal_unidadViewSet,SendmailViewset,ResetPasswordViewset,Formal_RFC_Carga_Masiva,Funcional_RFC_Carga_Masiva
from .views import Formal_RFC_Carga_Masiva_Complementaria,Funcional_RFC_Carga_Masiva_Complementaria,formal_unidad_jerarquiaviewset
from .views import Formal_empleadoViewSet,Funcional_empleadoViewSet,Formal_Relacion_LaboralViewSet,Formal_OrganizacionViewSet
from .views import Formal_DivisionViewSet,Formal_Centro_CostoViewSet,Formal_Estado_civilViewSet,Funcional_Relacion_LaboralViewSet
from .views import Funcional_DivisionViewSet,Funcional_Centro_CostoViewSet,Funcional_OrganizacionViewSet,Funcional_Estado_civilViewSet,Formal_ParentescoViewSet
from .views import Funcional_ParentescoViewSet,Funcional_GeneroViewSet,Formal_GeneroViewSet,Formal_FuncionesViewSet,Funcional_FuncionesViewSet,Formal_Situacion_ActualViewSet,Funcional_Situacion_ActualViewSet
from .views import Funcional_CompañiaViewSet,Formal_CompañiaViewSet,Funcional_EspecialidadViewSet,Formal_EspecialidadViewSet,Formal_Contacto_EmergenciaViewSet,Funcional_Contacto_EmergenciaViewSet
from .views import Formal_Dependientes_EconomicoViewSet, Funcional_Dependientes_EconomicoViewSet,Funcional_Beneficiario_SeguroViewSet,Formal_Beneficiario_SeguroViewSet
from .views import Funcional_FormacionViewSet,Formal_FormacionViewSet,Formal_EquipoViewSet,Funcional_EquipoViewSet
from .views import Formal_Historial_LaboralViewSet,Funcional_Historial_LaboralViewSet,Formal_unidadjerarquiaViewSet
from .views import Formal_empleadonodoViewSet,Funcional_unidadjerarquiaViewSet,Funcional_empleadonodoViewSet
from .views import funcional_unidad_jerarquiaviewset
from .views import Formal_InstitutoViewSet,Formal_TituloViewSet,Formal_DiagnosticoViewSet,Formal_SaludViewSet,Formal_EducacionViewSet
from .views import Funcional_InstitutoViewSet,Funcional_TituloViewSet,Funcional_DiagnosticoViewSet,Funcional_SaludViewSet,Funcional_EducacionViewSet
from .views import Formal_User_DataViewSet,Funcional_User_DataViewSet
from .views import Formal_Division_PersonalViewSet,Funcional_Division_PersonalViewSet
from .views import Formal_empleado_jerarquiaViewSet,Funcional_empleado_jerarquiaViewSet
from .views import Funcional_LaboratorioViewSet,Funcional_VacunaViewSet,Funcional_Empleado_VacunaViewSet
from .views import Formal_LaboratorioViewSet,Formal_VacunaViewSet,Formal_Empleado_VacunaViewSet,Formal_busqueda_empleadoViewSet,Funcional_busqueda_empleadoViewSet
from .views import Formal_JefesViewSet,Funcional_JefesViewSet
from .views import *
from .views import RFC_Tiempos_Empleadoviewset
#para clima laboral
from .views import Clima_ObjetoViewset,Clima_Sub_ObjetoViewset,Clima_Tipo_PreguntaViewset,Clima_Tipo_HerramientaViewset
from .views import Clima_PlantillaViewset,Clima_Plantilla_PreguntasViewset,Clima_Plantilla_OpcionesViewset
from .views import Clima_SegmentoViewset,Clima_Funcional_PuestoXUnidad_OrganizativaViewset,Clima_Funcional_PuestoXUnidad_OrganizativaViewset
from .views import Clima_CuestionarioViewset,Clima_Cuestionario_PreguntasViewset,Clima_Cuestionario_OpcionesViewset
from .views import Clima_Usuarios_ResponsablesViewSet,Clima_CampañaViewset,Clima_EncuestaViewSet,Clima_RespuestasViewset,Clima_MonitorViewSet,Clima_Envio_Masivo_Encuestas_X_CorreoViewSet
from .views import Clima_Encuesta_CheckListViewSet
from .views import On_off_bording_tareaViewSet,On_off_bording_bloqueViewSet,On_off_bording_workflowViewSet,On_off_bording_workflow_plantillaViewSet
from .views import On_off_bording_bloque_plantillaViewSet,On_off_bording_tarea_plantillaViewSet, On_off_bording_bienvenidaViewSet,On_off_bording_bienvenida_postViewSet
from .views import On_off_bording_bienvenida_embebidaViewSet,On_off_bording_envio_correoViewSet
from .views import On_off_bording_bienvenida_embebidaViewSet,On_off_bording_monitorViewSet,On_off_boarding_Control_FechasViewSet,On_off_bording_posicionViewSet
from .views import On_off_bording_estadoViewSet,On_off_bording_navegacion
from .views import Formal_Checkear_Check_list_Empleado,Funcional_Checkear_Check_list_Empleado
from .views import On_off_bording_workflow_duplicar,On_off_bording_navegacion_anterior,archivos_gestor_postViewSet, archivos_gestor_formatos_oficiales_postViewSet
from .views import descriptor_perfil_datos_unidad_medidaViewSet,descriptor_perfil_tipo_competenciaViewSet,descriptor_perfil_areaViewSet,descriptor_perfil_competenciaViewSet,descriptor_perfil_formacion_area_conocimientoViewSet,descriptor_perfil_formacion_nivel_educativoViewSet
from .views import descriptor_perfil_tituloViewSet,descriptor_perfil_conocimiento_tecnicoViewSet,descriptor_perfil_formacionViewSet,descriptor_perfil_preparacionViewSet,descriptor_perfil_conocimiento_tecnico_adquiridoViewSet,descriptor_perfil_proposito_descriptorViewSet,descriptor_perfil_indicador_descriptorViewSet
from .views import archivos_gestor_competenciaViewSet,archivos_gestor_competencia_postViewSet,descriptor_perfil_experienciaViewSet,descriptor_perfil_envio_correoViewSet,seleccion_contratacion_dashboard_motivo_solicitud,seleccion_contratacion_dashboard_contrataciones
from .views import easyaudit_RequestEventViewSet,easyaudit_CRUDEventViewSet,easyaudit_LoginEventViewSet,seleccion_contratacion_plaza_vacantesViewSet,seleccion_contratacion_motivoViewSet,seleccion_contratacion_paisViewSet,seleccion_contratacion_solicitud_plaza_vacanteViewSet,descriptor_perfil_competencia_totalViewSet,Funcional_Funciones_filtrado_unidad_organizativaViewSet,descriptor_perfil_colaborador_FuncionViewSet
from .views import capacitacion_metrica_9_cajasViewSet,capacitacion_campaniaViewSet,capacitacion_archivo_gestor_formatos
##########################################################################
from rest_framework.authtoken import views
from AURORA.easyaudit.backend_easyaudit import ModelBackend
from .views import seleccion_contratacion_postulante_plazaViewSet
#from .views import capacitacion_tipo_capacitacionViewSet
from .views import evaluacion_frecuenciaViewSet,evaluacion_tipo_evaluacion,validacion,dashboard_evaluaciones_jefe
from .views.procesos_auxiliares import  cargar_posicion_empleado


app_name = 'api'
router = routers.DefaultRouter()
router.register(r'head_clima_pais',head_clima_paisViewSet)
router.register(r'head_clima_departamento',head_clima_departamentoViewSet)
router.register(r'head_clima_municipio',head_clima_municipioViewSet)
router.register(r'head_clima_pais_consulta',head_clima_pais_consultaViewSet)
router.register(r'nucleo_pruebas', nucleo_pruebasViewSet)
router.register(r'Formal_Puesto', Formal_PuestoViewSet)
router.register(r'Funcional_Puesto', Funcional_PuestoViewSet)
router.register(r'Formal_Plaza', Formal_PlazaViewSet)   
router.register(r'Funcional_Plaza', Funcional_PlazaViewSet)
router.register(r'User', UserViewSet)
router.register(r'Group', GroupViewSet)
router.register(r'Funcional_unidad', Funcional_unidadViewSet)
router.register(r'Formal_unidad', Formal_unidadViewSet)
router.register(r'Formal_empleado', Formal_empleadoViewSet)
router.register(r'Funcional_empleado', Funcional_empleadoViewSet)
router.register(r'Formal_Relacion_Laboral', Formal_Relacion_LaboralViewSet)
router.register(r'Formal_Division', Formal_DivisionViewSet)
router.register(r'Formal_Organizacion', Formal_OrganizacionViewSet)
router.register(r'Formal_Centro_Costo', Formal_Centro_CostoViewSet)
router.register(r'Formal_Estado_civil', Formal_Estado_civilViewSet)
router.register(r'Funcional_Relacion_Laboral', Funcional_Relacion_LaboralViewSet)
router.register(r'Funcional_Division', Funcional_DivisionViewSet)
router.register(r'Funcional_Centro_Costo', Funcional_Centro_CostoViewSet)
router.register(r'Funcional_Organizacion', Funcional_OrganizacionViewSet)
router.register(r'Funcional_Estado_civil', Funcional_Estado_civilViewSet)
router.register(r'Formal_Parentesco', Formal_ParentescoViewSet)
router.register(r'Funcional_Parentesco', Funcional_ParentescoViewSet)
router.register(r'Formal_Genero', Formal_GeneroViewSet)
router.register(r'Funcional_Genero', Funcional_GeneroViewSet)
router.register(r'Formal_Funciones', Formal_FuncionesViewSet)
router.register(r'Funcional_Funciones', Funcional_FuncionesViewSet)
router.register(r'Funcional_Funciones_filtrado_unidad_organizativa', Funcional_Funciones_filtrado_unidad_organizativaViewSet)
router.register(r'Formal_Situacion_Actual', Formal_Situacion_ActualViewSet)
router.register(r'Funcional_Situacion_Actual', Funcional_Situacion_ActualViewSet)
router.register(r'Formal_Compania', Formal_CompañiaViewSet)
router.register(r'Funcional_Compania', Funcional_CompañiaViewSet)
router.register(r'Formal_Especialidad', Formal_EspecialidadViewSet)
router.register(r'Funcional_Especialidad', Funcional_EspecialidadViewSet)
router.register(r'Formal_Contacto_Emergencia', Formal_Contacto_EmergenciaViewSet)
router.register(r'Funcional_Contacto_Emergencia', Funcional_Contacto_EmergenciaViewSet)
router.register(r'Formal_Dependientes_Economico', Formal_Dependientes_EconomicoViewSet)
router.register(r'Funcional_Dependientes_Economico', Funcional_Dependientes_EconomicoViewSet)
router.register(r'Formal_Beneficiario_Seguro', Formal_Beneficiario_SeguroViewSet)
router.register(r'Funcional_Beneficiario_Seguro', Funcional_Beneficiario_SeguroViewSet)
router.register(r'Formal_Formacion', Formal_FormacionViewSet)
router.register(r'Funcional_Formacion', Funcional_FormacionViewSet)
router.register(r'Formal_Equipo', Formal_EquipoViewSet)
router.register(r'Funcional_Equipo', Funcional_EquipoViewSet)
router.register(r'Formal_Historial_Laboral', Formal_Historial_LaboralViewSet)
router.register(r'Funcional_Historial_Laboral', Funcional_Historial_LaboralViewSet)
router.register(r'Formal_unidadjerarquia', Formal_unidadjerarquiaViewSet)
router.register(r'Formal_empleadonodo',Formal_empleadonodoViewSet)
router.register(r'Funcional_unidadjerarquia', Funcional_unidadjerarquiaViewSet)
router.register(r'Funcional_empleadonodo',Funcional_empleadonodoViewSet)

router.register(r'Formal_Instituto',Formal_InstitutoViewSet)
router.register(r'Formal_Titulo',Formal_TituloViewSet)
router.register(r'Formal_Diagnostico',Formal_DiagnosticoViewSet)
router.register(r'Formal_Salud',Formal_SaludViewSet)
router.register(r'Formal_Educacion',Formal_EducacionViewSet)

router.register(r'Funcional_Instituto',Funcional_InstitutoViewSet)
router.register(r'Funcional_Titulo',Funcional_TituloViewSet)
router.register(r'Funcional_Diagnostico',Funcional_DiagnosticoViewSet)
router.register(r'Funcional_Salud',Funcional_SaludViewSet)
router.register(r'Funcional_Educacion',Funcional_EducacionViewSet)
router.register(r'Formal_Division_Personal',Formal_Division_PersonalViewSet)
router.register(r'Funcional_Division_Personal',Funcional_Division_PersonalViewSet)
router.register(r'Formal_empleado_jerarquia',Formal_empleado_jerarquiaViewSet)
router.register(r'Funcional_empleado_jerarquia',Funcional_empleado_jerarquiaViewSet)

router.register(r'Actualizacion_Contacto',Actualizacion_ContactoViewSet)
router.register(r'Actualizacion_Dependiente',Actualizacion_DependienteViewSet)
router.register(r'Actualizacion_Domicilio',Actualizacion_DomicilioViewSet)
router.register(r'Actualizacion_Educacion',Actualizacion_EducacionViewSet)
router.register(r'Actualizacion_Estado_Civil',Actualizacion_Estado_CivilViewSet)

router.register(r'Formal_Check_List',Formal_Check_ListViewSet)
router.register(r'Funcional_Check_List',Funcional_Check_ListViewSet)
router.register(r'Formal_Empleado_Check_List',Formal_Empleado_Check_ListViewSet)
router.register(r'Funcional_Empleado_Check_List',Funcional_Empleado_Check_ListViewSet)
router.register(r'Configuracion_Actualizacion_Empleado',Configuracion_Actualizacion_EmpleadoViewset)

#Agregado Para manejo de Vacunas 
router.register(r'Funcional_Laboratorio',Funcional_LaboratorioViewSet)
router.register(r'Funcional_Vacuna',Funcional_VacunaViewSet)
router.register(r'Funcional_Empleado_Vacuna',Funcional_Empleado_VacunaViewSet)
router.register(r'Formal_Laboratorio',Formal_LaboratorioViewSet)
router.register(r'Formal_Vacuna',Formal_VacunaViewSet)
router.register(r'Formal_Empleado_Vacuna',Formal_Empleado_VacunaViewSet)
router.register(r'Funcional_Relacion_Laboral_Anterior',Funcional_Relacion_Laboral_AnteriorViewSet)
router.register(r'Formal_Relacion_Laboral_Anterior',Formal_Relacion_Laboral_AnteriorViewSet)
router.register(r'Formal_filtro_empleado',Formal_filtro_empleadoViewSet)
router.register(r'Formal_Clasificacion',Formal_ClasificacionViewSet)
router.register(r'Funcional_Clasificacion',Funcional_ClasificacionViewSet)



router.register(r'Funcional_empleado_foto',Funcional_empleado_fotoViewSet)
router.register(r'Formal_empleado_foto',Formal_empleado_fotoViewSet)
router.register(r'Funcional_empleado_lista_sencilla',Funcional_empleado_lista_sencillaviewsets)
router.register(r'Funcional_empleado_activos_lista_sencilla',Funcional_empleado_activos_lista_sencillaviewsets)

#Agregado para nueva busqueda
router.register(r'Formal_busqueda_empleado',Formal_busqueda_empleadoViewSet)
router.register(r'Funcional_busqueda_empleado',Funcional_busqueda_empleadoViewSet)

#agregado para api de jefes
router.register(r'Formal_Jefes',Formal_JefesViewSet)
router.register(r'Funcional_Jefes',Funcional_JefesViewSet)

router.register(r'Absentismo_Empleado',Absentismo_EmpleadosViewSet)
router.register(r'Tiempos_Empleado',Tiempos_EmpleadoViewSet)
router.register(r'Dias_Laborados_Empleado',Dias_Laborados_EmpleadoViewSet)

#para clima laboral
router.register(r'Clima_Objeto',Clima_ObjetoViewset)
router.register(r'Clima_Sub_Objeto',Clima_Sub_ObjetoViewset)
router.register(r'Clima_Tipo_Pregunta',Clima_Tipo_PreguntaViewset)
router.register(r'Clima_Tipo_Herramienta',Clima_Tipo_HerramientaViewset)
router.register(r'Clima_Plantilla',Clima_PlantillaViewset)
router.register(r'Clima_Plantilla_Preguntas',Clima_Plantilla_PreguntasViewset)
router.register(r'Clima_Plantilla_Opciones',Clima_Plantilla_OpcionesViewset)
router.register(r'Clima_Segmento', Clima_SegmentoViewset)
#router.register(r'Clima_Funcional_PuestoXUnidad_Organizativa',Clima_Funcional_PuestoXUnidad_OrganizativaViewset)
#router.register(r'Clima_Funcional_Unidad_OrganizativaXOrganizacion',Clima_Funcional_Unidad_OrganizativaXOrganizacionViewset)
router.register(r'Clima_Cuestionario',Clima_CuestionarioViewset)
router.register(r'Clima_Cuestionario_Preguntas',Clima_Cuestionario_PreguntasViewset)
router.register(r'Clima_Cuestionario_Opciones',Clima_Cuestionario_OpcionesViewset)
router.register(r'Clima_Campaña',Clima_CampañaViewset)
router.register(r'Clima_Encuesta',Clima_EncuestaViewSet)
router.register(r'Clima_Respuestas',Clima_RespuestasViewset)
router.register(r'Clima_Encuesta_CheckList',Clima_Encuesta_CheckListViewSet)
###########################################################################
#ON_OFF_BORDING
router.register(r'On_off_bording_workflow',On_off_bording_workflowViewSet)
router.register(r'On_off_bording_bloque',On_off_bording_bloqueViewSet)
router.register(r'On_off_bording_tarea',On_off_bording_tareaViewSet)
router.register(r'On_off_bording_workflow_plantilla',On_off_bording_workflow_plantillaViewSet)
router.register(r'On_off_bording_bloque_plantilla',On_off_bording_bloque_plantillaViewSet)
router.register(r'On_off_bording_tarea_plantilla',On_off_bording_tarea_plantillaViewSet)

###########################################################################
#NUCLEO####################################################################
router.register(r'nucleo_modulos',nucleo_modulosViewSet)
router.register(r'nucleo_tipo_mensaje',nucleo_tipo_mensajeViewSet)
router.register(r'nucleo_configuracion_correos',nucleo_configuracion_correosViewSet)
router.register(r'nucleo_variables_envio_correos',nucleo_variables_envio_correosViewSet)
#############################################################################


###Gestor Documental#################################################################
router.register(r'archivos_gestor',archivos_gestorViewSet)

##SANCIONES#########################################################################
router.register(r'sanciones_categoria_desvinculacion',sanciones_categoria_desvinculacionViewSet)
router.register(r'sanciones_motivo_accion',sanciones_motivo_accion_disciplinariaViewSet)
router.register(r'sanciones_accion_disciplinaria',sanciones_tipo_accion_disciplinariaViewSet)
router.register(r'sanciones_mantenimiento_medidas_disciplinarias',sanciones_medidas_disciplinariasViewSet)
router.register(r'sanciones_nivel_gravedad',sanciones_tipo_faltaViewSet)
router.register(r'sanciones_estatus',sanciones_estatusViewSet)
router.register(r'sanciones_caso_disciplinario',sanciones_casos_disciplinariosViewSet)
router.register(r'sanciones_accion_disciplinaria_correos',sanciones_accion_disciplinaria_correosViewSet)
router.register(r'sanciones_plantilla_formatos_oficiales',sanciones_plantilla_formatos_oficialesViewSet)

router.register(r'sanciones_sancion',sanciones_accion_disciplinariaViewSet)

router.register(r'sanciones_plantilla_formatos_oficiales',sanciones_plantilla_formatos_oficialesViewSet)
####################################################################################



######################################################################################################

##DESCRIPTORES Y PERFILES###############################################################################
router.register(r'descriptor_perfil_tipo_competencia',descriptor_perfil_tipo_competenciaViewSet)
router.register(r'descriptor_perfil_datos_unidad_medida',descriptor_perfil_datos_unidad_medidaViewSet)
router.register(r'descriptor_perfil_area',descriptor_perfil_areaViewSet)
router.register(r'descriptor_perfil_proposito',descriptor_perfil_propositoViewSet)
router.register(r'descriptor_perfil_formacion_area_conocimiento',descriptor_perfil_formacion_area_conocimientoViewSet)
router.register(r'descriptor_perfil_cursos_diplomados_seminario_pasantia',descriptor_perfil_cursos_diplomados_seminario_pasantiaViewSet)
router.register(r'descriptor_perfil_preparacion',descriptor_perfil_preparacionViewSet)
router.register(r'descriptor_perfil_datos_generales',descriptor_perfil_datos_generalesViewSet)
router.register(r'descriptor_perfil_competencia',descriptor_perfil_competenciaViewSet)
router.register(r'descriptor_perfil_indicador',descriptor_perfil_indicadorViewSet)
router.register(r'descriptor_perfil_competencia_descriptor',descriptor_perfil_competencia_descriptorViewSet)
#router.register(r'descriptor_perfil_competencia_descriptor_archivo',descriptor_perfil_competencia_descriptor_archivoViewSet)
router.register(r'descriptor_perfil_politicas_procedimientos',descriptor_perfil_politicas_procedimientosViewSet)
router.register(r'descriptor_perfil_indicador_descriptor',descriptor_perfil_indicador_descriptorViewSet)
router.register(r'descriptor_perfil_experiencia',descriptor_perfil_experienciaViewSet)
router.register(r'descriptor_perfil_competencia_total',descriptor_perfil_competencia_totalViewSet)

##EASYAUDIT###############################################################################
router.register(r'easyaudit_RequestEvent',easyaudit_RequestEventViewSet)
router.register(r'easyaudit_CRUDEvent',easyaudit_CRUDEventViewSet)
router.register(r'easyaudit_LoginEvent',easyaudit_LoginEventViewSet)


##SELECCION Y CONTRATACION###############################################################################

router.register(r'seleccion_contratacion_plaza_vacantes',seleccion_contratacion_plaza_vacantesViewSet)


##SELECCION Y CONTRATACION###############################################################################

router.register(r'seleccion_contratacion_plaza_vacantes',seleccion_contratacion_plaza_vacantesViewSet)


##SELECCION Y CONTRATACION###############################################################################

router.register(r'seleccion_contratacion_plaza_vacantes',seleccion_contratacion_plaza_vacantesViewSet)
router.register(r'seleccion_contratacion_motivo',seleccion_contratacion_motivoViewSet)
router.register(r'seleccion_contratacion_pais',seleccion_contratacion_paisViewSet)
router.register(r'seleccion_contratacion_solicitud_plaza_vacante',seleccion_contratacion_solicitud_plaza_vacanteViewSet)
router.register(r'seleccion_contratacion_estado',seleccion_contratacion_estadoViewSet)
router.register(r'seleccion_contratacion_postulante_plaza',seleccion_contratacion_postulante_plazaViewSet)
router.register(r'informacin_powerbi',informacin_powerBIviewsets)






router.register(r'descriptor_perfil_formacion_nivel_educativo',descriptor_perfil_formacion_nivel_educativoViewSet)
router.register(r'descriptor_perfil_titulo',descriptor_perfil_tituloViewSet)
router.register(r'descriptor_perfil_conocimiento_tecnico',descriptor_perfil_conocimiento_tecnicoViewSet)
router.register(r'descriptor_perfil_formacion',descriptor_perfil_formacionViewSet)
router.register(r'descriptor_perfil_preparacion',descriptor_perfil_preparacionViewSet)
router.register(r'descriptor_perfil_colaborador_Funcion',descriptor_perfil_colaborador_FuncionViewSet)
router.register(r'descriptor_perfil_conocimiento_tecnico_adquirido',descriptor_perfil_conocimiento_tecnico_adquiridoViewSet)
router.register(r'descriptor_perfil_funcion',descriptor_perfil_funcionViewSet)
router.register(r'descriptor_perfil_proposito_descriptor',descriptor_perfil_proposito_descriptorViewSet)
router.register(r'archivos_gestor_competencia',archivos_gestor_competenciaViewSet)
router.register(r'descriptor_perfil_competencia_descriptor_correccion',descriptor_perfil_competencia_descriptor_correccionViewSet)

##EVALUACION DEL DESEMPEÑO###############################################################################
router.register(r'evaluacion_metrica_competencia',evaluacion_metrica_competenciaViewSet)
router.register(r'evaluacion_metrica_factor',evaluacion_metrica_factorViewSet)
router.register(r'evaluacion_frecuencia',evaluacion_frecuenciaViewSet)
router.register(r'evaluacion_tipo_evaluacion',evaluacion_tipo_evaluacionViewSet)

router.register(r'evaluacion_factor',evaluacion_factorViewSet)
router.register(r'evaluacion_competencia',evaluacion_competenciaViewSet)
router.register(r'evaluacion_tipo_plan_accion',evaluacion_tipo_plan_accionViewSet)
router.register(r'evaluacion_archivo_plan_accion_gestor',evaluacion_archivo_plan_accion_gestorViewSet)
router.register(r'categoria_desempeno',categoria_desempenoViewSet)
router.register(r'evaluacion_plantilla_factor',evaluacion_plantilla_factorViewSet)
router.register(r'monitor_colaborador',monitor_colaboradorViewSet)
router.register(r'evaluacion_plantilla_competencia',evaluacion_plantilla_competenciaViewSet)
router.register(r'evaluacion_configuracion_periodo',evaluacion_configuracion_periodoViewSet)
router.register(r'evaluacion_periodicidad',evaluacion_periodicidadViewSet)
router.register(r'evaluacion_encabezado',evaluacion_encabezadoViewSet)
router.register(r'monitor_evaluacion',Monitor_evaluacionViewSet)
router.register(r'detalle_evaluacion_factor',detalle_evaluacion_factorViewSet)
router.register(r'detalle_evaluacion_factor_indicador',detalle_evaluacion_factor_indicadorViewSet)

router.register(r'evaluacion_despliegue_preguntas_competencia',evaluacion_despliegue_preguntas_competenciaViewSet)

router.register(r'evaluacion_factor_plantilla_encabezado',evaluacion_factor_plantilla_encabezadoViewSet)
router.register(r'evaluacion_competencia_plantilla_encabezado',evaluacion_competencia_plantilla_encabezadoViewSet)
router.register(r'resumen_general_evaluaciones',resumen_general_evaluacionesViewSet)

router.register(r'evaluacion_despliegue_preguntas_factor',evaluacion_despliegue_preguntas_factorViewSet)
router.register(r'evaluacion_cambio_pesos_factor',evaluacion_cambio_pesos_factorViewSet)


####MODULO DE CAPACITACION##########################################################################################
router.register(r'capacitacion_tipo_capacitacion',capacitacion_tipo_capacitacionViewSet)
router.register(r'capacitacion_modalidad',capacitacion_modalidadViewSet)
router.register(r'capacitacion_enfoque',capacitacion_enfoqueViewSet)
router.register(r'capacitacion_motivo_inasistencia',capacitacion_motivo_inasistenciaViewSet)


router.register(r'capacitacion_origen',capacitacion_origenViewSet)
router.register(r'capacitacion_estado',capacitacion_estadoViewSet)
router.register(r'capacitacion_curso',capacitacion_cursoViewSet)
router.register(r'capacitacion_metrica_evaluacion_factor',capacitacion_metrica_evaluacion_factorViewSet)
router.register(r'capacitacion_metrica_9_cajas',capacitacion_metrica_9_cajasViewSet)
router.register(r'capacitacion_campania',capacitacion_campaniaViewSet)
router.register(r'capacitacion_metrica_experiencia_puesto',capacitacion_metrica_experiencia_puestoViewSet)
router.register(r'capacitacion_matriz_9_caja',capacitacion_matriz_9_cajaViewSet)
router.register(r'capacitacion_metrica_educacion_formal',capacitacion_metrica_educacion_formalViewSet)
router.register(r'capacitacion_monitor_colaborador',capacitacion_monitor_colaboradorViewSet)
router.register(r'capacitacion_evento_capacitacion',capacitacion_evento_capacitacionViewSet)
router.register(r'busqueda_personas_por_rol',busqueda_personas_por_rolViewSet)
router.register(r'capacitacion_asistencia',capacitacion_asistenciaViewSet)
router.register(r'monitor_capacitaciones',monitor_capacitacionesViewSet)
router.register(r'capacitacion_archivo_gestor_formatos_gestor',capacitacion_archivo_gestor_formatos_gestorViewSet)


















##NOTIFICACIONES EN AURORA###############################################################################
router.register(r'notificacion_aurora',notificacion_auroraViewSet)



####################################################################################
urlpatterns = [
    path('app/', include(router.urls)),
    path('app/permiso/', AutorizacionViewSet.as_view(), name='permiso'),
    path('app/logout/', LogoutViewset.as_view(), name='logout'),
    path('app/sendmail/',SendmailViewset.as_view(),name='sendmail'),
    path('app/resetpassword/',ResetPasswordViewset.as_view(),name='resetpassword'),
    path('app/admin_reset_password/',ResetPassword_administradorViewset.as_view(),name='admin_reset_password'),

    
    path('app/Formal_RFC_Carga_Masiva/',Formal_RFC_Carga_Masiva.as_view(),name='Formal_RFC_Carga_Masiva'),
    path('app/Formal_RFC_Carga_Masiva_Complementaria/',Formal_RFC_Carga_Masiva_Complementaria.as_view(),name='Formal_RFC_Carga_Masiva_Complementaria'),
    path('app/Funcional_RFC_Carga_Masiva/',Funcional_RFC_Carga_Masiva.as_view(),name='Funcional_RFC_Carga_Masiva'),
    path('app/Funcional_RFC_Carga_Masiva_Complementaria/',Funcional_RFC_Carga_Masiva_Complementaria.as_view(),name='Funcional_RFC_Carga_Masiva_Complementaria'),
    path('app/RFC_Tiempos_Empleado/',RFC_Tiempos_Empleadoviewset.as_view(),name='RFC_Tiempos_Empleado'),
    path('app/Funcional_arbol_viewset/',Funcional_arbol_viewset.as_view(),name='Funcional_arbol_viewset'),
    path('app/formal_unidad_jerarquiaviewset/',formal_unidad_jerarquiaviewset.as_view(),name='formal_unidad_jerarquiaviewset'),
    path('app/funcional_unidad_jerarquiaviewset/',funcional_unidad_jerarquiaviewset.as_view(),name='funcional_unidad_jerarquiaviewset'),
    path('app/Formal_User_Data/',Formal_User_DataViewSet.as_view(),name='Formal_User_Data'),
    path('app/Funcional_User_Data/',Funcional_User_DataViewSet.as_view(),name='Funcional_User_Data'),
    path('app/dashboard_plazas_contrataciones/',dashboard_plazas_contratacionesViewset.as_view(),name='dashboard_plazas_contratacionesViewset'),
    path('app/Actualizacion_Datos_Excel/',Actualizacion_Datos_Excel.as_view()),
    path('app/Formal_Checkear_Empleado/',Formal_Checkear_Empleado.as_view()),
    path('app/Funcional_Checkear_Empleado/',Funcional_Checkear_Empleado.as_view()),
    path('app/Creacion_Usuario_sin_correo/',Creacion_Usuario_sin_correo.as_view()),
    path('app/Funcional_Vacuna_Checkear_Empleado',Funcional_Vacuna_Checkear_Empleado.as_view()),
    path('app/Actualizacion_Datos_Actualizado/',Actualizacion_Datos_Actualizado.as_view()),
    path('app/Existe_Correo/',Existe_CorreoViewSet.as_view(),name='Existe_CorreoViewSet'),
    #Existe_CorreoViewSet
    #funcional_unidad_jerarquiaviewset
    path('token',ModelBackend.as_view()),
    #CLIMA SEGUNDA ETAPA
    path('app/Clima_Usuarios_Responsables/',Clima_Usuarios_ResponsablesViewSet.as_view(),name='Clima_Usuarios_ResponsablesViewSet'),
    path('app/Clima_Monitor/',Clima_MonitorViewSet.as_view(),name='Clima_MonitorViewSet'),
    path('app/Clima_Envio_Masivo_Encuestas_X_Correo/',Clima_Envio_Masivo_Encuestas_X_CorreoViewSet.as_view()),
    path('app/Reporte_ultima_sesion/',Reporte_ultima_sessionViewset.as_view()),
    path('app/Clima_Funcional_Unidad_OrganizativaXOrganizacion/',Clima_Funcional_Unidad_OrganizativaXOrganizacionViewset.as_view()),
    path('app/Clima_Funcional_PuestoXUnidad_Organizativa/',Clima_Funcional_PuestoXUnidad_OrganizativaViewset.as_view()),
    path('app/LLenar_Log_SessionViewset/',LLenar_Log_SessionViewset.as_view()),
    path('app/Onoff_boarding_grabar/',Copia_workflowviewset.as_view()),
    path('app/Copia_masiva_workflow/',Copia_masiva_workflowviewset.as_view()),
    path('app/Funciona_listado_hijos_nohijos_unidad/',Funciona_listado_hijos_nohijos_unidad.as_view()),
    path('app/Funcionas_unidad_quitar_hijos/',Funcionas_unidad_quitar_hijos.as_view()),
    path('app/Funcionas_unidad_agregar_hijos/',Funcionas_unidad_agregar_hijos.as_view()),
    path('app/On_off_boarding_bienvenida/<int:id>/',On_off_bording_bienvenidaViewSet.as_view()),
    path('app/On_off_boarding_bienvenida/',On_off_bording_bienvenida_postViewSet.as_view()),
    path('app/On_off_bording_bienvenida_embebida/',On_off_bording_bienvenida_embebidaViewSet.as_view()),
    path('app/On_off_bording_envio_correo/',On_off_bording_envio_correoViewSet.as_view()),
    path('app/On_off_bording_monitor/',On_off_bording_monitorViewSet.as_view()),
    path('app/On_off_bording_posicion/',On_off_bording_posicionViewSet.as_view()),

    path('app/On_off_boarding_Control_Fechas/',On_off_boarding_Control_FechasViewSet.as_view()),
    path('app/Clima_generacion_enlace_encuestas/',Clima_generacion_enlace_encuestas.as_view()),
    path('app/On_off_bording_mostrar_bienvenida/',On_off_bording_mostrar_bienvenida.as_view()),
    path('app/On_off_bording_estado/',On_off_bording_estadoViewSet.as_view()),
    path('app/On_off_bording_navegacion/',On_off_bording_navegacion.as_view()),
    path('app/On_off_bording_Dashboard_jefe_responsable/',On_off_bording_Dashboard_jefe_responsable.as_view()),
    path('app/Formal_Checkear_Check_list_Empleado/',Formal_Checkear_Check_list_Empleado.as_view()),
    path('app/Funcional_Checkear_Check_list_Empleado/',Funcional_Checkear_Check_list_Empleado.as_view()),
    path('app/On_off_boarding_workflow_Control_Fechas/',On_off_boarding_workflow_Control_FechasViewSet.as_view()),
    path('app/Actualizacion_Datos_Excel_cambio_estado/',Actualizacion_Datos_Excel_cambio_estado.as_view()),
    path('app/On_off_bording_eliminar_workflow/<int:id>/',On_off_bording_eliminar_workflow.as_view()),
    path('app/On_off_bording_workflow_duplicar/',On_off_bording_workflow_duplicar.as_view()),
    path('app/On_off_bording_navegacion_anterior/',On_off_bording_navegacion_anterior.as_view()),

    path('app/archivos_gestor_postViewSet/',archivos_gestor_postViewSet.as_view()),
    path('app/archivos_gestor_postViewSet/<int:pk>/', archivos_gestor_postViewSet.as_view()),

    path('app/archivos_gestor_formatos_oficiales_post/',archivos_gestor_formatos_oficiales_postViewSet.as_view()),
    path('app/archivos_gestor_formatos_oficiales_post/<int:pk>/', archivos_gestor_formatos_oficiales_postViewSet.as_view()),
    
    path('app/archivos_gestor_competencia_postViewSet/<int:pk>/', archivos_gestor_competencia_postViewSet.as_view()),
    path('app/archivos_gestor_competencia_postViewSet/', archivos_gestor_competencia_postViewSet.as_view()),
    
    path('app/Monitor_bajas/', Monitor_bajas.as_view()),
    path('app/sanciones_envio_correo/',sanciones_envio_correoViewSet.as_view()),
    path('app/descriptor_perfil_envio_correo/',descriptor_perfil_envio_correoViewSet.as_view()),
    path('app/Descargar_Manual_Descriptor/<int:id>/', CrearArchivoViewset.as_view()),
    path('app/seleccion_contratacion_plan_requerimiento/<int:id>/', seleccion_contratacion_plan_requerimientoViewset.as_view()),
    path('app/seleccion_contratacion_dashboard_motivo_solicitud/',seleccion_contratacion_dashboard_motivo_solicitud.as_view()),
    path('app/seleccion_contratacion_dashboard_contrataciones/', seleccion_contratacion_dashboard_contrataciones.as_view()),
    path('app/seleccion_contratacion_dashboard_vacantes/', seleccion_contratacion_dashboard_vacantes.as_view()),
    path('app/envio_correo_seleccion_contratacion/', envio_correo_seleccion_contratacion.as_view()),
    path('app/evaluacion_archivo_plan_accion/', evaluacion_archivo_plan_accion.as_view()),
    path('app/evaluacion_archivo_plan_accion/<int:pk>/', evaluacion_archivo_plan_accion.as_view()),
    path('app/copiado_evaluacion_plantilla_competencia/', copiado_evaluacion_plantilla_competencia.as_view()),
    path('app/copiado_evaluacion_plantilla_factor/', copiado_evaluacion_plantilla_factor.as_view()),
    path('app/calculo_calificaciones/', calculo_calificaciones.as_view()),
    path('app/cargar_posicion_empleado/', cargar_posicion_empleado.as_view()),
    path('app/correo_evaluaciones/', correo_evaluaciones.as_view()),
    path('app/validacion/<int:pk>/',validacion.as_view()),
    path('app/dashboard_evaluaciones_jefe/',dashboard_evaluaciones_jefe.as_view()),
     
    
   
    path('app/seleccion_contratacion_dashboard_vacantes/', seleccion_contratacion_dashboard_vacantes.as_view()),
    path('app/envio_correo_seleccion_contratacion/', envio_correo_seleccion_contratacion.as_view()),
    path('app/validar_envio_evaluacion_colaborador/', validar_envio_evaluacion_colaborador.as_view()),
    path('app/validacion_decriptor_colaborador/', validacion_decriptor_colaborador.as_view()),
    path('app/ordenamiento_9cajas/', ordenamiento_9cajasViewSet.as_view()),
    path('app/ordenamiento_9cajas/', ordenamiento_9cajasViewSet.as_view()),
    path('app/correo_capacitaciones/', correo_capacitaciones.as_view()),

    
    path('app/capacitacion_llenado_9cajas/', capacitacion_llenado_9cajasViewSet.as_view()),


    path('app/validar_envio_evaluacion_colaborador/', validar_envio_evaluacion_colaborador.as_view()),
    path('app/validacion_decriptor_colaborador/', validacion_decriptor_colaborador.as_view()),
    
    path('app/capacitacion_archivo_gestor_formatos/', capacitacion_archivo_gestor_formatos.as_view()),
    path('app/capacitacion_archivo_gestor_formatos/<int:pk>/', capacitacion_archivo_gestor_formatos.as_view()),
    path('app/capacitacion_archivo_evaluacionViewset/<int:id>/', capacitacion_archivo_evaluacionViewset.as_view()),
    
    

    

    
]

    

