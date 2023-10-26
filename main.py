largeur_de_la_grille = 10
hauteur_de_la_grille = 10

grille = [[0 for i in range(hauteur_de_la_grille)] for i in range(largeur_de_la_grille)]


for ligne in grille:
    print(ligne)

def obtenir_case(x, y):
    return grille[y % hauteur_de_la_grille][x % largeur_de_la_grille]

case1 = obtenir_case(10, 11)
print(case1)

case2 = obtenir_case(0, 4)