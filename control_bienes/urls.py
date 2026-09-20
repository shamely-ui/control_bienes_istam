"""
URL configuration for control_bienes project.
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

# Permite mostrar las fotografías subidas durante el desarrollo
from django.conf import settings
from django.conf.urls.static import static

from inventario import views


urlpatterns = [

    # Administración
    path('admin/', admin.site.urls),

    # Página principal
    path('', views.dashboard, name='dashboard'),


    # ==========================
    # CATEGORÍAS
    # ==========================

    path(
        'categorias/',
        views.lista_categorias,
        name='lista_categorias'
    ),

    path(
        'categorias/nueva/',
        views.nueva_categoria,
        name='nueva_categoria'
    ),

    path(
        'categorias/editar/<int:id>/',
        views.editar_categoria,
        name='editar_categoria'
    ),

    path(
        'categorias/estado/<int:id>/',
        views.cambiar_estado_categoria,
        name='cambiar_estado_categoria'
    ),


    # ==========================
    # UBICACIONES
    # ==========================

    path(
        'ubicaciones/',
        views.lista_ubicaciones,
        name='lista_ubicaciones'
    ),

    path(
        'ubicaciones/nueva/',
        views.nueva_ubicacion,
        name='nueva_ubicacion'
    ),

    path(
        'ubicaciones/editar/<int:id>/',
        views.editar_ubicacion,
        name='editar_ubicacion'
    ),

    path(
        'ubicaciones/estado/<int:id>/',
        views.cambiar_estado_ubicacion,
        name='cambiar_estado_ubicacion'
    ),


    # ==========================
    # CUSTODIOS
    # ==========================

    path(
        'custodios/',
        views.lista_custodios,
        name='lista_custodios'
    ),

    path(
        'custodios/nuevo/',
        views.nuevo_custodio,
        name='nuevo_custodio'
    ),

    path(
        'custodios/editar/<int:id>/',
        views.editar_custodio,
        name='editar_custodio'
    ),

    path(
        'custodios/estado/<int:id>/',
        views.cambiar_estado_custodio,
        name='cambiar_estado_custodio'
    ),

    path(
        'custodios/importar/',
        views.importar_custodios,
        name='importar_custodios'
    ),


    # ==========================
    # BIENES
    # ==========================

    path(
        'bienes/',
        views.lista_bienes,
        name='lista_bienes'
    ),

    path(
        'bienes/detalle/<int:id>/',
        views.detalle_bien,
        name='detalle_bien'
    ),

    path(
        'bienes/nuevo/',
        views.nuevo_bien,
        name='nuevo_bien'
    ),

    path(
        'bienes/editar/<int:id>/',
        views.editar_bien,
        name='editar_bien'
    ),

    path(
        'bienes/estado/<int:id>/',
        views.cambiar_estado_bien,
        name='cambiar_estado_bien'
    ),

    path(
        'bienes/importar/',
        views.importar_bienes,
        name='importar_bienes'
    ),


    # ==========================
    # ASIGNACIONES
    # ==========================

    path(
        'asignaciones/',
        views.lista_asignaciones,
        name='lista_asignaciones'
    ),

    path(
        'asignaciones/nueva/',
        views.nueva_asignacion,
        name='nueva_asignacion'
    ),

    path(
        'asignaciones/editar/<int:id>/',
        views.editar_asignacion,
        name='editar_asignacion'
    ),

    path(
        'asignaciones/devolucion/<int:id>/',
        views.registrar_devolucion,
        name='registrar_devolucion'
    ),

    path(
        'asignaciones/acta/<int:id>/',
        views.acta_asignacion,
        name='acta_asignacion'
    ),

    path(
        'asignaciones/eliminar/<int:id>/',
        views.eliminar_asignacion,
        name='eliminar_asignacion'
    ),

    path(
        'asignaciones/importar-actas/',
        views.importar_matriz_actas,
        name='importar_matriz_actas'
    ),


    # ==========================
    # CONSTATACIONES
    # ==========================

    path(
        'constataciones/',
        views.lista_constataciones,
        name='lista_constataciones'
    ),

    path(
        'constataciones/nueva/',
        views.nueva_constatacion,
        name='nueva_constatacion'
    ),

    path(
        'constataciones/editar/<int:id>/',
        views.editar_constatacion,
        name='editar_constatacion'
    ),


    # ==========================
    # BAJAS
    # ==========================

    path(
        'bajas/',
        views.lista_bajas,
        name='lista_bajas'
    ),

    path(
        'bajas/nueva/',
        views.nueva_baja,
        name='nueva_baja'
    ),


    # ==========================
    # REPORTES
    # ==========================

    path(
        'reportes/',
        views.reportes,
        name='reportes'
    ),


    # ==========================
    # RECUPERACIÓN DE CONTRASEÑA
    # ==========================

    path(
        'recuperar-password/',
        auth_views.PasswordResetView.as_view(
            template_name='inventario/recuperar_password.html'
        ),
        name='recuperar_password'
    ),

    path(
        'recuperar-password/enviado/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='inventario/recuperar_password_enviado.html'
        ),
        name='password_reset_done'
    ),

    path(
        'restablecer-password/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='inventario/restablecer_password.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'restablecer-password/completado/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='inventario/password_completado.html'
        ),
        name='password_reset_complete'
    ),


    # ==========================
    # SESIÓN
    # ==========================

    path(
        'login/',
        views.iniciar_sesion,
        name='login'
    ),

    path(
        'logout/',
        views.cerrar_sesion,
        name='logout'
    ),

]


# Permite visualizar fotografías guardadas en MEDIA durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )