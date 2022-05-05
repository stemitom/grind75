from email.mime import base
from unicodedata import decimal


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


def baseConverter(decimalNumber, base):
    digits = "0123456789ABCDEF"
    stack = Stack()
    while decimalNumber > 0:
        remainder = decimalNumber % base
        stack.push(remainder)
        decimalNumber = decimalNumber // base
    
    string = ""
    while not stack.is_empty():
        string += digits[stack.pop()]
    return string

print(baseConverter(25,2))