class Inventory:
    def __init__(self, items=None):
        self.items = set(items) if items else set()

    def add(self, item):
        self.items.add(item)

    def has(self, item):
        return item in self.items

    def __contains__(self, item):
        return item in self.items

    def __repr__(self):
        return f"Inventory({list(self.items)})"
