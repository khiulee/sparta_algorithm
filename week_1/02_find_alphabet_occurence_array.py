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


print(find_alphabet_occurrence_array("hello my name is sparta"))
