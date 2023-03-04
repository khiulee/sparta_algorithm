import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


def get_dist(house_loc, chicken_loc):
    return abs(house_loc[0] - chicken_loc[0]) + abs(house_loc[1] - chicken_loc[1])


def get_total_dists(houses, chickens):
    max_value = sys.maxsize
    result = 0
    for house in houses:
        min_value = max_value
        for chicken in chickens:
            temp = get_dist(house, chicken)
            if temp < min_value:
                min_value = temp
        result += min_value
    return result


def get_min_city_chicken_distance(n, m, city_map):
    houses = []
    chickens = []
    for row_index in range(n):
        for col_index in range(n):
            if city_map[row_index][col_index] == 1:
                houses.append([row_index, col_index])
            elif city_map[row_index][col_index] == 2:
                chickens.append([row_index, col_index])
    case_list = list(itertools.combinations(chickens, m))
    min_result = sys.maxsize
    for case in case_list:
        temp = get_total_dists(houses, case)
        if temp < min_result:
            min_result = temp
    return min_result


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
