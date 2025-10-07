# Path: src/models/plate_waste.py
class PlateWaste:
    def __init__(self, menu_item_id, leftover_quantity, created_at):
        self.menu_item_id = menu_item_id
        self.leftover_quantity = leftover_quantity
        self.created_at = created_at

    def __repr__(self):
        return f"<PlateWaste MenuItemID:{self.menu_item_id}, Leftover:{self.leftover_quantity}, Date:{self.created_at}>"
