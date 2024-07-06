from tkinter import ttk
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox 
class ContentController:
    def __init__(self, model, product, view,disc):
        self.model= model
        self.product = product
        self.view= view
        self.disc = disc
        self._bind()
        self.prodTable = self.create_table(self.view.tableFrame,self.product)
        self.cartTable = self.createCartTable(self.view.cartFrame,self.model.items)
        self.model.add_event_listener("CART_CHANGED", self.changeCart)

    def _bind(self):
        self.view.inputFrame.add_to_cart_button.configure(command=self.add_to_cart)
        self.view.inputFrame.apply_voucher_button.configure(command=self.apply_voucher)

    def findProductByCode(self,code):
        for product in self.product:
            if product.code == code.upper():
                return product
            
        return None

    def changeCart(self,data):
        self.update_cart_table(self.cartTable,data.items)


    def add_to_cart(self):
        code =  self.view.inputFrame.code_entry.get()
        quantity = int(self.view.inputFrame.quantity_entry.get())
        self.view.inputFrame.code_entry.delete(0,999)
        self.view.inputFrame.quantity_entry.delete(0,999)
        selected_product = self.findProductByCode(code)
        if selected_product:
            self.model.add_item(selected_product, quantity)
    
    def apply_voucher(self):
        voucher_code = self.view.inputFrame.voucher_entry.get()
        disc = self.disc.get(voucher_code)
        self.view.inputFrame.voucher_entry.delete(0,999)
        if disc !=None:
            CTkMessagebox(title="Voucher Used",message=f"{voucher_code} used, get {(disc*100):.0f}% discount")
            self.model.calculate_disc(disc)
            return
        CTkMessagebox(title="Invalid Voucher",icon='cancel', message="Invalid voucher code. No discount applied.")
        
    def update_cart_table(self,tree,new_data):
        for item in tree.get_children():
            tree.delete(item)

        for i,item in enumerate(new_data, start=1):
            tree.insert("", "end", iid=i,values=( item.product.name, item.quantity, f'Rp. {item.product.price*item.quantity:,.2f}'))


    def createCartTable(self, parent, data):
        style = ttk.Style(parent)
        style.configure("Treeview",fieldground="#212942")
        tree = ttk.Treeview(parent, columns=("Name", "QTY","Price"), style="Treeview",selectmode="browse")
        tree.tag_configure("back")

        tree.heading("#0", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("QTY", text="QTY")
        tree.heading("Price", text="Price")

        for i,item in enumerate(data, start=1):
            tree.insert("", "end", iid=i,values=( item.product.name, item.quantity, item.product.name*item.quantity))

        # Set column widths
        tree.column('#0',width=0,stretch="no")
        tree.column("Name", width=150)
        tree.column("QTY", width=50)
        tree.column("Price", width=150)

        # Pack the Treeview widget
        tree.pack(expand=True, fill=ctk.BOTH,side=ctk.LEFT)
        verscrll = ttk.Scrollbar(parent,orient='vertical',command=tree.yview)
        verscrll.pack(side=ctk.RIGHT,fill=ctk.Y)
        tree.configure(xscrollcommand=verscrll.set)
        return tree
    
    def create_table(self,parent, data):
    # Create a Treeview widget
        tree =  ttk.Treeview(parent, columns=("Code", "Name", "Price"),selectmode="browse")

        # Define columns
        tree.heading("#0", text="ID")
        tree.heading("Code", text="Code")
        tree.heading("Name", text="Name")
        tree.heading("Price", text="Price")

        # Insert data into the table
        for i,item in enumerate(data, start=1):
            tree.insert("", "end", iid=i,values=( item.code, item.name, f'Rp. {item.price:,.2f}'))

        # Set column widths
        tree.column("#0", width=0, stretch="no")
        tree.column("Code", width=50)
        tree.column("Name", width=150)
        tree.column("Price", width=150)
        
        # Pack the Treeview widget
        tree.pack(expand=True, fill=ctk.BOTH,side=ctk.LEFT)
        verscrll = ttk.Scrollbar(parent,orient='vertical',command=tree.yview)
        verscrll.pack(side=ctk.RIGHT, fill=ctk.BOTH)
        tree.configure(xscrollcommand=verscrll.set)