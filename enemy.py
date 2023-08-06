class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.skills = []
        self.new_skill = False

    def get_stats(self):
        return f"{self.name}\tHP: {str(self.hp)}\tDMG: {str(self.damage)}"

    def show_stats(self):
        print(self.get_stats() + "\n")