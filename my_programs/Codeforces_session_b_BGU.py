# Поликарп учится в Берляндском государственном университете. Совсем скоро ему предстоит сдать сессию. Он должен сдать
# n экзаменов.

# Для каждого экзамена i известны два дня:  a — день основной сдачи экзамена,  b — день пересдачи ( a < b ).
# В один день Поликарп может сдавать не более одного экзамена. Для каждого экзамена Поликарп самостоятельно выбирает,
# в какой из двух дней его сдать. Необходимо сдать все n  экзаменов.

# Поликарп хочет сдать сессию как можно быстрее.
# Выведите минимальный номер дня, в который Поликарп сможет сдать все n экзаменов, либо выведите -1, если сдать сессию
# полностью невозможно.

# Ввод:
# 2
# 1 5
# 1 7
# Вывод:
# 5

# Кол-во экзаменов
while True:
    try:
        print("Введите кол-во экзаменов у студента")
        count_exam = int(input())
        if 1 <= count_exam <= 10 ** 6:
            pass
        else:
            print("Число не должно превышать 10^6")
            continue
    except ValueError:
        print('Введите число')
    else:
        break

a, b, list_of_day = [], [], []
count = None

# Дни экзаменов
for i in range(count_exam):

    print('Введите первый день экзамена', i)
    while True:
        try:
            a.append(int(input()))
        except ValueError:
            print('Введите число')
        else:
            break

    print('Введите день пересдачи экзамена', i)
    while True:
        try:
            b.append(int(input()))
            if b[i] < a[i]:
                print('Значение должно быть больше предыдущего!')
                b.pop()
                continue
            else:
                break
        except ValueError:
            print('Введите число')

    if i == 0:
        count = a[i]
    else:
        if a[i] > count:
            count = a[i]
            break
        elif a[i] == count:
            if b[i] > count:
                count = b[i]
                if b[i] > b[i - 1]:
                    count = b[i - 1]
        else:
            count = -1

print(count)
