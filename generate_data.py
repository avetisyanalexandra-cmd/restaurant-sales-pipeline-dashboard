import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta
from sqlalchemy import create_engine

# --- 1. SET UP SQL CONNECTION ---
engine = create_engine('sqlite:///restaurant_database.db')

# --- 2. GENERATE MENU DATA ---
menu_data = {
    'Item_Name': ['Classic Burger', 'Cheeseburger', 'Veggie Burger', 'French Fries', 'Onion Rings', 
                  'Caesar Salad', 'Margherita Pizza', 'Pepperoni Pizza', 'Coca-Cola', 'Craft Beer', 
                  'Cappuccino', 'Cheesecake', 'Chocolate Brownie'],
    'Category': ['Burgers', 'Burgers', 'Burgers', 'Sides', 'Sides', 
                 'Salads', 'Pizza', 'Pizza', 'Drinks', 'Drinks', 
                 'Drinks', 'Desserts', 'Desserts'],
    'Price': [12.99, 13.99, 11.99, 4.50, 5.00, 10.50, 14.99, 16.99, 2.50, 6.50, 3.50, 7.00, 6.50],
    'Cost': [4.20, 4.80, 3.90, 1.10, 1.25, 3.10, 4.50, 5.50, 0.50, 2.00, 0.90, 2.10, 1.80]
}
df_menu = pd.DataFrame(menu_data)

# Injecting dirty data elements
df_menu.loc[0, 'Item_Name'] = '  Classic Burger '
df_menu.loc[3, 'Category'] = 'sides'

# --- 3. GENERATE ORDERS DATA ---
random.seed(42)
np.random.seed(42)
num_orders = 700
start_date = datetime(2026, 1, 1)

weekend_days = [4, 5]
items_pool = [1, 2, 3]

orders = []
for i in range(num_orders):
    order_id = f"ORD-{1000 + i}"
    days_to_add = random.randint(0, 59)
    order_date = start_date + timedelta(days=days_to_add)
    
    num_items_in_order = random.randint(1, 4)
    if order_date.weekday() in weekend_days:
        num_items_in_order += random.randint(1, 2)
        
    for _ in range(num_items_in_order):
        item_row = df_menu.sample(1).iloc[0]
        item_name = item_row['Item_Name']
        quantity = random.choices(items_pool, weights=[0.7, 0.2, 0.1])[0]
        cust_type = random.choice(['In-person', 'Delivery'])
        
        orders.append([order_id, order_date.strftime('%Y-%m-%d'), item_name, quantity, cust_type])

df_orders = pd.DataFrame(orders, columns=['Order_ID', 'Date', 'Item_Name', 'Quantity', 'Customer_Type'])

# --- 4. EXPORT TO SQL & DESKTOP ---
print("Exporting data to SQL Database...")
df_menu.to_sql('raw_menu', con=engine, if_exists='replace', index=False)
df_orders.to_sql('raw_orders', con=engine, if_exists='replace', index=False)

# Находим путь к Рабочему столу вашего Mac
desktop_path = os.path.expanduser("~/Desktop")

print("Saving files directly to your Desktop...")
df_menu.to_csv(os.path.join(desktop_path, 'restaurant_menu.csv'), index=False)
df_orders.to_csv(os.path.join(desktop_path, 'restaurant_orders.csv'), index=False)
print("Done! Look at your Desktop now.")
