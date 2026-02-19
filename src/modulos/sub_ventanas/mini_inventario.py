import customtkinter as ctk
from CTkTreeview import CTkTreeview # type: ignore


def abrir_busqueda(root):
    ventana = ctk.CTkToplevel(root)
    ventana.title('busqueda de productos')
    ventana.geometry('600x500')
    ventana.propagate(False)
    ventana.resizable(False,False)
    ventana.lift()
    ventana.grab_set()
    ventana.focus_force()
    cabecera(ventana)
    contenido(ventana)

def cabecera(ventana):
    frame_cabecera = ctk.CTkFrame(ventana, height=30, corner_radius=1)
    frame_cabecera.pack(pady=(0,5), fill='x')

    lbl = ctk.CTkLabel(frame_cabecera, text='Busqueda', fg_color='#80F2B5',
                       font=('Roboto', 25), text_color='white')
    lbl.pack(pady=(3,3), padx=(3,3), fill='x', expand=True)

    busqueda = ctk.CTkEntry(frame_cabecera, placeholder_text='Buscar Producto', corner_radius=1)
    busqueda.pack(fill='x', padx=(5,5), pady=(5,5))

def contenido(ventana):
    contenido = ctk.CTkFrame(ventana, fg_color='gray')
    contenido.pack(fill='both', expand=True)
    contenido.pack_propagate(False)

    tabla = CTkTreeview(contenido, columns=['Descripcion','Precio Venta'], show='headings')
    tabla.pack(pady=(5,5) , padx=(5,5))

    with tabla.headings() as th:
        th.text('Descripcion','Descripcion del Producto')
        th.text('Precio Venta','Precio de Venta')
    
    tabla.column('Descripcion',width=400)
    tabla.column('Precio Venta', anchor='e')