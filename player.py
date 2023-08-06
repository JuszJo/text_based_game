class Player:
    def __init__(self):
        self.name = "King"
        self.hp = 100
        self.mp = 100
        self.skills = []
        self.new_skill = False

    def get_stats(self):
        return f"{self.name}\tHP: {str(self.hp)}\tMP: {str(self.mp)}\n\nSkills: {[self.skills[i].name for i in range(len(self.skills))]}"

    def show_stats(self):
        print(self.get_stats() + "\n")

    def use_gains(self, type, amount):
        if type is "hp":
            self.hp += amount
        else:
            self.mp += amount

    def add_skill(self, skill):
        self.skills.append(skill)

        self.new_skill = True

    def alert_new_skill(self):
        print(f"New skill learned: {self.skills[-1].name}!\n")

        self.new_skill = False