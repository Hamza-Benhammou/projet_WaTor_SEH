import random

largeur_de_la_grille = 10
hauteur_de_la_grille = 10

grille = [[ 0 for hauteur in range(largeur_de_la_grille)] for largeur in range(hauteur_de_la_grille)]


x = random.choice(range(largeur_de_la_grille))
y = random.choice(range(hauteur_de_la_grille))
valeur_poisson = 1  
grille[y % hauteur_de_la_grille][x % largeur_de_la_grille] = valeur_poisson

chronon = 0

while chronon < 50:
    deplacement_possible = [[x + 1,y],[x - 1,y],[x, y + 1],[x, y -1]]

    deplacement_choisi = random.choice(deplacement_possible)
    x = deplacement_choisi[0]
    y = deplacement_choisi[1]
    valeur_poisson = "🐟"
    
    if deplacement_choisi == deplacement_possible[0]:
        grille[y % hauteur_de_la_grille][x % largeur_de_la_grille] = valeur_poisson
        grille[y % hauteur_de_la_grille][(x - 1) % largeur_de_la_grille] = 0

    elif deplacement_choisi == deplacement_possible[1]:
        grille[y % hauteur_de_la_grille][x % largeur_de_la_grille] = valeur_poisson
        grille[y % hauteur_de_la_grille][(x + 1) % largeur_de_la_grille] = 0

    elif deplacement_choisi == deplacement_possible[2]:
        grille[y % hauteur_de_la_grille][x % largeur_de_la_grille] = valeur_poisson
        grille[(y - 1) % hauteur_de_la_grille][x % largeur_de_la_grille] = 0

    elif deplacement_choisi == deplacement_possible[3]:
        grille[y % hauteur_de_la_grille][x % largeur_de_la_grille] = valeur_poisson
        grille[(y + 1) % hauteur_de_la_grille][x % largeur_de_la_grille] = 0


    
    for ligne in grille:
        print(*ligne)
    print("-------------------------------")

    chronon += 1
