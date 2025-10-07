# Path: src/dao/ingredient_dao.py
# Purpose: Database access for Ingredient table

from config.supabase_client import supabase

class IngredientDAO:
    @staticmethod
    def create(ingredient_data):
        ingredient_data.pop("id", None)
        return supabase.table("ingredient").insert(ingredient_data).execute().data

    @staticmethod
    def get_all():
        return supabase.table("ingredient").select("*").execute().data

    @staticmethod
    def get_by_id(ingredient_id):
        return supabase.table("ingredient").select("*").eq("id", ingredient_id).execute().data

    @staticmethod
    def delete(ingredient_id):
        return supabase.table("ingredient").delete().eq("id", ingredient_id).execute()
