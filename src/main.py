from modulos.ui_ventas import UIVentas
import customtkinter as ctk

class Manager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False,False)
        self.title("Punto De Venta A&L")

        self.ventas = UIVentas(self)
        self.ventas.draw()


if __name__ == "__main__":
    app = Manager()
    app.mainloop()