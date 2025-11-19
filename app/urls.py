from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),


    # Salas (solo admin)
    path("salas/", views.salas_list, name="salas_list"),
    path("salas/nueva/", views.sala_crear, name="sala_crear"),
    path("salas/<int:id>/editar/", views.sala_editar, name="sala_editar"),
    path("salas/<int:id>/eliminar/", views.sala_eliminar, name="sala_eliminar"),
    path("salas/<int:id>/", views.sala_detalle, name="sala_detalle"),

    # Reservas
    path("reservas/", views.reservas_list, name="reservas_list"),
    path("reservas/nueva/", views.reservar, name="reservar"),
    path("reservas/<int:id>/editar/", views.reserva_editar, name="reserva_editar"),
    path("reservas/<int:id>/eliminar/", views.reserva_eliminar, name="reserva_eliminar"),
]

    path("salas/", views.salas_list, name="salas_list"),
    path("salas/nueva/", views.sala_crear, name="sala_crear"),
    path("salas/editar/<int:id>/", views.sala_editar, name="sala_editar"),
    path("salas/eliminar/<int:id>/", views.sala_eliminar, name="sala_eliminar"),


    path("salas/<int:id>/", views.sala_detalle, name="sala_detalle"),

    path("reservas/", views.reservas_list, name="reservas_list"),
    path("reservas/nueva/", views.reservar, name="reservar"),
    path("reservas/editar/<int:id>/", views.reserva_editar, name="reserva_editar"),
    path("reservas/eliminar/<int:id>/", views.reserva_eliminar, name="reserva_eliminar"),
]
