from time import sleep
from rich_console import print_colors_text

def delay_print(string, time=0.2):
    for character in string:
        print(character, end="")
        sleep(time)

# intro
print_intro_1 = "Bienvenue sur l'ile aux python !!\n"
print_intro_2 = "Pour prendre la succession de ton mentor, il te faut terminer ses recherches.\n"
print_intro_3 = "Ainsi ta quête t'as conduit jusqu'à cette ile dont aucun être vivant n'a foulée le sol depuis des siècles.\n"
print_intro_4 = "Seulement pour obtenir ces réponses, tu dois d'abord explorer ce territoire inconnu,\n"
print_intro_5 = '\033[38;5;196m' + "ET Y SURVIVRE.\n" + '\033[0m'

# suite à une action
# print("tu as trouver de la nourriture")
# print("tu as trouver de l'eau")
# print("tu as trouver quelque chose")
# print("tu as trouver une sorte de petite dalle de pierre qui ressemble vaguement à un plan de l'ile. Et par prudence, tu la prends en photo")
# print("tu as trouver une sorte de petite dalle de pierre sur laquelle est inscrit des notes")
# print("tu as trouver l'une des clefs que tu recherche")
# print("tu as trouver un endroit ou te reposer")
