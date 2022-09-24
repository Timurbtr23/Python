import random


class Card:
    def __init__(self, num, suit, name):
        self.num = num
        self.suit = suit
        self.name = name


deck_of_cards = []
discard_heap = []
cards_of_player = []
cards_of_computer = []

h6 = Card(6, '♥', '6')
deck_of_cards.append(h6)
c6 = Card(6, '♣', '6')
deck_of_cards.append(c6)
s6 = Card(6, '♠', '6')
deck_of_cards.append(s6)
d6 = Card(6, '♦', '6')
deck_of_cards.append(d6)

h7 = Card(7, '♥', '7')
deck_of_cards.append(h7)
c7 = Card(7, '♣', '7')
deck_of_cards.append(c7)
s7 = Card(7, '♠', '7')
deck_of_cards.append(s7)
d7 = Card(7, '♦', '7')
deck_of_cards.append(d7)

h8 = Card(8, '♥', '8')
deck_of_cards.append(h8)
c8 = Card(8, '♣', '8')
deck_of_cards.append(c8)
s8 = Card(8, '♠', '8')
deck_of_cards.append(s8)
d8 = Card(8, '♦', '8')
deck_of_cards.append(d8)

h9 = Card(9, '♥', '9')
deck_of_cards.append(h9)
c9 = Card(9, '♣', '9')
deck_of_cards.append(c9)
s9 = Card(9, '♠', '9')
deck_of_cards.append(s9)
d9 = Card(9, '♦', '9')
deck_of_cards.append(d9)

h10 = Card(10, '♥', '10')
deck_of_cards.append(h10)
c10 = Card(10, '♣', '10')
deck_of_cards.append(c10)
s10 = Card(10, '♠', '10')
deck_of_cards.append(s10)
d10 = Card(10, '♦', '10')
deck_of_cards.append(d10)

hJ = Card(11, '♥', 'J')
deck_of_cards.append(hJ)
cJ = Card(11, '♣', 'J')
deck_of_cards.append(cJ)
sJ = Card(11, '♠', 'J')
deck_of_cards.append(sJ)
dJ = Card(11, '♦', 'J')
deck_of_cards.append(dJ)

hQ = Card(12, '♥', 'Q')
deck_of_cards.append(hQ)
cQ = Card(12, '♣', 'Q')
deck_of_cards.append(cQ)
sQ = Card(12, '♠', 'Q')
deck_of_cards.append(sQ)
dQ = Card(12, '♦', 'Q')
deck_of_cards.append(dQ)

hK = Card(13, '♥', 'K')
deck_of_cards.append(hK)
cK = Card(13, '♣', 'K')
deck_of_cards.append(cK)
sK = Card(13, '♠', 'K')
deck_of_cards.append(sK)
dK = Card(13, '♦', 'K')
deck_of_cards.append(dK)

hA = Card(14, '♥', 'A')
deck_of_cards.append(hA)
cA = Card(14, '♣', 'A')
deck_of_cards.append(cA)
sA = Card(14, '♠', 'A')
deck_of_cards.append(sA)
dA = Card(14, '♦', 'A')
deck_of_cards.append(dA)


def distribution_of_card():
    for i in range(6):
        random_card = random.choice(deck_of_cards)
        cards_of_player.append(random_card)
        deck_of_cards.remove(random_card)

        random_card = random.choice(deck_of_cards)
        cards_of_computer.append(random_card)
        deck_of_cards.remove(random_card)


def trump_card():
    global main_suit

    random.shuffle(deck_of_cards)
    main_suit = deck_of_cards[-1].suit
    print("Trump card is: ", main_suit)
    return main_suit


def whose_move():
    smallest_card_of_player = 23
    smallest_card_of_computer = 23
    main_suit = trump_card()

    for card in cards_of_player:
        if card.suit == main_suit:
            if smallest_card_of_player > card.num:
                smallest_card_of_player = card.num
            if smallest_card_of_player == 6:
                return 1

    for card in cards_of_computer:
        if card.suit == main_suit:
            if smallest_card_of_computer > card.num:
                smallest_card_of_computer = card.num
            if smallest_card_of_computer == 6:
                return 0

    if smallest_card_of_player < smallest_card_of_computer:
        return 1
    else:
        return 0


def first_attack():
    global whose_turn
    global selected_card_by_comp
    global selected_card_by_player

    whose_turn = whose_move()

    if whose_turn == 1:
        print("Your move first")
        print("Choose card:")
        for card in cards_of_player:
            print(card.name, card.suit)
        selected_card_by_player = choose_card_by_player()
        defense_by_computer()

    elif whose_turn == 0:
        print("The computer starts the move")
        for num, card in enumerate(cards_of_computer):
            # print(card.num, card.suit)
            if num == 0:
                selected_card_by_comp = card
            if card.num < selected_card_by_comp.num and card.suit != main_suit or \
                    selected_card_by_comp.suit == main_suit:
                selected_card_by_comp = card
        cards_of_computer.remove(selected_card_by_comp)
        print(selected_card_by_comp.name, selected_card_by_comp.suit)
        defense_by_player()


def add_card_by_player():
    print("Your move")
    print("Choose card:")
    for card in cards_of_player:
        print(card.name, card.suit)
    choose_card_by_player()
    defense_by_computer()


def attack_by_computer():
    print("Move of the computer")
    for num, card in enumerate(cards_of_computer):
        print(card.num, card.suit)
        if num == 0:
            selected_card = card
            continue
        if card.num < selected_card_by_comp.num and card.suit != main_suit:
            selected_card_by_comp = card
    print(selected_card_by_comp.num, selected_card_by_comp.suit)


def choose_card_by_player():
    choice = int(input("Choose card: "))
    for i in range(7):
        if choice == i + 1:
            selected_card_by_player = cards_of_player[i]
        elif choice == 7:
            pass
    cards_of_player.remove(selected_card_by_player)
    print("Your choice is:", selected_card_by_player.name, selected_card_by_player.suit)
    return selected_card_by_player


def defense_by_player():
    print("Your move")
    print("Choose card:")
    for card in cards_of_player:
        print(card.name, card.suit)
    selected_card = choose_card_by_player()
    if (selected_card.num > selected_card_by_comp.num and \
            selected_card.suit == selected_card_by_comp.suit) or (selected_card.suit == main_suit and selected_card.num > selected_card_by_comp.num):
        check_more_cards(selected_card_by_comp.suit)
    else:
        cards_of_player.append(selected_card)
        print("Wrong card! Choose another card: ")
        defense_by_player()


def check_more_cards(suit):
    for card in cards_of_computer:
        if card.suit == suit:
            selected_card_by_comp = card
            cards_of_computer.remove(selected_card_by_comp)
            print(selected_card_by_comp.name, selected_card_by_comp.suit)
            defense_by_player()
            break
    else:
        print("BITO")
        print(cards_of_player)
        print(cards_of_computer)


def defense_by_computer():
    for card in cards_of_computer:
        if (card.suit == selected_card_by_player.suit and card.num > selected_card_by_player.num) or \
                (card.suit == main_suit and card.num > selected_card_by_player.num):
            print("Computer move...")
            print(card.name, card.suit)
            cards_of_computer.remove(card)
            add_card_by_player()
            break
    else:
        print("Computer take...")


def game():
    distribution_of_card()
    first_attack()


game()
