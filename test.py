# coding: utf-8

import variables as var
import os
import sys


def move_user () :
    
    print(var.command_play)
    command_user = input("Entrez une commande : ").lower()
    ClearConsole()

    while var.player_y != 3 and var.player_x != 19 :

        if command_user == "z" :
            var.player_y -= 1
            print(var.command_play)
            command_user = input("Entrez une commande : ").lower()
            ClearConsole()
     
        elif command_user == "q" :
            var.player_x -= 1
            print(var.command_play)
            command_user = input("Entrez une commande : ").lower()
            ClearConsole()
     
        elif command_user == "s" :
            var.player_y += 1
            print(var.command_play)
            command_user = input("Entrez une commande : ").lower()
            ClearConsole()
     
        elif command_user == "d" :
            var.player_x += 1
            print(var.command_play)
            command_user = input("Entrez une commande : ").lower()
            ClearConsole()

        else :
            print(var.command_play)
            command_user = input("Entrez une commande : ").lower()
            ClearConsole()
            move_user 


# while player_yx(y,x) != map(y,x) :
    # if player_yx(y) est < map(y) and si player_yx(x) est = map(x) :
        # alors player_yx(y + 1)
    # 
    # if player_yx(y) est = map(y) and si player_yx(x) est < map(x) :
        # alors player_yx(x + 1)
    # 
    # if player_yx(y) est > map(y) and si player_yx(x) est = map(x) :
        # alors player_yx(y - 1)
    # 
    # if player_yx(y) est = map(y) and si player_yx(x) est > map(x) :
        # alors player_yx(x - 1)


def ClearConsole():

    # for windows
    if "win" in sys.platform.lower():
        os.system("cls")

    # for linux
    elif "linux" in sys.platform.lower():
        os.system("clear")


if __name__ == "__main__" :

    # print("z = haut\nq = gauche\ns = bas\nd = droite")
    move_user ()
    