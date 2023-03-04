input = "hello my name is sparta"

index_of_a = ord("a")
index_of_A = ord("A")
index_diff = index_of_a - index_of_A


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    for i in string:
        if not i.isalpha():
            continue
        order_of_char = (ord(i) - index_of_a) % index_diff
        alphabet_occurrence_array[order_of_char] += 1
    return alphabet_occurrence_array

def find_max_occurred_alphabet(string):
    alphabet_list = "abcdefghijklmnopqrstuvwxyz"
    max_occurence = 0
    max_appeared_alphabet = 'z'
    counted_list = find_alphabet_occurrence_array(string)
    for i in range(len(counted_list)):
        if counted_list[i] > max_occurence:
            max_occurence = counted_list[i]
            max_appeared_alphabet = alphabet_list[i]
    return max_appeared_alphabet


result = find_max_occurred_alphabet(input)
print(result)