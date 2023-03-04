input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_list = "abcdefghijklmnopqrstuvwxyz"
    max_occurence = 0
    max_appeared_alphabet = 'a'
    for i in alphabet_list:
        occurence = 0
        for j in string:
            if j == i:
                occurence += 1
        if max_occurence < occurence:
            max_occurence = occurence
            max_appeared_alphabet = i
    return max_appeared_alphabet


result = find_max_occurred_alphabet(input)
print(result)