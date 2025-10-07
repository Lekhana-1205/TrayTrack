# Path: src/models/menu_item.py
class MenuItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"<MenuItem {self.name} ({self.category}) - ₹{self.price}>"
