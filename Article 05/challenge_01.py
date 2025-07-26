players = ["emma Watson","Ana de Armas","TAYLOR SWIFT","jennifer lawrence"]


def titalize(name: str) -> str:
    if name != "Ana de Armas":
        return name.title()
    return name

players = list(map(titalize, players))
print(players)