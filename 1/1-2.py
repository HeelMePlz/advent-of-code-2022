total_inventory = []

# Parse the input
with open("input.txt") as input:
    lines = input.readlines()
    
    elf_inventory = []
    
    for line in lines:
        item = line.strip()
        
        if item == "":
            total_inventory.append(elf_inventory)
            elf_inventory = []
        else:
            elf_inventory.append(int(item))
    
    total_inventory.append(elf_inventory)
    elf_inventory = []

# Find Elf carrying most Calories

total_calories = []

for inventory in total_inventory:
    total_calories.append(sum(inventory))

total_calories.sort(reverse=True)

top_three = total_calories[:3]

print(sum(top_three))
