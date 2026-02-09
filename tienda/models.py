from django.db import models

# Create your models here.

from django.db import models

# 1 Usuario/Cliente
class Usuario(models.Model):
    nombre = models.CharField(max_length=15)
    correo_electronico = models.TextField(unique=True)
    contraseña = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField()

    def __str__(self):
        return self.nombre
    
# 2 Perfil del usuario/cliente
class Perfil_Usuario(models.Model):
    nombre_usuario=models.CharField(max_length=15, unique=True)
    biografia=models.CharField(max_length=200)
    telefono=models.CharField(max_length=9)
    direccion=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_usuario
    
# 3 Prenda de ropa
class Prenda (models.Model):
    TALLAS = [
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
    ]
  
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)
    precio=models.DecimalField(max_digits=8,decimal_places=2)
    talla=models.CharField(max_length=3, choices=TALLAS)

# 4 Marca/Creador/Vendedor
class Marca (models.Model):
    nombre=models.CharField(max_length=20 ,unique=True)
    pais_origen=models.CharField(max_length=100, blank=True)
    descripcion=models.TextField(blank=True)
    año_fundacion=models.PositiveIntegerField(null=True,blank=True)#Que es esto??

# 5 Cesta
class Cesta (models.Model):
    fecha_creacion=models.DateTimeField()
    activo=models.BooleanField()
    objetos_en_cesta=models.IntegerField()
    total=models.FloatField()

# 6 Inventario
class Inventario (models.Model):
    cantidad_disponible=models.PositiveIntegerField(default=0)
    ubicacion_almacen=models.CharField(max_length=255,blank=True)
    stock_minimo=models.PositiveIntegerField(default=1)
    stock_maximo=models.PositiveIntegerField(default=100)

# 7 Pedido
class Pedido (models.Model):
    ESTADOS = [
        ('PEND', 'Pendiente'),
        ('PROC', 'Procesando'),
        ('ENV', 'Enviado'),
        ('ENT', 'Entregado'),
    ]
        
    fecha=models.DateTimeField(auto_now_add=True)
    total=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    estado=models.CharField(max_length=4,choices=ESTADOS, default='PEND')
    direccion_envio = models.CharField(max_length=255)

# 8 Detalle_Pedido
class Detalle_Pedido (models.Model):
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

# 9 Descuento
class Descuento (models.Model):
    codigo=models.CharField(max_length=20 , unique=True)
    porcentaje=models.DecimalField(max_digits=5 , decimal_places=2)
    activo=models.BooleanField(default=True)
    fecha_expiracion=models.DateField()

# 10 Opinion/Reseña
class Opinion (models.Model):
    clasificacion=models.PositiveIntegerField()
    comentario=models.TextField(blank=True)
    fecha=models.DateField(auto_now_add=True)
    recomendado=models.BooleanField(default=True)