#Step 1
import random
word_list = ["apple", "banana", "cherry", "strawberry", "pineapple", "mango"]

chosen_word = random.choice(word_list)
lives = 6
display = []
end_of_game = False

for _ in chosen_word:
    display += "_"
print(display)

print(f"You have total of {lives} life to finish this Game. Good luck! Have Fun!")
while not end_of_game:
    guess = input("Guess a letter\n").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        print("wrong guess, you lose a life")
        print(f"Total life: {lives}")
        if lives == 0:
            end_of_game = True
            print("You lost")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("\nYou win!")




