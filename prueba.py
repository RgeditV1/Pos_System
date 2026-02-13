import customtkinter

app = customtkinter.CTk()

notebook = customtkinter.CTkTabview(app)
notebook.pack(padx=10, pady=10, fill="both", expand=True)

# Crear pestañas
notebook.add("Tab1")
notebook.add("Tab2")

# Definir fuente
my_font = customtkinter.CTkFont(size=30, weight="bold")

# Cambiar tamaño y fuente de los botones de pestañas
for btn in notebook._segmented_button._buttons_dict.values():
    btn.configure(width=200, height=60, font=my_font)

app.mainloop()
