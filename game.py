import os
import json
from player import *
from choices import *
from skill import *

with open("choices.json", "r") as f: data = json.load(f)

choices = Choices(data)
player = Player()

game_end = False

def clear():
    os.system("cls")

def check_gains():
    gains = choices.data.get("gains")

    if gains: player.use_gains(gains.get("type"), gains.get("amount"))

def check_skill():
    skill = choices.data.get("skill")

    if skill:
        player_skill = Skill(skill.get("name"), skill.get("damage"), skill.get("cost"))

        player.add_skill(player_skill)

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

        check_gains()

        check_skill()

main()