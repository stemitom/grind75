class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

def parChecker(symbolString, balanced=True):
    s = Stack()
    idx = 0
    while idx < len(symbolString) and balanced:
        symbol = symbolString[idx]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        idx += 1
    
    if balanced and s.is_empty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))