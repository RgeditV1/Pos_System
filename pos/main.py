from PySide6.QtWidgets import (QApplication, QMainWindow, 
                               QVBoxLayout, QTabWidget, QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200,650)
        self.setWindowTitle('Punto De Venta')

        self.names = {'Venta':QWidget(),
                      'Inventario':QWidget(),
                      'Cliente':QWidget(),
                      'Factura':QWidget(),
                      'Corte':QWidget(),
                      'Reportes':QWidget(),
                      'Configuracion':QWidget()
                      }
        self._main_widget = QWidget()
        self._main_layout = QVBoxLayout(self._main_widget)
        self._tabs = QTabWidget()
        self._main_layout.addWidget(self._tabs)
        self.setCentralWidget(self._main_widget)
        self._add_tabs()

    def _add_tabs(self):
        for (name,tab) in self.names.items():
            self._tabs.addTab(tab, name)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()