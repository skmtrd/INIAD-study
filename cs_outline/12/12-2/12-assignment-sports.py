sports = ["cricket", "lacrosses", "hockey", "water_polo", "kabaddi", "tug_of_war"]
n_players = [11, 10, 6, 7, 7, 8]

# sp_players = dict(zip(sports, n_players))
sp_players = {}
for index, sport in enumerate(sports):
    sp_players[sport] = n_players[index]
print(sp_players)
    
