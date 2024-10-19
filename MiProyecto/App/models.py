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


    def __str__(self):
        return f'{self.nombre} - {self.categoria.nombre}'

class Guarnicion(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()


    def __str__(self):
        return self.nombre

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()


    def __str__(self):
        return self.nombre

class Postre(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre

class CafeTe(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()


    def __str__(self):
        return self.nombre


    def __str__(self):
        return self.nombre

class Mesa(models.Model):
    numero_mesa = models.IntegerField()
    sector= models.CharField(max_length=50)

    def __str__(self):
        return f'Mesa {self.numero_mesa} - Sector{self.sector}'

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    
    plato_principal = models.ForeignKey(Comida, on_delete=models.CASCADE)
    adicional_plato_principal = models.ForeignKey(Adicional, related_name='adicionales_plato', blank=True, null=True, on_delete=models.SET_NULL)
    guarnicion = models.ForeignKey(Guarnicion, on_delete=models.SET_NULL, blank=True, null=True) 
    adicional_guarnicion = models.ForeignKey(Adicional, related_name='adicionales_guarnicion', blank=True, null=True, on_delete=models.SET_NULL)
    bebida = models.ForeignKey(Bebida, on_delete=models.CASCADE)
    adicional_bebida = models.ForeignKey(Adicional, related_name='adicionales_bebida', blank=True, null=True, on_delete=models.SET_NULL)
    postre = models.ForeignKey(Postre, on_delete=models.SET_NULL, blank=True, null=True) 
    adicional_postre = models.ForeignKey(Adicional, related_name='adicionales_postre', blank=True, null=True, on_delete=models.SET_NULL)
    cafe_te = models.ForeignKey(CafeTe, on_delete=models.SET_NULL, blank=True, null=True)  
    adicional_cafe_te = models.ForeignKey(Adicional, related_name='adicionales_cafe_te', blank=True, null=True, on_delete=models.SET_NULL)
    fecha_pedido = models.DateTimeField(default=timezone.now)
    total = models.FloatField(default=0.0)
    entregado = models.BooleanField(default=False)

    def calcular_total(self):
        # Sumar el precio de los productos
        total = self.plato_principal.precio + \
                (self.guarnicion.precio if self.guarnicion else 0) + \
                self.bebida.precio + \
                (self.postre.precio if self.postre else 0) + \
                (self.cafe_te.precio if self.cafe_te else 0)

        # Sumar los adicionales seleccionados para cada producto
        if self.adicional_plato_principal:
            total += self.adicional_plato_principal.precio
        if self.adicional_guarnicion:
            total += self.adicional_guarnicion.precio
        if self.adicional_bebida:
            total += self.adicional_bebida.precio
        if self.adicional_postre:
            total += self.adicional_postre.precio
        if self.adicional_cafe_te:
            total += self.adicional_cafe_te.precio

        return total

    def save(self, *args, **kwargs):
        # Calcula el total automáticamente antes de guardar
        self.total = self.calcular_total()
        super().save(*args, **kwargs)

    def __str__(self):
        estado_entrega = "Entregado" if self.entregado else "No entregado"
        return f'Pedido en Mesa {self.mesa.numero_mesa} - Total: {self.total} - {estado_entrega}'

