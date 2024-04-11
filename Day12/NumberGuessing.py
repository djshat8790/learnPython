import random

computer_chosen_number = random.randint(1, 100)


def num_guess():
    level = input("Choose the difficulty. Type 'easy' or 'hard':\n")
    if level == "easy":
        number_of_attempts = 10
    else:
        number_of_attempts = 5
    number_found = False
    while not number_found and not number_of_attempts == 0:
        print(f"Number of attempts left: {number_of_attempts}")
        user_chosen_number = int(input("Guess the number\n"))
        if user_chosen_number > computer_chosen_number:
            print("Too high")
            number_of_attempts -= 1
        elif user_chosen_number < computer_chosen_number:
            print("Too low")
            number_of_attempts -= 1
        else:
            print("You found it")
            number_found = True
            print(f"Computer thought of {computer_chosen_number}")
    if number_of_attempts == 0:
        print("No attempts left! Game over")
        print(f"Computer thought of {computer_chosen_number}")


num_guess()
