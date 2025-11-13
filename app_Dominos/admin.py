from django.contrib import admin
from .models import Cliente, Pedido, Producto

# ADMIN: CLIENTE
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id_cliente',
        'nombre',
        'apellido',
        'email',
        'telefono',
        'direccion',
        'fecha_registro',
        'metodo_pago_preferido',
    )
    search_fields = ('nombre', 'apellido', 'email')


# ADMIN: PEDIDO
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'id_pedido',
        'id_cliente',
        'producto',
        'fecha_pedido',
        'estado',
        'total',
        'direccion',
        'metodo_pago',
    )
    search_fields = ('producto', 'estado', 'metodo_pago')


# ADMIN: PRODUCTO
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id_producto',
        'nombre',
        'descripcion',
        'precio',
        'tamaño',
        'categoria',
        'disponibilidad',
        'fecha_creacion',
        'cliente',
    )
    list_filter = ('categoria', 'disponibilidad')
    search_fields = ('nombre', 'categoria', 'descripcion')
