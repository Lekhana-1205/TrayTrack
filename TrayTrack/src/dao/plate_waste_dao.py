# Path: src/dao/plate_waste_dao.py
from config.supabase_client import supabase

class PlateWasteDAO:
    @staticmethod
    def create(waste_data):
        # Insert waste data into plate_waste table
        return supabase.table("plate_waste").insert(waste_data).execute().data

    @staticmethod
    def get_all():
        # Fetch all plate waste records
        return supabase.table("plate_waste").select("*").execute().data

    @staticmethod
    def get_by_id(waste_id):
        # Fetch specific plate waste record by ID
        return supabase.table("plate_waste").select("*").eq("id", waste_id).execute().data

    @staticmethod
    def delete(waste_id):
        # Delete plate waste record by ID
        return supabase.table("plate_waste").delete().eq("id", waste_id).execute().data
