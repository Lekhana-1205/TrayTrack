# Path: src/services/ingredient_service.py
from dao.ingredient_dao import IngredientDAO

class IngredientService:
    @staticmethod
    def add_ingredient(name, quantity, unit):
        ingredient_data = {
            "name": name,
            "quantity": quantity,
            "unit": unit
        }
        return IngredientDAO.create(ingredient_data)

    @staticmethod
    def list_ingredients():
        return IngredientDAO.get_all()

    @staticmethod
    def get_ingredient_by_id(ingredient_id):
        return IngredientDAO.get_by_id(ingredient_id)

    @staticmethod
    def delete_ingredient(ingredient_id):
        return IngredientDAO.delete(ingredient_id)
