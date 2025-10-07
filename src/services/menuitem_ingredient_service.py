# Path: src/services/menuitem_ingredient_service.py
from dao.menuitem_ingredient_dao import MenuItemIngredientDAO

class MenuItemIngredientService:
    @staticmethod
    def add_mapping(menu_item_id, ingredient_id, quantity):
        mapping_data = {
            "menu_item_id": menu_item_id,
            "ingredient_id": ingredient_id,
            "quantity": quantity
        }
        return MenuItemIngredientDAO.create(mapping_data)

    @staticmethod
    def list_mappings():
        return MenuItemIngredientDAO.get_all()

    @staticmethod
    def get_mapping_by_id(mapping_id):
        return MenuItemIngredientDAO.get_by_id(mapping_id)

    @staticmethod
    def delete_mapping(mapping_id):
        return MenuItemIngredientDAO.delete(mapping_id)
