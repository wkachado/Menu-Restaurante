from django.urls import path
from  App import views

urlpatterns = [
    path('', views.mostrar_index, name='Principal'),
    path('bebidas/', views.mostrar_bebidas, name='Bebidas'),
    path('comidas/', views.mostrar_comida, name='Comida'),
    path('pedidos/', views.mostrar_pedidos, name='Pedido'),
    path('categorias/', views.mostrar_categoria, name='Categoria'),
    path('guarniciones/', views.mostrar_guarnicion, name='Guarnicion'),
    path('CafeTe/', views.mostrar_cafe_te, name='CafeTe'),
    path('adicionales/', views.mostrar_adicional, name='Adicional'),
    path('mesas/', views.mostrar_mesas, name='Mesa'),
    path('postres/', views.mostrar_postres, name='Postre'),
    path('crear_bebidas/', views.crear_bebida, name='Crear Bebida'),
    path('crear_comida/',  views.crear_comida, name='Crear Comida'),
    path('crear_categoria/', views.crear_categoria, name='Crear Categoria'),
    path('crear_adicional/', views.crear_adicional, name='Crear Adicional'),
    path('crear_guarnicion/', views.crear_guarnicion, name='Crear Guarnicion'),
    path('crear_bebida/', views.crear_bebida, name='Crear Bebida'),
    path('crear_postre/', views.crear_postre, name='Crear Postre'),
    path('crear_cafete/', views.crear_cafete, name='Crear CafeTe'),
    path('crear_mesa/', views.crear_mesa, name='Crear Mesa'),
    path('crear_pedido/', views.crear_pedido, name='Crear Pedido'),
]