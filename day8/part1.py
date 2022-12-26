def read_file(filename):
    with open(filename+".txt", 'r') as f:
        for line in f:
            line = line.replace("\n","")
            yield line

def generate_map():
    tree_map = []
    for line in read_file("day8"):
        tree_map.append([])
        for high in line:
            tree_map[-1].append(int(high))
    return tree_map

tree_map = generate_map()
for row in tree_map:
    print(row)