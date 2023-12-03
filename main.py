import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox 
import database 
import pyautogui
# screen varaible
screen_width, screen_height = pyautogui.size()
x = 10 
app = customtkinter.CTk()
app.title('Service Team Inventory Management System')
app.geometry(f'{screen_width}x{screen_height}+0+0')
app.config(bg='#151C25')
app.resizable(TRUE,TRUE)


font1 =('Arial',23,'bold')
font2 =('Arial',15,'bold')
font3 = ('Arial',8,'bold')
startinglabel_x_corrdinate = 20
startinglabel_y_corrdinate = 20 

def add_to_treeview():
    items = database.fetch_items()
    tree.delete(*tree.get_children())
    for item in items:
        tree.insert('',END,values=item)
def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
    name_entry.delete(0,END)
    quantity_entry.delete(0,END)
    office_location_entry.delete(0,END)
    Item_location_entry.delete(0,END)
    category_entry.delete(0,END)
    chroma_partNumber_entry.delete(0,END)
    manufacture_partNumber_entry.delete(0,END)

def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        name_entry.insert(0,row[0])
        quantity_entry.insert(0,row[1])
        office_location_entry.insert(0,row[2])
        Item_location_entry.insert(0,row[3])
        category_entry.insert(0,row[4])
        chroma_partNumber_entry.insert(0,row[5])
        manufacture_partNumber_entry.insert(0,row[6])
    else: pass 
        

        
     
# Name label and entry
name_label = customtkinter.CTkLabel(app, font = font1, text='ItemName:', text_color='#fff',bg_color='#161C25')
name_label.place(x=startinglabel_x_corrdinate,y=startinglabel_y_corrdinate)

name_entry = customtkinter.CTkEntry(app, font= font1, text_color='#000', fg_color='#fff',border_color='#0C9295',border_width = 3, width = 200)
name_entry.place(x=startinglabel_x_corrdinate+205, y=startinglabel_y_corrdinate)

# Quantity label and entry 
quantity_label = customtkinter.CTkLabel(app, font = font1, text='Quantity:', text_color='#fff',bg_color='#161C25')
quantity_label.place(x=startinglabel_x_corrdinate,y=startinglabel_y_corrdinate+80)

quantity_entry = customtkinter.CTkEntry(app, font= font1, text_color='#000', fg_color='#fff',border_color='#0C9295',border_width = 3, width = 200)
quantity_entry.place(x=startinglabel_x_corrdinate+205, y=startinglabel_y_corrdinate+80)

# Office Location label and entry
office_location_label = customtkinter.CTkLabel(app, font = font1, text='OfficeLocation:', text_color='#fff',bg_color='#161C25')
office_location_label.place(x=startinglabel_x_corrdinate,y=startinglabel_y_corrdinate+160)

office_location_entry = customtkinter.CTkEntry(app, font= font1, text_color='#000', fg_color='#fff',border_color='#0C9295',border_width = 3, width = 200)
office_location_entry.place(x=startinglabel_x_corrdinate+205, y=startinglabel_y_corrdinate+160)

# Item Location label and entry
Item_location_label = customtkinter.CTkLabel(app, font = font1, text='ItemLocation:', text_color='#fff',bg_color='#161C25')
Item_location_label.place(x=20,y=260)

Item_location_entry = customtkinter.CTkEntry(app, font= font1, text_color='#000', fg_color='#fff',border_color='#0C9295',border_width = 3, width = 200)
Item_location_entry.place(x=startinglabel_x_corrdinate+205, y=startinglabel_y_corrdinate+240)


# Category label and entry
category_label = customtkinter.CTkLabel(app, font = font1, text='Category:', text_color='#fff',bg_color='#161C25')
category_label.place(x=startinglabel_x_corrdinate,y=startinglabel_y_corrdinate+320)

