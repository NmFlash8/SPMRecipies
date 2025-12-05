import random
from combination import Combination
from trip import Trip
from game_data import *


def find_best_combinations(goal, inventory):
    """Return a list of the best-scoring Combination objects to make `goal`."""
    best_combos = []
    best_score = float('-inf')

    for (item1, item2) in recipes.get(goal, []):
        combo = Combination(item1, goal, item2)
        score = combo.score(inventory)

        if score > best_score:
            best_score = score
            best_combos = [combo]
        elif score == best_score:
            best_combos.append(combo)

    return best_combos


def recursive_trip(goal, inventory, trip, chain, missing_items):
    """Recursively collect combinations needed to craft `goal`."""

    # Stop when we hit the max trip length
    if len(trip) >= 10:
        return

    # Already own the item → no need to craft it
    if goal in inventory.items:
        return

    # If the item is uncraftable, blank, shop-only, or has no recipe
    if goal == "" or goal in shop_items or goal not in recipes:
        missing_items.add(goal)
        return

    # Prevent circular crafting loops
    if goal in chain:
        return

    # Select the best combination to craft this item
    best_combos = find_best_combinations(goal, inventory)
    if not best_combos:
        missing_items.add(goal)
        return

    chosen_combo = random.choice(best_combos)

    # Extract ingredients safely from Combination object
    itemA = chosen_combo.item1
    itemB = chosen_combo.item2

    # Add crafting step to trip
    trip.append((itemA, itemB, goal))

    # Track recursion chain
    chain.add(goal)

    # Recurse into required ingredients
    recursive_trip(itemA, inventory, trip, chain, missing_items)

    if itemB:  # Some recipes only need 1 ingredient
        recursive_trip(itemB, inventory, trip, chain, missing_items)

    # Done exploring this branch
    chain.remove(goal)


def build_trip(inventory, needed):
    """Pick a tier 6 item from `needed` and recursively generate a trip."""
    trip = []
    missing_items = set()
    chain = set()

    # Only generate trips for tier 6 items the user needs
    goals = list(set(needed) & set(tier6))
    if not goals:
        return trip, missing_items

    first_goal = random.choice(goals)

    recursive_trip(first_goal, inventory, trip, chain, missing_items)

    return trip, missing_items
