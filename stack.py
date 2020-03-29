class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def is_empty(self):
        return self.items==[]
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def stack(self):
        return self.items
