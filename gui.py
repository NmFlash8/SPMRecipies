import tkinter as tk
from tkinter import ttk
import random
import json
import os

from inventory import Inventory
from logic import build_trip
from game_data import all_items, needed
from dme_reader import read_all_items, dme


class TripGUI:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Calculator - By NmFlash8")
        master.iconbitmap(False, 'icon.ico')

        # Local state (avoid mutating globals directly)
        self.inventory = Inventory([])
        self.needed = list(needed)

        # UI
        self.create_add_item_section()
        self.create_inventory_section()
        self.create_trip_section()
        self.create_missing_section()
        self.create_full_needed_section()
        self.create_buttons()

        # Load persisted data
        self.load_data()

        # Initial render
        self.refresh_full_needed()
        self.generate_trip()

        # Autosave
        self.start_autosave()

    # =========================================================
    # UI BUILDERS
    # =========================================================

    def create_add_item_section(self):
        ttk.Label(self.master, text="Add Item to Inventory:") \
            .grid(row=0, column=0, sticky="w")

        self.add_entry = ttk.Entry(self.master, width=25)
        self.add_entry.grid(row=1, column=0, padx=5, sticky="w")
        self.add_entry.bind("<KeyRelease>", self.update_autofill)
        self.add_entry.bind("<Return>", self.add_item_from_enter)

        self.autofill_listbox = tk.Listbox(self.master, width=25, height=5)
        self.autofill_listbox.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="w")
        self.autofill_listbox.bind("<<ListboxSelect>>", self.add_item_from_click)

    def create_inventory_section(self):
        ttk.Label(self.master, text="Inventory:") \
            .grid(row=3, column=0, sticky="w")

        self.inventory_listbox = tk.Listbox(self.master, width=25, height=10)
        self.inventory_listbox.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.inventory_listbox.bind("<<ListboxSelect>>", self.remove_inventory_item)

    def create_trip_section(self):
        ttk.Label(self.master, text="Trip Steps:") \
            .grid(row=0, column=1, sticky="w")

        self.trip_listbox = tk.Listbox(self.master, width=40, height=15)
        self.trip_listbox.grid(row=1, column=1, rowspan=2, padx=5, pady=5, sticky="n")
        self.trip_listbox.bind("<<ListboxSelect>>", self.use_crafted_recipe)

    def create_missing_section(self):
        ttk.Label(self.master, text="Missing Items Needed:") \
            .grid(row=0, column=2, sticky="w")

        self.missing_listbox = tk.Listbox(self.master, width=40, height=15)
        self.missing_listbox.grid(row=1, column=2, rowspan=2, padx=5, pady=5, sticky="n")
        self.missing_listbox.bind("<<ListboxSelect>>", self.add_missing_to_inventory)

    def create_full_needed_section(self):
        ttk.Label(self.master, text="All Needed Recipes (Full List):") \
            .grid(row=0, column=3, sticky="w")

        self.full_needed_listbox = tk.Listbox(self.master, width=40, height=15)
        self.full_needed_listbox.grid(row=1, column=3, rowspan=2, padx=5, pady=5, sticky="n")
        self.full_needed_listbox.bind("<<ListboxSelect>>", self.remove_needed_item)

    def create_buttons(self):
        ttk.Button(self.master, text="Generate Trip", command=self.generate_trip) \
            .grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(self.master, text="Remove 5 Needed Items", command=self.remove_needed) \
            .grid(row=3, column=2, padx=10, pady=10)

        ttk.Button(self.master, text="Update From Game", command=self.update_inventory_from_game) \
            .grid(row=3, column=3, padx=10, pady=10)

        ttk.Button(self.master, text="Export Trip to TXT", command=self.export_trip_to_file) \
            .grid(row=4, column=1, padx=10, pady=10)

    # =========================================================
    # AUTOFILL
    # =========================================================

    def update_autofill(self, event=None):
        query = self.add_entry.get().lower().strip()
        self.clear_listbox(self.autofill_listbox)

        if not query:
            return

        matches = [item for item in all_items if query in item.lower()]
        self.autofill_listbox.insert(tk.END, *matches)

    def add_item_to_inventory(self, item):
        if item in all_items:
            self.inventory.items.append(item)
        self.add_entry.delete(0, tk.END)
        self.clear_listbox(self.autofill_listbox)
        self.generate_trip()

    def add_item_from_click(self, event):
        selection = self.autofill_listbox.curselection()
        if selection:
            self.add_item_to_inventory(self.autofill_listbox.get(selection[0]))

    def add_item_from_enter(self, event):
        if self.autofill_listbox.size() > 0:
            self.add_item_to_inventory(self.autofill_listbox.get(0))

    # =========================================================
    # INVENTORY / NEEDED HANDLERS
    # =========================================================

    def remove_inventory_item(self, event):
        selection = self.inventory_listbox.curselection()
        if selection:
            self.inventory.items.pop(selection[0])
            self.generate_trip()

    def remove_needed_item(self, event):
        selection = self.full_needed_listbox.curselection()
        if selection:
            self.needed.pop(selection[0])
            self.generate_trip()

    def add_missing_to_inventory(self, event):
        selection = self.missing_listbox.curselection()
        if not selection:
            return

        item = self.missing_listbox.get(selection[0])
        if item not in self.inventory.items:
            self.inventory.items.append(item)

        if item in self.needed:
            self.needed.remove(item)

        self.generate_trip()

    def use_crafted_recipe(self, event):
        selection = self.trip_listbox.curselection()
        if not selection:
            return

        line = self.trip_listbox.get(selection[0])
        if "→" not in line:
            return

        ingredients_part, product = line.split("→")
        ingredients = [x.strip() for x in ingredients_part.split("+")]
        product = product.strip()

        for item in ingredients:
            if item in self.inventory.items:
                self.inventory.items.remove(item)

        if product not in self.inventory.items:
            self.inventory.items.append(product)

        if product in self.needed:
            self.needed.remove(product)

        self.generate_trip()

    # =========================================================
    # TRIP LOGIC
    # =========================================================

    def generate_trip(self):
        self.clear_listbox(self.inventory_listbox)
        self.inventory_listbox.insert(tk.END, *self.inventory.items)

        trip, missing_items = build_trip(self.inventory, self.needed)

        self.clear_listbox(self.trip_listbox)
        for a, b, c in trip:
            self.trip_listbox.insert(tk.END, f"{a} + {b} → {c}")

        self.clear_listbox(self.missing_listbox)
        self.missing_listbox.insert(tk.END, *missing_items)

        self.refresh_full_needed()

    def remove_needed(self):
        for _ in range(5):
            if self.needed:
                self.needed.pop(random.randrange(len(self.needed)))
        self.generate_trip()

    # =========================================================
    # SAVE / LOAD
    # =========================================================

    def save_data(self):
        with open("inventory.json", "w") as f:
            json.dump(self.inventory.items, f, indent=2)

        with open("needed.json", "w") as f:
            json.dump(self.needed, f, indent=2)

    def load_data(self):
        if os.path.exists("inventory.json"):
            with open("inventory.json", "r") as f:
                self.inventory.items = json.load(f)

        if os.path.exists("needed.json"):
            with open("needed.json", "r") as f:
                self.needed = json.load(f)

    def start_autosave(self):
        self.save_data()
        self.master.after(10000, self.start_autosave)

    # =========================================================
    # GAME MEMORY
    # =========================================================

    def update_inventory_from_game(self):
        try:
            self.inventory.items = read_all_items(dme)
        except Exception as e:
            print("Game read error:", e)
        self.generate_trip()

    # =========================================================
    # EXPORT / HELPERS
    # =========================================================

    def export_trip_to_file(self):
        with open("CurrentTrip.txt", "w") as f:
            for i in range(self.trip_listbox.size()):
                f.write(self.trip_listbox.get(i) + "\n")

    def clear_listbox(self, listbox):
        listbox.delete(0, tk.END)

    def refresh_full_needed(self):
        self.clear_listbox(self.full_needed_listbox)
        self.full_needed_listbox.insert(tk.END, *self.needed)
