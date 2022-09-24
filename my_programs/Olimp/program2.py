import sys


class Bonus:

    def __init__(self):
        self.data = None
        self.all_values = []
        self.max_value = 0

    def open_file(self):
        file = open('book.in', 'r')
        self.data = int(file.readlines()[1])
        if 1000 >= self.data >= 999999999:
            sys.exit()
        self.data = list(str(self.data))

    def main(self):
        self.open_file()
        for i in range(0, len(self.data)):
            copy = self.data.copy()
            copy.pop(i)
            if (i+1) > len(self.data):
                break
            else:
                copy.pop(i-1)
            self.all_values.append(int(''.join([str(i) for i in copy])))
        self.max_value = max(self.all_values)
        self.write_file()

    def write_file(self):
        with open('book.out', 'w') as f:
            f.write(str(self.max_value))


bonus = Bonus()
bonus.main()
