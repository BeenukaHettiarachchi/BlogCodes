my_ex_list = [
    "Zendaya",
    "Emma Watson",
    "Scarlett Johansson",
    "Margot Robbie",
    "Ana de Armas",
    "Alexandra Daddario",
    "Gal Gadot",
    "Selena Gomez",
    "Taylor Swift",
    "Jennifer Lawrence",
    "Sydney Sweeney",
    "Megan Fox",
    "Dua Lipa",
    "Emilia Clarke",
    "Florence Pugh",
    "Millie Bobby Brown",
    "Natalie Portman",
    "Rihanna",
    "Ariana Grande",
    "Sabrina Carpenter"
]

crush_list = [celeb for celeb in my_ex_list if len(celeb.split(' ')[0]) <= 5]

print(crush_list)