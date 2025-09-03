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