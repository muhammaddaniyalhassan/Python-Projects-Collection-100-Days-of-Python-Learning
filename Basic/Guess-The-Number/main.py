import random
from art import logo
print(logo)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
           31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
           71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
           91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
difficulty=str(input("Choose a difficulty, type 'easy' or 'hard'"))
user_attempts = 0  # Initialize user_attempts

if difficulty=="easy":
    attempts=10
else:
    attempts=5
print(f"You have {attempts} attempts remaining to guess the number.")
choice=random.choice(numbers)

for _ in range(0,attempts):
    guess=int(input("Make a guess: "))
    user_attempts += 1
    remaining_attempts=attempts-user_attempts
    if guess == choice:
        print("correct answer")
        print(f"You had {remaining_attempts} attempts left")
        break
    elif guess>choice:
        print("Too High")
    else:
        print("Too Low")
    print(f"You have {remaining_attempts} attempts left")
    if user_attempts >= attempts:
        print(f"Game Over. The number was {choice}. Better luck next time!")
        break







