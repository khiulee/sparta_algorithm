input = "abcba"


def is_palindrome(string):
    len_str = len(string)
    for i in range(len_str):
        if string[i] != string[len_str-i-1]:
            return False
    return True


print(is_palindrome(input))

print(is_palindrome("abcdefgfeddba"))