category_entry = customtkinter.CTkEntry(app, font= font1, text_color='#000', fg_color='#fff',border_color='#0C9295',border_width = 3, width = 200)
category_entry.place(x=startinglabel_x_corrdinate+205, y=startinglabel_y_corrdinate+320)

# Chroma PartNumber label and entry
chroma_partNumber_label = customtkinter.CTkLabel(app, font = font1, text='ChromaPN:', text_color='#fff',bg_color='#161C25')
chroma_partNumber_label.place(x=startinglabel_x_corrdinate,y=startinglabel_y_corrdinate+400)

chroma_partNumber_entry = customtkinter.CTkEntry(app, font= font1, text_color='#000', fg_color='#fff',border_color='#0C9295',border_width = 3, width = 200)
chroma_partNumber_entry.place(x=startinglabel_x_corrdinate+205, y=startinglabel_y_corrdinate+400)

# Manufacture PartNumber label and entry
manufacture_partNumber_label = customtkinter.CTkLabel(app, font = font1, text='ManufacturePN:', text_color='#fff',bg_color='#161C25')
manufacture_partNumber_label.place(x=startinglabel_x_corrdinate,y=startinglabel_y_corrdinate+480)

manufacture_partNumber_entry = customtkinter.CTkEntry(app, font= font1, text_color='#000', fg_color='#fff',border_color='#0C9295',border_width = 3, width = 200)
manufacture_partNumber_entry.place(x=startinglabel_x_corrdinate+205, y=startinglabel_y_corrdinate+480)

search_entry_label = customtkinter.CTkLabel(app, font = font1, text='Search:', text_color='#fff',bg_color='#161C25')
search_entry = customtkinter.CTkEntry(app, font= font2, text_color='#000', fg_color='#fff',border_color='#0C9295',border_width = 3, width = 200)
search_entry.pack()

itemlocation_var = tk.StringVar()
itemlocation_var.set("All Item Locations")  # Set a default value

officelocation_var = tk.StringVar()
officelocation_var.set("All Office Locations")  # Set a default value
# Create a StringVar for Category and set it as the default value for OptionMenu
category_var = tk.StringVar()
category_var.set("All Categories")  # Set a default value
# Create OptionMenu for itemLocation
itemlocation_options = ["All Item Locations"] + database.get_unique_item_locations()
itemlocation_menu = tk.OptionMenu(app, itemlocation_var, *itemlocation_options)
itemlocation_menu.config(font=font3, bg='#161C25', fg='#fff', borderwidth=3, relief="solid")
# Create OptionMenu for OfficeLocation
officelocation_options = ["All Office Locations"] + database.get_unique_office_locations()
officelocation_menu = tk.OptionMenu(app, officelocation_var, *officelocation_options)
officelocation_menu.config(font=font3, bg='#161C25', fg='#fff', borderwidth=3, relief="solid")

# Create OptionMenu for Category
category_options = ["All Categories"] + database.get_unique_categories()
category_menu = tk.OptionMenu(app, category_var, *category_options)
category_menu.config(font=font3, bg='#161C25', fg='#fff', borderwidth=3, relief="solid")


#category_menu.place(x=startinglabel_x_corrdinate+1080, y=startinglabel_y_corrdinate+320)

def update_filter_options():
    #  # Assuming location_options and category_options are global variables
    #location_options = ["All Item Locations"] + database.get_unique_office_locations()
    #category_options = ["All Categories"] + database.get_unique_categories()
    
    # Update the item location menu options
    itemlocation_var.set(itemlocation_options[0])  # Set the default value to "All Locations"
    itemlocation_menu['menu'].delete(0, 'end')  # Clear existing menu options
    for itemlocation in itemlocation_options:
        itemlocation_menu['menu'].add_command(label=itemlocation, command=tk._setit(itemlocation_var, itemlocation))
    
    # Update the office location menu options
    officelocation_var.set(officelocation_options[0])  # Set the default value to "All Locations"
    officelocation_menu['menu'].delete(0, 'end')  # Clear existing menu options
    for officelocation in officelocation_options:
        officelocation_menu['menu'].add_command(label=officelocation, command=tk._setit(officelocation_var, officelocation))
    
    # Update the category menu options
    category_var.set(category_options[0])  # Set the default value to "All Categories"
    category_menu['menu'].delete(0, 'end')  # Clear existing menu options
    for category in category_options:
        category_menu['menu'].add_command(label=category, command=tk._setit(category_var, category))

