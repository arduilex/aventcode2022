def match(p1:int, p2:int)->int:
    point = 0
    if (p1,p2) in [(3, 1), (1,2), (2,3)]:
            point = 6
    elif p1==p2:
        point = 3
    return point+p2

def final_score()->int:
    total = 0
    with open("day2.txt", 'r', encoding="utf-8") as f:
        for line in f:
            total += match(ord(line[0])-64, ord(line[-2])-87)
    return total

print(final_score())