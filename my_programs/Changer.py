while True:
    try:
        print("Введите cумму, которую хотите разменять")
        money = int(input())
        if money > 50000:
            print('Слишком большое число, введите меньше')
            continue
    except ValueError:
        print('Введите число')
    else:
        break

notes = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]

# while money > note[0]:
#     money -= note[0]

for i in notes:
    count = 0
    while money >= i:
        money -= i
        count += 1
    else:
        print('Купюр, номиналом в', i, 'рублей -', count, 'шт.')
        continue
