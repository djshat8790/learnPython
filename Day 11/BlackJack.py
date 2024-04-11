import random
import os
import time
from art import logo


def deal_card():
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card)


def calculate_score(list_of_cards):
    value = sum(list_of_cards)
    if value == 21:
        return 0
    elif value > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        value = sum(list_of_cards)
    return value


def game_start():
    play_more = True
    os.system("clear all")
    print(logo)
    while play_more:
        print("New Game Starting...")
        time.sleep(0.7)
        print("3..", end="")
        time.sleep(0.7)
        print("2..", end="")
        time.sleep(0.7)
        print("1..")
        time.sleep(0.5)
        print("Good Luck! Have Fun !...\n😊🥳\n")
        game_over_user = False
        game_over_computer = False
        user_cards = []
        computer_cards = []
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        total_score_user = calculate_score(user_cards)
        total_score_computer = calculate_score(computer_cards)
        print(f"Your card: {user_cards}")
        print(f"Opponent card: {computer_cards}\n")
        while not (game_over_user and game_over_computer):
            if not game_over_user:
                draw_another_card = input("Do u want to draw another card?\n").lower()
                if draw_another_card == "yes":
                    user_cards.append(deal_card())
                    total_score_user = calculate_score(user_cards)
                    if total_score_user == 0:
                        print(f"Your cards: {user_cards} = BlackJack\n")
                    else:
                        print(f"Your cards: {user_cards} = {total_score_user}\n")
                    if total_score_user == 0 or total_score_user > 21:
                        game_over_user = True
                else:
                    game_over_user = True
            elif not game_over_computer:
                if total_score_computer < 17:
                    computer_cards.append(deal_card())
                    total_score_computer = calculate_score(computer_cards)
                    if total_score_computer == 0 or total_score_computer > 21:
                        game_over_computer = True
                else:
                    game_over_computer = True
        os.system("clear all")
        print(logo)
        print(compare(total_score_user, total_score_computer))
        if input("\n😁Want to play another game of BLACKJACK 😁\n") == "no":
            play_more = False
            os.system("clear all")
            print("BYE BYE! Thanks 4 playing BLACKJACK")
            print("SEE U SOON\n👋👋👋👋")


def compare(user_score, computer_score):
    if user_score == 0:
        return f"\n🏆\nYou win! BlackJack!\nOpponent total: {computer_score}"
    elif computer_score == 0:
        return f"\n😭\nOpponent win! BlackJack!\nYour total: {user_score}"
    elif computer_score < user_score < 21:
        return f"\n🏆\nYou win!\nYour total: {user_score}\nOpponent total: {computer_score}"
    elif user_score < computer_score < 21:
        return f"\n😭\nOpponent win!\nYour total: {user_score}\nOpponent total: {computer_score}"
    elif computer_score > 21 and user_score > 21:
        return f"\n😤\nIts a Draw. Both lose.\nYour total: {user_score}\nOpponent total: {computer_score}"
    elif computer_score < user_score > 21:
        return f"\n😭\nOpponent win!\nYour total: {user_score}\nOpponent total: {computer_score}"
    elif user_score < computer_score > 21:
        return f"\n🏆\nYou win!\nYour total: {user_score}\nOpponent total: {computer_score}"
    else:
        return f"\n😤\nIts a Draw!\nYour total: {user_score}\nOpponent total: {computer_score}"


game_start()
