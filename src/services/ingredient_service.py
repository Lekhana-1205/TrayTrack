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
