# Path: src/dao/menuitem_ingredient_dao.py
from config.supabase_client import supabase

class MenuItemIngredientDAO:
    @staticmethod
    def create(mapping_data):
        return supabase.table("menuitem_ingredient").insert(mapping_data).execute().data

    @staticmethod
    def get_all():
        return supabase.table("menuitem_ingredient").select("*").execute().data

    @staticmethod
    def get_by_id(mapping_id):
        return supabase.table("menuitem_ingredient").select("*").eq("id", mapping_id).execute().data

    @staticmethod
    def delete(mapping_id):
        return supabase.table("menuitem_ingredient").delete().eq("id", mapping_id).execute()
