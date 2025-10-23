from django.urls import path
from . import views

app_name = 'app_uber' # Namespace para nuestras URLs

urlpatterns = [
    path('', views.listar_pasajeros, name='listar_pasajeros'),
    path('pasajero/<int:id_usuario>/', views.detalle_pasajero, name='detalle_pasajero'),
    path('pasajero/crear/', views.crear_pasajero, name='crear_pasajero'),
    path('pasajero/editar/<int:id_usuario>/', views.editar_pasajero, name='editar_pasajero'),
    path('pasajero/borrar/<int:id_usuario>/', views.borrar_pasajero, name='borrar_pasajero'),
]