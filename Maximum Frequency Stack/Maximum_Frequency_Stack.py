class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return None
        val = self.head.value
        self.head = self.head.next
        return val

    def is_empty(self):
        return self.head is None


class FreqStack:
    def __init__(self):
        self.freq = {}
        self.stackfreq = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f > self.max_freq:
            self.max_freq = f
        if f not in self.stackfreq:
            self.stackfreq[f] = MyStack()
        self.stackfreq[f].push(val)

    def pop(self) -> int:
        stack = self.stackfreq[self.max_freq]
        val = stack.pop()
        self.freq[val] -= 1
        if stack.is_empty():
            self.max_freq -= 1
        return val
