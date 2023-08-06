class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.player_attacked = False
        self.enemy_attacked = False
        self.turn = self.player.name
        self.end = False

    def init_battle(self, clear):
        print("player enters battle with " + self.enemy.name + "!\n")

        while self.end == False:
                self.show_battle_stats()

                if self.player_attacked:
                    print(f"player attacked {self.enemy.name}!\n")

                    self.turn = self.enemy.name

                if self.enemy_attacked:
                    print(f"{self.enemy.name} attacked player!\n")

                    self.turn = self.player.name

                if self.turn == self.player.name:
                    attack_answer = input("1. Attack\n2. Skill\n\nChoice: ")

                    clear()

                    self.player_attack(attack_answer)
                else:
                    if self.check_loss():
                        break

                    input("Press any button for enemies turn.")

                    clear()

                    self.enemy_attack()

    def show_battle_stats(self):
        print(self.player.get_stats() + "\t\t" + self.enemy.get_stats() + "\n")

    def player_attack(self, answer):
        if answer == "1":
            self.enemy.hp -= 10

            self.player_attacked = True
            self.enemy_attacked = False

    def enemy_attack(self):
        self.player.hp -= self.enemy.damage

        self.enemy_attacked = True
        self.player_attacked = False

    def check_loss(self):
        if self.enemy.hp <= 0:
            self.end_battle()

            return True
        elif self.player.hp <= 0:
            self.end_battle()

            return True

    def end_battle(self):
        self.end = True
