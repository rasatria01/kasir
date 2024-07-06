from CTkMessagebox import CTkMessagebox 

class FooterController:
    def __init__(self,cart,view,hist):
        self.cart = cart
        self.view = view
        self.hist = hist
        self.cart.add_event_listener("CART_CHANGED", self.update)
        self.view.check_payment_button.configure(command=self.apply_button)

    def update(self,data):
        self.updateValue(data)

    def apply_button(self):
        if not self.cart.items:
            CTkMessagebox(title="Missing Information", message="Please enter customer's name.",icon='warning')
            return
        
        confirm_payment = CTkMessagebox(title="Confirm Payment", message="Are you sure you want to proceed with the payment?",icon='question',option_2="Yes",option_1="No",cancel_button_color="red")
        response = confirm_payment.get()
        if response =="Yes":
            try:
                payment = int(self.view.payment_entry.get())
                self.view.payment_entry.delete(0,999)
                if payment >= self.cart.total*(1-self.cart.disc):
                    self.hist.add_item(self.cart.items)
                    self.cart.reset_cart()
                else:
                    CTkMessagebox(title="Insufficient Payment",icon='cancel',message=f"Insufficient payment.\nNeed Rp. {((self.cart.total*(1-self.cart.disc))-payment):,.2f} more.")
            except ValueError:
                CTkMessagebox(title="Invalid Input",icon='cancel',message="Please enter a valid numeric payment amount.")
        else:
            CTkMessagebox(title="Payment Cancelled", message="The payment has been cancelled.")

    def updateValue(self,data):
        self.view.total_label.configure(text=f"Total: Rp. {data.total:,.2f}")
        self.view.tax_label.configure(text=f"Tax(11%): Rp. {data.calculate_tax():,.2f}")
        self.view.discount_label.configure(text=f"Discount: Rp. {(data.total*data.disc):,.2f}")
        self.view.final_total_label.configure(text=f"Final Total: Rp. {(data.total*(1-data.disc)+data.calculate_tax()):,.2f}")