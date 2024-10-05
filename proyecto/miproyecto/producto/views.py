
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import gettext as _
from django.http import HttpResponseServerError
from .models import Producto
from .filters import ProductoFilter
from .forms import ProductoForm,ProductoViewForm
import logging
logger = logging.getLogger(__name__)

PAGINATION_SIZE=10
BACK_URL="/productos"

def listar_productos_view(request):
    try:
        productos = Producto.objects.all().order_by('id')
        productos_filter = ProductoFilter(request.GET,queryset=productos)
        productos_paginator = Paginator(productos_filter.qs, PAGINATION_SIZE)
        current_page = request.GET.get('page')
        offset=0
        try:
            productos_page = productos_paginator.page(current_page)
            offset=(int(current_page)-1)*int(PAGINATION_SIZE)
        except PageNotAnInteger:
            productos_page = productos_paginator.page(1)            
        except EmptyPage:
            productos_page = productos_paginator.page(productos_paginator.num_pages)
            offset=productos_paginator.num_pages*int(PAGINATION_SIZE)
        params = {
            'offset':offset,
            'back_url':BACK_URL,
            "filter":productos_filter,      
            "page":productos_page,         
        }
        return render(request,"listar.html",params)
    except Exception as e:
        logger.error('Error {}'.format(e))
        return HttpResponseServerError()
        
def crear_producto_view(request):
    try:
        if request.method == "POST":
            form = ProductoForm(request.POST)
            if form.is_valid():
                record = form.save(commit=False)
                record.save()
                return redirect('/productos/')
        else:
            form = ProductoForm()    
        labels={
            "save":_("Guardar"),
            "page_title":_("Agregar nuevo producto"),
            "section_title":_("Detalles"),
            "cancel":_("Cancel"),
        }
        params={
            'module_name':'Productos',
            'back_url':'/productos/',
            "form":form,
            "labels":labels
        }
        return render(request, "crear.html", params)
    except Exception as e:
        logger.error('Error {}'.format(e))
        return HttpResponseServerError()
        
def editar_producto_view(request,id):
    try:
        producto_model = Producto.objects.get(id=id)
        form = ProductoForm(request.POST or None, instance = producto_model)
        if request.method == "POST":
            if form.is_valid():
                record = form.save(commit=False)
                record.save()
                return redirect("/productos/")
            else:
                for field in form.errors:
                    form[field].field.widget.attrs['class'] += ' is-invalid'  
        labels={
            "save":_("Editar"),
            "page_title":_("Editar producto"),
            "section_title":_("Detalles"),
            "cancel":_("Cancelar"),
        }
        params={
            'module_name':_('Productos'),
            'back_url':"/productos",
            "form":form,
            "labels":labels,
            "current_id":producto_model.id
        }
        return render(request, "editar.html", params)
    except Exception as e:
        logger.error('Error {}'.format(e))
        return HttpResponseServerError()
        
def ver_producto_view(request,id):
    try:
        producto_model = Producto.objects.get(id=id) 
        producto_form = ProductoViewForm(instance=producto_model)
        labels={
            "back":_("Regresar"),
            "page_title":_("Ver Producto"),
            "section_title":_("Detalles de producto"),
            "cancel":_("Cancelar"),
        }
        params={
            'module_name':_('Productos'),
            'back_url':"/productos",
            "form":producto_form,
            "labels":labels
        }
        return render(request,"ver.html", params)
    except Exception as e:
        logger.error('Error {}'.format(e))
        return HttpResponseServerError()
        
def eliminar_producto_view(request,id):
    try:
        model = Producto.objects.get(id=id)
        model.delete()
        return redirect("/productos")
    except Exception as e:
        logger.error('Error {}'.format(e))
        return HttpResponseServerError()