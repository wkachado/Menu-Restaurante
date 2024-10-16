from django.shortcuts import render
from App.models import *
from .forms import (
    Crear_Comida_forms, Crear_Categoria_forms, Crear_Adicional_forms,
    Crear_Guarnicion_forms, Crear_Bebida_forms, Crear_Postre_forms,
    Crear_CafeTe_forms, Crear_Mesa_forms, Crear_Pedido_forms
)

def mostrar_index(request):


    return render(request, 'App/index.html')

def mostrar_bebidas(request):
    
    bebida = Bebida.objects.all()

    context = {'bebida' :  bebida }

    return render(request,'App/Bebida.html', context=context)

def mostrar_comida(request):

    comida = Comida.objects.all()

    context = {'comida': comida}

    return render(request, 'App/Comida.html', context)

def mostrar_pedidos(request):

    pedido = Pedido.objects.all()

    context = {'pedido': pedido}

    return render(request, 'App/Pedido.html', context)


def mostrar_categoria(request):

    categoria = Categoria.objects.all()

    context = {'categoria': categoria}

    return render(request, 'App/Categoria.html', context)

def mostrar_guarnicion(request):
    
    guarnicion = Guarnicion.objects.all()

    context = {'guarnicion': guarnicion}

    return render(request, 'App/Guarnicion.html', context)

def mostrar_adicional(request):
    adicional = Adicional.objects.all()

    context = {'adicional': adicional}

    return render(request, 'App/Adicional.html', context)

def mostrar_cafe_te(request):

    cafete = CafeTe.objects.all()

    context = {'cafete': cafete}

    return render(request, 'App/Cafete.html', context)

def mostrar_mesas(request):

    mesa = Mesa.objects.all()

    context = {'mesa': mesa}

    return render(request, 'App/Mesa.html', context)

def mostrar_postres(request):

    postre = Postre.objects.all()

    context = {'postre': postre}

    return render(request, 'App/Postre.html', context)

def crear_comida(request):
    if request.method == 'POST':
        form = Crear_Comida_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            comida = Comida(nombre=formulario_limpio['nombre'], descripcion=formulario_limpio['descripcion'], 
                            precio=formulario_limpio['precio'], categoria=formulario_limpio['categoria'])
            comida.save()
            return render (request,'App/index.html')
    else:
        form = Crear_Comida_forms()
    return render(request, 'App/Crear_Comida.html', {'form': Crear_Comida_forms})

def crear_categoria(request):
    if request.method == 'POST':
        form = Crear_Categoria_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            categoria = Categoria(nombre=formulario_limpio['nombre'])
            categoria.save()
            return render(request,'App/index.html')
    else:
        form = Crear_Categoria_forms()
    return render(request, 'App/Crear_Categoria.html', {'form': Crear_Categoria_forms})

def crear_adicional(request):
    if request.method == 'POST':
        form = Crear_Adicional_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            adicional = Adicional(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'])
            adicional.save()
            return render(request,'App/index.html')
    else:
        form = Crear_Adicional_forms()
    return render(request, 'App/Crear_Adicional.html', {'form': Crear_Adicional_forms})

def crear_guarnicion(request):
    if request.method == 'POST':
        form = Crear_Guarnicion_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            guarnicion = Guarnicion(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'])
            guarnicion.save()
            return render(request,'App/index.html')
    else:
        form = Crear_Guarnicion_forms()
    return render(request, 'App/Crear_Guarnicion.html', {'form': Crear_Guarnicion_forms})

def crear_bebida(request):
    if request.method == 'POST':
        form = Crear_Bebida_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            bebida = Bebida(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'])
            bebida.save()
            return render(request,'App/index.html')
    else:
        form = Crear_Bebida_forms()
    return render(request, 'App/Crear_Bebida.html', {'form': Crear_Bebida_forms})

def crear_postre(request):
    if request.method == 'POST':
        form = Crear_Postre_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            postre = Postre(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'])
            postre.save()
            return render(request,'App/index.html')
    else:
        form = Crear_Postre_forms()
    return render(request, 'App/Crear_Postre.html', {'form': Crear_Postre_forms})

def crear_cafete(request):
    if request.method == 'POST':
        form = Crear_CafeTe_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            cafete = CafeTe(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'])
            cafete.save()
            return render(request,'App/index.html')
    else:
        form = Crear_CafeTe_forms()
    return render(request, 'App/Crear_Cafete.html', {'form': Crear_CafeTe_forms})

def crear_mesa(request):
    if request.method == 'POST':
        form = Crear_Mesa_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            mesa = Mesa(numero_mesa=formulario_limpio['numero_mesa'])
            mesa.save()
            return render(request,'App/index.html')
    else:
        form = Crear_Mesa_forms()
    return render(request, 'App/Crear_Mesa.html', {'form': Crear_Mesa_forms})

def crear_pedido(request):
    if request.method == 'POST':
        form = Crear_Pedido_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            pedido = Pedido(
                mesa=formulario_limpio['mesa'],
                plato_principal=formulario_limpio['plato_principal'],
                adicional_plato_principal=formulario_limpio['adicional_plato_principal'],
                guarnicion=formulario_limpio['guarnicion'],
                adicional_guarnicion=formulario_limpio['adicional_guarnicion'],
                bebida=formulario_limpio['bebida'],
                adicional_bebida=formulario_limpio['adicional_bebida'],
                postre=formulario_limpio['postre'],
                adicional_postre=formulario_limpio['adicional_postre'],
                cafe_te=formulario_limpio['cafe_te'],
                adicional_cafe_te=formulario_limpio['adicional_cafe_te'],
                entregado=formulario_limpio['entregado']
            )
            pedido.save()
            return render(request,'App/index.html')
    else:
        form = Crear_Pedido_forms()
    return render(request, 'App/Crear_Pedido.html', {'form': Crear_Pedido_forms})