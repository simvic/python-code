import random;

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

draw = '🧐'

win = '🪗'

loose = '😔'

game_images = [rock, paper, scissors]


user_choice = int(input("What do you choose? type 0 Rock, 1 for paper, 2 for scissors:\n"))
if user_choice >= 3 or user_choice < 0:
    print(f"you typed an invalid number you loose {loose}")
else:

    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer choose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print(f"you win {rock}")


    elif computer_choice > user_choice:
        print(f"ohh noo..{loose} you loose")


    elif user_choice > computer_choice:
        print(f"you win {win}")


    elif user_choice == 2 and computer_choice == 0:
        print(f"ohh.. sorry you loose {loose}")

    elif (user_choice == computer_choice):
        print(f"draw {draw}")