"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from ejemplo.views import (index, saludar_a, sumar, buscar, monstrar_familiares, mostrar_familiaresMVP, 
                                                    BuscarFamiliar, AltaFamiliar, ActualizarFamiliar,
                                                     FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar,
                                                     VehiculoList, VehiculoCrear, VehiculoActualizar, VehiculoBorrar,
                                                     MascotaList, MascotaCrear, MascotaActualizar, MascotaBorrar,
                                                     VacacionesList, VacacionesCrear, VacacionesActualizar, VacacionesBorrar,
                                                     BuscarVacaciones, BuscarMascota, BuscarVehiculo)
from turismo_arg.views import (index, PostList, PostCrear, PostDetalle, PostActualizar, PostBorrar, AvatarActualizar,
                               UserSignUp, UserLogin, UserLogout, UserActualizar, MensajeDetalle, MensajeListar, MensajeCrear, MensajeBorrar)                                                 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
    path("saludar_a/<nombre>/", saludar_a),
    path("sumar/<int:a>/<int:b>/", sumar),
    path('buscar/', buscar),
    path('mi-familia/', monstrar_familiares), # nueva vista)
    path("familia-MVP/", mostrar_familiaresMVP), #MVP a ver si sale
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarList.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('success_update_messagge/', TemplateView.as_view(template_name="ejemplo/success_update_messagge")),
    path('panel-vehiculo/', VehiculoList.as_view()),
    path('panel-vehiculo/crear', VehiculoCrear.as_view()),
    path('panel-vehiculo/<int:pk>/borrar', VehiculoBorrar.as_view()),
    path('panel-vehiculo/<int:pk>/actualizar', VehiculoActualizar.as_view()),
    path('panel-mascota/', MascotaList.as_view()),
    path('panel-mascota/crear', MascotaCrear.as_view()),
    path('panel-mascota/<int:pk>/borrar', MascotaBorrar.as_view()),
    path('panel-mascota/<int:pk>/actualizar', MascotaActualizar.as_view()),
    path('panel-vacaciones/', VacacionesList.as_view()),
    path('panel-vacaciones/crear', VacacionesCrear.as_view()),
    path('panel-vacaciones/<int:pk>/borrar', VacacionesBorrar.as_view()),
    path('panel-vacaciones/<int:pk>/actualizar', VacacionesActualizar.as_view()),
    path('vacaciones/buscar', BuscarVacaciones.as_view()),
    path('vehiculo/buscar', BuscarVehiculo.as_view()),
    path('mascota/buscar', BuscarMascota.as_view()),
    path('turismo-arg/', index, name= 'turismo-arg-index'),
    path('turismo-arg/<int:pk>/detalle', PostDetalle.as_view(), name= "turismo-arg-detalle"),
    path('turismo-arg/listar', PostList.as_view(), name= "turismo-arg-listar"),
    path('turismo-arg/crear', PostCrear.as_view(), name= "turismo-arg-crear"),
    path('turismo-arg/<int:pk>/borrar', PostBorrar.as_view(), name= "turismo-arg-borrar"),
    path('turismo-arg/<int:pk>/actualizar', PostActualizar.as_view(), name= "turismo-arg-actualizar"),
    path('turismo-arg/signup', UserSignUp.as_view(), name="turismo-arg-signup"),
    path('turismo-arg/login/', UserLogin.as_view(), name="turismo-arg-login"),
    path('turismo-arg/logout/', UserLogout.as_view(), name="turismo-arg-logout"),
    path('turismo-arg/avatares/<int:pk>/actualizar/', AvatarActualizar.as_view(), name= "turismo-arg-avatares-actualizar"),
    path('turismo-arg/users/<int:pk>/actualizar/', UserActualizar.as_view(), name= "turismo-arg-users-actualizar"),
    path('turismo-arg/mensajes/crear/', MensajeCrear.as_view(), name= "turismo-arg-mensajes-crear"),
    path('turismo-arg/mensajes/<int:pk>/detalle', MensajeDetalle.as_view(), name= "turismo-arg-mensajes-detalle"),
    path('turismo-arg/mensajes/listar/', MensajeListar.as_view(), name= "turismo-arg-mensajes-listar"),
    path('turismo-arg/mensajes/<int:pk>/borrar', MensajeBorrar.as_view(), name= "turismo-arg-mensajes-borrar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)