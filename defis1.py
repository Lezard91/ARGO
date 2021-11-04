# coding : utf-8
# FIZZ BUZZ

from random import randint
import variables as var
import rich_console as r_c
from time import sleep


def fizz_buzz():
    r_c.clear_console()

    # liste des joueurs, chaque joueur est un dictionnaire
    list_player = [
        {"name" : "singe 1",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "singe 2",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "singe 3",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "singe 4",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "singe 5",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "singe 6",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "singe 7",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "singe 8",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "singe 9",
        "luck_min" : 10, 
        "luck_max" : 70},
        {"name" : "KING KONG",
        "luck_min" : 50, 
        "luck_max" : 80},
        {"name" : var.player_data["name"],
        "luck_min" : 80, 
        "luck_max" : 90}
    ]

    print("\nLes joueurs sont :\n")

    # pour chaque joueur (dictionnaire) dans la liste des joueurs
    for player in list_player:
        sleep(0.4)
        # affiche le nom du joueur (clé "name" du dictionnaire)
        print(player["name"])

        # tire un nombre aléatoire "luck_player" compris entre "luck _min" et "luck_max"
        luck_player = randint(player["luck_min"],player["luck_max"])

        # ajoute  la nouvelle clé "luck" au dictionnaire avec la valeur "luck_player"
        player["luck"] = luck_player

    print("\nDébut du fizz buzz\n")

    # definir le compteur de départ à 1
    compteur = 1
    # définir l'index du joueur courant à 0
    index_player = 0
    # tant qu'il reste au moin un joueur dans la liste
    while len(list_player) > 1:
        sleep(0.5)

        if compteur % 3 == 0 and compteur % 5 == 0 :
            answer = "FIZZ BUZZ"

        elif compteur % 5 == 0 :
            answer = "BUZZ"

        elif compteur % 3 == 0 :
            answer = "FIZZ"

        else :
            answer = compteur

        # selectionner le prochain joueur dans la liste
        # while index_player != len(list_player):
        current_player = list_player[index_player]

        # afficher le compteur
        print(f"tour n°{compteur}")

        # afficher le nom du joueur
        print("C'est à",current_player["name"],"de jouer")

        # tirer un nombre aléatoire entre 1 et 100
        score_player = randint(1,100)

        # si ce nombre est inférieur ou égal a la chance du joueur
        if score_player <= current_player["luck"]:

            # alors afficher bonne réponse 
            print(answer)
            print(current_player["name"],"a donné la bonne réponse car il a obtenu",score_player,"alors que ses chances sont de",current_player["luck"],"\n")
            input()
            # et ajouter 1 à l'index du joueur courant
            index_player = index_player + 1

        # sinon afficher mauvaise réponse 
        else:
            print("Perdu !!")
            print(current_player["name"],"a perdu car il a obtenu",score_player,"alors que ses chances sont de",current_player["luck"],"\n")
            input()

            if current_player["name"] == var.player_data["name"] :
                r_c.print_colors_text("Le jeu est terminer puisque tu es assez idiot pour donner une mauvaise réponse à un jeu aussi simple.","fg_196")
                input("\nPresse 'ENTER' pour continuer.")
                r_c.clear_console()
                break

            # et retirer le joueur de la liste
            list_player.pop(index_player)

        if len(list_player) == 1:
            var.player_data["défi_1"] = True
            # afficher le nom du dernier joueur (le gagnant)
            print("Le gagnant est :", end="")
            r_c.print_colors_text(list_player[0]["name"],"fg_46")
            input("\nPresse 'ENTER' pour continuer.")
            r_c.clear_console()

        # si l'index du joueur courant est égal à la longueur de la liste alors repasser l'index à 0
        if index_player == len(list_player):
            index_player = 0
                
        # ajouter 1 au compteur
        compteur = compteur + 1

        

if __name__ == "__main__":
    fizz_buzz()