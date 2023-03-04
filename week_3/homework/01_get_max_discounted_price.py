shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    sorted_prices = sorted(shop_prices, reverse=True)
    sorted_coupons = sorted(user_coupons, reverse=True)
    len_coupons = len(sorted_coupons)
    result = 0
    for i in range(len(sorted_prices)):
        if i < len_coupons:
            result += sorted_prices[i]*(100 - sorted_coupons[i])//100
        else:
            result += sorted_prices[i]

    return result


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.