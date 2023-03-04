seat_count = 9
vip_seat_array = [4, 7]

fibo_memo = {
    1: 1,
    2: 2
}


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    # vip석이 없을 때, 길이 n의 자리에 앉는 경우의 수는 피보나치 수열과 같다
    # 이때 fib(1) == 1 and fib(2) == 2이다.
    # 그 증명은 쉽다. 맨 끝자리 번호가 바뀌었을 때의 경우의 수는 fib(n-2)이고
    # 그렇지 않았을 때의 경우의 수는 fib(n-1)이기 때문에 fib(n) == fib(n-1) + fib(n-2)이다.

    # 단순히 vip석을 기준으로 배열을 여러 하부 배열로 나눈 뒤,
    # 그 하부 배열이 가지는 경우의 수를 전부 곱하면 된다.
    new_fixed_array = [0]+fixed_seat_array+[(seat_count+1)]
    term_array = []
    for i in range(len(new_fixed_array)-1):
        term_array.append((new_fixed_array[i+1]-new_fixed_array[i]-1))
    result = 1
    for j in term_array:
        result *= fib(j)
    return result


def fib(n):
    global fibo_memo
    if n in fibo_memo:
        return fibo_memo[n]
    else:
        fibo_memo[n] = fib(n - 1) + fib(n - 2)
        return fibo_memo[n]


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
