def read_file(filename):
    with open(filename+".txt", 'r') as f:
        for line in f:
            line = line.replace("\n","")
            yield line

class Forest:
    def __init__(self):
        self.forest_map = self.generate_map()
        self.row_size = len(self.forest_map)
        self.col_size = len(self.forest_map[0])

    def generate_map(self):
        gmap = []
        for line in read_file("day8"):
            gmap.append([])
            for tree_high in line:
                gmap[-1].append(int(tree_high))
        return gmap
    def edge_tree_counter(self):
        return self.row_size*2+self.col_size*2-4

    def count_visible_tree(self):
        visible_tree_counter = 0
        for row in range(1, self.row_size-1):
            for col in range(1, self.col_size-1):
                visible_tree_counter += self.is_tree_visible(row, col)
        return visible_tree_counter+self.edge_tree_counter()

    def is_tree_visible(self, row, col):
        size_center = self.forest_map[row][col]
        row_compare = self.forest_map[row]
        col_compare = self.create_column(col)
        is_visible_left = self.is_line_visible(row_compare[:col], size_center)
        is_visible_right = self.is_line_visible(row_compare[col+1:], size_center)
        is_visible_up = self.is_line_visible(col_compare[:row], size_center)
        is_visible_down = self.is_line_visible(col_compare[row+1:], size_center)
        if is_visible_left or is_visible_right or is_visible_up or is_visible_down:
            return 1
        else:
            return 0

    def is_line_visible(self, tree_line, compare_size):
        is_visible = True
        for tree in tree_line:
            if tree >= compare_size:
                is_visible = False
        return is_visible

    def create_column(self, column):
        column_list = []
        for row in self.forest_map:
            column_list.append(row[column])
        return column_list

myForest = Forest()
print(myForest.count_visible_tree())