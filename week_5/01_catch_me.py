from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    b_loc_list = [None, None, brown_loc]
    nth_turn = 1
    start_index = 3
    finish_index = 6
    while True:
        for i in range(start_index, finish_index):
            parent_index = i // 3 + 1
            rule_num = i % 3
            b_loc_list.append(rule(rule_num, b_loc_list[parent_index]))
            if b_loc_list[i] == c_loc(cony_loc,nth_turn):
                return nth_turn

        start_index = finish_index
        finish_index += 3**(nth_turn+1)
        nth_turn += 1

    return


def c_loc(init_loc, n):
    return int(init_loc + ((n * (n + 1)) // 2))


def rule(rule_num, n):
    if rule_num == 0:
        return n - 1
    elif rule_num == 1:
        return n + 1
    elif rule_num == 2:
        return n * 2
    else:
        return None


print(catch_me(c, b))  # 5가 나와야 합니다!
