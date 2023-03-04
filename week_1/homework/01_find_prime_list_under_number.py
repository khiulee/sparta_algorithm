input = 20


def find_prime_list_under_number(number):
    result = []
    list_of_num = list(range(2, number + 1))
    temp_1 = list_of_num[0]
    while list_of_num:
        temp_1 = list_of_num[0]
        result.append(temp_1)
        for i in list_of_num:
            if i % temp_1 == 0:
                list_of_num.remove(i)
    return result


result = find_prime_list_under_number(input)
print(result)