def update():
    selected_item = tree.focus()
    if not selected_item: 
        messagebox.showerror('Error', 'Choose an item to update')
    else : 
        olditemName = tree.item(selected_item)['values'][0]
        oldofficelocation = tree.item(selected_item)['values'][2]
        itemName = name_entry.get()
        quantity = quantity_entry.get()
        officelocation = office_location_entry.get()
        itemlocation = Item_location_entry.get()
        category = category_entry.get()
        chromaPN = chroma_partNumber_entry.get()
        manufacturePN = manufacture_partNumber_entry.get()
        database.update_item(itemName,quantity,officelocation,itemlocation,category, chromaPN,manufacturePN, olditemName,oldofficelocation)
        add_to_treeview()
        clear()
        update_filter_options()
        messagebox.showinfo('Success', 'Data has been updated')
def delete():
    selected_item = tree.focus()
    if not selected_item: 
        messagebox.showerror('Error', 'Choose an item to delete')
    else : 
        itemName = name_entry.get()
        officelocation = office_location_entry.get()
        catagory = category_entry.get()
        database.delete_item(itemName,officelocation,catagory)
        add_to_treeview()
        clear()
        update_filter_options()
        messagebox.showinfo('Success', 'Data and QRcode have been deleted ')

def insert():
    itemName = name_entry.get()
    quantity = quantity_entry.get()
    officelocation = office_location_entry.get()
    itemlocation = Item_location_entry.get()
    category = category_entry.get()
    chromaPN = chroma_partNumber_entry.get()
    manufacturePN = manufacture_partNumber_entry.get()
    if not(itemName and quantity and officelocation and itemlocation and category):
        messagebox.showerror('Error','Enter name, quantity, officelocation, itemlocation and category')
    elif not ((quantity.isnumeric())):
        messagebox.showerror('Error','Please enter an numeric value for quantity')
    else :
        database.insert_item(itemName,quantity,officelocation,itemlocation,category, chromaPN,manufacturePN)
        add_to_treeview()
        update_filter_options()

# add button for adding new item into database 
add_button = customtkinter.CTkButton(app, command=insert,font= font1, text_color='#fff', text ='Add Item',fg_color='#05A312', hover_color='#008508',bg_color='#161C25',cursor='hand2', corner_radius=20,width=300)
add_button.place(x=startinglabel_x_corrdinate, y = startinglabel_y_corrdinate+540)

# clear button for clear the input 
clear_button = customtkinter.CTkButton(app, command = lambda:clear(True), font= font1, text_color='#fff', text ='Clear Input',fg_color='#161C25',border_color='#F15704', hover_color='#FF5002',bg_color='#161C25',border_width = 3,cursor='hand2', corner_radius=20,width=300)
clear_button.place(x=startinglabel_x_corrdinate,y=startinglabel_y_corrdinate+650 )
# update button to update specific item info 
update_button = customtkinter.CTkButton(app,command=update,font= font1, text_color='#fff', text ='Update Item',fg_color='#161C25',border_color='#F15704', hover_color='#FF5002',bg_color='#161C25',border_width = 3,cursor='hand2', corner_radius=20,width=300)
update_button.place(x=startinglabel_x_corrdinate+400,y=startinglabel_y_corrdinate+650 )
# delete button to delete specific item info 
delete_button = customtkinter.CTkButton(app, command=delete,font= font1, text_color='#fff', text ='Delete Item',fg_color='#E40404',border_color='#E40404', hover_color='#AE0000',bg_color='#161C25',border_width = 3,cursor='hand2', corner_radius=20,width=300)
delete_button.place(x=startinglabel_x_corrdinate+800,y=startinglabel_y_corrdinate+650)



