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
    for instruction_read in instruciton_read():
        fragment_instruction = instruction_read.split(' ')
        instruction["move"].append(int(fragment_instruction[1]))
        instruction["from"].append(int(fragment_instruction[3]))
        instruction["to"].append(int(fragment_instruction[5]))
    return instruction

class Cargo:
    def __init__(self):
        self.cargo = init_cargo()
        self.number_row = len(self.cargo[0])
        self.number_column = len(self.cargo)
    def crane(self, n, start, arival):
        for i in range(n):
            crate_name = self.take(start, self.find_row(start))
            self.drop(arival, self.find_row(arival)+1, crate_name)
            self.cut_high_row()
            self.show()
            sleep(0.03)
    def find_row(self, column):
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
    def cut_high_row(self):
        maxi_high_row = 0
        for column in range(self.number_column):
            row_high_result = self.find_row(column)
            if row_high_result > maxi_high_row:
                maxi_high_row = row_high_result
        if maxi_high_row > self.number_row:
            for i in range(abs(self.number_row)-maxi_high_row):
                for column in range(self.number_column):
                    del(self.cargo[column][-1])
        self.number_row = maxi_high_row

    def show(self):
        print()
        for row in range(self.number_row-1, -1, -1):
            temp = []
            for col in range(self.number_column):
                temp.append(self.cargo[col][row])
            print(temp)
        print("-"*45)
        #print([str(i) for i in range(1,10)])
    def top_crate(self):
        

mc = Cargo()
instruction = init_instruction()

mc.show()
sleep(1)
for i in range(len(instruction["move"])):
    mc.crane(instruction["move"][i], instruction["from"][i]-1, instruction["to"][i]-1)
print(mc.top)