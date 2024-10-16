from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Adicional(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class Comida(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    precio = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    adicional = models.ForeignKey(Adicional, on_delete=models.SET_NULL, blank=True, null=True)  # Solo un adicional

    def __str__(self):
        return f'{self.nombre} - {self.categoria.nombre}'

class Guarnicion(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    adicional = models.ForeignKey(Adicional, on_delete=models.SET_NULL, blank=True, null=True)  # Solo un adicional

    def __str__(self):
        return self.nombre

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    adicional = models.ForeignKey(Adicional, on_delete=models.SET_NULL, blank=True, null=True)  # Solo un adicional

    def __str__(self):
        return self.nombre

class Postre(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    adicional = models.ForeignKey(Adicional, on_delete=models.SET_NULL, blank=True, null=True)  # Solo un adicional

    def __str__(self):
        return self.nombre

class CafeTe(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    adicional = models.ForeignKey(Adicional, on_delete=models.SET_NULL, blank=True, null=True)  # Solo un adicional

    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    numero_mesa = models.IntegerField()

    def __str__(self):
        return f'Mesa {self.numero_mesa}'

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    plato_principal = models.ForeignKey(Comida, on_delete=models.CASCADE)
    guarnicion = models.ForeignKey(Guarnicion, on_delete=models.SET_NULL, blank=True, null=True)  # Opcional
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    postre = models.ForeignKey(Postre, on_delete=models.SET_NULL, blank=True, null=True)  # Opcional
    cafe_te = models.ForeignKey(CafeTe, on_delete=models.SET_NULL, blank=True, null=True)  # Opcional
    fecha_pedido = models.DateTimeField(default=timezone.now)
    total = models.FloatField(default=0.0)
    entregado = models.BooleanField(default=False)

    def calcular_total(self):
        # Sumar el precio de los productos y su adicional si existe
        total = self.plato_principal.precio + \
            (self.guarnicion.precio if self.guarnicion else 0) + \
            self.bebida.precio + \
            (self.postre.precio if self.postre else 0) + \
            (self.cafe_te.precio if self.cafe_te else 0)
        
        # Sumar el precio del adicional si existe en cada producto
        if self.plato_principal.adicional:
            total += self.plato_principal.adicional.precio
        if self.guarnicion and self.guarnicion.adicional:
            total += self.guarnicion.adicional.precio
        if self.bebida.adicional:
            total += self.bebida.adicional.precio
        if self.postre and self.postre.adicional:
            total += self.postre.adicional.precio
        if self.cafe_te and self.cafe_te.adicional:
            total += self.cafe_te.adicional.precio

        return total

    def save(self, *args, **kwargs):
        # Calcula el total automáticamente antes de guardar
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        estado_entrega = "Entregado" if self.entregado else "No entregado"
        return f'Pedido en Mesa {self.mesa.numero_mesa} - Total: {self.total} - {estado_entrega}'
