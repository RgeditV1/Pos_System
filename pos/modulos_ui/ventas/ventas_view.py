'''
LOS MODULOS VIEW SOLO SERAN PARA ESTABLECER SU UI Y HACER MODIFICACIONES
'''
import logging
from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QTableWidgetItem, QAbstractItemView
from .ventas_ui import Ui_main
from pos.core.productos import Producto


logger = logging.getLogger(__name__)


class VENTA:
    def __init__(self, widget):
        self.widget = widget
        self.ui_ventas = Ui_main()
        self.ui_ventas.setupUi(self.widget)
        self.consulta = Producto()
        self.__hacer_mods()
        self.__accion()
        self._itbis_rate = 0.18 #en un futuro hare que esto puede variar manualmente
        self._mostrar_itbis = False           # label itbis_nro queda en 0
        self._aplicar_itbis_en_total = False  # total no suma itbis por ahora
        self._itbis_calculado = 0.0



    def __accion(self):
        self.ui_ventas.agregar_articulo.clicked.connect(self.get_producto)
        self.ui_ventas.eliminar_articulo.clicked.connect(self.__eliminar_articulo)
        self.ui_ventas.limpiar_lista.clicked.connect(self.__limpiar_tabla)
        self.ui_ventas.editar_articulo.clicked.connect(self.__editar_articulo)
        
        self.tabla.itemChanged.connect(self.__modificar_item)


        #Enter Binding
        self.ui_ventas.entry_cantidad.returnPressed.connect(self.get_producto)
        self.ui_ventas.entry_producto.returnPressed.connect(self.get_producto)
        
        #Delete Binding
        self.shortcut_delete = QShortcut(QKeySequence("Delete"), self.widget) # type: ignore
        self.shortcut_delete.activated.connect(self.__eliminar_articulo)

    def __editar_articulo(self) -> None:
        fila = self.tabla.currentRow()
        if fila < 0:
            logger.info("No hay fila seleccionada para editar")
            return

        item_cantidad = self.tabla.item(fila, 3)
        if item_cantidad is None:
            logger.warning("No se encontro celda de cantidad en fila=%s", fila)
            return

        self.tabla.setCurrentItem(item_cantidad)
        self.tabla.editItem(item_cantidad) # este es el metodo que te permite modificar la celda

    def __hacer_mods(self):
        self.__mod_tabla()

    def __mod_tabla(self):
        self.tabla = self.ui_ventas.tabla_widget
        self.tabla.setColumnCount(5)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)  # type: ignore
        #para la seleccoin de una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection) # type: ignore
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

    def __formato_moneda(self, valor: float) -> str: #Formato Latino mis panas
        base = f"{valor:,.2f}"
        return base.replace(",", "X").replace(".", ",").replace("X", ".")

    def __parse_moneda(self, texto: str) -> float: # entrada de texto a num para calculos
        texto_limpio = texto.strip().replace(".", "").replace(",", ".")
        return float(texto_limpio)


    def __recalcular_totales(self):
        subtotal = 0.0
        for fila in range(self.tabla.rowCount()):
            item_total = self.tabla.item(fila, 4)
            if item_total is None:
                continue
            try:
                subtotal += self.__parse_moneda(item_total.text())
            except ValueError:
                logger.warning("Total invalido en fila=%s valor=%s", fila, item_total.text())

        itbis = subtotal * self._itbis_rate
        self._itbis_calculado = itbis

        itbis_mostrado = itbis if self._mostrar_itbis else 0.0
        total_general = subtotal + (itbis if self._aplicar_itbis_en_total else 0.0)

        self.ui_ventas.sub_nro.setText(self.__formato_moneda(subtotal))
        self.ui_ventas.itbis_nro.setText(self.__formato_moneda(itbis_mostrado))
        self.ui_ventas.total_nro.setText(self.__formato_moneda(total_general))

    def __crear_item(self, valor: str, editable: bool = False) -> QTableWidgetItem:
        item = QTableWidgetItem(valor)
        flags = Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled
        if editable:
            flags |= Qt.ItemFlag.ItemIsEditable
        item.setFlags(flags)
        return item

    def __modificar_item(self, item: QTableWidgetItem) -> None:
        # Para modificar el item, especificamente la cantidad
        if item.column() != 3: # Si la columna seleccionada no es cantidad(colum 3), no hacer nada
            return

        fila = item.row()
        precio_item = self.tabla.item(fila, 2)
        if precio_item is None: # obviamente si no hay precio el item no es valido, es obligatorio
            return

        texto_cantidad = item.text().strip()
        if not texto_cantidad.isdigit() or int(texto_cantidad) <= 0:
            logger.warning("Cantidad invalida en fila=%s valor=%s", fila, texto_cantidad)
            cantidad = 1
        else:
            cantidad = int(texto_cantidad)

        try:
            precio = self.__parse_moneda(precio_item.text())
        except ValueError:
            logger.warning("Precio invalido en fila=%s valor=%s", fila, precio_item.text())
            return

        total_nuevo = precio * cantidad
        estaba_ordenando = self.tabla.isSortingEnabled()
        self.tabla.blockSignals(True)
        self.tabla.setSortingEnabled(False)
        try:
            if item.text() != str(cantidad):
                item.setText(str(cantidad))

            total_item = self.tabla.item(fila, 4)
            if total_item is None:
                self.tabla.setItem(fila, 4, self.__crear_item(self.__formato_moneda(total_nuevo)))
            else:
                total_item.setText(self.__formato_moneda(total_nuevo))
                total_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        finally:
            self.tabla.setSortingEnabled(estaba_ordenando)
            self.tabla.blockSignals(False)

        self.__recalcular_totales()
    
    def _buscar_fila_por_id(self, id_producto):
        """esto servira como filtro contra los id repetidos"""
        for fila in range(self.tabla.rowCount()):
            item_id = self.tabla.item(fila, 0)
            if item_id and item_id.text() == str(id_producto):
                return fila
        return None


    def set_producto(self, producto):
       estaba_ordenando = self.tabla.isSortingEnabled()
       self.tabla.blockSignals(True)
       self.tabla.setSortingEnabled(False)

       try:
           fila = self._buscar_fila_por_id(producto["id"])

           if fila is None: # osea que no hay un id repetido pues jaja
               row = self.tabla.rowCount()
               self.tabla.insertRow(row)
               self.tabla.setItem(row, 0, self.__crear_item(str(producto["id"])))
               self.tabla.setItem(row, 1, self.__crear_item(str(producto["descripcion"])))
               self.tabla.setItem(row, 2, self.__crear_item(self.__formato_moneda(float(producto["precio"]))))
               self.tabla.setItem(row, 3, self.__crear_item(str(producto["cantidad"]), editable=True))
               self.tabla.setItem(row, 4, self.__crear_item(self.__formato_moneda(float(producto["total"]))))
           else:
               precio_item = self.tabla.item(fila, 2)
               cantidad_item = self.tabla.item(fila, 3)

               if precio_item is None or cantidad_item is None:
                   # realmente es poco probable que se active esto, pues siempre se agregara un 1, pero por si acaso
                   logger.warning("Fila existente sin datos completos para id=%s", producto["id"])
                   return

               precio_actual = self.__parse_moneda(precio_item.text())
               cantidad_actual = int(cantidad_item.text())
               cantidad_nueva = int(producto["cantidad"])
               cantidad_total = cantidad_actual + cantidad_nueva
               total_nuevo = precio_actual * cantidad_total

               cantidad_item.setText(str(cantidad_total))
               total_item = self.tabla.item(fila, 4)
               if total_item is None:
                   self.tabla.setItem(fila, 4, self.__crear_item(self.__formato_moneda(total_nuevo)))
               else:
                   total_item.setText(self.__formato_moneda(total_nuevo))
                   total_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
       finally:
           self.tabla.setSortingEnabled(estaba_ordenando)
           self.tabla.blockSignals(False)

       self.__recalcular_totales()
    
    def __eliminar_articulo(self):
        fila = self.tabla.currentRow()
        if fila < 0:
            logger.info('No Hay Fila Seleccionada Para Eliminar')
            return
        self.tabla.removeRow(fila)
        self.__recalcular_totales()

    def __limpiar_tabla(self):
        if self.tabla.rowCount() > 0:
            self.tabla.setRowCount(0)
            self.__recalcular_totales()
            return
        else:
            logger.info('No Hay Items para elimiminar')
