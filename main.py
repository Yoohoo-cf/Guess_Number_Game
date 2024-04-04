from art import logo
import random

# choose a random number between 1 and 100
def number_to_guess():
    return random.randint(1, 100)

def check_game_status(guessed_number, mode):
    ending_game = False

    if mode == 'easy':
        attempts = 10
    elif mode == 'hard':
        attempts = 5

    while not ending_game:

        print(f"You have {attempts} remaining to guess the number.")

        guess = int(input("Make a guess: "))

        attempts -= 1

        if attempts == 0:
            ending_game = True
            print(f"You've run out of your guesses, you lose")
        else:
            if guess == guessed_number:
                ending_game = True
                print(f"You got it. The answer was {guess}.")
            elif guess > guessed_number:
                print("Too high")
            else:
                print("Too low")


def play_game():

    print(logo)
    print("Welcome to the Number Guess Game!")
    print("I am thinking of a number betwwen 1 and 100")

    guessed_number = number_to_guess()

    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty_choice == 'easy':
        check_game_status(guessed_number, 'easy')

    elif difficulty_choice == 'hard':
        check_game_status(guessed_number, 'hard')


play_game()












