k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


class horse:
    def __init__(self, id_num=None, direction=None):
        self.id_num = id_num
        self.direction = direction


class horse_stack:
    def __init__(self, location, block_num):
        self.location = location
        self.block_num = block_num
        self.data = []

    def input_horse(self, new_horse):
        self.data.append(new_horse)


def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    horse_list = []
    for horse_id in range(horse_count):
        d = horse_location_and_directions[horse_id][:2]
        horse_list.append(horse(horse_id, [d[0], d[1]], horse_location_and_directions[horse_id][:2]))
    stack_list = []
    for row_num in range(len(game_map)):
        stack_list.append([])
        for block_num in range(len(game_map[0])):
            stack_list[row_num].append(horse_stack([row_num, block_num], game_map[row_num][block_num]))

    for horse_id in range(horse_count):
        d = horse_list[horse_id].location
        stack_list[d[0]][d[1]].input_horse(horse_list[horse_id])

    def move(horse_id):
        horse_loc = horse_list[horse_id].location
        cur_stack = stack_list[horse_loc[0], horse_loc[1]]
        cur_index = 0
        cur_horse = None
        for i in range(len(cur_stack)):
            cur_index = i
            if horse_id == cur_stack[cur_index].id_num:
                cur_horse = cur_stack[cur_index]
                break
        next_block = []
        next_block.append(cur_horse.location[0] + cur_horse.direction[0])
        next_block.append(cur_horse.location[1] + cur_horse.direction[1])
        b_num = 0
        if next_block[0] < 0 or next_block[0] > len(chess_map) or next_block[1] < 0 or next_block[1] > len(chess_map[0]):
            b_num = 2
        else:
            b_num = game_map[next_block[0]][next_block[1]]
        


    return


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
