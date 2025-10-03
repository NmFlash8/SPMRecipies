from recipe_dictionary import recipes
from shop_items import shop_items as shops

needed = [
    'Spicy Soup',
    'Snow Cone',
    'Electro Pop',
    'Meteor Meal',
    'Megaton Dinner',
    'Block Meal',
    'Courage Shell',
    'Mistake',
    'Golden Meal',
    'Fried Shroom Plate',
    'Roast Shroom Dish',
    'Shroom Steak',
    'Slimy Extract',
    'Dangerous Delight',
    'Sweet Cookie Snack',
    'Fried Egg',
    'Spaghetti Plate',
    'Hamburger',
    'Roast Meat',
    'Peach Juice',
    'Mango Juice',
    'Sky Juice',
    'Town Special',
    'Warm Cocoa',
    'Honey Candy',
    'Fire Burst',
    'Inky Soup',
    'Dayzee Syrup',
    'Sap Syrup',
    'Healthy Salad',
    'Koopa Tea',
    'Herb Tea',
    'Gold Bar',
    'Roast Whacka Bump',
    'Roast Horsetail',
    'Emergency Ration',
    'Space Food',
    'Volt Shroom',
    'Heavy Meal',
    'Mushroom Crepe',
    'Shroom Cake',
    'Egg Bomb',
    'Shroom Pudding',
    'Love Pudding',
    'Mousse',
    'Hot Dog',
    'Meat Pasta Dish',
    'Gorgeous Steak',
    'Fruity Shroom',
    'Gradual Syrup',
    'Peach Tart',
    'Fruity Hamburger',
    'Mango Pudding',
    'Fruity Punch',
    'Fruity Cake',
    'Omelette Plate',
    'Primordial Dinner',
    'Lovely Chocolate',
    'Shroom Choco-bar',
    'Standard Chocolate',
    'Chocolate Cake',
    'Choco Pasta Dish',
    'Golden Choco-bar',
    'Sweet Choco-bar',
    'Honey Shroom',
    'Honey Super',
    'Volcano Shroom',
    'Awesome Snack',
    'Spicy Dinner',
    'Spicy Pasta Dish',
    'Ink Pasta Dish',
    'Stamina Juice',
    'Shroom Delicacy',
    'Sap Muffin',
    'Weird Extract',
    'Snow Bunny',
    'Koopa Dumpling',
    'Koopasta Dish',
    'Koopa Pilaf',
    'Shroom Broth',
    'Horsetail Tart',
    'Fruit Parfait',
    'Life Shroom',
    'Super Shroom Shake',
    'Heartful Cake',
    'Love Noodle Dish',
    'Dyllis Breakfast',
    'Dyllis Lunch',
    'Odd Dinner',
    'Dyllis Dinner',
    'Veggie Set',
    'Mixed Shake',
    'Dyllis Special',
    'Dyllis Deluxe',
    'Gingerbread House',
    'Berry Snow Bunny',
    'Couple\'s Cake',
    'Trial Stew',
    'Luxurious Set',
    'Dyllis Dynamite',
]

tier1 = []
tier2 = []
tier3 = []
tier4 = []
tier5 = []
tier6 = []
tier7 = []

#########################################
for tier in needed:
    for combos in recipes[tier]:
        item_1, item_2 = combos
        if item_1 == "" or item_2 == "":
            tier1.append(tier)

# Remove all items in tier1 from needed
needed[:] = [x for x in needed if x not in tier1]
print("T1")
print(tier1)
print()

#########################################
for tier in needed:
    for combos in recipes[tier]:
        item_1, item_2 = combos
        if item_1 in shops and item_2 in shops:
            tier2.append(tier)
            break

needed[:] = [x for x in needed if x not in tier2]
print("T2")
print(tier2)
print()

#########################################
for tier in needed:
    for combos in recipes[tier]:
        item_1, item_2 = combos
        if item_1 in shops and item_2 in tier1 or \
           item_1 in tier1 and item_2 in shops:
            tier3.append(tier)
            break

