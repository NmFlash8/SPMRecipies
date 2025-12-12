import random
from combination import Combination
from trip import Trip
from game_data import *


# ============================================================
# BEST COMBINATION PICKING (DETERMINISTIC)
# ============================================================

def pick_best_combo(combos, inventory):
    """
    Deterministically pick the best combo from equally high-scoring options.
    Uses a secondary scoring heuristic for stable, non-random selection.
    """

    def secondary_score(combo):
        score = 0

        # Prefer items already in inventory
        if combo.item1 in inventory.items:
            score += 5
        if combo.item2 in inventory.items:
            score += 5

        # Penalize missing ingredients
        if combo.item1 not in inventory.items:
            score -= 1
        if combo.item2 not in inventory.items:
            score -= 1

        # Stable fallback so results never change order randomly
        score -= len(combo.item1) + len(combo.item2)

        return score

    # Sort by:
    #   1. highest secondary_score()
    #   2. alphabetical fallback (item1, item2)
    combos_sorted = sorted(
        combos,
        key=lambda combo: (-secondary_score(combo), combo.item1, combo.item2)
    )

    return combos_sorted[0]


# ============================================================
# FIND ALL BEST-SCORING COMBINATIONS
# ============================================================

def find_best_combinations(goal, inventory):
    """Return all Combination objects that tie for best score for `goal`."""
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


# ============================================================
# RECURSIVE TRIP BUILDER
# ============================================================

def recursive_trip(goal, inventory, trip, chain, missing_items):
    """Recursively collect combinations needed to craft `goal`."""

    # Cap recursion depth (avoid runaway chains)
    if len(trip) >= 10:
        return

    # Already owned
    if goal in inventory.items:
        return

    # Uncraftable or shop-only
    if goal == "" or goal in shop_items or goal not in recipes:
        missing_items.add(goal)
        return

    # Detect crafting loops
    if goal in chain:
        return

    # Determine best combination
    best_combos = find_best_combinations(goal, inventory)
    if not best_combos:
        missing_items.add(goal)
        return

    chosen_combo = pick_best_combo(best_combos, inventory)

    itemA = chosen_combo.item1
    itemB = chosen_combo.item2

    # Add to crafting trip
    trip.append((itemA, itemB, goal))

    # Track recursion path
    chain.add(goal)

    # Recurse into ingredients
    recursive_trip(itemA, inventory, trip, chain, missing_items)

    if itemB:  # Some recipes are only 1 ingredient
        recursive_trip(itemB, inventory, trip, chain, missing_items)

    # Done exploring this branch
    chain.remove(goal)


# ============================================================
# MAIN ENTRY POINT
# ============================================================

def build_trip(inventory, needed):
    """Pick a tier 6 item from needed and generate the best trip for it."""
    trip = []
    missing_items = set()
    chain = set()

    # Only generate trips for needed tier-6 goals
    goals = list(set(needed) & set(tier6))
    if not goals:
        return trip, missing_items

    # Pick the FIRST alphabetically instead of random
    # (consistent, predictable behavior)
    first_goal = sorted(goals)[0]

    recursive_trip(first_goal, inventory, trip, chain, missing_items)

    return trip, missing_items
