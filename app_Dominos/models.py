from django.db import models

# MODELO: CLIENTE
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    metodo_pago_preferido = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# MODELO: PEDIDO
class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, db_column='id_cliente', related_name='pedidos'
    )
    producto = models.CharField(max_length=200)
    fecha_pedido = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    direccion = models.CharField(max_length=200)
    metodo_pago = models.CharField(max_length=100)

    def __str__(self):
        return f"Pedido #{self.id_pedido} - {self.producto}"


# MODELO: PRODUCTO
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    tamaño = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    disponibilidad = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, db_column='id_cliente', related_name='productos'
    )

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"
