class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return

    def dequeue(self):
        result = self.head
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
        return result

    def peek(self):
        return self.head.data

    def is_empty(self):
        if self.head is None:
            return True
        return False

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
print(queue.dequeue().data)
print(queue.peek())