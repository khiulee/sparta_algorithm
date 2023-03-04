finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    arr_len = len(array)
    half_len = arr_len // 2
    half_value = array[half_len]
    if arr_len < 3:
        for i in array:
            if i == target:
                return True
        else:
            return False

    if target < half_value:
        return is_existing_target_number_binary(target, array[0:half_len])
    else:
        return is_existing_target_number_binary(target, array[half_len:])


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)
