import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:  # 6
    print("You type an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2: # 2
    print("You win!")
elif computer_choice == 0 and user_choice == 2: # 4
    print("You lose!")
elif computer_choice > user_choice: # 1
    print("You lose!")
elif user_choice > computer_choice: # 5
    print("You win!")
elif computer_choice == user_choice: # 3
    print("It's a draw!")
