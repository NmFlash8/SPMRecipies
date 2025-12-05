from game_data import recipes
import random

all_items = ['Awesome Snack', 'Berry Snow Bunny', 'Big Egg', 'Black Apple', 'Block Block', 'Block Meal', 'Blue Apple', 'Bone-In Cut', 'Cake Mix', 'Catch Card', 'Catch Card SP', 'Choco Pasta Dish', 'Chocolate Cake', 'Couple\'s Cake', 'Courage Shell', 'Dangerous Delight', 'Dayzee Syrup', 'Dayzee Tear', 'Dried Shroom', 'Dyllis Breakfast', 'Dyllis Deluxe', 'Dyllis Dinner', 'Dyllis Dynamite', 'Dyllis Lunch', 'Dyllis Special', 'Egg Bomb', 'Electro Pop', 'Emergency Ration', 'Fire Burst', 'Fresh Pasta Bunch', 'Fresh Veggie', 'Fried Egg', 'Fried Shroom Plate', 'Fruit Parfait', 'Fruity Cake', 'Fruity Hamburger', 'Fruity Punch', 'Fruity Shroom', 'Ghost Shroom', 'Gingerbread House', 'Gold Bar', 'Gold Bar x3', 'Gold Medal', 'Golden Choco-bar', 'Golden Leaf', 'Golden Meal', 'Gorgeous Steak', 'Gradual Syrup', 'Hamburger', 'Healthy Salad', 'Heartful Cake', 'Heavy Meal', 'Herb Tea', 'Honey Candy', 'Honey Jar', 'Honey Shroom', 'Honey Super', 'Horsetail', 'Horsetail Tart', 'Hot Dog', 'Hot Sauce', 'HP Plus', 'Ice Storm', 'Ink Pasta Dish', 'Inky Sauce', 'Inky Soup', 'Keel Mango', 'Koopa Dumpling', 'Koopa Pilaf', 'Koopa Tea', 'Koopasta Dish', 'Life Shroom', 'Long-Last Shake', 'Love Noodle Dish', 'Love Pudding', 'Lovely Chocolate', 'Luxurious Set', 'Mango Juice', 'Mango Pudding', 'Meat Pasta Dish', 'Megaton Dinner', 'Meteor Meal', 'Mighty Tonic', 'Mild Cocoa Bean', 'Miracle Dinner', 'Mistake', 'Mixed Shake', 'Mousse', 'Mushroom Crepe', 'Odd Dinner', 'Omelette Plate', 'Orange Apple', 'Peach Juice', 'Peach Tart', 'Peachy Peach', 'Pink Apple', 'Poison Shroom', 'POW Block', 'Power Plus', 'Power Steak', 'Primordial Dinner', 'Primordial Fruit', 'Red Apple', 'Roast Horsetail', 'Roast Meat', 'Roast Shroom Dish', 'Roast Whacka Bump', 'Sap Muffin', 'Sap Soup', 'Sap Syrup', 'Shell Shock', 'Shooting Star', 'Shroom Broth', 'Shroom Cake', 'Shroom Choco-bar', 'Shroom Delicacy', 'Shroom Pudding', 'Shroom Shake', 'Shroom Steak', 'Sky Juice', 'Sleepy Sheep', 'Slimy Extract', 'Slimy Shroom', 'Smelly Herb', 'Snow Bunny', 'Snow Cone', 'Space Food', 'Spaghetti Plate', 'Spicy Dinner', 'Spicy Pasta Dish', 'Spicy Soup', 'Stamina Juice', 'Standard Chocolate', 'Star Medal', 'Stop Watch', 'Super Shroom Shake', 'Sweet Choco-bar', 'Sweet Cookie Snack', 'Thunder Rage', 'Town Special', 'Trial Stew', 'Turtley Leaf', 'Ultra Shroom Shake', 'Veggie Set', 'Volcano Shroom', 'Volt Shroom', 'Warm Cocoa', 'Weird Extract', 'Whacka Bump']
shop_items = ['Fire Burst', 'Ice Storm', 'Thunder Rage', 'Shooting Star', 'POW Block', 'Shell Shock', 'Gold Bar', 'Gold Bar x3', 'Block Block', 'Volt Shroom', 'Ghost Shroom', 'Sleepy Sleep', 'Slimy Shroom', 'Stop Watch', 'Shroom Shake', 'Super Shroom Shake', 'Ultra Shroom Shake', 'Dried Shroom', 'Life Shroom', 'Long-Last Shake', 'Blue Apple', 'Yellow Apple', 'Red Apple', 'Pink Apple', 'Black Apple', 'Poison Shroom', 'Peachy Peach', 'Keel Mango', 'Primordial Fruit', 'Golden Leaf', 'Turtley Leaf', 'Cake Mix', 'Whacka Bump', 'Horsetail', 'Fresh Pasta Bunch', 'Hot Sauce', 'Inky Sauce', 'Dayzee Tear', 'Sap Soup', 'Bone-In Cut', 'Fresh Veggie', 'Smelly Herb', 'Honey Jar', 'Power Steak', 'Big Egg', 'Mild Cocoa Bean', 'Mighty Tonic', 'Mystery Box', 'Orange Apple', 'Red Apple']
tier1 = ['Spicy Soup', 'Snow Cone', 'Electro Pop', 'Meteor Meal', 'Megaton Dinner', 'Block Meal', 'Courage Shell', 'Mistake', 'Mistake', 'Golden Meal', 'Golden Meal', 'Fried Shroom Plate', 'Fried Shroom Plate', 'Fried Shroom Plate', 'Roast Shroom Dish', 'Roast Shroom Dish', 'Shroom Steak', 'Slimy Extract', 'Dangerous Delight', 'Dangerous Delight', 'Sweet Cookie Snack', 'Fried Egg', 'Spaghetti Plate', 'Hamburger', 'Roast Meat', 'Peach Juice', 'Mango Juice', 'Sky Juice', 'Sky Juice', 'Sky Juice', 'Sky Juice', 'Town Special', 'Warm Cocoa', 'Honey Candy', 'Fire Burst', 'Inky Soup', 'Dayzee Syrup', 'Sap Syrup', 'Healthy Salad', 'Koopa Tea', 'Herb Tea', 'Gold Bar', 'Roast Whacka Bump', 'Roast Horsetail']      
tier2 = ['Emergency Ration', 'Space Food', 'Volt Shroom', 'Heavy Meal', 'Mushroom Crepe', 'Shroom Cake', 'Egg Bomb', 'Shroom Pudding', 'Love Pudding', 'Mousse', 'Hot Dog', 'Meat Pasta Dish', 'Gorgeous Steak', 'Fruity Shroom', 'Gradual Syrup', 'Peach Tart', 'Fruity Hamburger', 'Mango Pudding', 'Fruity Punch', 'Fruity Cake', 'Omelette Plate', 'Primordial Dinner', 'Lovely Chocolate', 'Shroom Choco-bar', 'Standard Chocolate', 'Chocolate Cake', 'Choco Pasta Dish', 'Golden Choco-bar', 'Sweet Choco-bar', 'Honey Shroom', 'Honey Super', 'Volcano Shroom', 'Awesome Snack', 'Spicy Dinner', 'Spicy Pasta Dish', 'Ink Pasta Dish', 'Stamina Juice', 'Shroom Delicacy', 'Sap Muffin', 'Weird Extract', 'Snow Bunny', 'Koopa Dumpling', 'Koopasta Dish', 'Koopa Pilaf', 'Shroom Broth', 'Horsetail Tart']
tier3 = ['Fruit Parfait', 'Life Shroom', 'Super Shroom Shake', 'Heartful Cake', 'Love Noodle Dish', 'Dyllis Breakfast', 'Dyllis Lunch', 'Odd Dinner', 'Dyllis Dinner', 'Veggie Set']
tier4 = ['Mixed Shake', 'Dyllis Special', 'Dyllis Deluxe']
tier5 = ['Berry Snow Bunny']
tier6 = ['Gingerbread House', "Couple's Cake", 'Trial Stew', 'Luxurious Set', 'Dyllis Dynamite']
difficulty = {'Fire Burst': 1, 'Ice Storm': 2, 'Thunder Rage': 3, 'Shooting Star': 4, 'POW Block': 3, 'Shell Shock': 2, 'Gold Bar': 4, 'Gold Bar x3': 8, 'Block Block': 4, 'Volt Shroom': 3, 'Ghost Shroom': 3, 'Sleepy Sleep': 1, 'Slimy Shroom': 4, 'Stop Watch': 2, 'Shroom Shake': 1, 'Super Shroom Shake': 3, 'Ultra Shroom Shake': 3, 'Dried Shroom': 2, 'Life Shroom': 3, 'Long-Last Shake': 2, 'Blue Apple': 3, 'Yellow Apple': 3, 'Red Apple': 3, 'Pink Apple': 3, 'Black Apple': 3, 'Poison Shroom': 3, 'Peachy Peach': 2, 'Keel Mango': 2, 'Primordial Fruit': 2, 'Golden Leaf': 5, 'Turtley Leaf': 5, 'Cake Mix': 2, 'Whacka Bump': 3, 'Horsetail': 2, 'Fresh Pasta Bunch': 2, 'Hot Sauce': 2, 'Inky Sauce': 5, 'Dayzee Tear': 3, 'Sap Soup': 3, 'Bone-In Cut': 5, 'Fresh Veggie': 2, 'Smelly Herb': 2, 'Honey Jar': 2, 'Power Steak': 2, 'Big Egg': 2, 'Mild Cocoa Bean': 2, 'Mighty Tonic': 3 }
tiers = {'Miracle Dinner': 3, 'Spicy Soup': 1, 'Snow Cone': 1, 'Electro Pop': 1, 'Meteor Meal': 1, 'Megaton Dinner': 1, 'Block Meal': 1, 'Courage Shell': 1, 'Mistake': 1, 'Golden Meal': 1, 'Fried Shroom Plate': 1, 'Roast Shroom Dish': 1, 'Shroom Steak': 1, 'Slimy Extract': 1, 'Dangerous Delight': 1, 'Sweet Cookie Snack': 1, 'Fried Egg': 1, 'Spaghetti Plate': 1, 'Hamburger': 1, 'Roast Meat': 1, 'Peach Juice': 1, 'Mango Juice': 1, 'Sky Juice': 1, 'Town Special': 1, 'Warm Cocoa': 1, 'Honey Candy': 1, 'Fire Burst': 0, 'Inky Soup': 1, 'Dayzee Syrup': 1, 'Sap Syrup': 1, 'Healthy Salad': 1, 'Koopa Tea': 1, 'Herb Tea': 1, 'Gold Bar': 0, 'Roast Whacka Bump': 1, 'Roast Horsetail': 1, 'Emergency Ration': 2, 'Space Food': 2, 'Volt Shroom': 0, 'Heavy Meal': 2, 'Mushroom Crepe': 2, 'Shroom Cake': 2, 'Egg Bomb': 2, 'Shroom Pudding': 2, 'Love Pudding': 2, 'Mousse': 2, 'Hot Dog': 2, 'Meat Pasta Dish': 2, 'Gorgeous Steak': 2, 'Fruity Shroom': 2, 'Gradual Syrup': 2, 'Peach Tart': 2, 'Fruity Hamburger': 2, 'Mango Pudding': 2, 'Fruity Punch': 2, 'Fruity Cake': 2, 'Omelette Plate': 2, 'Primordial Dinner': 2, 'Lovely Chocolate': 2, 'Shroom Choco-bar': 2, 'Standard Chocolate': 2, 'Chocolate Cake': 2, 'Choco Pasta Dish': 2, 'Golden Choco-bar': 2, 'Sweet Choco-bar': 2, 'Honey Shroom': 2, 'Honey Super': 2, 'Volcano Shroom': 2, 'Awesome Snack': 2, 'Spicy Dinner': 2, 'Spicy Pasta Dish': 2, 'Ink Pasta Dish': 2, 'Stamina Juice': 2, 'Shroom Delicacy': 2, 'Sap Muffin': 2, 'Weird Extract': 2, 'Snow Bunny': 2, 'Koopa Dumpling': 2, 'Koopasta Dish': 2, 'Koopa Pilaf': 2, 'Shroom Broth': 2, 'Horsetail Tart': 2, 'Fruit Parfait': 3, 'Life Shroom': 0, 'Super Shroom Shake': 0, 'Heartful Cake': 3, 'Love Noodle Dish': 3, 'Dyllis Breakfast': 3, 'Dyllis Lunch': 3, 'Odd Dinner': 3, 'Dyllis Dinner': 3, 'Veggie Set': 3, 'Mixed Shake': 4, 'Dyllis Special': 4, 'Dyllis Deluxe': 4, 'Gingerbread House': 6, 'Berry Snow Bunny': 5, "Couple's Cake": 6, 'Trial Stew': 6, 'Luxurious Set': 6, 'Dyllis Dynamite': 6}
needed = ['Spicy Soup', 'Snow Cone', 'Electro Pop', 'Meteor Meal', 'Megaton Dinner', 'Block Meal', 'Courage Shell', 'Mistake', 'Golden Meal', 'Fried Shroom Plate', 'Roast Shroom Dish', 'Shroom Steak', 'Slimy Extract', 'Dangerous Delight', 'Sweet Cookie Snack', 'Fried Egg', 'Spaghetti Plate', 'Hamburger', 'Roast Meat', 'Peach Juice', 'Mango Juice', 'Sky Juice', 'Town Special', 'Warm Cocoa', 'Honey Candy', 'Fire Burst', 'Inky Soup', 'Dayzee Syrup', 'Sap Syrup', 'Healthy Salad', 'Koopa Tea', 'Herb Tea', 'Gold Bar', 'Roast Whacka Bump', 'Roast Horsetail', 'Emergency Ration', 'Space Food', 'Volt Shroom', 'Heavy Meal', 'Mushroom Crepe', 'Shroom Cake', 'Egg Bomb', 'Shroom Pudding', 'Love Pudding', 'Mousse', 'Hot Dog', 'Meat Pasta Dish', 'Gorgeous Steak', 'Fruity Shroom', 'Gradual Syrup', 'Peach Tart', 'Fruity Hamburger', 'Mango Pudding', 'Fruity Punch', 'Fruity Cake', 'Omelette Plate', 'Primordial Dinner', 'Lovely Chocolate', 'Shroom Choco-bar', 'Standard Chocolate', 'Chocolate Cake', 'Choco Pasta Dish', 'Golden Choco-bar', 'Sweet Choco-bar', 'Honey Shroom', 'Honey Super', 'Volcano Shroom', 'Awesome Snack', 'Spicy Dinner', 'Spicy Pasta Dish', 'Ink Pasta Dish', 'Stamina Juice', 'Shroom Delicacy', 'Sap Muffin', 'Weird Extract', 'Snow Bunny', 'Koopa Dumpling', 'Koopasta Dish', 'Koopa Pilaf', 'Shroom Broth', 'Horsetail Tart', 'Fruit Parfait', 'Life Shroom', 'Super Shroom Shake', 'Heartful Cake', 'Love Noodle Dish', 'Dyllis Breakfast', 'Dyllis Lunch', 'Odd Dinner', 'Dyllis Dinner', 'Veggie Set', 'Mixed Shake', 'Dyllis Special', 'Dyllis Deluxe', 'Gingerbread House', 'Berry Snow Bunny', 'Couple\'s Cake', 'Trial Stew', 'Luxurious Set', 'Dyllis Dynamite']

