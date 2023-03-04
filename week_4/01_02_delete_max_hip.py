class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        end_index = len(self.items) - 1
        if end_index < 2:
            return "ERROR: Empty Heap"
        self.items[end_index], self.items[1] = self.items[1], self.items[end_index]
        result = self.items[end_index]
        del self.items[end_index]
        cur_index = 1
        print(self.items)
        while True:
            child_index = cur_index * 2
            if child_index >= end_index:
                break
            if self.items[child_index] < self.items[child_index+1]:
                child_index += 1
            if self.items[child_index] > self.items[cur_index]:
                self.items[child_index], self.items[cur_index] = self.items[cur_index], self.items[child_index]
                print(self.items)
            else:
                break
            cur_index = child_index
        return result  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]