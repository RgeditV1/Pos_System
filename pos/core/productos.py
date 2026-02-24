from .inventario import Inventario
class Producto(Inventario):
    def __init__(self):
        super().__init__()

    def buscar_producto(self, id_producto=None, descripcion=None, cantidad=None):
        resultado = super().buscar_producto(id_producto, descripcion)
        list_producto = list(resultado[:3]) # type:ignore  e.g: id,desc,precio

        cantidad = cantidad #especificado por el usuario
        ag_cantidad = int
        if cantidad == "" and cantidad.isdigit() == False: # type: ignore
            ag_cantidad = 1 #cantidad por defecto
        else:
            ag_cantidad = cantidad
        
        total = int(ag_cantidad * list_producto[2])
        list_producto.append(ag_cantidad)
        list_producto.append(total)

        return list_producto