input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # num_sorted = 1
    loop_num = len(array)
    for i in range(1, loop_num):
        for j in range(i):
            if array[j] > array[i]:
                array[j], array[i] = array[i], array[j]
            else:
                break
    return


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
