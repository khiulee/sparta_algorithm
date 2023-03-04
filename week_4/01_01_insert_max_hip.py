class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        new_index = len(self.items)
        self.items.append(value)
        self.__compare__(new_index)
        return

    def __compare__(self, index):
        cur = index
        while cur > 1:
            cur_2 = cur // 2
            if self.items[cur] > self.items[cur_2]:
                self.items[cur], self.items[cur_2] = self.items[cur_2], self.items[cur]
                cur = cur_2
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
