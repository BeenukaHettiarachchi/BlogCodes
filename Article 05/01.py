# map()


# Normal Method 
players = ["emma Watson","Ana de Armas","TAYLOR SWIFT","jennifer lawrence"]

players = [name.title() for name in players]
print(players)

# Iterator
players = ["emma Watson","Ana de Armas","TAYLOR SWIFT","jennifer lawrence"]
players = map(str.title, players)

for i in players:
    print(i)

# Pro Method
players = ["emma Watson","Ana de Armas","TAYLOR SWIFT","jennifer lawrence"]

players = list(map(str.title, players))
print(players)

