overlap = 0
pairs = []

with open("input.txt") as input:
    lines = input.readlines()

    for line in lines:
        line = line.strip()
        pairs.append(line.split(","))

for pair in pairs:

    check = []

    for section in pair:

        section_assignments = []

        section_assignment = section.split("-")
        areas = range(int(section_assignment[0]), int(section_assignment[1]) + 1)

        for area in areas:
            section_assignments.append(area)

        check.append(section_assignments)

    for num in check[0]:
        if num in check[1]:
            overlap += 1
            break

print(overlap)
