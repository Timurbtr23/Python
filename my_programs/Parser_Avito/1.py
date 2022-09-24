def binary(num):
    bin_num = str(bin(num))
    return bin_num[2:]


def main():
    file = open('binpattern.in', 'r')
    f = open('binpattern.out', 'w')
    array_strings = file.readlines()

    for string in array_strings:
        num = int(string)
        if num > 2000000000:
            exit()
        num = binary(num)
        if '10101' in num:
            f.write('Pattern\n')
        else:
            f.write('No\n')


main()