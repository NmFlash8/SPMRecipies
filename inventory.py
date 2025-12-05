class Inventory:
    def __init__(self, items=None):
        # list allows duplicates naturally
        self.items = list(items) if items else []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        """Removes ONE instance of the item if it exists."""
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def count(self, item):
        return self.items.count(item)

    def has(self, item):
        return item in self.items

    def __contains__(self, item):
        return item in self.items

    def __repr__(self):
        return f"Inventory({self.items})"
