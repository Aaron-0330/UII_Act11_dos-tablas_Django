from django.db import models
from django.utils import timezone # Para usar DATETIME

class Usuario_pasajero(models.Model):
    id_usuario = models.AutoField(primary_key=True) # ID automático para el usuario
    nombre = models.CharField(max_length=100, help_text="Nombre completo del pasajero")
    email = models.EmailField(unique=True, help_text="Correo electrónico único del pasajero")
    telefono = models.IntegerField(help_text="Número de teléfono del pasajero")
    fecha_registro = models.DateTimeField(default=timezone.now, help_text="Fecha y hora de registro")
    foto = models.ImageField(upload_to='fotos_pasajeros/', blank=True, null=True, help_text="Foto de perfil del pasajero")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Usuario Pasajero"
        verbose_name_plural = "Usuarios Pasajeros"

class Tarjeta(models.Model):
    id = models.AutoField(primary_key=True) # ID automático para la tarjeta
    usuario_pasajero = models.ForeignKey(Usuario_pasajero, on_delete=models.CASCADE, related_name='tarjetas', help_text="Usuario al que pertenece esta tarjeta")
    numero_tarjeta = models.CharField(max_length=16, help_text="Número de tarjeta (solo últimos 4 dígitos visibles por seguridad)") # Usamos CharField porque no haremos operaciones matemáticas
    tipo_tarjeta = models.CharField(max_length=50, help_text="Ej: Visa, MasterCard, American Express")
    fecha_vencimiento = models.DateField(help_text="Fecha de vencimiento (MM/AA)") # Usamos DateField
    cvv = models.CharField(max_length=4, help_text="Código de seguridad (CVV)") # Usamos CharField

    def __str__(self):
        return f"**** **** **** {self.numero_tarjeta[-4:]} ({self.tipo_tarjeta}) - {self.usuario_pasajero.nombre}"

    class Meta:
        verbose_name = "Tarjeta de Pago"
        verbose_name_plural = "Tarjetas de Pago"