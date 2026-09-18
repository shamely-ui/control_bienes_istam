"""
URL configuration for control_bienes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página principal
    path('', views.dashboard, name='dashboard'),

    # Lista de categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),

    # Formulario para registrar una nueva categoría
    path('categorias/nueva/', views.nueva_categoria, name='nueva_categoria'),

    # Editar una categoría
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),

    # Activa o desactiva una categoría
    path('categorias/estado/<int:id>/',views.cambiar_estado_categoria, name='cambiar_estado_categoria'),

    # Lista de ubicaciones
    path(
        'ubicaciones/',
        views.lista_ubicaciones,
        name='lista_ubicaciones'
    ),


    # Nueva ubicación
    path(
        'ubicaciones/nueva/',
        views.nueva_ubicacion,
        name='nueva_ubicacion'
    ),

    # Editar ubicación
    path(
        'ubicaciones/editar/<int:id>/',
        views.editar_ubicacion,
        name='editar_ubicacion'
    ),


    # Activa o desactiva una ubicación
    path(
    'ubicaciones/estado/<int:id>/',
    views.cambiar_estado_ubicacion,
    name='cambiar_estado_ubicacion'
    ),


    # Lista de custodios
    path(
    'custodios/',
    views.lista_custodios,
    name='lista_custodios'
    ),

    # Nuevo custodio
    path(
    'custodios/nuevo/',
    views.nuevo_custodio,
    name='nuevo_custodio'
),

# Editar custodio
path(
    'custodios/editar/<int:id>/',
    views.editar_custodio,
    name='editar_custodio'
),

# Activa o desactiva un custodio
path(
    'custodios/estado/<int:id>/',
    views.cambiar_estado_custodio,
    name='cambiar_estado_custodio'
),

# Lista de bienes
path(
    'bienes/',
    views.lista_bienes,
    name='lista_bienes'
),

# Ver detalle de un bien
path(
    'bienes/detalle/<int:id>/',
    views.detalle_bien,
    name='detalle_bien'
),

# Nuevo bien
path(
    'bienes/nuevo/',
    views.nuevo_bien,
    name='nuevo_bien'
),

# Editar bien
path(
    'bienes/editar/<int:id>/',
    views.editar_bien,
    name='editar_bien'
),
# Activar o desactivar bien
path(
    'bienes/estado/<int:id>/',
    views.cambiar_estado_bien,
    name='cambiar_estado_bien'
),
# Lista de asignaciones
path(
    'asignaciones/',
    views.lista_asignaciones,
    name='lista_asignaciones'
),

# Nueva asignación
path(
    'asignaciones/nueva/',
    views.nueva_asignacion,
    name='nueva_asignacion'
),

# Editar asignación
path(
    'asignaciones/editar/<int:id>/',
    views.editar_asignacion,
    name='editar_asignacion'
),

# Registrar devolución
path(
    'asignaciones/devolucion/<int:id>/',
    views.registrar_devolucion,
    name='registrar_devolucion'
),

# Lista de constataciones
path(
    'constataciones/',
    views.lista_constataciones,
    name='lista_constataciones'
),

# Nueva constatación
path(
    'constataciones/nueva/',
    views.nueva_constatacion,
    name='nueva_constatacion'
),

# Editar constatación
path(
    'constataciones/editar/<int:id>/',
    views.editar_constatacion,
    name='editar_constatacion'
),

# Lista de bajas
path(
    'bajas/',
    views.lista_bajas,
    name='lista_bajas'
),

# Nueva baja
path(
    'bajas/nueva/',
    views.nueva_baja,
    name='nueva_baja'
),

# Reportes
path(
    'reportes/',
    views.reportes,
    name='reportes'
),


# Inicio de sesión
path(
    'login/',
    views.iniciar_sesion,
    name='login'
),

# Cerrar sesión
path(
    'logout/',
    views.cerrar_sesion,
    name='logout'
),

# Acta de entrega-recepción
path(
    'asignaciones/acta/<int:id>/',
    views.acta_asignacion,
    name='acta_asignacion'
),

# Importar bienes desde Excel
path(
    'bienes/importar/',
    views.importar_bienes,
    name='importar_bienes'
),

path(
    'custodios/importar/',
    views.importar_custodios,
    name='importar_custodios'
),

# Importar matriz de entrega de actas
path(
    'asignaciones/importar-actas/',
    views.importar_matriz_actas,
    name='importar_matriz_actas'
),
]


