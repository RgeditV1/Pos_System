import customtkinter as ctk
#Aqui definimos la estructura de los widgets
class UIdraw:
    def __init__(self, padre):
        self.padre = padre
        self.root = ctk.CTkFrame(self.padre, fg_color="black")
        self.root.pack(fill="both", expand=True, pady=(1,1), padx=(1,1))
        self.root.pack_propagate(False) # No queremos que se expanda fuera del marco de la ventana

    def draw(self):
        self.header()
        self.center()
        self.footer()

    def header(self):
        self.main_frame = ctk.CTkFrame(self.root, height=65, border_width=1, border_color='gray', corner_radius=0)
        self.main_frame.pack(fill="x")

    def center(self):
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)

    def footer(self):
        self.main_frame = ctk.CTkFrame(self.root, height=65, border_width=1, border_color='gray', corner_radius=0)
        self.main_frame.pack(fill="x")