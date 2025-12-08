import tkinter as tk
from tkinter import ttk
import random
from inventory import Inventory
from logic import build_trip
from game_data import all_items, needed, tier6

class TripGUI:
    def __init__(self, master):
        self.master = master
        master.title("Trip Builder")

        # Inventory
        self.inventory_label = ttk.Label(master, text="Inventory:")
        self.inventory_label.grid(row=0, column=0, sticky="w")

        self.inventory_listbox = tk.Listbox(master, width=30, height=10)
        self.inventory_listbox.grid(row=1, column=0, padx=5, pady=5)

        # Trip steps
        self.trip_label = ttk.Label(master, text="Trip Steps:")
        self.trip_label.grid(row=0, column=1, sticky="w")

        self.trip_listbox = tk.Listbox(master, width=60, height=10)
        self.trip_listbox.grid(row=1, column=1, padx=5, pady=5)

        # Missing items
        self.missing_label = ttk.Label(master, text="Missing Items Needed:")
        self.missing_label.grid(row=2, column=0, sticky="w")

        self.missing_listbox = tk.Listbox(master, width=30, height=10)
        self.missing_listbox.grid(row=3, column=0, padx=5, pady=5)

        # Needed list
        self.full_needed_label = ttk.Label(master, text="All Needed Recipes (Full List):")
        self.full_needed_label.grid(row=2, column=1, sticky="w")

        self.full_needed_listbox = tk.Listbox(master, width=60, height=10)
        self.full_needed_listbox.grid(row=3, column=1, padx=5, pady=5)

        # Buttons
        self.generate_button = ttk.Button(master, text="Generate Trip", command=self.generate_trip)
        self.generate_button.grid(row=4, column=0, pady=10)

        self.reset_needed_button = ttk.Button(master, text="Remove 5 Needed Items", command=self.remove_needed)
        self.reset_needed_button.grid(row=4, column=1, pady=10)

        # Initialize data
        self.inventory = Inventory([random.choice(all_items) for _ in range(10)])

        # Initial fill of needed list
        self.refresh_full_needed()

    def refresh_full_needed(self):
        """Refresh the full 96-needed listbox."""
        self.full_needed_listbox.delete(0, tk.END)
        for recipe in needed:
            self.full_needed_listbox.insert(tk.END, recipe)

    def remove_needed(self):
        """Remove 5 needed items at random."""
        global needed
        for _ in range(5):
            if needed:
                needed.pop(random.randrange(len(needed)))

        self.refresh_full_needed()
        self.generate_trip()

    def generate_trip(self):
        """Generate trip steps & update UI."""
        # Show inventory
        self.inventory_listbox.delete(0, tk.END)
        for item in self.inventory.items:
            self.inventory_listbox.insert(tk.END, item)

        # Build trip
        trip, missing_items = build_trip(self.inventory, needed)

        # Show trip steps
        self.trip_listbox.delete(0, tk.END)
        for combo in trip:
            self.trip_listbox.insert(tk.END, f'{combo[0]} + {combo[1]} → {combo[2]}')

        # Show missing
        self.missing_listbox.delete(0, tk.END)
        for item in missing_items:
            self.missing_listbox.insert(tk.END, item)

        # Refresh full needed list
        self.refresh_full_needed()

if __name__ == "__main__":
    root = tk.Tk()
    gui = TripGUI(root)
    root.mainloop()