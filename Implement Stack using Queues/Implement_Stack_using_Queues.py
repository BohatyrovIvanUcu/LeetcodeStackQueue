class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.is_empty():
            return None

        popped_value = self.head.value
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        return popped_value

    def peek(self):
        if self.head:
            return self.head.value
        return None


    def is_empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.q1 = MyQueue()
        self.q2 = MyQueue()

    def push(self, x: int) -> None:
        self.q2.push_back(x)

        while not self.q1.is_empty():
            self.q2.push_back(self.q1.pop_front())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.pop_front()

    def top(self) -> int:
        return self.q1.peek()

    def empty(self) -> bool:
        return self.q1.is_empty()
