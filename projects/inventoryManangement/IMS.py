import pandas as pd

def laod_inventory(file = "inventory.csv"):
    df = pd.read_csv(file)
    return df_to_nested(df)

def save_inventory(inventory, file="inventory.csv"):
    df = nested_to_df(inventory)
    df.to_csv(file, index=False
              
              )
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

def display_inventory(inventory):
    print("\n Current Inventory (by Category):\n")
    for cat, items in inventory.items():
        print(f"{cat}")

        for item in items:
            print(f" -{item["ProductName"]} (ID: {item["ProductID"]})" f"Qty: {item['Quantity']} Price: Rs.{item['Price']}")
    
    print()

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

def updated_quantity(inventory, category, pid, qty_change):
    if category in inventory:
        for item in inventory[category]:
            if item["ProductID"] == pid:
                item["Quantity"] = qty_change
                return inventory
    print("Product not found")
    return inventory

def delete_product(inventory, category, pid):
    if category in inventory:
        inventory[category] = [item for item in inventory[category] if item["ProductId"] != pid]
    return inventory

def search_product(inventory, keyword):
    results = []
    for cat, items in inventory.items():
        for item in items:
            if keyword.lower() in item["ProductName"].lower():
                results.append((cat, item))
    return results

def low_stock_report(inventory, threshold = 10):
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

if __name__ == "_main_":
    inventory = load_inventory()

    while True:
        print("\n Inventory Management System")
        print("1. Dispaly Inventory")
        print("2. Add Product")
        print("3. Update Quantity")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Low Stock Report")
        print("7. Inventory Value Report")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_inventory(inventory)
        
        elif choice == "2":
            cat = input("Enter Category: ")
            pid = int(input("Enter Product ID: "))
            name = input("Enter Produc Name: ")
            qty = int(input("Enter Quantity: "))
            price = float(input("Enter price: "))
            inventory = add_product(inventory, cat, pid, name, qty, price)
            save_inventory(inventory)
        