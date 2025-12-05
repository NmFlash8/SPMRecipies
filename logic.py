import random
from combination import Combination
from trip import Trip
from game_data import recipes, shop_items

def find_best_combinations(goal, inventory):
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


def recursive_trip(goal, inventory, trip, chain):
    if len(trip) >= 10:
        return

    if goal in chain:
        return
    if goal == "" or goal in shop_items:
        return
    if goal not in recipes:
        return

    best = find_best_combinations(goal, inventory)
    if not best:
        return

    chosen = random.choice(best)
    trip.add(chosen)

    chain.add(goal)

    recursive_trip(chosen.item1, inventory, trip, chain)
    if chosen.item2:
        recursive_trip(chosen.item2, inventory, trip, chain)

    chain.remove(goal)


def build_trip(inventory, needed, tier6):
    trip = Trip()
    chain = set()

    goals = list(set(needed) & set(tier6))
    if not goals:
        return trip

    first_goal = random.choice(goals)
    recursive_trip(first_goal, inventory, trip, chain)
    return trip
