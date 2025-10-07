# Path: src/services/manager_service.py
# Purpose: Business logic for Manager module

from dao.manager_dao import ManagerDAO

class ManagerService:
    @staticmethod
    def register_manager(name, role, email, password):
        # Validate email, hash password if needed, then create
        manager_data = {
            "name": name,
            "role": role,
            "email": email,
            "password": password
        }
        return ManagerDAO.create(manager_data)

    @staticmethod
    def list_managers():
        return ManagerDAO.get_all()
