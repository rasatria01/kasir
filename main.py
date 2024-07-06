import customtkinter as ctk
from View.header import Header
from View.cartview import ContentView
from View.footer import Footer
from Model.Cart import ShoppingCart 
from Model.Product import products
from Model.Product import disc
from Model.History import HistoryTransaction
from Controller.contentController import ContentController
from Controller.headerController import HeaderController
from Controller.footerController import FooterController
from Controller.histController import HistController
from tkinter import ttk

class CashierView(ctk.CTkFrame):
    def __init__(self,master, hist):
        super().__init__(master)
        self.master= master
        self.cart = ShoppingCart()
        self.products = products
        self.disc = disc
        self.hist = hist
        
        self.headercontroller = HeaderController(Header(self))
        self.master.after(1000, self.headercontroller.update_time)
        self.headercontroller.view.pack(fill=ctk.X, pady=5)
        self.headercontroller.update_time()
        self.contencontroller = ContentController(self.cart, self.products,ContentView(self), self.disc)
        self.contencontroller.view.pack(fill=ctk.X, pady=5)
        self.footercontroller = FooterController(self.cart,Footer(self),self.hist)
        self.footercontroller.view.pack(fill=ctk.X,pady=5)

class HistView(ctk.CTkFrame):
    def __init__(self,master,hist):
        super().__init__(master)
        self.hist = hist
        self.TitleLabel = ctk.CTkLabel(self,text="Histori Transaksi")
        self.TitleLabel.pack(fill=ctk.X,pady=10)

        self.histkontroller = HistController(self.hist,ctk.CTkFrame(self))
        
        self.histkontroller.view.pack(fill=ctk.BOTH, expand=True)

class AproView(ctk.CTkFrame):
    def __init__(self,master,hist):
        super().__init__(master)
        self.hist = hist

class CashierApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.hist = HistoryTransaction()
        self.title("testing")
        self.geometry("1000x700")
        bg_color = self._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = self._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = self._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        treestyle = ttk.Style()
        treestyle.theme_use('default')
        treestyle.configure("Treeview",background=bg_color, foreground=text_color,fieldbackground=bg_color,borderwidth=0)
        treestyle.map('Treeview',background=[('selected',bg_color)],foreground=[('selected',selected_color)])
        self.bind("<<TreeviewSelect>>", lambda event: self.focus_set())
        self.tabtab = ctk.CTkTabview(self)
        self.tabtab.pack(padx=20,pady=20, expand=True, fill=ctk.BOTH)
        self.kasirTab = self.tabtab.add("Kasir")
        self.histTab = self.tabtab.add("Transaksi")
        self.aprioriTab = self.tabtab.add("Apriori")
        self.tabtab.set("Kasir")

        self.main_frame = CashierView(self.kasirTab, self.hist)
        self.main_frame.pack(fill=ctk.BOTH, expand=True)
        self.hist_frame = HistView(self.histTab,self.hist)
        self.hist_frame.pack(fill=ctk.BOTH, expand=True)

if __name__ == "__main__":
    ctk.deactivate_automatic_dpi_awareness()
    app = CashierApp()
    app.mainloop()