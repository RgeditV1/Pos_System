'''ESTE MODULO ES UNICA Y EXCLUSIVAMENTE PARA ESTABLECER LAS INTERFACES Y DE MODIFICACIONES DE LAYOUTS Y WIDGETS
   DADO QUE SE UTILIZA QDESIGNER PARA GENERAR LAS UI, NO QUEREMOS MODIFICAR EL ARCHIVO PY GENERADO
   MEJOR MODIFICAMOS EXTERNAMENTE LOS ATRIBUTOS Y NO NOS METEMOS CON LOS MODULOS PY GENERADOS DE UI
'''
from PySide6.QtWidgets import QTableWidgetItem
from pos.modulos_ui.ventas import Ui_main
from pos.core.productos import Producto
import logging


logger = logging.getLogger(__name__)


class VENTA:
    def __init__(self, widget):
        self.ui_ventas = Ui_main()
        self.ui_ventas.setupUi(widget)
        self.consulta = Producto()
        self.__hacer_mods()
        self.__accion()

    def __accion(self):
        self.ui_ventas.agregar_articulo.clicked.connect(self.get_producto)

        #Enter Binding
        self.ui_ventas.entry_cantidad.returnPressed.connect(self.get_producto)
        self.ui_ventas.entry_producto.returnPressed.connect(self.get_producto)

    def __hacer_mods(self):
        self.__mod_tabla()

    def __mod_tabla(self):
        self.tabla = self.ui_ventas.tabla_widget
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Descripción",
                                         "Precio", "Cantidad", "Total"])
        self.tabla.setColumnWidth(1, 335)  # Columna "Descripción" con 300 px
        self.tabla.horizontalHeader().setStretchLastSection(True)

    
    def get_producto(self):
        self.id_input = self.ui_ventas.entry_producto
        self.cantidad_input = self.ui_ventas.entry_cantidad
        id_producto = self.id_input.text().strip()
        cantidad = self.cantidad_input.text().strip()

        logger.debug("Consulta de producto iniciada: id=%s, cantidad=%s", id_producto, cantidad)
        try:
            producto = self.consulta.buscar_producto(
                id_producto=id_producto,
                cantidad=cantidad
            )
            logger.info("Producto encontrado: %s", producto)
            self.set_producto(producto)
        except TypeError:
            if id_producto != '':
                logger.warning("ID no encontrado: %s", id_producto)
            else:
                logger.warning("Producto no encontrado: id vacio")
        except ValueError:
            logger.warning("Cantidad invalida para id=%s: %s", id_producto, cantidad)
        except Exception:
            logger.exception("Error inesperado al consultar producto")
        finally:
            self.id_input.clear()
            self.cantidad_input.clear()


    def _buscar_fila_por_id(self, id_producto):
        for fila in range(self.tabla.rowCount()):
            item_id = self.tabla.item(fila, 0)
            if item_id and item_id.text() == str(id_producto):
                return fila
        return None


    def set_producto(self, producto):
       estaba_ordenando = self.tabla.isSortingEnabled()
       self.tabla.setSortingEnabled(False)

       try:
           fila = self._buscar_fila_por_id(producto["id"])

           if fila is None:
               row = self.tabla.rowCount()
               self.tabla.insertRow(row)
               self.tabla.setItem(row, 0, QTableWidgetItem(str(producto["id"])))
               self.tabla.setItem(row, 1, QTableWidgetItem(str(producto["descripcion"])))
               self.tabla.setItem(row, 2, QTableWidgetItem(str(producto["precio"])))
               self.tabla.setItem(row, 3, QTableWidgetItem(str(producto["cantidad"])))
               self.tabla.setItem(row, 4, QTableWidgetItem(str(producto["total"])))
               return

           precio_item = self.tabla.item(fila, 2)
           cantidad_item = self.tabla.item(fila, 3)

           if precio_item is None or cantidad_item is None:
               logger.warning("Fila existente sin datos completos para id=%s", producto["id"])
               return

           precio_actual = float(precio_item.text())
           cantidad_actual = int(cantidad_item.text())
           cantidad_nueva = int(producto["cantidad"])
           cantidad_total = cantidad_actual + cantidad_nueva
           total_nuevo = precio_actual * cantidad_total

           self.tabla.setItem(fila, 3, QTableWidgetItem(str(cantidad_total)))
           self.tabla.setItem(fila, 4, QTableWidgetItem(str(total_nuevo)))
       finally:
           self.tabla.setSortingEnabled(estaba_ordenando)
