from .inventario import Inventario
class Producto(Inventario):
    def __init__(self):
        super().__init__()

    def buscar_producto(self, id_producto=None, descripcion=None, cantidad=None):
        resultado = super().buscar_producto(id_producto, descripcion)
        list_producto = list(resultado[:3]) # type: ignore
        cantidad = cantidad
        ag_cantidad = int
        if cantidad == "" and cantidad.isdigit() == False:
            ag_cantidad = 1 
        else:
            ag_cantidad = int(cantidad) # type: ignore
        
        sum_total = int(ag_cantidad + list_producto[2])
        list_producto.insert(3, ag_cantidad)
        list_producto.append(sum_total)

        return list_producto