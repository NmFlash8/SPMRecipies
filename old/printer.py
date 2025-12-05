from game_data import *
while True:
    item = input('Item: ')
    for recipe in recipes[item]:
        print(recipe)
'''
example str:
['Dyllis Dynamite', 'Egg Bomb', 'Megaton Dinner', 'Shroom Delicacy', 'Mango Pudding', 'Love Pudding', 'Lovely Chocolate', 'Golden Choco-bar', 'Shroom Choco-bar']

'''