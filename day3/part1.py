def find_alone_item(rucksack_stuff:str)->str:
    n = int(len(rucksack_stuff)/2)
    compartment1 = rucksack_stuff[:n]
    compartment2 = rucksack_stuff[n:]
    for item in compartment1:
        if item in compartment2:
            alone_item = item
    return alone_item
    
def sum_priorities()->int:
    with open("day3.txt", 'r', encoding="utf-8") as f:
        total = 0
        for line in f:
            item = find_alone_item(line)
            total += priorities[item]
    return total

priorities = {}
# chr translate unicode code in a letter of the unicode table
# a-z -> 97-122 
for i, unicode_letter in enumerate(range(97, 123), start=1):
    priorities[chr(unicode_letter)] = i
# A-Z -> 65-90
for i, unicode_letter in enumerate(range(65, 91), start=27):
    priorities[chr(unicode_letter)] = i
print(sum_priorities())