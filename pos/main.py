from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QVBoxLayout, QTabWidget, QWidget)
import logging
import os
from pos.modulos_ui.setup_ui import VENTA
from pos.core.logging_config import setup_logging


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

def main():
    env_level = os.getenv("POS_LOG_LEVEL", "INFO").upper()
    log_level = getattr(logging, env_level, logging.INFO)
    setup_logging(level=log_level)
    logger.info("Iniciando aplicacion POS")

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
