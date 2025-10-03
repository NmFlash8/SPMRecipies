class Item:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"Item(name='{self.name}')"


class Recipe:
    def __init__(self, item1: Item, item2: Item, product: Item):
        self.item1 = item1
        self.item2 = item2
        self.product = product

    def __str__(self):
        return f"Recipe({self.item1.name} + {self.item2.name} -> {self.product.name})"


class Trip:
    def __init__(self, recipes: list[Recipe] = None):
        self.recipes = recipes if recipes is not None else []

    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    def __str__(self):
        recipe_list = "\n  ".join(str(r) for r in self.recipes)
        return f"Trip with {len(self.recipes)} recipes:\n  {recipe_list}"


# -----------------------
# Example Usage
# -----------------------

# Items
flour = Item("Flour")
water = Item("Water")
bread = Item("Bread")
tomato = Item("Tomato")
soup = Item("Soup")

# Recipes
bread_recipe = Recipe(flour, water, bread)
soup_recipe = Recipe(tomato, water, soup)

# Trip
my_trip = Trip()
my_trip.add_recipe(bread_recipe)
my_trip.add_recipe(soup_recipe)

# Display
print(my_trip)
