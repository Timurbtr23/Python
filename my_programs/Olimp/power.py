
class Matrica:

    def __init__(self, file_name, file_write):
        self.file_name = file_name
        self.file_write = file_write
        self.data = []
        self.data_write = []
        self.first_row = []

    def open_file(self):
        with open(self.file_name, 'r') as f:
            temp_data_1 = f.readlines()
            temp_data = [i.split('\n')[0] for i in temp_data_1]
            self.data = temp_data

    def main(self):
        self.open_file()
        for line in self.data[1:]:
            answer = 0
            for j in line:
                answer += int(j)
            self.data_write.append(answer)
        self.write_file()

    def write_file(self):
        with open(self.file_write, 'w') as f:
            for i in self.data_write:
                if i == self.data_write[-1]:
                    f.write('{}'.format(i))
                else:
                    f.write('{}\n'.format(i))



matrica = Matrica('matrix.in', 'matrix.out')
matrica.main()
