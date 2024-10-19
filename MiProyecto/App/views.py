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

def buscar_comida(request):

    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        comida = Comida.objects.filter(nombre__icontains=nombre)

        return render(request, 'App/Buscar_Comida.html', {'comida': comida})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Comida.html', {'respuesta': respuesta})


def buscar_adicional(request):

    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        adicional = Adicional.objects.filter(nombre__icontains=nombre)

        return render(request, 'App/Buscar_Adicional.html', {'adicional': adicional})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Adicional.html', {'respuesta': respuesta})

def buscar_guarnicion(request):

    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        guarnicion = Guarnicion.objects.filter(nombre__icontains=nombre)

        return render(request, 'App/Buscar_Guarnicion.html', {'guarnicion': guarnicion})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Guarnicion.html', {'respuesta': respuesta})

def buscar_bebida(request):

    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        bebida = Bebida.objects.filter(nombre__icontains=nombre)

        return render(request, 'App/Buscar_Bebida.html', {'bebida': bebida})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Bebida.html', {'respuesta': respuesta})

def buscar_cafete(request):

    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        cafete = CafeTe.objects.filter(nombre__icontains=nombre)

        return render(request, 'App/Buscar_CafeTe.html', {'cafete': cafete})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_CafeTe.html', {'respuesta': respuesta})

def buscar_mesa(request):

    if request.GET.get('id', False):
        id = request.GET['id']
        mesa = Mesa.objects.filter(id__icontains=id)

        return render(request, 'App/Buscar_Mesa.html', {'mesa': mesa})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Mesa.html', {'respuesta': respuesta})


def buscar_categoria(request):

    if request.GET.get('nombre', False):
        categoria = request.GET['nombre']
        categoria = Categoria.objects.filter(nombre__icontains=categoria)

        return render(request, 'App/Buscar_Categoria.html', {'categoria': categoria})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Categoria.html', {'respuesta': respuesta})


def buscar_postre(request):

    if request.GET.get('nombre', False):
        postre = request.GET['nombre']
        postre = Postre.objects.filter(nombre__icontains=postre)

        return render(request, 'App/Buscar_Postre.html', {'postre': postre})
    else:
        respuesta ='No hay datos'
    return render(request, 'App/Buscar_Postre.html', {'respuesta': respuesta})


def buscar_pedido(request):
    if request.GET.get('pedido_id', False):
        pedido_id = request.GET['pedido_id']
        print(f"Buscando pedido con ID: {pedido_id}")
        pedidos = Pedido.objects.filter(id=pedido_id)

        print(f"Pedidos encontrados: {list(pedidos)}")
        return render(request, 'App/Buscar_Pedido.html', {'pedidos': pedidos})
    else:
        respuesta ='No hay datos'
        return render(request, 'App/Buscar_Pedido.html', {'respuesta': respuesta})





def actualizar_comida(request,comida_id):
    comida = Comida.objects.get(id=comida_id)
    if request.method == 'POST':
        form = Crear_Comida_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data

            comida.nombre= formulario_limpio['nombre']
            comida.precio= formulario_limpio['precio']
            comida.descripcion= formulario_limpio['descripcion']
            comida.categoria= formulario_limpio['categoria']

            comida.save()

            return render(request, 'App/index.html')

    else:
        form = Crear_Comida_forms(initial={'nombre': comida.nombre, 'nombre': comida.nombre})

    return render(request, 'App/Actualizar_Comida.html', {'form': Crear_Comida_forms})


def actualizar_bebida(request,bebida_id):
    bebida = Bebida.objects.get(id=bebida_id)
    if request.method == 'POST':
        form = Crear_Bebida_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            bebida.nombre= formulario_limpio['nombre']
            bebida.precio= formulario_limpio['precio']
            

            bebida.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Bebida_forms(initial={'nombre': bebida.nombre, 'precio': bebida.precio})

    return render(request, 'App/Actualizar_Bebida.html', {'form': Crear_Bebida_forms})

