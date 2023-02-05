from time import sleep

def parse_input(filename="day5.txt"):
    with open(filename, 'r') as f:
        for line in f:
            yield line

def cargo_read():
    for row in parse_input():
        if row[0] == '[':
            yield row.replace("\n","").split('[')[1:]
            
def instruciton_read():
    for line in parse_input():
        if line.split(' ')[0] == "move":
            yield line.replace("\n","")

def init_cargo():
    cargo_row = []
    for stack_row in cargo_read():
        row = []
        for crate in stack_row:
            row.append(crate[0])
            blank_space = len(crate)-2
            number_void_crates = blank_space//3-(blank_space//3//3)
            for i in range(number_void_crates):
                row.append(' ')
        cargo_row.append(row)
    cargo_column = []
    row_size, column_size = len(cargo_row), len(cargo_row[0])
    for column in range(column_size):
        cargo_column.append([])
        for row in range(row_size):
            cargo_column[-1].append(cargo_row[row][column])
        cargo_column[-1].reverse()
    return cargo_column

def init_instruction():
    instruction = {
        "move":[],
        "from":[],
        "to":[]}
    for line in instruciton_read():
        fragment_instruction = line.split(' ')
        instruction["move"].append(int(fragment_instruction[1]))
        instruction["from"].append(int(fragment_instruction[3]))
        instruction["to"].append(int(fragment_instruction[5]))
    return instruction

class Cargo:
    def __init__(self, print=False):
        self.cargo = init_cargo()
        self.number_row = len(self.cargo[0])
        self.number_column = len(self.cargo)
        self.counter = 1
        self.total = 0
        self.graphics = print
        self.speed = 0.026
    def crane(self, n, depart, arival):
        for i in range(n):
            take_row = self.find_top(depart)
            if take_row == -1:
                input()
            crate_name = self.take(depart, take_row)
            self.drop(arival, self.find_top(arival)+1, crate_name)
            if self.graphics:
                self.cut_blank_row()
                self.show()
                sleep(self.speed)
    def find_top(self, column):
        for i, row in enumerate(self.cargo[column]):
            if row == ' ':
                return i-1
        return self.number_row-1
    def take(self, col, row):
        crate_name = self.cargo[col][row]
        self.cargo[col][row] = ' '
        return crate_name
    def drop(self, col, row, crate_name):
        if row >= self.number_row:
            self.create_row()
        self.cargo[col][row] = crate_name
    def create_row(self):
        for column in range(self.number_column):
            self.cargo[column].append(' ')
        self.number_row += 1
    def cut_blank_row(self):
        maxi_high_row = 0
        for column in range(self.number_column):
            result_high_row = self.find_top(column)
            if result_high_row > maxi_high_row:
                maxi_high_row = result_high_row
        if self.number_row > maxi_high_row+1:
            for column in range(self.number_column):
                del(self.cargo[column][-1])
            self.number_row -= 1
    def show(self):
        print()
        for row in range(len(self.cargo[0])-1, -1, -1):
            temp = []
            for col in range(self.number_column):
                temp.append(self.cargo[col][row])
            print((" ","")[len(str(row+1))-1]+str(row+1), temp)
        print("-"*48)
        print("  ",[str(i) for i in range(1,self.number_column+1)], str(self.counter)+"/"+str(self.total))
    def top_crate(self):
        top = ''
        for i, column in enumerate(self.cargo):
            top+=column[self.find_top(i)]
        return top

mc = Cargo(print=1)
instruction = init_instruction()
n = len(instruction["move"])
mc.total = n
mc.show()
for i in range(n):
    mc.crane(instruction["move"][i], instruction["from"][i]-1, instruction["to"][i]-1)
    mc.counter = i+1
mc.show()
print("\n-->",mc.top_crate())