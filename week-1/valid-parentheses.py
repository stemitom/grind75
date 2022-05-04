"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true
"""

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

class Solution:
    def isValid(s: str) -> bool:
        parenthesesPair = {')':'(', ']':'[', '}':'{'}
        stack = Stack()
        idx = 0
        balanced = True
        while idx < len(s) and balanced:
            char = s[idx]
            if char == "(" or char == "[" or char == "{":
                stack.push(char)
            else:
                if stack.is_empty():
                    balanced = False
                    break
                elif parenthesesPair[char] == stack.peek():
                    stack.pop()
                else:
                    stack.push(char)
                    balanced=False
            idx += 1
        if stack.is_empty() and balanced == True:
            return True
        else:
            return False

print(Solution.isValid("()[]{}"))
print(Solution.isValid("(]"))
print(Solution.isValid("]()"))
print(Solution.isValid("())"))
print(Solution.isValid("[[]("))
print(Solution.isValid("(])"))