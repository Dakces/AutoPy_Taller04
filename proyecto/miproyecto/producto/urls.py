from django.urls import path,re_path

from . import views

urlpatterns = [
    re_path(r"$", views.listar_productos_view, name="listar_productos"),
    path(r"crear/", views.crear_producto_view, name="crear_producto"),
    path(r"editar/<int:id>", views.editar_producto_view, name="editar_producto_view"),
    path(r"ver/<int:id>", views.ver_producto_view, name="ver_producto_view"),
    path(r"eliminar/<int:id>", views.eliminar_producto_view, name="eliminar_producto_view"),
]
