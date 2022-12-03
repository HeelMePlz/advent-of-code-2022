import string

rucksacks = []
shared_items_index = []

with open("input.txt") as input:
    lines = input.readlines()

    for line in lines:
        line = line.strip()
        rucksacks.append(line)


i = 0

while i < len(rucksacks):

    group = rucksacks[i : i + 3]

    first = group[0]
    second = group[1]
    third = group[2]

    for character in first:
        if character in second and character in third:
            position = string.ascii_letters.index(character) + 1
            shared_items_index.append(position)
            break

    i += 3


print(sum(shared_items_index))
