import random
import os
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')
print(logo)


display = ["_" for i in chosen_word]
lives = 6
end_of_game = False


# Clearing the Screen - posix is os name for Linux or mac
def clear():
    if os.name == 'posix':
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clear screen
    clear()

    # check if letter has been guessed already
    if guess in display:
        print(f"you've already guessed {guess}")

    # check guessed letter
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not the word. You lose a life")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
