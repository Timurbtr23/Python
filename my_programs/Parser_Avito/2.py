def main():
    file = open('crossword.in', 'r')
    f = open('crossword.out', 'w')
    array_strings = file.readlines()
    count = 0

    for i in array_strings:
        if len(i) > 40:
            exit()

    for i in array_strings[0]:
        for j in array_strings[1]:
            if i in j:
                count += 1

    f.write(str(count))


main()