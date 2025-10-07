# Path: src/dao/menu_item_dao.py
# Purpose: Database access for Menu Item table

from config.supabase_client import supabase

class MenuItemDAO:
    @staticmethod
    def create(menu_item_data):
        menu_item_data.pop("id", None)
        return supabase.table("menu_item").insert(menu_item_data).execute().data

    @staticmethod
    def get_all():
        return supabase.table("menu_item").select("*").execute().data

    @staticmethod
    def get_by_id(menu_item_id):
        return supabase.table("menu_item").select("*").eq("id", menu_item_id).execute().data

    @staticmethod
    def delete(menu_item_id):
        return supabase.table("menu_item").delete().eq("id", menu_item_id).execute()
