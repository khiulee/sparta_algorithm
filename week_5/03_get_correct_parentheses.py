from collections import deque

balanced_parentheses_string = "()))((()"


def get_correct_parentheses(balanced_parentheses_string):
    if balanced_parentheses_string == '':
        return ''
    point_to_split = split_point(balanced_parentheses_string)
    u = balanced_parentheses_string[:point_to_split]
    v = balanced_parentheses_string[point_to_split:]
    if is_correct(u):
        return u + get_correct_parentheses(v)
    else:
        return correct(u) + get_correct_parentheses(v)
    return


def split_point(string):
    level = 0
    for i in range(len(string)):
        if string[i] == '(':
            level += 1
        else:
            level -= 1
        if level == 0:
            return i + 1
    return len(string)


def is_correct(string):
    level = 0
    for i in range(len(string)):
        if string[i] == '(':
            level += 1
        else:
            level -= 1

        if level < 0:
            return False
    return True


def correct(string):
    temp = string[1:-1]
    return '(' + reverse(temp) + ')'


def reverse(string):
    result = ''
    for i in string:
        if i == '(':
            result += ')'
        else:
            result += '('
    return result


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!
