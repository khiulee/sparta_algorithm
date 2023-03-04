top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    return [index_of_the_receiver(heights, i) for i in range(len(heights))]


def index_of_the_receiver(heights, index):
    height_of_sender = heights[index]
    candidates_of_receiver = heights[:index]
    gap = 0
    while candidates_of_receiver:
        height_of_candidate = candidates_of_receiver.pop()
        if height_of_candidate > height_of_sender:
            return index - gap
        else:
            gap += 1
    return 0


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
