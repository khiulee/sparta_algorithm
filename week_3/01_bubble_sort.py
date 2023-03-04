input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    shiftable = len(array) - 1
    for i in range(shiftable):
        for j in range(shiftable-i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!