games = []

with open("input.txt") as input:
    lines = input.readlines()
    
    for line in lines:
        battle = line.strip().split()
        games.append(battle)

total_score = 0



for game in games:
    
    if game[1] == "X": # Rock
        total_score += 1
    
    if game[1] == "Y": # Rock
        total_score += 2
        
    if game[1] == "Z": # Rock
        total_score += 3
    
    if game[0] == "A": # Rock
        if game[1] == "Y": # Paper - Win
            total_score += 6
        elif game[1] == "X": # Rock - Draw
            total_score += 3
    
    if game[0] == "B": # Paper
        if game[1] == "Z": # Scissors - Win
            total_score += 6
        elif game[1] == "Y": # Paper - Draw
            total_score += 3
            
    if game[0] == "C": # Scissors
        if game[1] == "X": # Rock - Win
            total_score += 6
        elif game[1] == "Z": # Scissors - Draw
            total_score += 3

print(total_score)
