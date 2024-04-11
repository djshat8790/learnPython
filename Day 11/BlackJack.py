import random
import os
import replit

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return card[random.choice(card)]


def calculate_score(list_of_cards):
    value = sum(list_of_cards)
    if value == 21:
        return 0
    elif value > 21:
        for ace in list_of_cards:
            if ace == 11:
                list_of_cards.remove(11)
                list_of_cards.append(1)
                value = sum(list_of_cards)
                break
    return value


def game_start():
    print("New Game Started...")
    os.system("clear all")
    play_more = True
    while play_more:
        game_over_user = False
        game_over_computer = False
        user_cards = []
        computer_cards = []
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        total_score_user = calculate_score(user_cards)
        total_score_computer = calculate_score(computer_cards)
        print(f"Your card: {user_cards}")
        print(f"Comp card: {computer_cards}\n")
        while not (game_over_user and game_over_computer):
            if not game_over_user:
                draw_another_card = input("Want to draw another card?\n").lower()
                if draw_another_card == "yes":
                    user_cards.append(deal_card())
                    total_score_user = calculate_score(user_cards)
                    print(f"Your cards: {user_cards} = {total_score_user}\n")
                    if total_score_user == 0:
                        game_over_user = True
                    elif total_score_user > 21:
                        game_over_user = True
                else:
                    game_over_user = True
            elif not game_over_computer:
                if total_score_computer < 17:
                    computer_cards.append(deal_card())
                    total_score_computer = calculate_score(computer_cards)
                    if total_score_computer == 0:
                        game_over_computer = True
                    elif total_score_computer > 21:
                        game_over_computer = True
                else:
                    game_over_computer = True

        if total_score_user == 0:
            print(f"\nYou win! BlackJack!\nComputer total {total_score_computer}")
        elif total_score_computer == 0:
            print(f"\nComputer win! BlackJack!\nYour total {total_score_user}")
        elif total_score_computer < total_score_user < 21:
            print(f"\nYou win!\nYour total: {total_score_user}\nComputer total {total_score_computer}")
        elif total_score_user < total_score_computer < 21:
            print(f"\nComputer win!\nYour total: {total_score_user}\nComputer total {total_score_computer}")
        elif total_score_computer > 21 and total_score_user > 21:
            print(f"\nIts a Draw. Both lose.\nYour total: {total_score_user}\nComputer total {total_score_computer}")
        elif total_score_computer < total_score_user > 21:
            print(f"\nComputer win!\nYour total: {total_score_user}\nComputer total {total_score_computer}")
        elif total_score_user < total_score_computer > 21:
            print(f"\nYou win!\nYour total: {total_score_user}\nComputer total {total_score_computer}")
        else:
            print(f"\nIts a Draw!\nYour total: {total_score_user}\nComputer total {total_score_computer}")

        if input("\nWant to play more\n") == "no":
            play_more = False
            print("\nGood Bye! Thanks for playing BlackJack")
        else:
            os.system("clear all")


game_start()
