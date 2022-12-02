games = []

with open("input.txt") as input:
    lines = input.readlines()

    for line in lines:
        battle = line.strip().split()
        games.append(battle)

total_score = 0


for game in games:

    if game[1] == "X":      # Lose
        total_score += 0

    if game[1] == "Y":      # Draw
        total_score += 3

    if game[1] == "Z":      # Win
        total_score += 6

    if game[0] == "A":          # Rock
        if game[1] == "X":      # Lose - Scissors
            total_score += 3
        elif game[1] == "Y":    # Draw - Rock
            total_score += 1
        else:                   # Win - Paper
            total_score += 2

    if game[0] == "B":          # Paper
        if game[1] == "X":      # Lose - Rock
            total_score += 1
        elif game[1] == "Y":    # Draw - Paper
            total_score += 2
        else:                   # Win - Scissors
            total_score += 3

    if game[0] == "C":          # Scissors
        if game[1] == "X":      # Lose - Paper
            total_score += 2
        elif game[1] == "Y":    # Draw - Scissors
            total_score += 3
        else:                   # Win - Rock
            total_score += 1

print(total_score)
