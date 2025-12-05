import random
from inventory import Inventory
from logic import build_trip
from game_data import all_items, needed, tier6

# Remove 5 needed items
def main():
    for _ in range(5):
        if needed:
            needed.pop(random.randrange(len(needed)))

    inventory = Inventory([random.choice(all_items) for _ in range(10)])

    trip, missing_items = build_trip(inventory, needed)

    print("=== Trip Steps ===")
    for combo in trip:
        print(f'{combo[0]:<20} + {combo[1]:<20} → {combo[2]}')

    print("\n=== Missing Items Needed ===")
    for item in missing_items:
        print(item)

    print("\n=== Inventory ===")
    for item in inventory.items:
        print(item)
        
if __name__ == "__main__":
    main()