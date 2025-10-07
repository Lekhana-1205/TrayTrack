# Path: src/services/report_service.py
from dao.report_dao import ReportDAO

class ReportService:
    @staticmethod
    def add_report(total_waste, notes, created_at):
        report_data = {
            "total_waste": total_waste,
            "notes": notes,
            "created_at": created_at
        }
        return ReportDAO.create(report_data)

    @staticmethod
    def list_reports():
        return ReportDAO.get_all()

    @staticmethod
    def get_report_by_id(report_id):
        return ReportDAO.get_by_id(report_id)

    @staticmethod
    def delete_report(report_id):
        return ReportDAO.delete(report_id)
