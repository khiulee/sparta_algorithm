input = [4, 6, 2, 9, 1]


def selection_sort(array):
    len_of_arr = len(array)
    for i in range(len_of_arr):
        min_till_now = array[i]
        loc_of_min = i
        for j in range(len_of_arr - i):
            temp = array[j+i]
            if temp < min_till_now:
                min_till_now = temp
                loc_of_min = j+i
        array[i], array[loc_of_min] = array[loc_of_min], array[i]
        print(array)
    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
