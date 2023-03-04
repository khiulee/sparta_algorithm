class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tale = self.head
        self.length = 1

    def append(self, data):
        self.tale.next = Node(data)
        self.tale = self.tale.next
        self.length += 1

    def search(self, index):
        if index >= self.length:
            return None
        cur = 0
        loc = self.head
        while cur < index:
            loc = loc.next
            cur += 1
        return loc

    def print_all(self):
        loc = self.head
        while loc is not None:
            print(loc.data)
            loc = loc.next

    def delete(self, index):
        node_to_delete = None
        if self.length == 1:
            print("오류! linked list에는 최소 하나의 원소가 포함되어야 합니다.")
            return
        elif index == 0:
            node_to_delete = self.head
            self.head = self.head.next
        else:
            node_to_delete = self.search(index)
            temp = self.search(index - 1)
            temp.next = temp.next.next
        del node_to_delete
        self.length -= 1

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prv_node = self.search(index - 1)
            next_node = prv_node.next
            prv_node.next = new_node
            new_node.next = next_node

        self.length += 1


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()

linked_list.delete(2)
linked_list.add_node(0, 1)
linked_list.print_all()
