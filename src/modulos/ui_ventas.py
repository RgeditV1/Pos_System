import customtkinter as ctk

class UIVentas:
    def __init__(self, frame):
        self.root = frame
        self.draw()

    def draw(self):
        self.header()

    def header(self):
        self.header_frame = ctk.CTkFrame(self.root, width=1000, height=200, corner_radius=1, border_width=1)
        self.header_frame.pack(padx=(5,5), pady=(5,5))