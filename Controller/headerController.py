from datetime import datetime

class HeaderController:
    def __init__(self, view):
        self.view = view
    
    def update_time(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.view.datetime_label.configure(text=current_datetime)
        self.view.after(1000,self.update_time)