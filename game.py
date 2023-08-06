import os
import json
from player import *
from choices import *

with open("choices.json", "r") as f: data = json.load(f)

choices = Choices(data)
player = Player()

game_end = False

def clear():
    os.system("cls")

def main():
    choices.start()

    while game_end == False:
        clear()

        if(choices.current_question == None):
            game_end == True

            print("Game End")

            break

        player.show_stats()

        answer = input(choices.current_question + "\n\nChoice: ");

        choices.next_question(answer)

main()