f=open("day1.txt", 'r', encoding="utf-8")
food = [[]]
for line in f:
    if line != '\n':
        food[-1].append(int(line[:-1]))
    else:
        food.append([])
somme = [0]*len(food)
for i, miam in enumerate(food):
    somme[i] = sum(miam)
somme = sorted(somme, reverse=True)
print("part1:",somme[0])
print("part2:",sum(somme[0:3]))