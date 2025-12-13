import dolphin_memory_engine as dme
from bighexlist import *

# Hook once at import time
dme.hook()

def read_all_items(dme):
    item_address = 0x804CEA88       # starting inventory address
    storage_address = 0x804CEA9C    # starting storage address
    item_count = 10                 # number of inventory items
    item_size = 2                   # size of each item in bytes
    storage_count = 32              # number of storage slots

    all_items = []

    # ===========================
    # Read INVENTORY items
    # ===========================
    for i in range(item_count):
        data = dme.read_bytes(item_address + i * item_size, item_size)

        # stop on null
        if data == b'\x00\x00':
            break

        value = int.from_bytes(data, "big")
        item_name = HexList.get(value, f"Unknown 0x{value:04X}")
        all_items.append(item_name)

    # ===========================
    # Read STORAGE items
    # ===========================
    for i in range(storage_count):
        data = dme.read_bytes(storage_address + i * item_size, item_size)

        # optional: skip nulls in storage but do NOT break
        if data == b'\x00\x00':
            continue

        value = int.from_bytes(data, "big")
        item_name = HexList.get(value, f"Unknown 0x{value:04X}")
        all_items.append(item_name)

    return all_items

def main():
    dme.hook()
    print("Connected to Dolphin Memory Engine\n")

    items = read_all_items(dme)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()
