import django_filters
from .models import Producto
from django import forms
from django.utils.translation import gettext_lazy as _

class ProductoFilter(django_filters.FilterSet):   
    codigo = django_filters.CharFilter(
        label=_("Código"),
        lookup_expr='icontains',
        widget = forms.TextInput(attrs={'class': 'form-control','placeholder':_("Ingresar el código del producto")})
    )
    class Meta:
        model=Producto
        fields=['codigo']