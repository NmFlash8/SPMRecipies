import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from tkinter import ttk
from all_items import all_items
import random

# Inventory list with 10 random items to start
inventory = random.choices(all_items, k=10)

def update_inventory_display():
    inventory_list.delete(0, tk.END)
    for item in inventory:
        inventory_list.insert(tk.END, item)

def show_suggestions():
    typed = search_var.get().lower()
    suggestions_list.delete(0, tk.END)

    if typed == "":
        suggestions_list.place_forget()
        return

    matches = [item for item in all_items if typed in item.lower()]

    if matches:
        for item in matches:
            suggestions_list.insert(tk.END, item)

        x = search_entry.winfo_x()
        y = search_entry.winfo_y() + search_entry.winfo_height()

        suggestions_list.place(x=x, y=y)
        suggestions_list.lift()  # Bring above inventory list
    else:
        suggestions_list.place_forget()


def on_suggestion_click(event):
    try:
        index = suggestions_list.curselection()[0]
        selected = suggestions_list.get(index)
        inventory.append(selected)
        search_var.set("")
        suggestions_list.place_forget()
        update_inventory_display()
    except:
        pass

def remove_item(event):
    try:
        index = inventory_list.curselection()[0]
        inventory.pop(index)
        update_inventory_display()
    except:
        pass

# Main window
root = tk.Tk()
root.title("Inventory Manager")
root.geometry("350x400")

# Search Bar
search_var = tk.StringVar()
search_var.trace("w", lambda *args: show_suggestions())

search_entry = tk.Entry(root, textvariable=search_var, width=28)
search_entry.pack(pady=5)

# Autocomplete Suggestions List (hidden initially)
suggestions_list = tk.Listbox(root, width=28, height=5, bd=2, relief="solid")
suggestions_list.bind("<<ListboxSelect>>", on_suggestion_click)

# Inventory display
inventory_list = tk.Listbox(root, width=35, height=15)
inventory_list.pack(pady=(50,10))  # Push down inventory so suggestions are visible
inventory_list.bind("<<ListboxSelect>>", remove_item)

# Show the starting random inventory
update_inventory_display()

root.mainloop()
