input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 얼마나 자주 바뀌었는가 체크합니다
    how_often = change_num(string)
    # how_often에 저장된 정수를 n이라 하면 짝수면 n / 2 홀수면 n / 2 + 1이므로,
    # (n / 2) + (n % 2)를 하면 일관적입니다.
    return (how_often / 2) + (how_often % 2)


# 0이 나오다가 1, 또는 1이 나오다가 0이 되는 횟수가 얼마나 되는지 구합니다.
def change_num(string):
    str_itr = len(string) - 1
    result = 0
    for i in range(str_itr):
        # 인접한 두 항이 같지 않으면 result에 1을 증가시킵니다.
        if string[i] != string[i + 1]:
            result += 1
    return result


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)
