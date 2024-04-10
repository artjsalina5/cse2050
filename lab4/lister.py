class Lister:
    def __init__(self, data):
        self.data = data
    def div_by_5(self):
        return [num for num in self.data if num % 5 == 0]