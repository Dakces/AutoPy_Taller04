from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


def validar_nombre(value):
    if len(value) < 5 or len(value) > 80:
        raise ValidationError('El nombre debe tener entre 5 y 80 caracteres.')

def validar_descripcion(value):
    if len(value) < 10 or len(value) > 200:
        raise ValidationError('La descripción debe tener entre 10 y 200 caracteres.')
        
def validar_codigo(value):
    if len(value) != 8:
        raise ValidationError('El codigo debe tener exactamente 8 caracteres')
        
def validar_rango(value):
    if not (1 <= value <= 99):
        raise ValidationError(f'El valor {value} debe estar entre 1 y 999.')

class Producto(models.Model):
    codigo = models.CharField(
        max_length=8,
        validators=[validar_codigo]
    )
    nombre = models.CharField(
        max_length=80,
        validators=[validar_nombre]
    )
    descripcion = models.CharField(
        max_length=200,
        validators=[validar_descripcion]
    )
    cantidad_minima = models.IntegerField(
        default=0,
        validators=[validar_rango]
        )
    precio = models.FloatField(
    default=0,
        validators=[MinValueValidator(0.01), MaxValueValidator(999.00)]
    )
    
    def __str__(self):
        return f"{self.codigo} {self.nombre}"