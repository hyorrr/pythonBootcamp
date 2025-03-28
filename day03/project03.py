print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go?'
                ' Type "left" or "right"').lower()


if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.'
          ' Type "Wait" or "Swim"').lower()
    if choice2 == "wait":
        # game will continue
        choice3 = input("You arrived at the island unharmed."
                         "There is house with 3 doors. One red, "
                         "one yellow and one lue. "
                         "Which colour do you choose?").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Youo chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an agry trout. Game Over.")
else:
    print("Fall into a hole. Game over.")





