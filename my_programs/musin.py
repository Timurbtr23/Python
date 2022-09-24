a = [0, 0]

while True:
    try:
        print("Введите два числа через enter: ")
        a[0] = int(input())
        a[1] = int(input())
    except ValueError:
        print('Введите число!')
    else:
        break

count = 0
for i in a:
    if i > 0:
        count += 1
print(count, " - количество положительных чисел")