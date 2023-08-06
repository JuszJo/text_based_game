class Player:
    def __init__(self):
        self.name = "King"
        self.hp = 100
        self.mp = 100

    def get_stats(self):
        return f"{self.name}\tHP: {str(self.hp)}\tMP: {str(self.mp)}"

    def show_stats(self):
        print(self.get_stats() + "\n")