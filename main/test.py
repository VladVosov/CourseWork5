import json


class Read:
    def __init__(self, text):
        self.date = None
        self.text = text

    def read(self):
        with open(self.text, 'r') as f:
            self.date = json.load(f)

    def print(self):
        Read.read(self)
        return self.date



test1 = Read("data.json")
# test1.read()
print(test1.print())