
class Salavat:

    def __init__(self, file_name):
        self.file_name = file_name
        self.money = None
        self.euro_rate = 99999.
        self.data = []

    def open_file(self):
        with open(self.file_name, 'r') as f:
            temp_data_1 = f.readlines()
            temp_data = [float(i.split('\n')[0]) for i in temp_data_1]
            self.data = temp_data

    def how_much_money(self):
        self.money = int(self.data[0])
        self.data.pop(0)

    def best_euro_rate(self):
        for rate in self.data:
            if float(rate) < float(self.euro_rate):
                self.euro_rate = rate

    def change_money(self):
        with open("euro.out", 'w') as f:
            f.write(str(self.money / self.euro_rate))
        return self.money / self.euro_rate

    def main(self):
        self.open_file()
        self.how_much_money()
        self.best_euro_rate()


salavat = Salavat("euro.in.txt")
salavat.main()
salavat.change_money()
