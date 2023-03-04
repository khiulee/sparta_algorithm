from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]


def one_turn_move(renewed_map, blue_mar_loc, red_mar_loc):
    result = []
    cur_blue_loc = blue_mar_loc
    cur_red_loc = red_mar_loc
    for i in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        succeed = False
        failure = False
        red_moving = True
        blue_moving = True
        while red_moving or blue_moving:
            next_blue_loc = [cur_blue_loc[0] + i[0], cur_blue_loc[1] + i[1]]
            next_red_loc = [cur_red_loc[0] + i[0], cur_red_loc[1] + i[1]]
            if renewed_map[next_blue_loc[0]][next_blue_loc[1]] == 0:
                if next_blue_loc != cur_red_loc:
                    cur_blue_loc = next_blue_loc
                else:
                    blue_moving = False
            elif renewed_map[next_blue_loc[0]][next_blue_loc[1]] == 1:
                blue_moving = False
            else:
                cur_blue_loc = next_blue_loc
                blue_moving = False
                failure = True

            if renewed_map[next_red_loc[0]][next_red_loc[1]] == 0:
                if next_red_loc != cur_blue_loc:
                    cur_red_loc = next_red_loc
                else:
                    red_moving = False
            elif renewed_map[next_red_loc[0]][next_red_loc[1]] == 1:
                red_moving = False
            else:
                cur_red_loc = next_red_loc
                red_moving = False
                succeed = True

        if (blue_mar_loc == cur_blue_loc) or (red_mar_loc == cur_red_loc):
            continue
        result.append([cur_blue_loc, cur_red_loc, succeed, failure])
    return result


def is_available_to_take_out_only_red_marble(game_map):
    blue_mar_loc = []
    red_mar_loc = []
    renewed_map = []
    for row_index in range(len(game_map)):
        renewed_map.append([])
        for col_index in range(len(game_map[0])):
            if game_map[row_index][col_index] == "#":
                renewed_map[row_index].append(1)
            elif game_map[row_index][col_index] == "O":
                renewed_map[row_index].append(2)
            else:
                renewed_map[row_index].append(0)
                if game_map[row_index][col_index] == "B":
                    blue_mar_loc = [row_index, col_index]
                elif game_map[row_index][col_index] == "R":
                    red_mar_loc = [row_index, col_index]
    succeed = False
    failure = False
    moveset = [[blue_mar_loc, red_mar_loc, succeed, failure]]
    next_moveset = []
    turn_num = 0
    while turn_num < 11:
        turn_num += 1
        print("moveset")
        print(moveset)
        while moveset:
            move = moveset.pop(0)
            print("move")
            print(move)
            blue_mar_loc, red_mar_loc, succeed, failure = move
            next_moveset += (one_turn_move(renewed_map, blue_mar_loc, red_mar_loc))
            if succeed:
                return True
        moveset = next_moveset
        next_moveset = []
    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
