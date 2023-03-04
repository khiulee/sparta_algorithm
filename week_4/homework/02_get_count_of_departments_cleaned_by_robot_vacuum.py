current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    cleaned_block_num = [0]
    loc = [r, c]
    direction_vec = [0, 0]
    if d % 2 == 0:
        direction_vec[0] = d - 1
    else:
        direction_vec[1] = 2 - d
    print("초기방향 = " + str(direction_vec))
    go_ahead = True
    while go_ahead:
        go_ahead = move(room_map, loc, direction_vec, cleaned_block_num)
    print(room_map)
    return cleaned_block_num[0]


def left_turn(direction_vec):
    return [-direction_vec[1], direction_vec[0]]


def move(room_map, cur_loc, cur_dir, cleaned_block_num):
    if room_map[cur_loc[0]][cur_loc[1]] == 0:
        room_map[cur_loc[0]][cur_loc[1]] = 2
        cleaned_block_num[0] += 1
        print("cleaned_block_num: " + str(cleaned_block_num))
        return True
    # 2
    facing_dir = left_turn(cur_dir)
    facing_loc = [cur_loc[0] + facing_dir[0], cur_loc[1] + facing_dir[1]]
    rotation_num = 0
    while True:
        # 2-a
        if room_map[facing_loc[0]][facing_loc[1]] == 0:
            new_dir = left_turn(cur_dir)
            cur_dir[0] = new_dir[0]
            cur_dir[1] = new_dir[1]
            cur_loc[0] += cur_dir[0]
            cur_loc[1] += cur_dir[1]
            print("왼쪽방향에 청소하지 않은 공간 있음")
            print("cur_loc: " + str(cur_loc))
            print("cur_dir: " + str(cur_dir))
            return True

        if rotation_num == 4:
            # 2-c
            back_loc = [(cur_loc[0] - cur_dir[0]), (cur_loc[1] - cur_dir[1])]
            if (room_map[back_loc[0]][back_loc[1]] % 2) == 0:
                cur_loc[0] -= cur_dir[0]
                cur_loc[1] -= cur_dir[1]
                print("후진할 공간 있음")
                print("cur_loc: " + str(cur_loc))
                print("cur_dir: " + str(cur_dir))
                return True
            else:
                # 2-d
                print("후진할 공간 없음")
                print("cur_loc: " + str(cur_loc))
                print("cur_dir: " + str(cur_dir))
                return False
        # 2-b
        new_dir = left_turn(cur_dir)
        cur_dir[0] = new_dir[0]
        cur_dir[1] = new_dir[1]
        facing_dir = left_turn(cur_dir)
        facing_loc = [cur_loc[0] + facing_dir[0], cur_loc[1] + facing_dir[1]]
        rotation_num += 1
        print("rotation_num: " + str(rotation_num))


# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
