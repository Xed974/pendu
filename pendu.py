import random
choix = ["casserole", "cuillere", "patate", "souris"]
solution = random.choice(choix)

tentatives = 7
affichage = ""
lettres_trouvees = ""

for l in solution:
    affichage = affichage + "_ "

print(">> Bienvenue dans le pendu <<")

while tentatives > 0:
    print("\nMot à deviner : ", affichage)
    proposition = input("proposez une lettre : ")[0:1].lower()

    if proposition in solution:
        lettres_trouvees = lettres_trouvees + proposition
        print("-> Bien vu!")
    else:
        tentatives = tentatives - 1
        print("-> Nope")
        if tentatives == 6:
            print("============")
        elif tentatives == 5:
            print("/|")
            print("============")
        elif tentatives == 4:
            print(" |      / \ ")
            print("/|")
            print("============")
        elif tentatives == 3:
            print(" |     / | \ ")
            print(" |      / \ ")
            print("/|")
            print("============")
        elif tentatives == 2:
            print(" |       O")
            print(" |     / | \ ")
            print(" |      / \ ")
            print("/|")
            print("============")
        elif tentatives == 1:
            print(" |/      |")
            print(" |       O")
            print(" |     / | \ ")
            print(" |      / \ ")
            print("/|")
            print("============")
        elif tentatives == 0:
            print("=========V==       -(-( GAME OVER ! )-)-")
            print(" |/      |")
            print(" |       O")
            print(" |     / | \ ")
            print(" |      / \ ")
            print("/|")
            print("============\n")

    affichage = ""

    for v in solution:
        if v in lettres_trouvees:
            affichage += v + " "
        else:
            affichage += "_ "

    if "_" not in affichage: # Si toutes les lettres ont été découvertes
        print(">>> Gagné! <<<")
        break
     
print("\n    * Fin de la partie *    ")