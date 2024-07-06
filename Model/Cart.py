from .base import Observerable
class ShoppingCartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class ShoppingCart(Observerable):
    def __init__(self):
        super().__init__()
        self.items = []
        self.total= 0.0
        self.disc = 0.0

    def add_item(self, product, quantity):
        cart_item = ShoppingCartItem(product, quantity)
        self.total += product.price*quantity 
        self.items.append(cart_item)
        self.trigger_event("CART_CHANGED")


    def calculate_tax(self):
        tax_rate = 0.11  # 8% tax rate (adjust as needed)
        afterTax = (self.total*(1-self.disc)) * tax_rate
        return afterTax

    def calculate_disc(self,disc):
        self.disc = disc
        self.trigger_event("CART_CHANGED")

    def reset_cart(self):
        self.items = []
        self.total = 0.0
        self.disc = 0.0
        self.trigger_event("CART_CHANGED")
