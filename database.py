import psycopg2
from tkinter import messagebox
import QRcode
# Create a dictionary to store item names and quantities
db_config = {
    "dbname": "Inventory",
    "user": "postgres",
    "password": "3204",
    "host": "localhost",
    "port": "5432",
}


def create_table():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Create the items table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            quantity TEXT NOT NULL,
            Inventory_location TEXT NOT NULL,
            Item_location TEXT NOT NULL,
            catagory TEXT NOT NULL,
            Chroma_part_number TEXT,
            Manufacture_part_number TEXT
        )
    ''')
    conn.commit()
    conn.close()


def fetch_items(officelocation=None,itemlocation=None, category=None):
    #conn = psycopg2.connect(**db_config)
    #cursor = conn.cursor()
    #cursor.execute('''
    #               SELECT name,quantity,item_location,catagory,part_number FROM items
    #               ''')
    #items = cursor.fetchall()
    #conn.close()
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Build the SQL query with optional filters

    # Execute the query with parameters
    query = '''
            SELECT name, quantity, Inventory_location,Item_location, catagory, Chroma_part_number,Manufacture_part_number FROM items
            WHERE (%s IS NULL  OR Inventory_location = %s) AND (%s IS NULL  OR Item_location = %s)
            AND (%s IS NULL  OR catagory = %s)
            ORDER BY name  
        '''

    # Execute the query with parameters
    cursor.execute(query, (officelocation, officelocation,itemlocation,itemlocation, category, category))
    
    items = cursor.fetchall()
    conn.close()
    return items

def searchItems(name):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT name, quantity, Inventory_location,Item_location, catagory, Chroma_part_number,Manufacture_part_number FROM items WHERE name LIKE %s 
                   ''', (f"%{name}%",))
    items = cursor.fetchall()
    conn.close()
    return items



def checkItemExist(name, officelocation):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT name FROM items WHERE name = %s 
                   AND Inventory_location = %s''', (name, officelocation))
    item = cursor.fetchone()
    return item is not None


def insert_item(name, quantity, office_location,item_location, catagory, Chroma_part_number,Manufacture_part_number):
    if checkItemExist(name, office_location):
         messagebox.showinfo("Error", f"{name} already exists! at {office_location}")
    else:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO items (name, quantity, Inventory_location,item_location, catagory, Chroma_part_number,Manufacture_part_number)
            VALUES (%s, %s, %s, %s, %s,%s,%s)
        ''', (name, quantity,office_location, item_location, catagory, Chroma_part_number,Manufacture_part_number))
        conn.commit()
        conn.close()
        QRcode.create_qr_code(name,item_location,catagory)
        messagebox.showinfo('Success','Data has been inserted and QRcode has been generated')
def get_unique_office_locations():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        # Execute a query to get unique locations
        cursor.execute("SELECT DISTINCT Inventory_location FROM items")
        office_locations = [row[0] for row in cursor.fetchall()]
        return office_locations
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        conn.close()       
def get_unique_item_locations():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        # Execute a query to get unique locations
        cursor.execute("SELECT DISTINCT item_location FROM items")
        item_location = [row[0] for row in cursor.fetchall()]
        return item_location
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        conn.close()
def get_unique_categories():
    try:
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        # Execute a query to get unique locations
        cursor.execute("SELECT DISTINCT catagory FROM items")
        categories = [row[0] for row in cursor.fetchall()]
        return categories
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the database connection
        conn.close() 
        
def delete_item(name, office_location,category):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
                   DELETE FROM items WHERE name = %s 
                   AND Inventory_location = %s AND catagory = %s''', (name, office_location,category))
    conn.commit()
    print("delete successful")
    QRcode.delete_qr_code(name, office_location,category)
    conn.close()
    
    
def update_item(name, quantity, office_location, item_location, catagory, Chroma_part_number, Manufacture_part_number,oldname,oldlocation):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE items
        SET name = %s, quantity = %s, Inventory_location = %s, item_location = %s, catagory = %s, Chroma_part_number = %s, Manufacture_part_number = %s
        WHERE name = %s AND Inventory_location = %s
     ''', (name, quantity, office_location, item_location, catagory, Chroma_part_number, Manufacture_part_number, oldname, oldlocation))
    conn.commit()
    conn.close()
# Example usage
#create_table()
#insert_item("Item1", 10, "LocationA","locationb", "Category1", Chroma_part_number=12345,Manufacture_part_number=21321)
#update_item("Item2", 10, "LocationA","locationb", "Category1", Chroma_part_number=12345,Manufacture_part_number=21321)
