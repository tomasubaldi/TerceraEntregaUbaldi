from django import forms
from .models import EquipoMusical

class EquipoMusicalForm(forms.ModelForm):
    
    class Meta:
        model = EquipoMusical
        fields = ('marca', 'modelo', 'potencia', 'descripcion')