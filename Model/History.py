from .base import Observerable
class HistoryItem:
    def __init__(self,item,date):
        self.item = item
        self.date = date

class HistoryTransaction(Observerable):
    def __init__(self):
        super().__init__()
        self.item = []


    def add_item(self, item):
        self.item.append(item)
        self.trigger_event("HIST_ADDED")

    def clear_hist(self):
        self.item = []
        self.trigger_event("HIST_CLEARED")

