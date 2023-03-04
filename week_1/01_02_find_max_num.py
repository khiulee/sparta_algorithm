input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    max_num = array[0]
    for i in range(1, len(array)):
        if max_num < array[i]:
            max_num = array[i]
    return max_num


result = find_max_num(input)
print(result)
