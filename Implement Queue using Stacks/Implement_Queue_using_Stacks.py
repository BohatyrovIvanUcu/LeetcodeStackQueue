class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        self.head = Node(x, self.head)

    def pop(self):
        val = self.head.value
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.value

    def empty(self):
        return self.head is None


class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2.empty():
            return self.s2.peek()
        while not self.s1.empty():
            self.s2.push(self.s1.pop())
        return self.s2.peek()

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()
