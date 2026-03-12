from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QVBoxLayout, QTabWidget, QWidget)
import logging
import os
import sys
import traceback
from pos.modulos_ui.ventas.ventas_view import VENTA
from pos.core.logging_config import setup_logging
from .__init__ import parsedOptions

logger = logging.getLogger(__name__)
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,650)
        self.setWindowTitle('Punto De Venta')

        self.names = {'Venta':QWidget(), #Tabs
                      'Inventario':QWidget(),
                      'Cliente':QWidget(),
                      'Factura':QWidget(),
                      'Corte':QWidget(),
                      'Reportes':QWidget(),
                      'Configuracion':QWidget()
                      }
        
        self.__main_widget = QWidget() #algo asi como el frame principal para los que usen tkinter
        self.__main_layout = QVBoxLayout(self.__main_widget) #contenedor vertical para las tabs
        self.__tabs = QTabWidget()
        self.__main_layout.addWidget(self.__tabs)
        self.setCentralWidget(self.__main_widget)

        self.__add_tabs()
        self.__setup_venta_tab()


    def __add_tabs(self): # creamos las tabs
        for (name,tab) in self.names.items():
            self.__tabs.addTab(tab, name)

    def __setup_venta_tab(self): # Crear instancia de la UI generada
        self.interfaz_venta = VENTA(self.names['Venta'])

def main(argv=None):
    argv = sys.argv
    if len(argv) > 1:
        argv.pop(0) #el primer argumento es el script mismo
        parsedOptions(argv)

    env_level = os.getenv("POS_LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, env_level, logging.INFO)
    setup_logging(level=log_level)
    logger.info("Iniciando aplicacion POS")
    logger.info(
        "Entorno de ejecucion: frozen=%s executable=%s cwd=%s",
        getattr(sys, "frozen", False),
        sys.executable,
        os.getcwd(),
    )

    def _capturar_excepcion(tipo, valor, tb):
        detalle = "".join(traceback.format_exception(tipo, valor, tb))
        logger.critical("Excepcion no controlada:\n%s", detalle)

    sys.excepthook = _capturar_excepcion

    try:
        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec()
    except Exception:
        logger.exception("Error critico al iniciar la interfaz principal")
        raise


if __name__ == "__main__":
    main()
