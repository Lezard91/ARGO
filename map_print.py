#  coding: utf-8

import variables as var
import json
import rich_console as r_c
import defis1

def load_from_file() :
    """
    chargement de la map
    """

    with open("map/map 1", "r", encoding="utf-8") as my_file:
        map_data = my_file.readlines()

    var.map_data = []

    # parse map data into 2D list
    # for each line in map data
    for Y, map_line in enumerate(map_data):
        # define empty list for current line
        current_line = []
        # for each character in line
        for X, character in enumerate(map_line):
            if character != "\n":
                current_line.append(character)
                if character == "l":
                    # point de départ du joueur
                    var.player_data["player_y"] = Y + 1
                    var.player_data["player_x"] = X + 1
        var.map_data.append(current_line)

    var.text_line = len(var.map_data) + 2

def load_element_map_from_file() :
    """
        chargement des elements de la map
    """

    with open("data/data_map.json", "r", encoding="utf-8") as my_file:
        var.elements_map = json.load(my_file)

def load_from_data_player_json () :
    """
        chargement des data du joueur
    """
    with open ("data/data_player.json", "r", encoding = "utf-8") as my_file :
        var.player_data = json.load(my_file)
        
def save_from_data_player_json () :
    """
        sauvegarde des data du joueur
    """
    with open ("data/data_player.json", "w", encoding = "utf-8") as my_file :
        var.player_data = json.dump(my_file)

def move_user (command_user) :
    # save_from_data_player_json ()
    # sauvegarde de la position actuelle
    player_Y = var.player_data["player_y"]
    player_X = var.player_data["player_x"]

    # calcul de la nouvelle position
    player_Y += var.possible_actions[command_user]["move_Y"]
    player_X += var.possible_actions[command_user]["move_X"]

    map_element_player_position = var.map_data[player_Y - 1][player_X - 1]
    map_element_data = var.elements_map[map_element_player_position]
    r_c.clear_line()
    if map_element_data["can_walk"]:
        draw_player_2(True)
        # sauvegarde de la nouvelle position
        var.player_data["player_y"] = player_Y
        var.player_data["player_x"] = player_X
        draw_player_2()

        # condition de lancement du fizz buzz
        if map_element_player_position == "f":
            r_c.clear_console()
            print("Veux-tu commencer le FIZZ-BUZZ?\no = OUI\nn = NON\n")
            yes_or_no = input()
            if yes_or_no == "o":
                defis1.fizz_buzz()
            draw_map_2()

        # condition de fin de game
        if map_element_player_position == "s":
            if var.player_data["défi_1"] == True:
                # r_c.clear_console()
                r_c.print_colors_text(
                    "\nBien. Tu ne le sais peut-être pas, mais tu as trouver ce qu'il te faut pour ouvrir la porte et découvrir les secrets qu'elle renferme.\nTu peux à présent partir en paix.",
                    "fg_16",
                    "bg_46",
                    Y=var.text_line+4,
                    X=1)
                var.game_is_run = False
            else:
                r_c.clear_console()
                print("Tu rigole ou quoi?\nTu n'as pas ce qu'il faut pour obtenir les secrets qui se cache derrière cette porte.\nReviens quand tu auras trouver ce qu'il te manque.\nET SURTOUT PAS AVANT ! ! !")
                input()
                r_c.clear_console()
                draw_map_2()

    else:
        # si on arrive sur obstacle
        print("NON je refuse. Demande moi autre chose.")

def draw_player_2(Erase = False) :
    """
        affiche le joueur sur la map
    """

    icon_player = var.player_data["icon"]
    fg_player = var.player_data["foreground"]
    bg_player = var.player_data["background"]

    elements_map = var.elements_map[
        var.map_data[var.player_data["player_y"] - 1]
        [var.player_data["player_x"] - 1]]
    
    if Erase == True:
        icon_player = elements_map["icon"]
        fg_player = elements_map["foreground"]
        bg_player = elements_map["background"]

    # affiche le symbole du joueur à sa position
    r_c.print_colors_text(icon_player, fg_player, bg_player, var.player_data["player_y"], var.player_data["player_x"])


def draw_map_2() :
    """
        affiche la map à partir d'une liste 2D
    """

    r_c.clear_console()

    # each line in 2D list
    for Y, Line in enumerate(var.map_data):
        # pour chaque colonne dans la ligne courante
        for X, Character in enumerate(Line):
            map_element = var.elements_map[Character]
            r_c.print_colors_text(map_element["icon"], map_element["foreground"], map_element["background"], Y + 1, X + 1)

# if __name__ == "__main__" :
#     load_from_data_player_json ()
#     load_element_map_from_file()
#     load_from_file()
#     draw_map_2()
#     daw_player_2()
    
