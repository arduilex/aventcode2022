def find_badge(group: list) -> str:
    group.sort(key=len)
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badge = item
    return badge


def create_group(all_elf) -> list:
    group_list = []
    for i, elf in enumerate(all_elf):
        if i % 3 == 0:
            group_list.append([])
        group_list[-1].append(elf[:-1])
    return group_list


def sum_priorities_group() -> int:
    with open("day3.txt", 'r', encoding="utf-8") as f:
        total = 0
        for group in create_group(f):
            total += priorities[find_badge(group)]
    return total


priorities = {}
# chr translate unicode code in a letter of the unicode table
# a-z -> 97-122
for i, unicode_letter in enumerate(range(97, 123), start=1):
    priorities[chr(unicode_letter)] = i
# A-Z -> 65-90
for i, unicode_letter in enumerate(range(65, 91), start=27):
    priorities[chr(unicode_letter)] = i

print(sum_priorities_group())
