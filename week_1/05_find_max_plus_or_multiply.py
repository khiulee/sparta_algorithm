input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    len_array = len(array) -1
    temp = 2 ** len_array
    max = 0
    for i in range(temp):
        result_1 = array[0]
        bin_str = '{0:b}'.format(i).zfill(len_array)
        for j in range(len_array):
            if bin_str[j] == '1':
                result_1 *= array[j + 1]
            else:
                result_1 += array[j + 1]
        if result_1 > max:
            max = result_1

    return max


result = find_max_plus_or_multiply(input)
print(result)
