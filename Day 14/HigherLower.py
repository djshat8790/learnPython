from game_data import data
import random
import os


# random number generator
def get_random_data():
    return random.choice(data)


def game():
    game_data_copy = []
    game_over = False
    previous_data = get_random_data()
    game_data_copy.append(previous_data["name"])
    user_score = 0
    while not game_over:
        os.system("clear all")
        next_data = get_random_data()
        while next_data["name"] in game_data_copy:
            next_data = get_random_data()
        game_data_copy.append(next_data["name"])
        print("\nWho has the most follower?\n")
        print(f"{previous_data['name']}, {previous_data['description']}, from {previous_data['country']}")
        print("---------------VS--------------")
        print(f"{next_data['name']}, {next_data['description']}, from {next_data['country']}")
        answer = input("\nType 'A' or 'B':\n")
        if answer == 'A' and previous_data["follower_count"] > next_data["follower_count"]:
            previous_data = next_data
            user_score += 100
        elif answer == 'B' and previous_data["follower_count"] < next_data["follower_count"]:
            previous_data = next_data
            user_score += 100
        else:
            game_over = True
    os.system("clear all")
    print("\nGame Over")
    print(f"Total Score: {user_score}")

game()
