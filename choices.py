class Choices:
    def __init__(self, data):
        self.data = data
        self.current_question = None

    def start(self):
        self.current_question = self.data.get("q")
    
    def next_question(self, answer):
        self.data = self.data.get(answer)
        self.current_question = self.data.get("q")