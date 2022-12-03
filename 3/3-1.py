import string

shared_items = []

with open("input.txt") as input:
    lines = input.readlines()

    for line in lines:
        line = line.strip()

        halfway = int(len(line) / 2)

        first_half = line[:halfway]
        second_half = line[halfway:]

        for character in first_half:
            if character in second_half:
                position = string.ascii_letters.index(character) + 1
                shared_items.append(position)
                break

print(sum(shared_items))
