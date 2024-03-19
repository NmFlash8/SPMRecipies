import csv
from all_items import *
from shop_items import *
from recipe_dictionary import *
from needed import *
import os

'''
This method is "Brute Forcing" all individual ways to make an item.

This File will create a directory that will create CSV files with all possible paths to make the given item.
A maximum of 10 items will be allowed to be used.
if the set doesn't end in an item that can be found or bought the current chain will be scrapped.

Dyllis Lunch owns the most possible ways to make boasting 175k different ways to make the item with 10 inventory slots
'''

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_path(path, place=0, depth=0, max_depth=10):
    if place >= len(path):
        all_paths.append(path)
        with open(os.path.join('AllRoutes', f'{item_search}.csv'), 'a', newline='') as csv_file:  # Save inside 'AllRoutes' folder
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(path)
        print(len(all_paths), path)
        return

    target = path[place]
    place += 1
    depth += 1

    if depth >= max_depth:
        return
    
    if len(path) > 10:
        return
    
    if target in shop_items:
        find_path(path, place, depth, max_depth)

    if not target:  # Check if the target is an empty string
        find_path(path, place, depth, max_depth)

    for recipe in recipes.get(target, []):
        new_path = list(path)
        new_path.append(recipe[0])
        new_path.append(recipe[1])
        find_path(new_path, place, depth, max_depth)

# Create 'AllRoutes' folder if it doesn't exist
if not os.path.exists('AllRoutes'):
    os.makedirs('AllRoutes')

for item_search in needed:
    if item_search in teir3:
        continue
    all_paths = []
    current_path = [item_search]
    find_path(current_path)

    print(f"Paths processed for {item_search}")

print("All paths processing completed.")
