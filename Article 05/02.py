# zip()

players = ["Emma Watson","Ana de Armas","Taylor Swift","Jennifer Lawrence"]
roles = ["Midfielder","Defender","Goalkeeper","Striker"]

# Normal Method
lineup = []
for i,player in enumerate(players):
    lineup.append((player,roles[i]))
print(lineup)

# One liner Method
lineup = [(player,roles[i]) for i,player in enumerate(players)]
print(f'{lineup}')

# Iterator
lineup = zip(players, roles)
for i in lineup:
    print(i)

# Pro Method
lineup = list(zip(players, roles))
print(lineup)