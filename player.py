class Player:
    def __init__(self):
        self.name = "King"
        self.hp = 100
        self.mp = 100
        self.skills = []

    def __str__(self):
        return self.get_stats() + "\tSkills: " + str(self.skills) + "\n"

    def get_stats(self):
        return f"{self.name}\tHP: {str(self.hp)}\tMP: {str(self.mp)}\t Skills: {[self.skills[i].name for i in range(len(self.skills))]}"

    def show_stats(self):
        print(self.get_stats() + "\n")

    def use_gains(self, type, amount):
        if type is "hp":
            self.hp += amount
        else:
            self.mp += amount

    def add_skill(self, skill):
        self.skills.append(skill)