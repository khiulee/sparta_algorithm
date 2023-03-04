class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def ll_to_num(linked_list):
    loc = linked_list.head
    num = 0

    while loc is not None:
        num = num * 10 + loc.data
        loc = loc.next
    return num


def get_linked_list_sum(linked_list_1, linked_list_2):
    return ll_to_num(linked_list_1) + ll_to_num(linked_list_2)


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
