list_cards = []
while True:
    try:
        print("Введите кол-во карточек")
        count_card = int(input())
        if count_card < 1 or count_card > 10:
            print("Введите число от 1 до 10")
            continue
    except ValueError:
        print('Введите число')

    try:
        print("Введите натуральные числа на карточках")
        for i in range(count_card):
            list_cards.append(int(input()))
    except ValueError:
        print('Введите числа')

    try:
        print("Введите число, которое надо получить")
        expect_number = int(input())
    except ValueError:
        print('Введите числа')

    else:
        break


def nicety(list):
    for i in list:
        if i > expect_number:
            list.remove(i)
    print(list)


nicety(list_cards)