from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path("login/", LoginView.as_view(), name="login"),
    path('logout/', views.cerrar_sesion, name="logout"),

    path('salas/', views.salas_list, name='salas_list'),
    path('salas/nueva/', views.sala_crear, name='sala_crear'),
    path('salas/<int:id>/', views.sala_detalle, name='sala_detalle'),
    path('salas/<int:id>/editar/', views.sala_editar, name='sala_editar'),
    path('salas/<int:id>/eliminar/', views.sala_eliminar, name='sala_eliminar'),

    path('reservas/', views.reservas_list, name='reservas_list'),
    path('reservas/nueva/', views.reservar, name='reservar'),
    path('reservas/<int:id>/editar/', views.reserva_editar, name='reserva_editar'),
    path('reservas/<int:id>/eliminar/', views.reserva_eliminar, name='reserva_eliminar'),
]
