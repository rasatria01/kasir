from View.card import Card
import customtkinter as ctk
class HistController:
    def __init__(self,hist,view):
        self.hist = hist
        self.view = view
        self.listItem = []
        self.hist.add_event_listener("HIST_ADDED", self.updateCard)
        self.createCard()

    def createCard(self):
        for i in range(len(self.hist.item)):
            frame = Card(self.view,self.convertToString(self.hist.item[i]),i+1)
            frame.pack(fill=ctk.X,pady=10,padx=10)
            self.listItem.append(frame)

    def deleteCard(self):
        for frame in self.listItem:
            frame.destroy()
        self.listItem = []
        return
    
    def updateCard(self,data):
        frame = Card(self.view,self.convertToString(data.item[-1]),len(data.item))
        frame.pack(fill=ctk.X,pady=10,padx=10)
        self.listItem.append(frame)

    def convertToString(self,data):
        newlist = [x.product.name for x in data]
        return ", ".join(newlist)
