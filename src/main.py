from modulos.ui_draw import UIdraw
import customtkinter as ctk

class Manager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x720")
        self.resizable(False,False)
        self.title("Punto De Venta A&L")

        UIdraw(self)

if __name__ == "__main__":
    app = Manager()
    app.mainloop()