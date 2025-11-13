print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

crossroad = input("""You're at a cross road. Where do you want to go?
    Type "left" or "right".""")

if crossroad == 'right':
    print('Game Over.')
elif crossroad == 'left':
    lake = input("""You've come to a lake. There is an island in the middle of the lake.
    Type "wait" to wait for a boat. Type "swim" to swim across.""")
    if lake == 'swim':
        print('Game Over.')
    elif lake == 'wait':
        island = input("""You arrive at the island unharmed. There is a house with 3 doors.
    One red, one yellow and one blue. Which colour do you choose?""")
        if island == 'red':
            print('Game Over.')
        elif island == 'blue':
            print('Game Over.')
        elif island == 'yellow':
            print('You Win!')