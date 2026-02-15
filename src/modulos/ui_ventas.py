import customtkinter as ctk

class UIVentas:
    def __init__(self, frame):
        self.root = frame
        self.draw()

    def draw(self):
        self.header()

    def botones_debajo(form):
        '''
            Esto es solo para no alargar la funcion de form, pero si hay una forma mejor implementa, estoy
            solo en este proyecto >(
        '''
        def wrapper(self, *args, **kwargs):
            try:
                # Ejecuta primero el formulario
                resultado = form(self, *args, **kwargs)

                # Luego crea el frame de botones debajo
                self.buttons = ctk.CTkFrame(self.header_frame, fg_color='transparent')
                self.buttons.pack(pady=10, padx=10, fill='x')

                self.btn_widget = {}
                botones = ['Agregar Articulos', 'Eliminar Articulo',
                           'Editar Articulo', 'Limpiar Lista', 'Buscar Inventario']
                for texto in botones:
                    btn = ctk.CTkButton(self.buttons, text=texto, height=40)
                    btn.pack(padx=(10,10), side='left')

                    self.btn_widget[texto]= btn

                return resultado

            except Exception as err:
                print(f'Error en decorador botones: {err}')

        return wrapper


    @botones_debajo
    def form(self):

        self.formulario = ctk.CTkFrame(self.header_frame, fg_color='transparent')
        self.formulario.pack(pady=(5,5), expand=True, fill='both')

        labels = ['Cliente:', 'Producto:', 'Cantidad:', 'Stock:', 'Nro. de Factura:']

        self.widgets = {}  # para guardar referencias

        for i, texto in enumerate(labels):

            fila = i // 2
            columna_label = (i % 2) * 2      # 0 o 2
            columna_widget = columna_label + 1  # 1 o 3

            # Label principal
            lbl = ctk.CTkLabel(self.formulario, text=texto, font=('Roboto', 20))
            lbl.grid(row=fila, column=columna_label, padx=10, pady=10, sticky="w")

            # ---- Crear widget según el tipo ----
            if texto == "Cliente:":
                widget = ctk.CTkComboBox(self.formulario, values=["Cliente 1", "Cliente 2"], width=200)
            
            elif texto == "Producto:":
                widget = ctk.CTkEntry(self.formulario, placeholder_text='Buscar ID', width=300)
            
            elif texto == "Cantidad:":
                widget = ctk.CTkEntry(self.formulario)
            
            elif texto == "Stock:":
                widget = ctk.CTkLabel(self.formulario, text="0", font=('Roboto', 20))
            
            elif texto == "Nro. de Factura:":
                widget = ctk.CTkLabel(self.formulario, text="0000", font=('Roboto', 20))

            widget.grid(row=fila, column=columna_widget, padx=10, pady=10, sticky="w")

            self.widgets[texto] = widget  # guardamos referencia


    def header(self):
        self.header_frame = ctk.CTkFrame(self.root, corner_radius=1, border_width=1)
        self.header_frame.pack(padx=(5,5), pady=(5,5))
        self.header_frame.pack_propagate(True)
        self.form()