from random import randint

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
import random

image=[rock, paper, scissors]
user_choice=int(input("select 1:rock 2:paper 3:scissors"))
computer = randint(0,2)
print("computer chose:\n" + image[computer])
print("you chose: " + image[user_choice])
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer == 2:
    print("You win!")
elif computer == 0 and user_choice == 2:
    print("You lose!")
elif computer > user_choice:
    print("You lose!")
elif user_choice > computer:
    print("You win!")
elif computer== user_choice:
    print("It's a draw!")

