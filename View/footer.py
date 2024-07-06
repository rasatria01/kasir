import customtkinter as ctk
class Footer(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1,weight=1)
        self.grid_columnconfigure(2,weight=1)
        self.grid_columnconfigure(3,weight=1)
        self.grid_columnconfigure(4,weight=1)

        self.total_label = ctk.CTkLabel(self,text="Total: Rp 0.00")
        self.total_label.grid(row=0, column=0, sticky="nsew", pady=5)

        self.tax_label = ctk.CTkLabel(self,text="Tax(11%): Rp 0.00")
        self.tax_label.grid(row=0, column=3, sticky="nsew", pady=5)

        self.discount_label = ctk.CTkLabel(self, text="Discount: Rp 0.00" )
        self.discount_label.grid(row=1, column=0, sticky="nsew", pady=5)

        self.final_total_label = ctk.CTkLabel(self, text="Final Total: Rp 0.00")
        self.final_total_label.grid(row=0, column=4, sticky="nsew", pady=5)

        self.payment_label = ctk.CTkLabel(self, text="Enter Payment:" )
        self.payment_label.grid(row=1, column=4, sticky="nsew", pady=5)
        
        self.payment_entry = ctk.CTkEntry(self, width=100)
        self.payment_entry.grid(row=2,column=4,pady=10)

        self.check_payment_button = ctk.CTkButton(self,width=120 ,text="Check Payment")
        self.check_payment_button.grid(row=3, column=4, pady=10)

    