# Path: src/cli/main_cli.py
# Main CLI for TrayTrack
# Menu-driven interface to manage Managers, Menu Items, Ingredients, Plate Waste, and Report1

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.manager_service import ManagerService
from services.menu_item_service import MenuItemService
from services.ingredient_service import IngredientService
from services.menuitem_ingredient_service import MenuItemIngredientService
from services.plate_waste_service import PlateWasteService
from services.report_service import ReportService
from datetime import datetime

def main_menu():
    while True:
        print("\n--- TrayTrack CLI ---")
        print("1. Manager Module")
        print("2. Menu Item Module")
        print("3. Ingredient Module")
        print("4. Plate Waste Module")
        print("5. Reports")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager_menu()
        elif choice == '2':
            menu_item_menu()
        elif choice == '3':
            ingredient_menu()
        elif choice == '4':
            plate_waste_menu()
        elif choice == '5':
            report_menu()
        elif choice == '6':
            print("Exiting TrayTrack CLI...")
            break
        else:
            print("Invalid choice. Try again.")

# ---------------- Manager Menu ----------------
def manager_menu():
    while True:
        print("\n--- Manager Menu ---")
        print("1. Add Manager")
        print("2. List Managers")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            role = input("Role: ")
            email = input("Email: ")
            password = input("Password: ")
            result = ManagerService.register_manager(name, role, email, password)
            print("Manager added:", result)
        elif choice == '2':
            managers = ManagerService.list_managers()
            for m in managers:
                print(m)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# ---------------- Menu Item Menu ----------------
def menu_item_menu():
    while True:
        print("\n--- Menu Item Menu ---")
        print("1. Add Menu Item")
        print("2. List Menu Items")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Menu Item Name: ")
            category = input("Category: ")
            price = float(input("Price: "))
            result = MenuItemService.add_menu_item(name, category, price)
            print("Menu Item added:", result)
        elif choice == '2':
            items = MenuItemService.list_menu_items()
            for item in items:
                print(item)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# ---------------- Ingredient Menu ----------------
def ingredient_menu():
    while True:
        print("\n--- Ingredient Menu ---")
        print("1. Add Ingredient")
        print("2. List Ingredients")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Ingredient Name: ")
            quantity = float(input("Quantity: "))
            unit = input("Unit (kg/liter/pcs): ")
            result = IngredientService.add_ingredient(name, quantity, unit)
            print("Ingredient added:", result)
        elif choice == '2':
            ingredients = IngredientService.list_ingredients()
            for ing in ingredients:
                print(ing)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# ---------------- Plate Waste Menu ----------------
def plate_waste_menu():
    while True:
        print("\n--- Plate Waste Menu ---")
        print("1. Record Plate Waste")
        print("2. List Plate Waste")
        print("3. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
         menu_item_id = input("Menu Item ID: ")  # Can be int or string UUID
         leftover_quantity = float(input("Quantity Wasted: "))
         date_input = input("Date (YYYY-MM-DD) [optional]: ") or None  # optional

         result = PlateWasteService.add_plate_waste(menu_item_id, leftover_quantity, date_input)
         ("Plate Waste recorded:", result)

        
        elif choice == '2':
            wastes = PlateWasteService.list_plate_waste()
            for w in wastes:
                print(w)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

# ---------------- Report Menu ----------------
def report_menu():
    while True:
        print("\n--- Reports Menu ---")
        print("1. Waste Summary")
        print("2. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Simple summary: sum quantity per menu item
            wastes = PlateWasteService.list_plate_waste()
            summary = {}
            for w in wastes:
                item_id = w["menu_item_id"]
                summary[item_id] = summary.get(item_id, 0) + w["leftover_quantity"]

            
            print("\nTotal Waste Summary:")
            for item_id, qty in summary.items():
                print(f"{item_id} -> {qty} wasted")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Try again.")

# ---------------- Start CLI ----------------
if __name__ == "__main__":
    main_menu()
