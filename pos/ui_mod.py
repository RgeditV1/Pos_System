'''ESTE MODULO ES UNICA Y EXCLUSIVAMENTE PARA USO DE MODIFICACIONES DE LAYOUTS Y WIDGETS
   DADO QUE SE UTILIZA QDESIGNER PARA GENERAR LAS UI, NO QUEREMOS MODIFICAR EL ARCHIVO PY GENERADO
   MEJOR MODIFICAMOS EXTERNAMENTE LOS ATRIBUTOS Y NO NOS METEMOS CON LOS MODULOS PY GENERADOS DE UI
'''
from modulos.ventas import Ui_main


class Mod:
    def __init__(self, widget):
        self.ui_ventas = Ui_main()
        self.ui_ventas.setupUi(widget)
        self.__do_mods()

    def __do_mods(self):
        self._mod_tabla()

    def _mod_tabla(self):
        tabla = self.ui_ventas.tabla_widget
        tabla.setColumnCount(5)
        tabla.setHorizontalHeaderLabels(["ID", "Descripción",
                                         "Precio", "Cantidad", "Total"])
        tabla.setColumnWidth(1, 335)  # Columna "Descripción" con 300 px
