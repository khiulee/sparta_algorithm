class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, next_node):
        self.next = next_node


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "ERROR: empty stack"

        temp = self.head
        self.head = self.head.next
        return temp

    def peek(self):
        if self.is_empty():
            return "ERROR: empty stack"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):

        return self.head is None

stack = Stack()
stack.push(3)

print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.pop().data)
print(stack.peek())