"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack.
    If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently.
    If there are no elements in the stack, then it should throw an error or return null.
"""


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __lt__(self, other):
        return self.val < other

class Stack:
    def __init__(self, top=None):
        self.top = top
        self.max = None

    def push(self, value):
        self.top = Node(value, nxt=self.top)
        if self.max is None or self.max <= value:
            self.max = Node(value, nxt=self.max)

    def pop(self):
        if self.top:
            n, self.top = self.top, self.top.nxt
            if n == self.max.value:
                self.max = self.max.nxt
            return n
        return None

    def max(self):
        return self.max.value

