from collections import Counter


def ShoeShop():
    # numbers_of_shoes = input()
    shoe_size_in_shop = input().split(' ')
    number_of_customers = int(input())
    all_sizes_in_dict = Counter(shoe_size_in_shop)

    money_collected = 0

    for customer in range(number_of_customers):
        size_and_cash = input().split(' ')
        size = size_and_cash[0]
        money = int(size_and_cash[1])

        if size in all_sizes_in_dict:
            all_sizes_in_dict[size] -= 1
            money_collected += money
            if all_sizes_in_dict[size] <= 0:
                del all_sizes_in_dict[size]

    return money_collected


print((ShoeShop()))
