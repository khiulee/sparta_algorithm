input = "abadabac"


def find_not_repeating_character(string):
    str_len = len(string)
    i = 0
    while i < str_len:
        cut_char = string[i]
        cut_str = string[:i] + string[i + 1:]
        for j in cut_str:
            if j == cut_char:
                break
        else:
            return cut_char
        i += 1

    return "_"


result = find_not_repeating_character(input)
print(result)
