from django import forms
from .models import Sala, Reserva

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ["nombre", "capacidad"]


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["sala", "persona", "inicio", "fin"]
        widgets = {
            "inicio": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "fin": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