def combination_score(combination, inventory):
    item1, item2 = combination

    def get_diff(item):
        if item:
            if item in difficulty:
                return difficulty[item]
            if item in tiers:
                # Convert tier to difficulty — tweak scaling if needed
                return tiers[item] * 2  
            print(f"[WARNING] No difficulty or tier found for: {item}")
        return 0

    diff1 = get_diff(item1)
    diff2 = get_diff(item2)

    score1 = -diff1 / 2 if item1 in inventory else -diff1
    score2 = -diff2 / 2 if item2 in inventory else -diff2

    return score1 + score2


def find_best_combinations(goal, inventory):
        best_combos = []
        best_score = float('-inf')  # lowest possible starting score

        for combination in recipes[goal]:
            score = combination_score(combination, inventory)
            # print(combination, score)

            if score > best_score: # Reset the list if we find a new highest.
                best_score = score
                best_combos = [combination]

            elif score == best_score:
                best_combos.append(combination)
        return best_combos

def recursive_trip(goal, inventory, trip, chain):
    if len(trip) >= 10:
        return
    
    # Stop circular dependency loops
    if goal in chain:
        return
    
    if goal == "" or goal in shop_items:
        return

    if goal not in recipes:
        return

    best_combos = find_best_combinations(goal, inventory)
    if not best_combos:
        return

    chosen_combo = random.choice(best_combos)
    itemA, itemB = chosen_combo

    # Append including the product (goal)
    trip.append((itemA, itemB, goal))

    # Track chain to stop cycles
    chain.add(goal)

    recursive_trip(itemA, inventory, trip, chain)
    recursive_trip(itemB, inventory, trip, chain)

    chain.remove(goal)

def build_trip(inventory, needed):
    trip = []
    chain = set()  # renamed for clarity

    goals = list(set(needed) & set(tier6))
    if not goals:
        return trip

    first_goal = random.choice(goals)
    recursive_trip(first_goal, inventory, trip, chain)

    return trip

# Remove 10 items at random
for _ in range(5):
    if needed:  # make sure the list isn't empty
        needed.pop(random.randrange(len(needed)))

# Fill Inventory with 10 random items from all_items
inventory = [random.choice(all_items) for _ in range(10)]

trip = build_trip(inventory, needed)
for combination in trip:
    print(combination)

print()
print("--Inventory--")
for item in inventory:
    print(item)