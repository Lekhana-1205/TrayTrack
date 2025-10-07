# Path: src/services/menu_item_service.py
from dao.menu_item_dao import MenuItemDAO

class MenuItemService:
    @staticmethod
    def add_menu_item(name, category, price):
        menu_item_data = {
            "name": name,
            "category": category,
            "price": price
        }
        return MenuItemDAO.create(menu_item_data)

    @staticmethod
    def list_menu_items():
        return MenuItemDAO.get_all()

    @staticmethod
    def get_menu_item_by_id(menu_id):
        return MenuItemDAO.get_by_id(menu_id)

    @staticmethod
    def delete_menu_item(menu_id):
        return MenuItemDAO.delete(menu_id)
