import json

def load_from_json () :
    with open ("data/data_player.json", "r", encoding = "utf-8") as My_file :
        players = json.load(My_file)

def save_from_json () :
    with open ("data.json", "w", encoding = "utf-8") as My_file :
        players = json.dump(My_file)

if __name__ == "__main__" :
    load_from_json ()