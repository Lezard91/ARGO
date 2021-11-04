# coding: utf-8

import variables as var
import rich_console as r_c
import map_print as map
from time import sleep

def print_intro():
    r_c.clear_console()
    for character in "Bienvenue sur l'ile aux python !!\n":
        print(character, end="")
        sleep(0.08)
    for character in "Pour prendre la succession de ton mentor, il te faut terminer ses recherches.\n":
        print(character, end="")
        sleep(0.04)
    for character in "Ainsi ta quête t'as conduit jusqu'à cette ile dont aucun être vivant n'a foulée le sol depuis des siècles.\n":
        print(character, end="")
        sleep(0.04)
    for character in "Seulement pour obtenir ces réponses, tu dois d'abord explorer ce territoire inconnu,\n":
        print(character, end="")
        sleep(0.04)
    for character in "\nET Y SURVIVRE.\n":
        print('\033[38;5;196m' + character + '\033[0m', end="")
        sleep(0.2)
    for character in "\nPresse 'ENTER' si tu es prêt.":
        print(character, end="")
        sleep(0.02)
    input()

# functions
def Start():
    """
        Début du game
    """
    
    r_c.clear_console()

    map.load_from_data_player_json()
    map.load_element_map_from_file()
    map.load_from_file()
    map.draw_map_2()
    map.draw_player_2()

def Run():
    """
        boucle qui permet au jeu de tourner
        
    """

    while var.game_is_run:
        map.draw_player_2()
        r_c.print_colors_text(f"", Y=var.text_line, X=1)
        # affiche les commandes possibles
        print(f"Commandes possible:\n{var.command_play}")
        action = input("Prochaine action : ").lower()

        # relance la dernière commande du joueur si il n'en a pas rentrer une nouvelle
        if action == "":
            action = var.player_data["last_action"]
        
        # démo cheater
        elif action == "c":
            var.player_data["défi_1"] = True
        
        if action in var.possible_actions.keys():
            
            if action == "z" or action == "s" or action == "q" or action == "d":
                map.move_user(action)
                var.player_data["last_action"] = action

                
            
            elif action == "p":
                var.game_is_run = False
                r_c.clear_console()
                print("On n'abandonne pas la bataille, mais un repli stratégique s'impose.")

        else:
            # mauvaise action
            print("Ce n'est pas une commande valide.")

    print("\nAu revoir")

if __name__ == "__main__" :
    print_intro()
    Start()
    Run()