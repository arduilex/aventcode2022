from part1 import Forest

class Forest_scenic(Forest):
    def __init__(self, filename):
        Forest.__init__(self, filename)
    def max_forest_scenic_score(self):
        index = (0, 0)
        maxi = 0
        for row in self.forest_scenic_score():
            for value in row:
                if value > maxi:
                    maxi = value
        return maxi
        
    def forest_scenic_score(self):
        forest_score = [[0]*self.row_size for i in range(self.col_size)]
        for row in range(self.row_size):
            for col in range(self.col_size):
                forest_score[row][col] = self.scenic_calcul(row, col)
        return forest_score
    
    def scenic_calcul(self, row, col):
        size_center = self.forest_map[row][col]
        row_compare = self.forest_map[row]
        col_compare = self.create_column(col)
        scenic_left = self.count_visible_tree(row_compare[:col][::-1], size_center)
        scenic_right = self.count_visible_tree(row_compare[col+1:], size_center)
        scenic_up = self.count_visible_tree(col_compare[:row][::-1], size_center)
        scenic_down = self.count_visible_tree(col_compare[row+1:], size_center)
        return scenic_down*scenic_up*scenic_left*scenic_right
    
    def count_visible_tree(self, tree_line, compare_size):
        count_visible = 0
        for tree_size in tree_line:
            count_visible += 1
            if tree_size >= compare_size:
                break
        return count_visible

if __name__ == "__main__":
    myForest = Forest_scenic("day8")
    print(myForest.max_forest_scenic_score())