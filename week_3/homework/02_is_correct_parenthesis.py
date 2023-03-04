s = "(())()"


def is_correct_parenthesis(string):
    level = 0
    for i in string:
        if i == '(':
            level += 1
        else:
            level -= 1

        if level < 0:
            return False
    if level == 0:
        return True
    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!

input_string = input("input : ")
print(is_correct_parenthesis(input_string))