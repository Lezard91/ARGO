# coding: utf-8


# map
command_play = "\t Z = haut\nQ = gauche\tD = droite\n\t S = bas"
# GameIsRunning = game_is_run
game_is_run = True
# PossibleActions = possible_actions
possible_actions = {
    "z" : { "move_Y" : -1, "move_X" : 0}, 
    "s" : { "move_Y" : 1, "move_X" : 0}, 
    "q" : { "move_Y" : 0, "move_X" : -1}, 
    "d" : { "move_Y" : 0, "move_X" : 1}, 
    "p" : { "move_Y" : 0, "move_X" : 0}
}
# PlayerData = player_data
player_data = None
# MapElements = elements_map
elements_map = None
# MapData = map_data
map_data = []
text_line = 0

# command_user = input("Entre une commande : ").lower()

