def multiplay(num1, num2):
    result = num1 * num2
    return result


def physics_lab():
    file = open('math.in', 'r')
    f = open('math.out', 'w')
    array_strings = file.readlines()

    for string in array_strings:
        num_1 = int(string.split(' ')[0])
        num_2 = int(string.split(' ')[1])
        if num_1 > 2**63-1 or num_2 > 2**63-1:
            exit()
        num12 = multiplay(num_1, num_2)
        if num12 < 2**63-1:
            f.write('NO\n')
        else:
            f.write('YES\n')


physics_lab()