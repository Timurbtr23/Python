import random


class Field:

    def __init__(self):
        self.items = [0, 200, 100, 450, 400, 150, "*", 500, 350, 250, "+", 50, "$", 300]

    def spin(self):
        return random.choice(self.items)


class Game:

    def __init__(self):
        self.diction = {
            "slovo": "definition0",
            "slovo1": "definition1",
            "slovo2": "definition2",
        }
        self.word = None
        self.definition = None
        self.word_stars = None
        self.table = 0

    def word_of_the_game(self):
        self.word = random.choice(list(self.diction.keys()))
        self.definition = self.diction[self.word]
        self.word_stars = "*" * len(self.word)

    def open_the_letter(self):
        pass


class Player:

    def __init__(self):
        self.score = 0


class User(Player):

    def __init__(self):
        super().__init__()

    def guess(self, answer):
        guess_word = input("Try to guess: ")
        if guess_word == answer:
            return True
        else:
            return False

    def guess_letter(self):
        return input("Try to guess a letter: ")


if __name__ == "__main__":

    game = Game()
    user = User()
    field = Field()

    while True:

        game.word_of_the_game()
        print("Definition is: ", game.definition)
        print("Word is: ", game.word_stars)

        while True:
            want2guess = input("Do you want to guess the word? y/n ")

            if want2guess == "y":
                if user.guess(game.word):
                    print("Win")
                    break
                else:
                    print("lose")
                    break

            elif want2guess == "n":
                game.table = field.spin()
                if game.table == "$":
                    pass
                elif game.table == 0:
                    pass
                elif game.table == "+":
                    game.open_the_letter()
                else:
                    print("На барабане {} очков".format(game.table))
                    if user.guess_letter() in game.word:
                        # todo game delete star
                        if game.table == "*":
                            user.score *= 2
                        else:
                            user.score += game.table
                        print("You have", user.score)

        while True:
            game_continue = input("Do you want to continue? y/n - ")
            if game_continue == "y":
                break
            elif game_continue == "n":
                print("Thank you for the game")
                exit()
            else:
                continue

