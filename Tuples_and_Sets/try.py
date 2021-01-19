class CustomSet:
    def __init__(self):
        self.capacity = 8
        self.values = [None]*self.capacity

    def add(self, value):
        value_hash = hash(value)
        index = value_hash % self.capacity
        print(value_hash, index)

    def remove(self, value):
        pass
