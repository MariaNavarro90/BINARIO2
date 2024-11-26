from django import forms
from .models import Servicio, Proyecto, Consulta, Testimonio


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class BusquedaForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Buscar')

class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['cliente_nombre', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu testimonio aquí...'})
        }