import customtkinter as ctk
from modulos.ui_ventas import UIVentas
class UIdraw:
    def __init__(self, padre):
        self.padre = padre
        self.root = ctk.CTkFrame(self.padre)
        self.root.pack(fill="both", expand=True, pady=(0,0))
        self.pestaña = {}
        self.pestañas = ['Ventas', 'Inventario', 'Clientes', 'Proveedor', 'Pedidos', 'Informacion']
        self.draw()


    def draw(self):
        self.contenido()
        self.footer()

    @staticmethod #si no lo tuviera, tendria que ponerle self y seria un quilombo
    def tab_conf(func): #Configuramos las tabs, una fucion solo para esto
        def wrapper(self):
            func(self)
            fuente = ctk.CTkFont(family='Roboto',size=25, weight="bold")
            # Cambiar tamaño y fuente de los botones de pestañas
            for btn in self.frame_tab._segmented_button._buttons_dict.values():
                btn.configure(width=25, height=25, font=fuente)
        return wrapper

    @tab_conf
    def tabs(self):
        for tab in self.pestañas:
            self.pestaña[tab] = self.frame_tab.add(tab)
        self.frame_tab.set('Ventas') #Tab por defecto


    def contenido(self):
        self.frame_tab = ctk.CTkTabview(self.root, corner_radius=5)
        self.frame_tab.pack(fill='both', expand=True,pady=(0,0))
        self.frame_tab.pack_propagate(False)
        self.tabs()

        UIVentas(self.pestaña['Ventas'])
        



    def footer(self):
        self.footer_frame = ctk.CTkFrame(self.root, height=65, border_width=1, border_color='gray', corner_radius=0)
        self.footer_frame.pack(fill="x")