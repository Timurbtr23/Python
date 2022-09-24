import sys

class Matrica:

    def __init__(self, file_name, file_write):
        self.file_name = file_name
        self.file_write = file_write
        self.data = []
        self.data_write = []
        self.sort_array = []
        self.first_row = None
        self.count = 0

    def open_file(self):
        with open(self.file_name, 'r') as f:
            temp_data_1 = f.readlines()
            self.data = [i.split('\n')[0] for i in temp_data_1]
        self.first_row = self.data[0].split()
        for i in range(2):
            if int(self.first_row[i]) > 1024:
                sys.exit()

    def write_file(self):
        with open(self.file_write, 'w') as f:
            for i in self.data_write:
                f.write('{}\n'.format(str(i)))
            f.write(str(self.count))

    def array_sort(self):
        for line in self.data_write:
            self.sort_array.append(line)
        self.sort_array.sort()
        for i in self.sort_array:
            if i == self.sort_array[-1]:
                self.count += 1

    def main(self):
        self.open_file()
        for line in self.data[1:]:
            answer = 0
            for j in line:
                answer += int(j)
            self.data_write.append(answer)
        self.array_sort()
        self.write_file()


matrica = Matrica('matrix.in', 'matrix.out')
matrica.main()
