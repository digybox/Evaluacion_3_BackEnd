from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    def actualizar_disponibilidad(self):
        ahora = timezone.now()
        hay_reserva = self.reserva_set.filter(fin__gte=ahora).exists()
        self.disponible = not hay_reserva
        self.save()

    def obtener_reserva_activa(self):
        ahora = timezone.now()
        return self.reserva_set.filter(inicio__lte=ahora, fin__gte=ahora).first()


class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    persona = models.CharField(max_length=100, verbose_name="RUT")
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

    def clean(self):
        if self.inicio >= self.fin:
            raise ValidationError("La hora de inicio debe ser menor a la hora de fin.")

        solapada = Reserva.objects.filter(
            sala=self.sala,
            inicio__lt=self.fin,
            fin__gt=self.inicio,
        ).exclude(id=self.id).exists()

        if solapada:
            raise ValidationError("La sala ya está reservada en ese horario.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
        self.sala.actualizar_disponibilidad()

    def delete(self, *args, **kwargs):
        sala = self.sala
        super().delete(*args, **kwargs)
        sala.actualizar_disponibilidad()

    def __str__(self):
        return f"{self.persona} - {self.sala.nombre}"
