import customtkinter as ctk
import modulos.sub_ventanas.mini_inventario as mini_inventario
from CTkTreeview import CTkTreeview # pyright: ignore[reportPrivateImportUsage]
from core.productos import Producto

class UIVentas:
    def __init__(self, frame):
        self.root = frame
        self.dibujar()

    def dibujar(self):
        self.cabecera()
        self.contenido()

    def cabecera(self):
        self.header_frame = ctk.CTkFrame(self.root, corner_radius=1, border_width=1)
        self.header_frame.pack(padx=(5,5), pady=(5,5))
        self.form()

    def contenido(self):
        self.contenido_frame = ctk.CTkFrame(self.root, fg_color='transparent')
        self.contenido_frame.pack()
        self.tabla()

#Inicio de la definicion de notificaciones---------------------------
    def mostrar_info(self, text:str):
        noti = ctk.CTkToplevel()
        noti.overrideredirect(True)  # Quita bordes y barra de título
        #noti.geometry("250x80")
        noti.attributes("-topmost", True)  # Siempre encima

        label = ctk.CTkLabel(noti, text=text, fg_color="orange", bg_color="#2b2b2b")
        label.pack(expand=True, fill='both')

        # Cerrar automáticamente después de 3 segundos
        noti.after(3000, noti.destroy)

#Fin de la definicion de notificaciones------------------------------
    def accion_btn(self, btn: dict):
        btn['Agregar Articulos'].configure(command=lambda:self.agregar_producto())
        btn['Eliminar Articulo'].configure(command=lambda:self.eliminar_producto())
        btn['Buscar Inventario'].configure(command=lambda:self.buscar_inventario())
    
    @staticmethod
    def botones_debajo(form):
        '''
            Esto es solo para no alargar la funcion de form, pero si hay una forma mejor implementa, estoy
            solo en este proyecto >(
        '''
        def wrapper(self):
            try:
                # Ejecuta primero el formulario
                resultado = form(self)

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
                
                self.accion_btn(self.btn_widget)

                return resultado

            except Exception as err:
                print(f'Error en decorador botones: {err}')

        return wrapper

    def cambiar_texto(self, texto): #Nota: usare para cambiar el texto de factura y stock dinamicamente
        return ctk.StringVar(value=str(texto))

    @botones_debajo
    def form(self):
        '''
        Aqui esta todo el formulario de ventas donde iran los labels para cliente, producto etc..
        junto con sus respectivos entry
        '''
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
                widget.bind('<Return>', self.agregar_producto)
            
            elif texto == "Cantidad:":
                widget = ctk.CTkEntry(self.formulario)
            
            elif texto == "Stock:":
                widget = ctk.CTkLabel(self.formulario, textvariable=self.cambiar_texto('0'), font=('Roboto', 20))
            
            elif texto == "Nro. de Factura:":
                widget = ctk.CTkLabel(self.formulario, textvariable=self.cambiar_texto('000'), font=('Roboto', 20))

            widget.grid(row=fila, column=columna_widget, padx=10, pady=10, sticky="w")

            self.widgets[texto] = widget  # guardamos referencia

    @staticmethod
    def mod_tabla(tabla):
        def wrapper(self):
            tabla(self)
            with self.tabla.headings() as th:
                for texto in self.cabeceras:
                    th.text(texto, texto)

            # Configurar columnas con ancho y alineación
            for ca in self.cabeceras:
                if ca == 'id':
                    self.tabla.column(ca, width=70, anchor="center")
                elif ca == 'descripcion':
                    self.tabla.column(ca, width=450, anchor="w")
                else:
                    self.tabla.column(ca, width=100, anchor="e")
        return wrapper


    @mod_tabla                    
    def tabla(self):
        '''
        Aqui se define como sera la tabla donde se insertaran los datos de factura
        '''
        self.cabeceras = ['id', 'descripcion', 'precio', 'cantidad', 'total']
        self.tabla = CTkTreeview(self.contenido_frame, width=10, height=15,
                                 columns=self.cabeceras, show='headings') # type: ignore
        self.tabla.pack(pady=(3,5)) # type: ignore
        self.tabla.bind('<Delete>', self.eliminar_producto) # pyright: ignore[reportAttributeAccessIssue]
    
    #pasales None a los events para que sea opcional usar el teclado, si no te tira error jaja
    def agregar_producto(self, event=None): #añade productos a la tabla
        try:
            cantidad = self.widgets['Cantidad:'].get()
            id = self.widgets['Producto:'].get()
            producto = Producto().buscar_producto(id_producto=id, cantidad=cantidad)
            # para evaluar cada vez que se añada un item nuevo
            for item in self.tabla.get_children(): # type: ignore
                #e.g item id en tabla == item id por agregar = no agregar item nuevo
                if self.tabla.item(item, 'values')[0] == producto[0]:#type: ignore 
                    return  
            self.tabla.insert("", 'end', values=producto) # type: ignore
        except Exception as err:
            print(f"error: {err}")
            self.mostrar_info(text='Producto no encontrado.\nInserte un id y una cantidad valida')

    def eliminar_producto(self, event=None): # solo elimina el item de la tabla, no del inventario XD
        try:
            seleccion = self.tabla.selection() # type: ignore
            self.tabla.delete(seleccion) # type: ignore
        except:
            print('Seleccione un item')

    def buscar_inventario(self):
        mini_inventario.abrir_busqueda(self.root)