import sys
import random


class Slowomeska:

    def __init__(self):

        self.score = 0
        self.words = {
            "Danil": "it's my name",
            "Bogdan": "name of my friend",
            "Oksana": "name of my mother",
            "Sasha": "name of my father",
            "Eugen": "name of my brother"
        }

    def start(self):
        print("Welcome to Word Jumble!")
        print("Unscramble the letters to make а word")
        print("Enter 'hint' for а hint")
        print("Enter 'quit' to quit the game")
        print("")

    def choose_a_word(self):
        the_word = random.choice(list(self.words))
        the_hint = self.words[the_word]
        jumble = ''.join(random.sample(the_word, len(the_word)))
        print("The jumble is: ", jumble)

        return the_hint, the_word

    def engine(self):

        the_hint, the_word = self.choose_a_word()
        guess = ""

        while (guess != the_word) or (guess != "quit"):

            guess = input("Your move: ")

            if guess == "quit":
                print("Looser")
                sys.exit()

            if guess == "hint":
                self.score -= 2
                print("Your score is: ", self.score)
                print(the_hint)
                continue

            if guess == the_word:
                self.score += len(the_word)
                print("Wow it's impossible!")
                print("Your score is: ", self.score)

                res = input("Thank you for playing! Do u wanna play again? Y/n: ")
                if res == "Y":
                    self.engine()
                else:
                    sys.exit()
            else:
                print("Na-ah, try again")
                continue

    def main(self):
        self.start()
        self.engine()


slowomeska = Slowomeska()
slowomeska.main()
