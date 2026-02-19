from modulos.ui_draw import UIdraw
import customtkinter as ctk

class Manager(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x720")
        self.title("Punto De Venta A&L")
        self.resizable(False,False)

        ctk.set_default_color_theme('green')
        ctk.set_appearance_mode('light')

        UIdraw(self)

if __name__ == "__main__":
    app = Manager()
    app.mainloop()