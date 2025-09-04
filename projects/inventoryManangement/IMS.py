import pandas as pd
import streamlit as st

# ---------- Your Functions ----------
def load_inventory(file="inventory.csv"):
    df = pd.read_csv(file)
    return df_to_nested(df)

def save_inventory(inventory, file="inventory.csv"):
    df = nested_to_df(inventory)
    df.to_csv(file, index=False)

def df_to_nested(df):
    inventory = {}
    for _, row in df.iterrows():
        cat = row["Category"]
        if cat not in inventory:
            inventory[cat] = []
        inventory[cat].append({
            "ProductID": int(row["ProductID"]),
            "ProductName": row["ProductName"],
            "Quantity": int(row["Quantity"]),
            "Price": float(row["Price"])
        })
    return inventory

def nested_to_df(inventory):
    rows = []
    for cat, items in inventory.items():
        for item in items:
            rows.append([cat, item["ProductID"], item["ProductName"], item["Quantity"], item["Price"]])
    return pd.DataFrame(rows, columns=["Category", "ProductID", "ProductName", "Quantity", "Price"])

def add_product(inventory, category, pid, name, qty, price):
    if category not in inventory:
        inventory[category] = []
    inventory[category].append({
        "ProductID": pid,
        "ProductName": name,
        "Quantity": qty,
        "Price": price
    })
    return inventory

def update_quantity(inventory, category, pid, qty_change):
    if category in inventory:
        for item in inventory[category]:
            if item["ProductID"] == pid:
                item["Quantity"] = qty_change
                return inventory
    return inventory

def delete_product(inventory, category, pid):
    if category in inventory:
        inventory[category] = [item for item in inventory[category] if item["ProductID"] != pid]
    return inventory

def search_product(inventory, keyword):
    results = []
    for cat, items in inventory.items():
        for item in items:
            if keyword.lower() in item["ProductName"].lower():
                results.append((cat, item))
    return results

def low_stock_report(inventory, threshold=10):
    report = []
    for cat, items in inventory.items():
        for item in items:
            if item["Quantity"] <= threshold:
                report.append((cat, item))
    return report

def inventory_value(inventory):
    total = 0
    for cat, items in inventory.items():
        for item in items:
            total += item["Quantity"] * item["Price"]
    return total

# ---------- Streamlit App ----------
st.title("📦 Inventory Management System")

# Load inventory once
inventory = load_inventory()

# Sidebar Menu
menu = st.sidebar.radio("Choose an action:", 
                        ["Display Inventory", "Add Product", "Update Quantity", 
                         "Delete Product", "Search Product", "Low Stock Report", 
                         "Inventory Value Report"])

if menu == "Display Inventory":
    st.subheader("Current Inventory")
    df = nested_to_df(inventory)
    st.dataframe(df)

elif menu == "Add Product":
    st.subheader("Add a New Product")
    cat = st.text_input("Category")
    pid = st.number_input("Product ID", min_value=1, step=1)
    name = st.text_input("Product Name")
    qty = st.number_input("Quantity", min_value=0, step=1)
    price = st.number_input("Price", min_value=0.0, step=0.1)

    if st.button("Add"):
        inventory = add_product(inventory, cat, pid, name, qty, price)
        save_inventory(inventory)
        st.success(f"✅ {name} added to {cat}")

elif menu == "Update Quantity":
    st.subheader("Update Product Quantity")
    cat = st.text_input("Category")
    pid = st.number_input("Product ID", min_value=1, step=1)
    qty = st.number_input("New Quantity", min_value=0, step=1)
    if st.button("Update"):
        inventory = update_quantity(inventory, cat, pid, qty)
        save_inventory(inventory)
        st.success("✅ Quantity updated")

elif menu == "Delete Product":
    st.subheader("Delete a Product")
    cat = st.text_input("Category")
    pid = st.number_input("Product ID", min_value=1, step=1)
    if st.button("Delete"):
        inventory = delete_product(inventory, cat, pid)
        save_inventory(inventory)
        st.warning("🗑 Product deleted")

elif menu == "Search Product":
    st.subheader("Search Product")
    keyword = st.text_input("Enter product name")
    if st.button("Search"):
        results = search_product(inventory, keyword)
        if results:
            df = pd.DataFrame(
                [(cat, item["ProductID"], item["ProductName"], item["Quantity"], item["Price"]) 
                 for cat, item in results],
                columns=["Category", "ProductID", "ProductName", "Quantity", "Price"]
            )
            st.dataframe(df)
        else:
            st.info("No products found.")

elif menu == "Low Stock Report":
    st.subheader("Low Stock Report")
    threshold = st.number_input("Threshold", min_value=1, value=10)
    report = low_stock_report(inventory, threshold)
    if report:
        df = pd.DataFrame(
            [(cat, item["ProductID"], item["ProductName"], item["Quantity"], item["Price"]) 
             for cat, item in report],
            columns=["Category", "ProductID", "ProductName", "Quantity", "Price"]
        )
        st.dataframe(df)
    else:
        st.success("🎉 No low stock items")

elif menu == "Inventory Value Report":
    st.subheader("Inventory Value Report")
    total = inventory_value(inventory)
    st.metric("Total Inventory Value (Rs.)", f"{total:,.2f}")
