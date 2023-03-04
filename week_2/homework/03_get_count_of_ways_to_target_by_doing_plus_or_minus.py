numbers = [1, 1, 1, 1, 1]
target_number = 3


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    sum_of_arr = 0
    for i in array:
        sum_of_arr += i
    len_of_arr = len(array)

    return sub_func(sum_of_arr, len_of_arr, array, target)


def sub_func(sum_of_arr, len_of_arr, array, target):
    # print("=========================")
    # print("sum = " + str(sum_of_arr))
    # print("len = " + str(sum_of_arr))
    # print("arr = " + str(array))
    # print("target = " + str(target))
    if len_of_arr < 2:
        if (array[0]**2) == (target**2):
            # print("existing")
            return 1
        else:
            # print("not existing")
            return 0
    if (sum_of_arr - target) % 2 == 1:
        # print("not even")
        return 0

    return sub_func((sum_of_arr - array[0]), (len_of_arr - 1), array[1:], (target - array[0])) + sub_func((sum_of_arr - array[0]), (len_of_arr - 1), array[1:], (target + array[0]))


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!
