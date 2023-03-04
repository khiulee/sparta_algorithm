input = "abcabcabcabcdededededede"


def string_compression(string):
    len_str = len(string)
    min_len = len_str
    for i in range(2,len_str//2+1):
        new_len = len(compress_by(i, string))
        if new_len < min_len:
            min_len = new_len
    return min_len


def compress_by(n, string):
    split_str = []
    for i in range(len(string) // n):
        split_str.append(string[(i * n):((i + 1) * n)])
    residue = len(string) % n
    if residue != 0:
        split_str.append(string[-residue:])

    print(split_str)
    cur_num = 1
    cur_word = split_str[0]
    answer = []
    for j in range(len(split_str) - 1):
        if split_str[j] == split_str[j + 1]:
            cur_num += 1
        else:
            if cur_num == 1:
                answer.append(cur_word)
            else:
                answer.append(str(cur_num) + cur_word)
            cur_num = 1
            cur_word = split_str[j + 1]
    if cur_num == 1:
        answer.append(cur_word)
    else:
        answer.append(str(cur_num) + cur_word)
    print(''.join(answer))
    return ''.join(answer)


print(compress_by(3, 'abaaabaabcd'))

print(string_compression(input))  # 14 가 출력되어야 합니다!
