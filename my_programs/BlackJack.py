import random


def move_user(count):
    random_card = random.choice(deck_of_cards)
    deck_of_cards.remove(random_card)
    count += random_card
    return count


def move_computer(count):
    random_card = random.choice(deck_of_cards)
    deck_of_cards.remove(random_card)
    count += random_card
    return count


def count_computer():
    count_of_computer = 0
    while count_of_computer <= 21:
        move = move_computer(count_of_computer)
        if count_of_computer + move > 21:
            break
        count_of_computer += move
    return count_of_computer


def question():
    result = move_user(0)
    print(result)
    while True:
        print("Желаете взять еще карту? 1 - Да, 0 - Нет")
        choice = int(input())
        if choice == 1:
            result += move_user(result)
            print(result)
            if result > 21:
                print("Ты проиграл")
                break
        if choice == 0:
            break
    return result


def finish():
    count_pc = count_computer()
    count_player = question()
    if count_player <= 21:
        if count_player > count_pc:
            print("Ваш счет:", count_player)
            print("Счет компьютера:", count_pc)
            print("Ты победил!!!")
        else:
            print("Ты проиграл")


deck_of_cards = []

for i in range(15):
    if i < 2:
        continue
    for j in range(4):
        deck_of_cards.append(i)

finish()
