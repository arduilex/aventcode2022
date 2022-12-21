# X = loose 
# Y = draw
# Z = win
translate = {"X":"loose",
            "Y":"draw",
            "Z":"win"}
win_against = {3:1,1:2,2:3}
loose_against = {1:3,2:1,3:2}

def match(p1:int, p2:int)->int:
    point = 0
    if (p1,p2) in [(3, 1), (1,2), (2,3)]:
        point = 6
    elif p1==p2:
        point = 3
    return point+p2

def select(p1:int, action:str)->int:
    if translate[action] == "win":
        return win_against[p1]
    elif translate[action] == "loose":
        return loose_against[p1]
    else:
        return p1
        
def final_score()->int:
    total = 0
    with open("day2.txt", 'r', encoding="utf-8") as f:
        for line in f:
            p1_int = ord(line[0])-64
            p2_str = line[-2]
            total += match(p1_int, select(p1_int, p2_str))
    return total

print(final_score())