import customtkinter as ctk
#Aqui definimos la estructura de los widgets
class UIdraw:
    def __init__(self, padre):
        self.padre = padre
        self.root = ctk.CTkFrame(self.padre, fg_color="black")
        self.root.pack(fill="both", expand=True, pady=(1,1), padx=(1,1))
        self.root.pack_propagate(False)
    def draw(self):
        self.header()
        self.center()
        self.footer()

    def header(self):
        self.main_frame = ctk.CTkFrame(self.root, height=65)
        self.main_frame.pack(fill="x")

        #Botones

        self.pestañas = ['Ventas', 'Inventario', 'Clientes', 'Proveedor', 'Pedidos', 'Informacion']
        for nombre in self.pestañas:
            text = nombre
            btn = ctk.CTkButton(self.main_frame, text=text, font=('Roboto',25),
                                        height=25, corner_radius=1,
                                        border_width=1, fg_color='#1976D2', bg_color='black')
            btn.pack(side='left', padx=(1,1), pady=(2,2), fill='x', expand=True)


    def center(self):
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=0)
        self.main_frame.pack(fill="both", expand=True)

    def footer(self):
        self.main_frame = ctk.CTkFrame(self.root, height=65, border_width=1, border_color='gray', corner_radius=0)
        self.main_frame.pack(fill="x")