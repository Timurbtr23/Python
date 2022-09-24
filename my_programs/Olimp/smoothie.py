class Smoothie:

    def __init__(self, file_name, file_write):
        self.file_name = file_name
        self.file_write = file_write
        self.data = 0
        self.answer = 0

    def open_file(self):
        with open(self.file_name, 'r') as f:
            temp_data_1 = f.readlines()
            self.data = int(temp_data_1[0][0]) + int(temp_data_1[0][2])

    def write_file(self, sth):
        with open(self.file_write, 'w') as f:
            f.write(str(sth))

    def main(self):
        self.open_file()
        self.answer = round(self.data / 3)
        self.write_file(self.answer)

smoothie = Smoothie("smoothie.in", "smoothie.out")
smoothie.main()
