# Path: src/dao/manager_dao.py
# Purpose: Database access for Manager table

from config.supabase_client import supabase

class ManagerDAO:
    @staticmethod
    def create(manager_data):
        """
        Insert a new manager record.
        Ensures 'id' is not included so Postgres can auto-generate it.
        """
        manager_data.pop("id", None)  # Remove 'id' if present
        return supabase.table("manager").insert(manager_data).execute().data

    @staticmethod
    def get_all():
        """Fetch all managers"""
        return supabase.table("manager").select("*").execute().data

    @staticmethod
    def get_by_email(email):
        """Fetch manager by email"""
        return supabase.table("manager").select("*").eq("email", email).execute().data

    @staticmethod
    def delete(manager_id):
        """Delete manager by ID"""
        return supabase.table("manager").delete().eq("id", manager_id).execute()
