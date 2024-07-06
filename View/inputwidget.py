import customtkinter as ctk
class InputFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.grid_rowconfigure(0,weight=1)
        self.grid_rowconfigure(1,weight=1)
        self.grid_rowconfigure(2,weight=1)
        self.grid_rowconfigure(3,weight=1)
        self.grid_rowconfigure(4,weight=1)
        self.grid_rowconfigure(5,weight=1)
        self.grid_rowconfigure(6,weight=1)
        self.grid_rowconfigure(7,weight=1)
        self.columnconfigure(4,weight=1)
        
        self.code_label = ctk.CTkLabel(self, text="Enter Product Code:")
        self.code_label.grid(row=0, column=4, sticky="nsew", pady=5)

        self.code_entry = ctk.CTkEntry(self, width=100)
        self.code_entry.grid(row=1, column=4, pady=5)

        self.quantity_label = ctk.CTkLabel(self, text="Enter Quantity:")
        self.quantity_label.grid(row=2, column=4, sticky="nsew",pady=5)

        self.quantity_entry = ctk.CTkEntry(self, width=100)
        self.quantity_entry.grid(row=3, column=4, pady=5)

        self.add_to_cart_button = ctk.CTkButton(self, width=120, text="Add to Cart")
        self.add_to_cart_button.grid(row=4, column=4, pady=10)

        self.voucher_label = ctk.CTkLabel(self, text="Enter Voucher Code:")
        self.voucher_label.grid(row=5, column=4, sticky="nsew", pady=5)

        self.voucher_entry = ctk.CTkEntry(self, width=100)
        self.voucher_entry.grid(row=6, column=4, pady=5)

        self.apply_voucher_button = ctk.CTkButton(self, width=120, text="Apply Voucher")
        self.apply_voucher_button.grid(row=7, column=4, pady=10)
        