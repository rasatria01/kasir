import customtkinter as ctk
class Card(ctk.CTkFrame):
    def __init__(self,parent,data, i):
        super().__init__(parent)
        self.parent = parent

        self.grid_columnconfigure(1,weight=1)

        self.nomer = ctk.CTkLabel(self,text=i)
        self.nomer.grid(row=0,column=0, sticky="w",padx=10,pady=10)

        self.hist = ctk.CTkLabel(self,text=data)
        self.hist.grid(row=0,column=1, sticky="w",padx=10,pady=10)