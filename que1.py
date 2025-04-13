import random

def random_num():
    num = random.randint(1, 10)
    try:
        user_input = input("Guess a number between 1 and 10: ")
        user = int(user_input)
        
        if user < 1 or user > 10:
            print("The number is out of range. Please enter a number between 1 and 10.")
        elif user == num:
            print(f"Congratulations! You guessed it right. The number was {num}.")
        else:
            print(f"Sorry, wrong guess. The number was {num}.")
            
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

random_num()
