from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Producto
#from core.widgets import TempusWidget

class ProductoForm(forms.ModelForm):  
    class Meta:        
        model = Producto
        fields = ('codigo','nombre','descripcion','precio','cantidad_minima')
        labels = {            
            'codigo':_("Codigo"),
            'nombre':_("Nombre"),            
            'descripcion':_("Descripción"),
            'precio':_("Precio"),
            'cantidad_minima':_("Cantidad Minima"),
        }        
        widgets = {
            'codigo':forms.TextInput(attrs={"placeholder": _("Codigo"),"class":"form-control"}),
            'nombre':forms.TextInput(attrs={"placeholder": _("Nombre"),"class":"form-control upper-text"}),
            'descripcion':forms.TextInput(attrs={"placeholder": _("Descripción"),"class":"form-control upper-text"}),
            'precio':forms.TextInput(attrs={"placeholder": _("Precio"),"class":"form-control upper-text"}),          
            'cantidad_minima':forms.TextInput(attrs={"placeholder": _("Cantidad Minima"),"class":"form-control upper-text"}),          
        }
        
class ProductoViewForm(forms.ModelForm):  
    class Meta:        
        model = Producto
        fields = ('codigo','nombre','descripcion','precio','cantidad_minima')
        labels = {            
            'codigo':_("Codigo"),
            'nombre':_("Nombre"),            
            'descripcion':_("Descripción"),
            'precio':_("Precio"),
            'cantidad_minima':_("Cant. Minima"),
        }