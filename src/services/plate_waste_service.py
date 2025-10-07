from dao.plate_waste_dao import PlateWasteDAO

class PlateWasteService:
    @staticmethod
    def add_plate_waste(menu_item_id, leftover_quantity, recorded_at):
        waste_data = {
            "menu_item_id": menu_item_id,
            "leftover_quantity": leftover_quantity,
            "recorded_at": recorded_at
        }
        return PlateWasteDAO.create(waste_data)

    @staticmethod
    def list_plate_waste():
        return PlateWasteDAO.get_all()
