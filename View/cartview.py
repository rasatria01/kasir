from .inputwidget import InputFrame
import customtkinter as ctk
class ContentView(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.tableFrame = ctk.CTkFrame(self, width=300)
        self.tableFrame.grid(row=1,column=0, sticky="nsew", padx=5,pady=5)

        self.product_label = ctk.CTkLabel(self.tableFrame, text="Available Items:")
        self.product_label.pack(fill=ctk.X,pady=5)
        
        self.cartFrame = ctk.CTkFrame(self,width=300)
        self.cartFrame.grid(row=1, column=1, sticky="nsew", padx=5,pady=5)

        self.cart_label = ctk.CTkLabel(self.cartFrame, text="Shopping Cart:")
        self.cart_label.pack(fill=ctk.X,pady=5)

        self.inputFrame = InputFrame(self)
        self.inputFrame.grid(row=1,column=2, sticky="nsew", padx=10,pady=5)