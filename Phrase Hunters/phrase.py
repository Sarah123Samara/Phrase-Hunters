class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guessed_letters):
        display_phrase = ""
        for letter in self.phrase:
            if letter == " ":
                display_phrase += " "
            elif letter in guessed_letters:
                display_phrase += letter
            else:
                display_phrase += "_"
        return display_phrase

    def check_letter(self, letter):
        return letter in self.phrase

    def check_complete(self, guessed_letters):
        return all(letter in guessed_letters or letter == " " for letter in self.phrase)
