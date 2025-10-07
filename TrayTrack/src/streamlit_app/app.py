import sys
import os
import streamlit as st

# Add the parent of services to sys.path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.manager_service import ManagerService
from services.menu_item_service import MenuItemService
from services.ingredient_service import IngredientService
from services.plate_waste_service import PlateWasteService


st.set_page_config(page_title="TrayTrack 🍽️", layout="wide")
st.title("TrayTrack - Smart Dining Waste Monitor 🍱")

# Sidebar
module = st.sidebar.selectbox(
    "Select Module 🛠️",
    ["Manager 👤", "Menu Item 🍔", "Ingredient 🥬", "Plate Waste 🗑️", "Reports 📊"]
)

# Manager Module
if module == "Manager 👤":
    st.header("Manager Module 👤")
    st.subheader("Add Manager ➕")

    name = st.text_input("Name")
    role = st.selectbox("Role", ["Admin", "Restaurant Manager", "Kitchen Supervisor", "Waste Analyst"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Add Manager 👏"):
        if name and role and email and password:
            try:
                result = ManagerService.register_manager(name, role, email, password)
                st.success(f"Manager added: {result} ✅")
            except Exception as e:
                st.error(f"Error: {e} ❌")
        else:
            st.warning("Fill all fields! ⚠️")

    st.subheader("List of Managers 👥")
    try:
        managers = ManagerService.list_managers()
        for m in managers:
            st.write(f"👤 {m['name']} ({m['role']}) - {m['email']}")
    except Exception as e:
        st.error(f"Error fetching managers: {e} ❌")

# Menu Item Module
elif module == "Menu Item 🍔":
    st.header("Menu Item Module 🍔")
    st.subheader("Add Menu Item ➕")

    menu_name = st.text_input("Menu Item Name")
    category = st.text_input("Category")
    price = st.number_input("Price", min_value=0.0, step=1.0)

    if st.button("Add Menu Item 🍽️"):
        if menu_name and category:
            try:
                result = MenuItemService.add_menu_item(menu_name, category, price)
                st.success(f"Menu item added: {result} ✅")
            except Exception as e:
                st.error(f"Error: {e} ❌")
        else:
            st.warning("Fill all fields! ⚠️")

    st.subheader("All Menu Items 🍔")
    try:
        items = MenuItemService.list_menu_items()
        for item in items:
            st.write(f"🍔 {item['name']} ({item['category']}) - ₹{item['price']}")
    except Exception as e:
        st.error(f"Error fetching menu items: {e} ❌")

# Ingredient Module
elif module == "Ingredient 🥬":
    st.header("Ingredient Module 🥬")
    st.subheader("Add Ingredient ➕")

    name = st.text_input("Ingredient Name")
    quantity = st.number_input("Quantity", min_value=0.0, step=0.1)
    unit = st.text_input("Unit (kg/liter/pcs)")

    if st.button("Add Ingredient 🥗"):
        if name and unit:
            try:
                result = IngredientService.add_ingredient(name, quantity, unit)
                st.success(f"Ingredient added: {result} ✅")
            except Exception as e:
                st.error(f"Error: {e} ❌")
        else:
            st.warning("Fill all fields! ⚠️")

    st.subheader("All Ingredients 🥬")
    try:
        ingredients = IngredientService.list_ingredients()
        for ing in ingredients:
            st.write(f"🥬 {ing['name']} - {ing['quantity']} {ing['unit']}")
    except Exception as e:
        st.error(f"Error fetching ingredients: {e} ❌")

# Plate Waste Module
elif module == "Plate Waste 🗑️":
    st.header("Plate Waste Module 🗑️")
    st.subheader("Record Plate Waste ➕")

    menu_item_id = st.text_input("Menu Item ID")
    qty_waste = st.number_input("Quantity Wasted", min_value=0.0, step=0.1)
    date = st.date_input("Date")

    if st.button("Record Waste 🚮"):
        if menu_item_id:
            try:
                result = PlateWasteService.add_plate_waste(menu_item_id, qty_waste, date.isoformat())
                st.success(f"Plate waste recorded: {result} ✅")
            except Exception as e:
                st.error(f"Error: {e} ❌")
        else:
            st.warning("Menu Item ID required! ⚠️")

    st.subheader("All Plate Waste Records 🗑️")
    try:
        wastes = PlateWasteService.list_plate_waste()
        for w in wastes:
            st.write(f"🥡 Menu Item ID {w['menu_item_id']} -> {w['leftover_quantity']} wasted on {w.get('recorded_at', 'N/A')}")
    except Exception as e:
        st.error(f"Error fetching plate waste: {e} ❌")

# Reports Module
elif module == "Reports 📊":
    st.header("Reports Module 📊")
    st.subheader("Waste Summary 📈")

    try:
        wastes = PlateWasteService.list_plate_waste()
        menu_items = {item['id']: item['name'] for item in MenuItemService.list_menu_items()}

        summary = {}
        for w in wastes:
            item_id = w["menu_item_id"]
            summary[item_id] = summary.get(item_id, 0) + w.get("leftover_quantity", 0)

        for item_id, qty in summary.items():
            item_name = menu_items.get(item_id, f"Item {item_id}")
            st.write(f"🥡 {item_name} -> {qty} wasted")
    except Exception as e:
        st.error(f"Error generating report: {e} ❌")
