from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Pedido, Producto
from django.utils import timezone

# =====================================
# INICIO
# =====================================
def inicio_dominos(request):
    return render(request, 'inicio.html')


# =====================================
# CRUD CLIENTE
# =====================================
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        apellido = request.POST.get('apellido', '')
        email = request.POST.get('email', '')
        telefono = request.POST.get('telefono', '')
        direccion = request.POST.get('direccion', '')
        metodo_pago_preferido = request.POST.get('metodo_pago_preferido', '')

        Cliente.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            direccion=direccion,
            metodo_pago_preferido=metodo_pago_preferido,
            fecha_registro=timezone.now().date()
        )
        return redirect('ver_cliente')
    return render(request, 'cliente/agregar_cliente.html')


def ver_cliente(request):
    clientes = Cliente.objects.all().order_by('id_cliente')
    return render(request, 'cliente/ver_cliente.html', {'clientes': clientes})


def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})


def realizar_actualizacion_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre', cliente.nombre)
        cliente.apellido = request.POST.get('apellido', cliente.apellido)
        cliente.email = request.POST.get('email', cliente.email)
        cliente.telefono = request.POST.get('telefono', cliente.telefono)
        cliente.direccion = request.POST.get('direccion', cliente.direccion)
        cliente.metodo_pago_preferido = request.POST.get('metodo_pago_preferido', cliente.metodo_pago_preferido)
        cliente.save()
        return redirect('ver_cliente')
    return redirect('ver_cliente')


def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_cliente')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})


# =====================================
# CRUD PEDIDO
# =====================================
def agregar_pedido(request):
    if request.method == "POST":
        id_cliente = request.POST.get('id_cliente')
        producto = request.POST.get('producto')
        estado = request.POST.get('estado')
        total = request.POST.get('total')
        direccion = request.POST.get('direccion')
        metodo_pago = request.POST.get('metodo_pago')

        if id_cliente:
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente)
            Pedido.objects.create(
                id_cliente=cliente,
                producto=producto,
                fecha_pedido=timezone.now().date(),
                estado=estado,
                total=total,
                direccion=direccion,
                metodo_pago=metodo_pago
            )
        return redirect('ver_pedido')

    clientes = Cliente.objects.all()
    return render(request, 'pedido/agregar_pedido.html', {'clientes': clientes})


def ver_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/ver_pedido.html', {'pedidos': pedidos})


def actualizar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id_pedido=id)
    clientes = Cliente.objects.all()
    return render(request, 'pedido/actualizar_pedido.html', {'pedido': pedido, 'clientes': clientes})


def realizar_actualizacion_pedido(request, id):
    pedido = get_object_or_404(Pedido, id_pedido=id)
    if request.method == "POST":
        pedido.producto = request.POST.get('producto', pedido.producto)
        pedido.estado = request.POST.get('estado', pedido.estado)
        pedido.total = request.POST.get('total', pedido.total)
        pedido.direccion = request.POST.get('direccion', pedido.direccion)
        pedido.metodo_pago = request.POST.get('metodo_pago', pedido.metodo_pago)
        id_cliente = request.POST.get('id_cliente')

        if id_cliente:
            pedido.id_cliente = get_object_or_404(Cliente, id_cliente=id_cliente)

        pedido.save()
        return redirect('ver_pedido')
    return redirect('ver_pedido')


def borrar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id_pedido=id)
    if request.method == 'POST':
        pedido.delete()
        return redirect('ver_pedido')
    return render(request, 'pedido/borrar_pedido.html', {'pedido': pedido})


# =====================================
# CRUD PRODUCTO
# =====================================
def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        tamaño = request.POST.get('tamaño')
        categoria = request.POST.get('categoria')
        disponibilidad = bool(request.POST.get('disponibilidad'))
        id_cliente = request.POST.get('id_cliente')

        cliente = None
        if id_cliente:
            cliente = get_object_or_404(Cliente, id_cliente=id_cliente)

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            tamaño=tamaño,
            categoria=categoria,
            disponibilidad=disponibilidad,
            fecha_creacion=timezone.now().date(),
            cliente=cliente
        )
        return redirect('ver_producto')

    clientes = Cliente.objects.all()
    return render(request, 'producto/agregar_producto.html', {'clientes': clientes})


def ver_producto(request):
    productos = Producto.objects.all().order_by('id_producto')
    return render(request, 'producto/ver_producto.html', {'productos': productos})


def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    clientes = Cliente.objects.all()
    return render(request, 'producto/actualizar_producto.html', {'producto': producto, 'clientes': clientes})


def realizar_actualizacion_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre', producto.nombre)
        producto.descripcion = request.POST.get('descripcion', producto.descripcion)
        producto.precio = request.POST.get('precio', producto.precio)
        producto.tamaño = request.POST.get('tamaño', producto.tamaño)
        producto.categoria = request.POST.get('categoria', producto.categoria)
        producto.disponibilidad = bool(request.POST.get('disponibilidad', producto.disponibilidad))

        id_cliente = request.POST.get('id_cliente')
        if id_cliente:
            producto.cliente = get_object_or_404(Cliente, id_cliente=id_cliente)

        producto.save()
        return redirect('ver_producto')
    return redirect('ver_producto')


def borrar_producto(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_producto')
    return render(request, 'producto/borrar_producto.html', {'producto': producto})
