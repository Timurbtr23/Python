class Lala:

    def __init__(self, file_name, file_write):
        self.file_name = file_name
        self.file_write = file_write
        self.data = []
        self.right_data = []

    def open_file(self):
        with open(self.file_name, 'r') as f:
            temp_data_1 = f.readlines()
            self.data = [int(i.split('\n')[0]) for i in temp_data_1]
            self.data.pop(0)

    def write_file(self):
        with open(self.file_write, 'w') as f:
            for j in self.right_data:
                if j == self.right_data[-1]:
                    f.write('{}'.format(j))
                else:
                    f.write('{}\n'.format(j))

    def main(self):
        self.open_file()
        for i in self.data:
            if i not in self.right_data:
                self.right_data.append(i)
        self.write_file()


lala = Lala("d.in", "d.out")
lala.main()
