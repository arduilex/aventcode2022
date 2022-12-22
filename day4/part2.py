def find_range(item):
    start, end = item.split('-')
    return (int(start), int(end))

def init_pair():
    left_pair, right_pair = [], []
    with open("day4.txt", 'r', encoding='utf-8') as f:
        for line in f:
            left_elf, right_elf = line.replace("\n", "").split(',')
            left_pair.append(find_range(left_elf))
            right_pair.append(find_range(right_elf))
    return tuple(left_pair), tuple(right_pair)

def count_overlap(left_pair, right_pair):
    counter = 0
    for i in range(len(left_pair)):
        overlap = False
        right_pair_enumerate = list(range(right_pair[i][0], right_pair[i][1]+1))
        left_pair_enumerate = list(range(left_pair[i][0], left_pair[i][1]+1))
        for section_right in right_pair_enumerate:
            for section_left in left_pair_enumerate:
                if section_left == section_right:
                    overlap = True
        if overlap:
            counter += 1
    return counter
    
print(count_overlap(*init_pair()))