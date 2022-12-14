import prime

def num_1(x):
    """
    Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
    Найдите сумму всех чисел меньше 1000, кратных 3 или 5.
    """
    sum = 0
    for i in range(x):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    return sum


def num_2(count):
    """
    Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2,
    первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
    """
    fib1 = 1
    fib2 = 1
    sum = 0

    while fib1 < count:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        if fib2 % 2 == 0:
            sum += fib2

    return sum


def num_3(x):
    """
    Простые делители числа 13195 - это 5, 7, 13 и 29.
    Каков самый большой делитель числа 600851475143, являющийся простым числом?
    """
    
    
    
    
    z = x
    y = x // 2
    while y > 0:
        if y % 2 == 0:
            y -= 1
        while x % y == 0:
            while z != 0 and y != 0:
                if z > y:
                    z %= y
                else:
                    y %= z
            z = z + y
            print(z)
            if z % 3 == 0 or z % 5 == 0 or z % 7 == 0:
                y = z
                continue
            else:
                print(z)
                break
        y -= 2
    # SO HAAAARD


def num_4(x, y):
    """
    Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
    полученное умножением двух двузначных чисел – 9009 = 91 × 99.
    Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
    """
    target = 0
    for i in range(x, y):
        for j in range(i, y):
            mult = i * j
            s = str(mult)
            if (str(mult)[0] == str(mult)[-1]) and (str(mult)[1] == str(mult)[-2]) and (str(mult)[2] == str(mult)[-3]):
                if mult > target:
                    target = mult

    return target


def num_5(x):
    """
    2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
    Какое самое маленькое число делится нацело на все числа от 1 до 20?
    """
    i = 1
    s = 0
    while i >= 0:
        for j in range(1, x+1):
            if i % j == 0:
                s += 1
            else:
                s = 0
                break
        if s == x:
            return i
        if i == 1:
            i += 19
        else:
            i += 20


def num_6(x):
    """
    Сумма квадратов первых десяти натуральных чисел равна 12 + 22 + ... + 102 = 385
    Квадрат суммы первых десяти натуральных чисел равен (1 + 2 + ... + 10)2 = 552 = 3025
    Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных
    чисел составляет 3025 − 385 = 2640.
    Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
    """
    first_sum = 0
    second_sum = 0
    for i in range(x+1):
        first_sum += i**2
    for j in range(x+1):
        second_sum += j
    second_sum = second_sum**2
    difference = second_sum - first_sum
    return difference


def num_7():
    """
    Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
    Какое число является 10001-ым простым числом?
    """
    print(prime.list_prime(1, 9999999)[10002])