def filter_treeview():
    selected_officelocation = officelocation_var.get()
    selected_itemlocation = itemlocation_var.get()
    selected_category = category_var.get()
    if selected_officelocation == "All Office Locations":
        selected_officelocation = None

    if selected_itemlocation == "All Item Locations":
        selected_itemlocation = None
    
    if selected_category == "All Categories":
        selected_category = None
 
    items = database.fetch_items(selected_officelocation, selected_itemlocation, selected_category)
    tree.delete(*tree.get_children())
    for item in items:
        tree.insert('', END, values=item)
       
def search(event):
    word = search_entry.get()
    items =database.searchItems(word)
    tree.delete(*tree.get_children())
    for item in items:
        tree.insert('', END, values=item)


filter_button = customtkinter.CTkButton(app, command=filter_treeview, font=font2, text_color='#fff', text='Filter', fg_color='#05A312',
                                    hover_color='#008508', bg_color='#161C25', cursor='hand2', corner_radius=10, width=100)



# Tree style and display data
style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font = font2, foreground ='#fff',background ='#000',fieldbackground ='#313837')
style.map('Treeview', background =[('selected','#1A8F2D')])

tree = ttk.Treeview(app,height=15)
tree['column'] = ('Name', 'Quantity', 'OfficeLocation','ItemLocation','Category','ChromaPN','ManufacturePN')
tree.column('#0', width=0,stretch=tk.NO)
tree.column('Name', anchor=tk.CENTER, width=155)
tree.column('Quantity', anchor=tk.CENTER, width=155)
tree.column('OfficeLocation', anchor=tk.CENTER, width=155)
tree.column('ItemLocation', anchor=tk.CENTER, width=155)
tree.column('Category', anchor=tk.CENTER, width=155)
tree.column('ChromaPN', anchor=tk.CENTER, width=155)
tree.column('ManufacturePN', anchor=tk.CENTER, width=155)

tree.heading('Name', text='Name')
tree.heading('Quantity', text='Quantity')
tree.heading('OfficeLocation', text='OfficeLocation')
tree.heading('ItemLocation', text='ItemLocation')
tree.heading('Category', text='Category')
tree.heading('ChromaPN', text='ChromaPN')
tree.heading('ManufacturePN', text='ManufacturePN')
app.update_idletasks()
# Place the category menu
#category_menu.place(x=category_menu_x, y=category_menu_y)
# Create vertical scrollbar

def place_treefilter():
    vsb = ttk.Scrollbar(app, orient="vertical", command=tree.yview)
    vsb.place(x=tree.winfo_x() + tree.winfo_width(), y=tree.winfo_y(), height=tree.winfo_height())
    tree.configure(yscrollcommand=vsb.set)
    category_column_x = 155*4 
    itemlocation_column_x = 155*3 
    officelocation_column_x = 155*2
    filter_column_x = 155*5
    menu_x = tree.winfo_x() 
    menu_y = tree.winfo_y() + tree.winfo_height()
    # Place the category menu
    category_menu.place(x=menu_x+category_column_x, y=menu_y)
    # Place the item location menu 
    itemlocation_menu.place(x=menu_x+itemlocation_column_x,y=menu_y)
    # Place the office location menu
    officelocation_menu.place(x=menu_x+officelocation_column_x,y=menu_y)
    filter_button.place(x=menu_x+filter_column_x, y=menu_y)
    search_entry_label.place(x=menu_x, y=menu_y)
    search_entry.place(x=menu_x+90, y=menu_y)
tree.place(x=450,y=20)
tree.bind('<ButtonRelease>', display_data)
search_entry.bind("<KeyRelease>", search)
add_to_treeview()
app.after(20, place_treefilter)
app.mainloop()