needed[:] = [x for x in needed if x not in tier3]
print("T3")
print(tier3)
print()

#########################################
for tier in needed:
    for combos in recipes[tier]:
        item_1, item_2 = combos
        if item_1 in tier1 and item_2 in tier1 or \
           item_1 in tier1 and item_2 in tier1:
            tier4.append(tier)
            break

needed[:] = [x for x in needed if x not in tier4]
print("T4")
print(tier4)
print()

#########################################
for tier in needed:
    for combos in recipes[tier]:
        item_1, item_2 = combos
        if item_1 in shops and item_2 in tier2 or \
           item_1 in tier2 and item_2 in shops:
            tier5.append(tier)
            break

needed[:] = [x for x in needed if x not in tier5]
print("T5")
print(tier5)
print()

print("T6")
print(needed)
print()

tier1 = ['Spicy Soup', 'Snow Cone', 'Electro Pop', 'Meteor Meal', 'Megaton Dinner', 'Block Meal', 'Courage Shell', 'Mistake', 'Mistake', 'Golden Meal', 'Golden Meal', 'Fried Shroom Plate', 'Fried Shroom Plate', 'Fried Shroom Plate', 'Roast Shroom Dish', 'Roast Shroom Dish', 'Shroom Steak', 'Slimy Extract', 'Dangerous Delight', 'Dangerous Delight', 'Sweet Cookie Snack', 'Fried Egg', 'Spaghetti Plate', 'Hamburger', 'Roast Meat', 'Peach Juice', 'Mango Juice', 'Sky Juice', 'Sky Juice', 'Sky Juice', 'Sky Juice', 'Town Special', 'Warm Cocoa', 'Honey Candy', 'Fire Burst', 'Inky Soup', 'Dayzee Syrup', 'Sap Syrup', 'Healthy Salad', 'Koopa Tea', 'Herb Tea', 'Gold Bar', 'Roast Whacka Bump', 'Roast Horsetail']      
tier2 = ['Emergency Ration', 'Space Food', 'Volt Shroom', 'Heavy Meal', 'Mushroom Crepe', 'Shroom Cake', 'Egg Bomb', 'Shroom Pudding', 'Love Pudding', 'Mousse', 'Hot Dog', 'Meat Pasta Dish', 'Gorgeous Steak', 'Fruity Shroom', 'Gradual Syrup', 'Peach Tart', 'Fruity Hamburger', 'Mango Pudding', 'Fruity Punch', 'Fruity Cake', 'Omelette Plate', 'Primordial Dinner', 'Lovely Chocolate', 'Shroom Choco-bar', 'Standard Chocolate', 'Chocolate Cake', 'Choco Pasta Dish', 'Golden Choco-bar', 'Sweet Choco-bar', 'Honey Shroom', 'Honey Super', 'Volcano Shroom', 'Awesome Snack', 'Spicy Dinner', 'Spicy Pasta Dish', 'Ink Pasta Dish', 'Stamina Juice', 'Shroom Delicacy', 'Sap Muffin', 'Weird Extract', 'Snow Bunny', 'Koopa Dumpling', 'Koopasta Dish', 'Koopa Pilaf', 'Shroom Broth', 'Horsetail Tart']
tier3 = ['Fruit Parfait', 'Life Shroom', 'Super Shroom Shake', 'Heartful Cake', 'Love Noodle Dish', 'Dyllis Breakfast', 'Dyllis Lunch', 'Odd Dinner', 'Dyllis Dinner', 'Veggie Set']
tier4 = ['Mixed Shake', 'Dyllis Special', 'Dyllis Deluxe']
tier5 = ['Berry Snow Bunny']
tier6 = ['Gingerbread House', "Couple's Cake", 'Trial Stew', 'Luxurious Set', 'Dyllis Dynamite']

