# Path: src/models/ingredient.py
class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return f"<Ingredient {self.name}: {self.quantity} {self.unit}>"
