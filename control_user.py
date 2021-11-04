# coding: utf-8

import variables as var

# play_y = var.player_y
# play_x = var.player_x

def move_user (command_user) :
    
    # save actual player position
    player_Y = var.player_data["Y"]
    player_X = var.player_data["X"]

    # calculate new player position
    player_Y += var.possible_actions[command_user]["position_Y"]
    player_X += var.possible_actions[command_user]["position_X"]

    var.player_data["Y"] = player_Y
    var.player_data["X"] = player_X

    map_element = var.player_in_map[
        var.map_data[var.player_data["Y"] - 1]
        [var.player_data["X"] - 1]]
    
    print(map_element)


if __name__ == "__main__" :

    # print("z = haut\nq = gauche\ns = bas\nd = droite")
    move_user (command_user=input("Entrez une commande : "))
