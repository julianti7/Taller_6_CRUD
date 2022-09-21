from django.urls import path
from .views import home, contacto, galeria, agregar_producto, listar_productos, editar_producto, eliminar_producto

urlpatterns = [
    #En la raiz del sitio se cargará el home.html
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"), 
    #CRUD
    path('agregar-producto/',agregar_producto, name="agregar_producto"),
    path('listar-producto/',listar_productos, name="listar_productos"),
    path('editar-producto/<id>/',editar_producto, name="editar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto,name="eliminar_producto"),
]
