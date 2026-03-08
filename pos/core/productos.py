from .inventario import Inventario
from functools import wraps
import logging

logger = logging.getLogger(__name__)

'''USA  my_func.__doc__  o my_func.__name__ CON PRINT O HELP PARA OBTENER INFORMACION'''
class Producto(Inventario):
    def __init__(self):
        super().__init__()

    @staticmethod
    def devolver_producto(func): #Convertira la lista en un diccionario mas legible
        @wraps(func)
        def wrapper(*args, **kwargs):
            lista = func(*args, **kwargs)
            logger.debug("Convirtiendo producto a dict: %s", lista)
            conversor = {'id': lista[0],
                         'descripcion':lista[1],
                         'precio':lista[2],
                         'cantidad':lista[3],
                         'total':lista[4]}
            return conversor
        return wrapper

    @devolver_producto  
    def buscar_producto(self, id_producto=None, descripcion=None, cantidad=None) -> list:
        """
            Esta funcion se encarga de buscar el item en la base de datos y luego
            devolver una lista con el item
        """
        resultado = super().buscar_producto(id_producto, descripcion)
        if resultado is None:
            logger.warning("Producto no encontrado en DB: id=%s descripcion=%s", id_producto, descripcion)
            raise TypeError("Producto no encontrado")

        list_producto = list(resultado[:3]) # type:ignore  e.g: id,desc,precio

        cantidad_texto = str(cantidad or "").strip()
        if not cantidad_texto:
            ag_cantidad = 1
        elif not cantidad_texto.isdigit():
            logger.warning("Cantidad invalida recibida: %s", cantidad)
            raise ValueError("Cantidad invalida")
        else:
            ag_cantidad = int(cantidad_texto)
        
        total = int(ag_cantidad * list_producto[2])
        logger.debug(
            "Producto calculado id=%s precio=%s cantidad=%s total=%s",
            list_producto[0],
            list_producto[2],
            ag_cantidad,
            total
        )
        list_producto.append(ag_cantidad)
        list_producto.append(total)

        return list_producto

    def mostrar_productos(self):
        self.lista = super().mostrar_productos()
        self.columnas = ['id','descripcion','precio','stock','costo','mayoreo']
        # -> devuelve una lista de diccionarios
        self.resultado = [dict(zip(self.columnas, columna)) for columna in self.lista]
        
        return self.resultado