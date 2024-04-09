#Step 1
import random
word_list = ["apple", "banana", "cherry", "strawberry", "pineapple", "mango"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)
lives = 6
#print(chosen_word)
display = []
for _ in chosen_word:
    display += "_"
print(display)
end_of_game = False
print(f"You have total of {lives} life left")
while not end_of_game:
    guess = input("Guess a letter\n").lower()
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} life left")
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("\nYou win!")