def actualizar_categoria(request,categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    if request.method == 'POST':
        form = Crear_Categoria_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            categoria.nombre= formulario_limpio['nombre']

            

            categoria.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Categoria_forms(initial={'nombre': categoria.nombre})

    return render(request, 'App/Actualizar_Categoria.html', {'form': Crear_Categoria_forms})

def actualizar_guarnicion(request,guarnicion_id):
    guarnicion = Guarnicion.objects.get(id=guarnicion_id)
    if request.method == 'POST':
        form = Crear_Guarnicion_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            guarnicion.nombre= formulario_limpio['nombre']
            guarnicion.precio= formulario_limpio['precio']
            

            guarnicion.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Guarnicion_forms(initial={'nombre': guarnicion.nombre, 'precio': guarnicion.precio})

    return render(request, 'App/Actualizar_Guarnicion.html', {'form': Crear_Guarnicion_forms})

def actualizar_adicional(request,adicional_id):
    adicional = Adicional.objects.get(id=adicional_id)
    if request.method == 'POST':
        form = Crear_Adicional_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            adicional.nombre= formulario_limpio['nombre']
            adicional.precio= formulario_limpio['precio']
            

            adicional.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Adicional_forms(initial={'nombre': adicional.nombre, 'precio': adicional.precio})

    return render(request, 'App/Actualizar_Adicional.html', {'form': Crear_Adicional_forms})

def actualizar_cafete(request,cafete_id):
    cafete = CafeTe.objects.get(id=cafete_id)
    if request.method == 'POST':
        form = Crear_CafeTe_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            cafete.nombre= formulario_limpio['nombre']
            cafete.precio= formulario_limpio['precio']
            

            cafete.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_CafeTe_forms(initial={'nombre': cafete.nombre, 'precio': cafete.precio})

    return render(request, 'App/Actualizar_CafeTe.html', {'form': Crear_CafeTe_forms})


def actualizar_postre(request,postre_id):
    postre = Postre.objects.get(id=postre_id)
    if request.method == 'POST':
        form = Crear_CafeTe_forms(request.POST)
        
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            
            postre.nombre= formulario_limpio['nombre']
            postre.precio= formulario_limpio['precio']
            

            postre.save()
            
            return render(request, 'App/index.html')
        
    else:
        form = Crear_Postre_forms(initial={'nombre': postre.nombre, 'precio': postre.precio})

    return render(request, 'App/Actualizar_Postre.html', {'form': Crear_Postre_forms})


def actualizar_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    if request.method == 'POST':
        form = Crear_Pedido_forms(request.POST)

        if form.is_valid():
            formulario_limpio = form.cleaned_data

            pedido.mesa = formulario_limpio['mesa']
            pedido.plato_principal = formulario_limpio['plato_principal']
            pedido.adicional_plato_principal = formulario_limpio['adicional_plato_principal']
            pedido.guarnicion = formulario_limpio['guarnicion']
            pedido.adicional_guarnicion = formulario_limpio['adicional_guarnicion']
            pedido.bebida = formulario_limpio['bebida']
            pedido.adicional_bebida = formulario_limpio['adicional_bebida']
            pedido.postre = formulario_limpio['postre']
            pedido.adicional_postre = formulario_limpio['adicional_postre']
            pedido.cafe_te = formulario_limpio['cafe_te']
            pedido.adicional_cafe_te = formulario_limpio['adicional_cafe_te']
            pedido.entregado = formulario_limpio['entregado']

            pedido.save()

            return render(request, 'App/index.html')

    else:
        form = Crear_Pedido_forms(initial={
            'mesa': pedido.mesa,
            'plato_principal': pedido.plato_principal,
            'adicional_plato_principal': pedido.adicional_plato_principal,
            'guarnicion': pedido.guarnicion,
            'adicional_guarnicion': pedido.adicional_guarnicion,
            'bebida': pedido.bebida,
            'adicional_bebida': pedido.adicional_bebida,
            'postre': pedido.postre,
            'adicional_postre': pedido.adicional_postre,
            'cafe_te': pedido.cafe_te,
            'adicional_cafe_te': pedido.adicional_cafe_te,
            'entregado': pedido.entregado
        })

    return render(request, 'App/Actualizar_Pedido.html', {'form': Crear_Pedido_forms})
def actualizar_mesa(request, id):
    mesa = Mesa.objects.get(id=id)
    if request.method == 'POST':
        form = Crear_Mesa_forms(request.POST)
        if form.is_valid():
            formulario_limpio = form.cleaned_data
            mesa.sector = formulario_limpio['sector']
            mesa.save()
            return render(request, 'App/index.html')
    else:
        form = Crear_Mesa_forms(initial={'sector': mesa.sector})
    
    return render(request, 'App/Actualizar_Mesa.html', {'form': Crear_Mesa_forms})




def eliminar_mesa(request,mesa_id):
    
    mesa = Mesa.objects.get(id=mesa_id)

    mesa.delete()

    mesa = mesa.objects.all()

    context = {'mesa': mesa}

    return render(request, 'App/index.html' ,context=context)



def eliminar_comida(request,comida_id):
    
    comida = Comida.objects.get(id=comida_id)

    comida.delete()

    comida = comida.objects.all()

    context = {'comida': comida}

    return render(request, 'App/index.html' ,context=context)


def eliminar_bebida(request,bebida_id):
    
    bebida = Bebida.objects.get(id=bebida_id)

    bebida.delete()

    bebida = bebida.objects.all()

    context = {'bebida': bebida}

    return render(request, 'App/index.html' ,context=context)

def eliminar_categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)

    categoria.delete()

    categorias = Categoria.objects.all()

    context = {'categorias': categorias}

    return render(request, 'App/index.html', context=context)

def eliminar_pedido(request, pedido_id):

    pedido = Pedido.objects.get(id=pedido_id)

    pedido.delete()

    pedido = pedido.objects.all()

    context = {'pedido': pedido}

    return render(request, 'App/index.html', context=context)

def eliminar_guarnicion(request, guarnicion_id):

    guarnicion = Guarnicion.objects.get(id=guarnicion_id)

    guarnicion.delete()

    guarnicion = guarnicion.objects.all()

    context = {'guarnicion': guarnicion}

    return render(request, 'App/index.html', context=context)

def eliminar_adicional(request, adicional_id):

    adicional= Adicional.objects.get(id=adicional_id)

    adicional.delete()

    adicional= adicional.objects.all()

    context = {'adicional': adicional}

    return render(request, 'App/index.html', context=context)


def eliminar_cafete(request, cafete_id):

    cafete= CafeTe.objects.get(id=cafete_id)

    cafete.delete()

    cafete= cafete.objects.all()

    context = {'cafete': cafete}

    return render(request, 'App/index.html', context=context)


def eliminar_postre(request, postre_id):

    postre= Postre.objects.get(id=postre_id)

    postre.delete()

    postre= postre.objects.all()

    context = {'postre': postre}

    return render(request, 'App/index.html', context=context)