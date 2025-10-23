from django import forms
from .models import Usuario_pasajero, Tarjeta

class UsuarioPasajeroForm(forms.ModelForm):
    class Meta:
        model = Usuario_pasajero
        fields = ['nombre', 'email', 'telefono', 'foto']
        # No incluimos fecha_registro ni id_usuario porque son automáticos o primarios

class TarjetaForm(forms.ModelForm):
    # Para la fecha de vencimiento, usaremos un DateInput para mejor UX
    fecha_vencimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'month', 'placeholder': 'MM/AAAA'}),
        input_formats=['%Y-%m'], # Formato esperado del input HTML type="month"
        help_text="Formato: MM/AAAA"
    )

    class Meta:
        model = Tarjeta
        fields = ['numero_tarjeta', 'tipo_tarjeta', 'fecha_vencimiento', 'cvv']
        widgets = {
            'numero_tarjeta': forms.TextInput(attrs={'placeholder': 'Número de tarjeta (últimos 4)', 'maxlength': '16'}),
            'cvv': forms.TextInput(attrs={'placeholder': 'CVV', 'maxlength': '4'}),
        }
        help_texts = {
            'numero_tarjeta': 'Introduce el número completo de la tarjeta.',
            'cvv': 'El código de seguridad de 3 o 4 dígitos en la parte trasera/frontal de tu tarjeta.',
        }