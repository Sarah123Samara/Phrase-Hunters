import random
from phrase import Phrase


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            "Hello world",
            "Python is fun",
            "Coding is great",
            "OpenAI is awesome",
            "I love programming",
        ]
        self.active_phrase = None
        self.guesses = []
        self.attempts = 0  # New attribute to track attempts

    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase()
        guessed_letters = []
        while self.missed < 5:
            display_phrase = self.active_phrase.display(guessed_letters)
            print(display_phrase)
            guess = self.get_guess()
            if guess in self.guesses:
                print("You have already guessed this letter.")
                print()
                continue
            self.guesses.append(guess)

            if self.active_phrase.check_letter(guess):
                print("Correct guess!")
                print()
                guessed_letters.append(guess)

                if self.active_phrase.check_complete(guessed_letters):
                    self.attempts += 1
                    # Display the full phrase
                    print("Congratulations! You've guessed the phrase correctly:")
                    print(self.active_phrase.phrase)
                    print()
                    print(f"It took you {self.attempts} attempts to guess the phrase.")
                    print()
                    self.play_again_prompt()  # Ask to play again
                    return
            else:
                self.missed += 1
                print(f"You have {5 - self.missed} out of 5 lives remaining!")

            self.attempts += 1  # Increment attempts

        self.game_over(False)

    def get_random_phrase(self):
        phrase = random.choice(self.phrases)
        return Phrase(phrase)

    def welcome(self):
        print()
        print("-" * 25)
        print("Welcome to Phrase Hunter!")
        print("-" * 25)
        print()
        print("Can you guess the phrase?")

    def get_guess(self):
        while True:
            print()
            guess = input("Guess a letter: ").lower()
            if len(guess) == 1 and guess.isalpha():
                return guess
            else:
                print("Invalid input. Please guess a single letter.")

    def play_again_prompt(self):
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                self.missed = 0
                self.guesses = []
                self.attempts = 0  # Reset attempts
                self.start()
                break
            elif play_again == "no":
                print()
                print("Thank You for playing!\nHave a nice day")
                print()
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                print()

    def game_over(self, is_winner):
        if is_winner:
            print()
            print("Congratulations! You've guessed the phrase correctly.")
            print(f"It took you {self.attempts} attempts to guess the phrase.")
        else:
            print()
            print(
                "Sorry, you've run out of lives. The phrase was:",
                self.active_phrase.phrase,
            )
            print()
        self.play_again_prompt()


if __name__ == "__main__":
    game = Game()
    game.start()
