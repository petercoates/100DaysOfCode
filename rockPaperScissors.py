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
rock_paper_scissors = [rock,paper,scissors]
print('Welcome to the ROCK,PAPER,SCISSORS Game')
players_choice = int(input("Pick a number,0 for Rock, 1 for Paper and 2 for Scissors: "))
print(f'You choose: {players_choice}')

if 0 <= players_choice <= 2:
    print(rock_paper_scissors[players_choice])
else:
    print("Invalid number entered, Game Over!")

computer_choice = random.randint(0,2)
print('Computer Choose : ')
print(rock_paper_scissors[computer_choice])

if  computer_choice == 0 and players_choice == 2:
    print("You lose")
elif    computer_choice == 2 and players_choice == 0:
    print("You Win")
elif computer_choice > players_choice:
    print("You lose!")
elif players_choice > computer_choice:
    print("You win!")
elif players_choice == computer_choice:
    print("You Draw!")




