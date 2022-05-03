# Week 1 - Grind75


## Stack
Stack is a LIFO/FILO linear data structure which has insertion and deletion at one end of the data structure. The insertion and deletion operations are called push and pop respectively. 

The functions included with the stack are:
- `empty()`: Returns bool if a stack is empty or not
- `top()`: Return the top most element of a stack
- `push(element)`: Push an element to the end/top of a stack
- `pop()`: Pop/Remove the element at the end/top of a stack
- `peek()`: Return the item at the top of a stack but does not remove it
- `size()`: Return the number of items in the stack

It should be noted that all these operations are performed at constant time `0(1)`

There is limited memory allocated to a stack and checks should be done to be sure there is enough space in a stack before a new item is added



## Implementation in Python
```python
import collections.deque as deque
stack = deque()
# pushing elements to the stack
stack.append('a')
stack.append('b')
stack.append('c')

print(f"Present stack: {stack}")
# popping elements from the stack
print(f"Popping element 3: {stack.pop()}")
print(f"Popping element 2: {stack.pop()}")
print(f"Popping element 1: {stack.pop()}")

print(f"Present stack: {stack}")

```

It should be noted that the `Deque` library is employed here over the Python `List` Data structure as append operation begin to slow down once memory is full. This is due to dynamic memory allocation in python. The deque allows the append and pop operations to be performed at constant time `0(1)`. Another alternative way to implement this is to use the `Queue.LIFOQueue` from the `Queue` std library in Python.

```python
from queue import LifoQueue
stack = LifoQueue(maxsize=5)
print(stack.qsize())
stack.put('a')
stack.put('b')
stack.put('c')

print(stack.get())
print(stack.get())
print(stack.get())

print(stack.empty())
print(stack.full())
print(stack.qsize())
```

We could also implement a Stack Abstract Data Type in python as follows:
```python
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
```

