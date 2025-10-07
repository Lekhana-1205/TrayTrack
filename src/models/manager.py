# Path: src/models/manager.py
# Purpose: Manager data model (OOP representation)

class Manager:
    def __init__(self, name, role, email, password):
        self.name = name
        self.role = role
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<Manager {self.name} ({self.email})>"
