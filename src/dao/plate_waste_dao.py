from config.supabase_client import supabase

class PlateWasteDAO:
    @staticmethod
    def create(waste_data):
        waste_data.pop("id", None)
        return supabase.table("plate_waste").insert(waste_data).execute().data

    @staticmethod
    def get_all():
        return supabase.table("plate_waste").select("*").execute().data
