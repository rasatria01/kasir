import customtkinter as ctk
class Header(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        self.parent = parent

        self.title_label = ctk.CTkLabel(self, text="Kasir", font=("Helvetica",20))
        self.title_label.pack(pady=10)

        self.datetime_label = ctk.CTkLabel(self, text="", font=("Helvetica",12))
        self.datetime_label.pack(pady=5)