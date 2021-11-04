# UTH 8

import os, sys

Prefix = "\x1b["
Style_Suffix = "m"
Reset = "0"
Colors = {
    "BLACK" : "0",
    "RED" : "1",
    "GREEN" : "2",
    "YELLOW" : "3",
    "BLUE" : "4",
    "PURPLE" : "5",
    "CYAN" : "6",
    "WHITE" : "7"
}
FG_Prefix = "3"
BG_Prefix = "4"
Position_Suffix = "H"
bcolors = {
    "fg_noir" : '\033[30m',
    "fg_rouge" : '\033[31m' ,
    "fg_vert" : '\033[32m' ,
    "fg_jaune" : '\033[33m' ,
    "fg_bleu" : '\033[34m',
    "fg_magenta" : '\033[35m',
    "fg_cyan" : '\033[36m',
    "fg_blanc" : '\033[37m',
    "fg_defaut_color" : '\033[39m',
    "fg_46" : '\033[38;5;46m',
    "fg_196" : '\033[38;5;196m',
    "fg_16" : '\033[38;5;16m',

    "bg_noir" : '\033[40m',
    "bg_rouge" : '\033[41m' ,
    "bg_vert" : '\033[42m' ,
    "bg_jaune" : '\033[43m' ,
    "bg_bleu" : '\033[44m',
    "bg_magenta" : '\033[45m',
    "bg_cyan" : '\033[46m',
    "bg_blanc" : '\033[47m',
    "bg_defaut_color" : '\033[49m',
    "bg_245" : '\033[48;5;245m',
    "bg_46" : '\033[48;5;46m'
}
res_colors = '\033[0m' 

chêne = "🌳"
rivière = "🔵"
mer = "🌊"
sable = "🟡"
prairie = "🌺"
pont = "🌉"
montagne = "🗻"
volcan = "🌋"
palmier = "🌴"
sapin = "🌲"
bord_de_map = "🌌"
joueur = " "

def print_emoji(icon,Y = None, X = None):

    position = ""
    if Y != None and X != None:
        position = f"{Prefix}{Y};{X}{Position_Suffix}"

    print (f"{position}{icon}",end="",flush=True)





def print_colors_text(icon, fg = "", bg = "",Y = None,X = None) :

    # foreground colors / fg_colors
    # background colors / bg_colors
    # res_colors = reset all colors
    if fg != "":
        fg = bcolors[fg]
    if bg != "":
        bg = bcolors[bg]

    position = ""
    if Y != None and X != None :
        position = f"{Prefix}{Y};{X}{Position_Suffix}"
    print(f"{position}{fg}{bg}{icon}{res_colors}", end="", flush=True)


def clear_console():

    # pour windows
    if "win" in sys.platform.lower():
        os.system("cls")

    # pour linux
    elif "linux" in sys.platform.lower():
        os.system("clear")

def clear_line():
    print("\033[0J")


    



# class controle :

#     haut = 'ESC[#A'  #déplace le curseur vers le haut de # lignes
#     bas = 'ESC[#B'  #déplace le curseur vers le bas de # lignes
#     droite = 'ESC[#C'  #déplace le curseur vers le droite de # lignes
#     gauche = 'ESC[#D'  #déplace le curseur vers le gauche de # lignes

# if __name__ == "__main__" :
#     print_1()
