# Path: src/services/plate_waste_service.py
from dao.plate_waste_dao import PlateWasteDAO
from datetime import datetime

class PlateWasteService:
    @staticmethod
    def add_plate_waste(menu_item_id, leftover_quantity, date_input=None):
        """
        Add a plate waste record.
        leftover_quantity: amount wasted
        date_input: optional, if not provided current timestamp is used
        """
        waste_data = {
            "menu_item_id": int(menu_item_id),
            "leftover_quantity": float(leftover_quantity)
        }

        # Handle optional date input
        if date_input:
            try:
                dt = datetime.strptime(date_input, "%Y-%m-%d")
                waste_data["recorded_at"] = dt.isoformat()  # ✅ Fix applied here
            except ValueError:
                print("Invalid date format! Using current timestamp.")

        return PlateWasteDAO.create(waste_data)

    @staticmethod
    def list_plate_waste():
        """
        List all plate waste records
        """
        return PlateWasteDAO.get_all()
