import tkinter as tk
from tkinter import ttk
import random
from inventory import Inventory
from logic import build_trip
from game_data import all_items, needed, tier6


class TripGUI:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Calculator")

        # Data
        self.inventory = Inventory([random.choice(all_items) for _ in range(10)])

        # UI Layout
        self.create_add_item_section()
        self.create_inventory_section()
        self.create_trip_section()
        self.create_missing_section()
        self.create_full_needed_section()
        self.create_buttons()

        # Initialize
        self.refresh_full_needed()
        self.generate_trip()

    # =========================================================
    # UI SECTION BUILDERS
    # =========================================================

    def create_add_item_section(self):
        ttk.Label(self.master, text="Add Item to Inventory:") \
            .grid(row=0, column=0, sticky="w")

        self.add_entry = ttk.Entry(self.master, width=30)
        self.add_entry.grid(row=1, column=0, padx=5, sticky="w")
        self.add_entry.bind("<KeyRelease>", self.update_autofill)
        self.add_entry.bind("<Return>", self.add_item_from_enter)

        self.autofill_listbox = tk.Listbox(self.master, width=30, height=5)
        self.autofill_listbox.grid(row=2, column=0, padx=5, pady=(0, 10), sticky="w")
        self.autofill_listbox.bind("<<ListboxSelect>>", self.add_item_from_click)

    def create_inventory_section(self):
        ttk.Label(self.master, text="Inventory:") \
            .grid(row=3, column=0, sticky="w")

        self.inventory_listbox = tk.Listbox(self.master, width=30, height=10)
        self.inventory_listbox.grid(row=4, column=0, padx=5, pady=5)
        self.inventory_listbox.bind("<<ListboxSelect>>", self.remove_inventory_item)

    def create_trip_section(self):
        ttk.Label(self.master, text="Trip Steps:") \
            .grid(row=0, column=1, sticky="w")

        self.trip_listbox = tk.Listbox(self.master, width=60, height=10)
        self.trip_listbox.grid(row=1, column=1, rowspan=3, padx=5, pady=5)

    def create_missing_section(self):
        ttk.Label(self.master, text="Missing Items Needed:") \
            .grid(row=3, column=1, sticky="w")

        self.missing_listbox = tk.Listbox(self.master, width=60, height=10)
        self.missing_listbox.grid(row=4, column=1, padx=5, pady=5)

    def create_full_needed_section(self):
        ttk.Label(self.master, text="All Needed Recipes (Full List):") \
            .grid(row=5, column=0, sticky="w")

        self.full_needed_listbox = tk.Listbox(self.master, width=60, height=10)
        self.full_needed_listbox.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        self.full_needed_listbox.bind("<<ListboxSelect>>", self.remove_needed_item)

    def create_buttons(self):
        ttk.Button(self.master, text="Generate Trip", command=self.generate_trip) \
            .grid(row=7, column=0, pady=10)

        ttk.Button(self.master, text="Remove 5 Needed Items", command=self.remove_needed) \
            .grid(row=7, column=1, pady=10)

    # =========================================================
    # AUTOFILL LOGIC
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
            item = self.autofill_listbox.get(selection[0])
            self.add_item_to_inventory(item)

    def add_item_from_enter(self, event):
        if self.autofill_listbox.size() > 0:
            self.add_item_to_inventory(self.autofill_listbox.get(0))

    # =========================================================
    # REMOVE HANDLERS
    # =========================================================

    def remove_inventory_item(self, event):
        selection = self.inventory_listbox.curselection()
        if selection:
            removed = self.inventory.items.pop(selection[0])
            print("Removed from inventory:", removed)
            self.generate_trip()

    def remove_needed_item(self, event):
        selection = self.full_needed_listbox.curselection()
        if selection:
            removed = needed.pop(selection[0])
            print("Removed from needed:", removed)
            self.generate_trip()

    # =========================================================
    # HELPER FUNCTIONS
    # =========================================================

    def clear_listbox(self, listbox):
        listbox.delete(0, tk.END)

    def refresh_full_needed(self):
        self.clear_listbox(self.full_needed_listbox)
        self.full_needed_listbox.insert(tk.END, *needed)

    def remove_needed(self):
        for _ in range(5):
            if needed:
                needed.pop(random.randrange(len(needed)))

        self.refresh_full_needed()
        self.generate_trip()

    # =========================================================
    # MAIN TRIP LOGIC
    # =========================================================

    def generate_trip(self):
        # Inventory
        self.clear_listbox(self.inventory_listbox)
        self.inventory_listbox.insert(tk.END, *self.inventory.items)

        # Trip + Missing Items
        trip, missing_items = build_trip(self.inventory, needed)

        self.clear_listbox(self.trip_listbox)
        for a, b, c in trip:
            self.trip_listbox.insert(tk.END, f"{a} + {b} → {c}")

        self.clear_listbox(self.missing_listbox)
        self.missing_listbox.insert(tk.END, *missing_items)

        # Needed recipes refresh
        self.refresh_full_needed()


if __name__ == "__main__":
    root = tk.Tk()
    TripGUI(root)
    root.mainloop()
