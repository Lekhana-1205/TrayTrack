# Path: src/dao/report_dao.py
from config.supabase_client import supabase

class ReportDAO:
    @staticmethod
    def create(report_data):
        return supabase.table("report").insert(report_data).execute().data

    @staticmethod
    def get_all():
        return supabase.table("report").select("*").execute().data

    @staticmethod
    def get_by_id(report_id):
        return supabase.table("report").select("*").eq("id", report_id).execute().data

    @staticmethod
    def delete(report_id):
        return supabase.table("report").delete().eq("id", report_id).execute()
