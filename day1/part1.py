
with open("input.txt", 'r', encoding="utf-8") as f:
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
    print(somme[0])