from django.urls import path
from app_Dominos import views

urlpatterns = [
    path('', views.inicio_dominos, name='inicio_dominos'),

    # --- CLIENTE ---
    path('cliente/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/ver/', views.ver_cliente, name='ver_cliente'),
    path('cliente/editar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('cliente/editar/realizar/<int:pk>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('cliente/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    # --- PEDIDO ---
    path('pedido/agregar/', views.agregar_pedido, name='agregar_pedido'),
    path('pedido/ver/', views.ver_pedido, name='ver_pedido'),
    path('pedido/actualizar/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('pedido/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_pedido, name='realizar_actualizacion_pedido'),
    path('pedido/borrar/<int:id>/', views.borrar_pedido, name='borrar_pedido'),

    # --- PRODUCTO ---
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/ver/', views.ver_producto, name='ver_producto'),
    path('producto/actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),
]
