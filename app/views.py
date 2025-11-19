from django.shortcuts import render, redirect, get_object_or_404
<<<<<<< HEAD
from django.contrib.auth.decorators import login_required, user_passes_test
=======
>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
from .models import Sala, Reserva
from .forms import SalaForm, ReservaForm


<<<<<<< HEAD
def es_admin(user):
    return user.is_staff


=======
>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def home(request):
    salas = Sala.objects.all()
    for s in salas:
        s.actualizar_disponibilidad()
<<<<<<< HEAD
    return render(request, "index.html", {"salas": salas})


# ---------- SALAS (SOLO ADMIN) ----------

@login_required
@user_passes_test(es_admin)
=======

    return render(request, "index.html", {"salas": salas})


>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def salas_list(request):
    salas = Sala.objects.all()
    return render(request, "app/salas_list.html", {"salas": salas})


<<<<<<< HEAD
@login_required
@user_passes_test(es_admin)
=======
>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def sala_crear(request):
    if request.method == "POST":
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("salas_list")
    else:
        form = SalaForm()
<<<<<<< HEAD
    return render(request, "app/salas_form.html", {"form": form, "titulo": "Nueva Sala"})


@login_required
@user_passes_test(es_admin)
=======
    return render(request, "app/salas_form.html", {
        "form": form,
        "titulo": "Nueva Sala"
    })


>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def sala_editar(request, id):
    sala = get_object_or_404(Sala, id=id)
    if request.method == "POST":
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect("salas_list")
    else:
        form = SalaForm(instance=sala)
<<<<<<< HEAD
    return render(request, "app/salas_form.html", {"form": form, "titulo": "Editar Sala"})


@login_required
@user_passes_test(es_admin)
=======
    return render(request, "app/salas_form.html", {
        "form": form,
        "titulo": "Editar Sala"
    })


>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def sala_eliminar(request, id):
    sala = get_object_or_404(Sala, id=id)
    sala.delete()
    return redirect("salas_list")


<<<<<<< HEAD
# ---------- RESERVAS ----------

# Admin: ve todas las reservas
@login_required
@user_passes_test(es_admin)
=======
def sala_detalle(request, id):
    sala = get_object_or_404(Sala, id=id)
    sala.actualizar_disponibilidad()
    reserva = sala.obtener_reserva_activa()

    return render(request, "app/sala_detalle.html", {
        "sala": sala,
        "reserva": reserva
    })


>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def reservas_list(request):
    reservas = Reserva.objects.all().order_by("-inicio")
    return render(request, "app/reservas_list.html", {"reservas": reservas})


<<<<<<< HEAD
# Usuario normal: puede crear reservas
@login_required
=======
>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def reservar(request):
    if request.method == "POST":
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
<<<<<<< HEAD
                reserva = form.save()
                return redirect("sala_detalle", id=reserva.sala.id)
=======
                form.save()
                return redirect("reservas_list")
>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
            except Exception as e:
                return render(request, "app/reservas_form.html", {
                    "form": form,
                    "titulo": "Nueva Reserva",
                    "error": str(e)
                })
    else:
        form = ReservaForm()

    return render(request, "app/reservas_form.html", {
        "form": form,
        "titulo": "Nueva Reserva"
    })


<<<<<<< HEAD
# Editar/eliminar reservas: SOLO admin

@login_required
@user_passes_test(es_admin)
=======
>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def reserva_editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            try:
                form.save()
                return redirect("reservas_list")
            except Exception as e:
                return render(request, "app/reservas_form.html", {
                    "form": form,
                    "titulo": "Editar Reserva",
<<<<<<< HEAD
                    "error": str(e),
                })
    else:
        form = ReservaForm(instance=reserva)
    return render(request, "app/reservas_form.html", {"form": form, "titulo": "Editar Reserva"})


@login_required
@user_passes_test(es_admin)
=======
                    "error": str(e)
                })
    else:
        form = ReservaForm(instance=reserva)

    return render(request, "app/reservas_form.html", {
        "form": form,
        "titulo": "Editar Reserva"
    })


>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
def reserva_eliminar(request, id):
    r = get_object_or_404(Reserva, id=id)
    r.delete()
    return redirect("reservas_list")

<<<<<<< HEAD

# ---------- DETALLE DE SALA (VISIBLE PARA TODOS) ----------

def sala_detalle(request, id):
    sala = get_object_or_404(Sala, id=id)
    sala.actualizar_disponibilidad()

    # TODAS las reservas de la sala
    reservas = sala.reserva_set.all().order_by("-inicio")

    return render(request, "app/sala_detalle.html", {
        "sala": sala,
        "reservas": reservas
    })

=======
>>>>>>> 948abcf8f54b812fa17f640d3add663291a2c337
