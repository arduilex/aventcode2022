def file_generator(filename):
    with open(filename+'.txt', 'r') as f:
        for line in f:
            yield line
            
def type_line(line)->str:
    space_splited = line.replace("\n", "").split(" ")
    if space_splited[0] == "$":
        return  "command", space_splited[1:]
    elif space_splited[0] == "dir":
        return  "command", space_splited[1:]
    else:
        return "file", space_splited

for line in file_generator("day7"):
    print(type_line(line))