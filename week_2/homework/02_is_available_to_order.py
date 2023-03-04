shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_sorted = sorted(menus)
    for i in orders:
        if not search_in_menus(menus_sorted, i):
            return False
    return True


def search_in_menus(menus_sorted, order):
    menus_len = len(menus_sorted)
    half_len = menus_len // 2
    half_value = menus_sorted[half_len]
    if menus_len < 3:
        for i in menus_sorted:
            if i == order:
                return True
        else:
            return False
    while order == half_value:
        half_len += 1
        half_value = menus_sorted[half_len]
    if ord(order[0]) < ord(half_value[0]):
        return search_in_menus(menus_sorted[0:half_len], order)
    else:
        return search_in_menus(menus_sorted[half_len:], order)


result = is_available_to_order(shop_menus, shop_orders)
print(result)
