from game_data import data
import random


# random number generator
def get_random_data():
    return random.choice(data)


def game():
    game_data_copy = []
    game_over = False
    previous_data = get_random_data()
    game_data_copy.append(previous_data["name"])
    while not game_over:
        next_data = get_random_data()
        if next_data["name"] not in game_data_copy:
            game_data_copy.append(next_data["name"])
        print(f"{previous_data["name"]}, {previous_data["description"]}, from {previous_data["country"]}")
        print("-----------VS----------")
        print(f"{next_data["name"]}, {next_data["description"]}, from {next_data["country"]}")
        answer = input()
        if answer == 'A':
            if previous_data["follower_count"] > next_data["follower_count"]:
                previous_data = next_data
            else:
                game_over = True
        else:
            if previous_data["follower_count"] < next_data["follower_count"]:
                previous_data = next_data
            else:
                game_over = True


        print(game_data_copy)






game()