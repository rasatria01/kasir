import tkinter as tk
from tkinter import ttk
from datetime import datetime
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

store_details = {
    "store_name": "Jaya Store",
    "address": "Solo, Central Java",
    "phone": "0822-8836-9966",
    "email": "info@jayastore.com",
}

vcode = {"hehehe":0.2,"betatest":0.5,"DISCOUNT10":0.1,"PROMO66":0.6}

class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class ShoppingCartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        cart_item = ShoppingCartItem(product, quantity)
        self.items.append(cart_item)

    def calculate_total(self):
        total = sum(item.product.price * item.quantity for item in self.items)
        return total

    def calculate_tax(self, total):
        tax_rate = 0.11  # 8% tax rate (adjust as needed)
        tax = total * tax_rate
        return tax

    def reset_cart(self):
        self.items = []

class CashierApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kasir") # Set the width and height of the window

        self.products = [
            Product("C01", "Tissu", 9900),
            Product("C02", "Lifebuoy", 20900),
            Product("C03", "Sunsilk", 28900),
            Product("C04", "Downy", 14300),
            Product("C05", "Molto", 9900),
            Product("C06", "Harpic", 21200),
            Product("C07", "Rinso", 10900),
            Product("C08", "Sunlight", 10900),
            Product("C09", "Baygon", 25900),
            Product("C10", "Hit", 34900),
            Product("M01", "Sari Roti", 18000),
            Product("M02", "Pop Mie", 5500),
            Product("M03", "Mie Gaga", 5800),
            Product("M03", "La Fonte", 7800),
            Product("M04", "Sarimi", 3300),
            Product("M05", "Lemonilo", 6800),
            Product("M06", "Mie Sedap", 2800),
            Product("M07", "Potabee", 7900),
            Product("M08", "Tango", 8800),
            Product("M09", "Pringles", 20500),
            Product("M10", "Sukro", 8300),
            Product("D01", "Mogu Mogu", 11200),
            Product("D02", "Crystalin", 2900),
            Product("D03", "Aqua", 3800),
            Product("D04", "Le Minerale", 3600),
            Product("D05", "Teh Botol", 5500),
            Product("D06", "Freshtea", 5500),
            Product("D06", "Javana", 3200),
            Product("D06", "Javana", 3200),
            Product("D07", "Indomilk", 7900),
            Product("D08", "Cimory", 7000),
            Product("D09", "Frisian Flag", 7500),
            Product("D10", "Nescafe", 7500),
            # Add more products as needed
        ]

        self.shopping_cart = ShoppingCart()
        
        

        self.main_frame = ctk.CTkFrame(master)
        self.main_frame.pack(fill=ctk.BOTH,expand=True)

        self.header_frame = ctk.CTkFrame(self.main_frame)
        self.header_frame.pack(fill=ctk.X,pady=5)
        
        self.title_label = ctk.CTkLabel(self.header_frame,text="Kasir", font=("Helvetica", 20))
        self.title_label.pack(pady=10)

        self.datetime_label = ctk.CTkLabel(self.header_frame, text="", font=("Helvetica", 12))
        self.datetime_label.pack(pady=5)

        self.update_datetime()

        self.content_frame = ctk.CTkFrame(self.main_frame)
        self.content_frame.pack(fill=ctk.BOTH,pady=5, expand=True)
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_columnconfigure(2, weight=1)

        self.table_frame = ctk.CTkFrame(self.content_frame)
        self.table_frame.grid(row=1,column=0, sticky="w",pady=5,padx=5)
        
        self.product_label = ctk.CTkLabel(self.table_frame, text="Available Items:")
        self.product_label.pack(fill=ctk.X,pady=5)
        self.create_table(self.table_frame, self.products)

        self.cart_frame = ctk.CTkFrame(self.content_frame)
        self.cart_frame.grid(row=1,column=1, sticky="w",pady=5,padx=5)

        self.input_frame = ctk.CTkFrame(self.content_frame)
        self.input_frame.grid(row=1,column=2,sticky="e",padx=5,pady=5)

        self.cart_label = ctk.CTkLabel(self.cart_frame, text="Shopping Cart:")
        self.cart_label.pack(fill=ctk.X,pady=5)

        # self.cart_listbox = ctk.Listbox(self.cart_frame, width=50)  # Set the width of the Listbox
        # self.cart_listbox.pack(fill=ctk.BOTH,pady=5)
        
        self.code_label = ctk.CTkLabel(self.input_frame, text="Enter Product Code:")
        self.code_label.grid(row=0, column=4, sticky="w", pady=5)

        self.code_entry = ctk.CTkEntry(self.input_frame, width=100)
        self.code_entry.grid(row=1, column=4, pady=5)

        self.quantity_label = ctk.CTkLabel(self.input_frame, text="Enter Quantity:")
        self.quantity_label.grid(row=2, column=4, sticky="w", pady=5)

        self.quantity_entry = ctk.CTkEntry(self.input_frame, width=100)
        self.quantity_entry.grid(row=3, column=4, pady=5)

        self.add_to_cart_button = ctk.CTkButton(self.input_frame,width=120, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.grid(row=4, column=4, pady=10)

        self.voucher_label = ctk.CTkLabel(self.input_frame, text="Enter Voucher Code:")
        self.voucher_label.grid(row=5, column=4, sticky="w", pady=5)

        self.voucher_entry = ctk.CTkEntry(self.input_frame, width=100)
        self.voucher_entry.grid(row=6, column=4, pady=5)

        self.apply_voucher_button = ctk.CTkButton(self.input_frame,width=120, text="Apply Voucher", command=self.apply_voucher)
        self.apply_voucher_button.grid(row=7, column=4, pady=10)

        self.footer_frame = ctk.CTkFrame(self.main_frame)
        self.footer_frame.pack(fill=ctk.BOTH,pady=5, expand=True)
        self.footer_frame.columnconfigure(0,weight=1)
        self.footer_frame.columnconfigure(1,weight=1)
        self.footer_frame.columnconfigure(2,weight=1)
        self.footer_frame.columnconfigure(3,weight=1)
        self.footer_frame.columnconfigure(4,weight=1)

        self.total_label = ctk.CTkLabel(self.footer_frame, text="Total: Rp 0.00")
        self.total_label.grid(row=0, column=0, sticky="nsew", pady=5)

        self.tax_label = ctk.CTkLabel(self.footer_frame, text="Tax(11%): Rp 0.00")
        self.tax_label.grid(row=1, column=0, sticky="nsew", pady=5)

        self.discount_label = ctk.CTkLabel(self.footer_frame, text="Discount: Rp 0.00")
        self.discount_label.grid(row=0, column=3, sticky="nsew", pady=5)

        self.final_total_label = ctk.CTkLabel(self.footer_frame, text="Final Total: Rp 0.00")
        self.final_total_label.grid(row=0, column=4, sticky="nsew", pady=5)

        self.payment_label = ctk.CTkLabel(self.footer_frame, text="Enter Payment:")
        self.payment_label.grid(row=1, column=4, sticky="nsew", pady=5)

        self.payment_entry = ctk.CTkEntry(self.footer_frame, width=100)
        self.payment_entry.grid(row=2, column=4, pady=5)

        self.check_payment_button = ctk.CTkButton(self.footer_frame,width=120 ,text="Check Payment", command=self.check_payment)
        self.check_payment_button.grid(row=3, column=4, pady=10)

        self.cart_table = self.create_table_cart(self.cart_frame, self.shopping_cart.items)

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

    def create_table_cart(self,parent, data):
    # Create a Treeview widget
        style = ttk.Style(parent)
        style.configure("Treeview",fieldground="#212942")
        tree =  ttk.Treeview(parent, columns=("Name", "QTY", "Price"),style="Treeview",selectmode="browse")
        tree.tag_configure("back")
        
        # Define columns
        tree.heading("#0", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("QTY", text="QTY")
        tree.heading("Price", text="Price")

        # Insert data into the table
        for i,item in enumerate(data, start=1):
            tree.insert("", "end", iid=i,values=( item.product.name, item.quantity, item.product.name*item.quantity))

        # Set column widths
        tree.column('#0',width=0,stretch="no")
        tree.column("Name", width=150)
        tree.column("QTY", width=50)
        tree.column("Price", width=150)

        # Pack the Treeview widget
        tree.pack(expand=True, fill="both",side=ctk.LEFT)
        verscrll = ttk.Scrollbar(parent,orient='vertical',command=tree.yview)
        verscrll.pack(side=ctk.RIGHT,fill=ctk.Y)
        tree.configure(xscrollcommand=verscrll.set)
        return tree
    
    def update_cart_table(self,tree,new_data):
        for item in tree.get_children():
            tree.delete(item)

        for i,item in enumerate(new_data, start=1):
            tree.insert("", "end", iid=i,values=( item.product.name, item.quantity, f'Rp. {item.product.price*item.quantity:,.2f}'))


    def update_datetime(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.datetime_label.configure(text=current_datetime)
        self.master.after(1000, self.update_datetime)  # Schedule the next update


    def add_to_cart(self):
        code = self.code_entry.get()
        quantity = int(self.quantity_entry.get())

        selected_product = self.find_product_by_code(code)
        if selected_product:
            self.shopping_cart.add_item(selected_product, quantity)
            self.update_cart()

    def apply_voucher(self):
        voucher_code = self.voucher_entry.get()
        
        disc= vcode.get(voucher_code)
        self.voucher_entry.delete(0,999)
        if disc != None:
            CTkMessagebox(title="Voucher Used",message=f"{voucher_code} used, get {(disc*100):.0f}% discount")
            self.update_cart(discount=disc)
            return 
        CTkMessagebox(title="Invalid Voucher",icon='cancel', message="Invalid voucher code. No discount applied.")

    def find_product_by_code(self, code):
        for product in self.products:
            if product.code == code:
                return product
        return None

    def update_cart(self, discount=0):
        # self.cart_listbox.delete(0, tk.END)
        self.total = self.shopping_cart.calculate_total()
        self.tax = self.shopping_cart.calculate_tax(self.total)
        self.discount = self.total*discount # Ensure the discount does not exceed the total
        self.update_cart_table(self.cart_table, self.shopping_cart.items)
        # for item in self.shopping_cart.items:
        #     self.cart_listbox.insert(tk.END, f"{item.product.name} - Quantity: {item.quantity} - ${item.product.price * item.quantity:.2f}")

        self.total_label.configure(text=f"Total: Rp. {self.total:,.2f}")
        self.tax_label.configure(text=f"Tax(11%): Rp. {self.tax:,.2f}")
        self.discount_label.configure(text=f"Discount: Rp. {self.discount:,.2f}")
        self.code_entry.delete(0,999)
        self.quantity_entry.delete(0,999)
        self.final_total = self.total + self.tax - self.discount
        self.final_total_label.configure(text=f"Final Total: Rp. {self.final_total:,.2f}")


    def create_receipt_item(self, frame, product, price, quantity):
        item_frame = ctk.CTkFrame(frame)
        item_frame.pack(fill=ctk.X, pady=5)

        # Product
        product_label = ctk.CTkLabel(item_frame, text=product, font=("Arial", 12))
        product_label.pack(side=ctk.LEFT, anchor=ctk.W, padx=5)
        
        total_label = ctk.CTkLabel(item_frame, text=f"Rp. {(quantity*price):10,.2f}", font=("Arial", 12))
        total_label.pack(side=ctk.RIGHT, anchor=ctk.E)

        # Quantity
        quantity_label = ctk.CTkLabel(item_frame, text=f"Qty: {quantity}", font=("Arial", 12))
        quantity_label.pack(side=ctk.RIGHT, anchor=ctk.E, padx=5)
        # Price
        price_label = ctk.CTkLabel(item_frame, text=price, font=("Arial", 12))
        price_label.pack(side=ctk.RIGHT, anchor=ctk.E,padx=5)



    def create_store_details(self, frame):
        store_frame = ctk.CTkFrame(frame)
        store_frame.pack(fill=ctk.X, pady=5)

        store_name_label = ctk.CTkLabel(store_frame,font=("Arial", 18,"bold"),text=store_details["store_name"])
        store_name_label.pack()

        address_label = ctk.CTkLabel(store_frame, text=store_details["address"], font=("Arial", 10))
        address_label.pack()

        phone_label = ctk.CTkLabel(store_frame, text=f"Phone: {store_details['phone']}", font=("Arial", 10))
        phone_label.pack()

        email_label = ctk.CTkLabel(store_frame, text=f"Email: {store_details['email']}", font=("Arial", 10))
        email_label.pack(pady=5)

    def create_widget_receipt(self,test,name):
        receipt_frame = ctk.CTkFrame(test)
        receipt_frame.pack(fill=ctk.BOTH, expand= True, padx=10,pady=10)
        self.create_store_details(receipt_frame)
        info_frame = ctk.CTkFrame(receipt_frame)
        info_frame.pack(fill=ctk.X)
        consum_label = ctk.CTkLabel(info_frame, text=f'Consumen: {name}',font=("Arial",14))
        consum_label.pack(side=ctk.LEFT,anchor=ctk.W)

        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_label = ctk.CTkLabel(info_frame,text=current_datetime,font=("Arial", 14))
        date_label.pack(side=ctk.RIGHT)

        header_label = ctk.CTkLabel(receipt_frame, text="Receipt", font=("Arial", 20, "bold"))
        header_label.pack(pady=10)
        item_frame = ctk.CTkScrollableFrame(receipt_frame,width=350)
        item_frame.pack(pady=5)
        for item in self.shopping_cart.items:
            self.create_receipt_item(item_frame, item.product.name , item.product.price, item.quantity)

        ctk.CTkFrame(receipt_frame, height=1, width=380, bg_color="black").pack(pady=5)
        subtotal_label = ctk.CTkLabel(receipt_frame, text=f"Subtotal: Rp. {self.total:,}.00", font=("Arial", 12))
        subtotal_label.pack( anchor=ctk.E)

        tax_label = ctk.CTkLabel(receipt_frame, text=f"Tax (11%): Rp. {self.tax:,.2f}", font=("Arial", 12))
        tax_label.pack( anchor=ctk.E)

        discount_label = ctk.CTkLabel(receipt_frame, text=f"Discount: Rp. {self.discount:,.2f}", font=("Arial", 12))
        discount_label.pack(anchor=ctk.E)

        total_label = ctk.CTkLabel(receipt_frame, text=f"Total: Rp. {(self.tax+self.total-self.discount):,.2f}", font=("Arial", 14, "bold"))
        total_label.pack(pady=10, anchor=ctk.E)

        paymentt_label = ctk.CTkLabel(receipt_frame, text=f"Payment: Rp. {self.paymentmoney:,.2f}", font=("Arial", 14, "bold"))
        paymentt_label.pack(pady=5, anchor=ctk.E)

        changee_label = ctk.CTkLabel(receipt_frame, text=f"Change: Rp. {(self.paymentmoney-(self.tax+self.total-self.discount)):,.2f}", font=("Arial", 12, "bold"))
        changee_label.pack(pady=5, anchor=ctk.E)

    def create_receipt(self):
        # Use tkinter.simpledialog to get customer's name
        inputname = ctk.CTkInputDialog(title="Customer Name", text="Enter customer's name:")
        customer_name = inputname.get_input()
        if not customer_name:
            CTkMessagebox(title="Missing Information", message="Please enter customer's name.",icon='warning')
            return
        test = ctk.CTkToplevel(self.master)
        test.title("Receipt")
        self.create_widget_receipt(test,customer_name)
    

    def check_payment(self):
        # Check if the shopping cart is empty
        if not self.shopping_cart.items:
            CTkMessagebox(title="Empty Cart", message="Please add items to the cart before checking out.",icon='warning')
            return

        # Use tkinter.simpledialog to confirm the payment
        confirm_payment = CTkMessagebox(title="Confirm Payment", message="Are you sure you want to proceed with the payment?",icon='question',option_2="Yes",option_1="No",cancel_button_color="red")
        response = confirm_payment.get()
        if response =="Yes":
            try:
                self.paymentmoney =int(self.payment_entry.get())
                self.payment_entry.delete(0,999) 
                if self.paymentmoney >= self.final_total:
                    self.create_receipt()
                    self.shopping_cart.reset_cart()
                    self.update_cart(discount=0)
                else:
                    CTkMessagebox(title="Insufficient Payment",icon='cancel',message=f"Insufficient payment.\nNeed Rp. {(self.final_total-self.paymentmoney):,.2f} more.")
            except ValueError:
                CTkMessagebox(title="Invalid Input",icon='cancel',message="Please enter a valid numeric payment amount.")
        else:
            CTkMessagebox(title="Payment Cancelled", message="The payment has been cancelled.")




if __name__ == "__main__":
    ctk.deactivate_automatic_dpi_awareness()
    ctk.set_default_color_theme("dark-blue")
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    bg_color = root._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
    text_color = root._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
    selected_color = root._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

    treestyle = ttk.Style()
    treestyle.theme_use('default')
    treestyle.configure("Treeview",background=bg_color, foreground=text_color,fieldbackground=bg_color,borderwidth=0)
    treestyle.map('Treeview',background=[('selected',bg_color)],foreground=[('selected',selected_color)])
    root.bind("<<TreeviewSelect>>", lambda event: root.focus_set())
    app = CashierApp(root)
    root.mainloop()
