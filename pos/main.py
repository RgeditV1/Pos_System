from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QVBoxLayout, QTabWidget, QWidget)
from ui_mod import Mod
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
        
        self._main_widget = QWidget() #algo asi como el frame principal para los que usen tkinter
        self._main_layout = QVBoxLayout(self._main_widget) #contenedor vertical para las tabs
        self._tabs = QTabWidget()
        self._main_layout.addWidget(self._tabs)
        self.setCentralWidget(self._main_widget)

        self._add_tabs()
        self._setup_venta_tab()


    def _add_tabs(self): # creamos las tabs
        for (name,tab) in self.names.items():
            self._tabs.addTab(tab, name)

    def _setup_venta_tab(self): # Crear instancia de la UI generada
        Mod(self.names['Venta'])

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()