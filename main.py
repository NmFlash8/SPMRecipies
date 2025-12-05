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

    trip = build_trip(inventory, needed, tier6)

    print("Trip:")
    print(trip)

    print("\nInventory:")
    print(inventory)

if __name__ == "__main__":
    main()