number_of_items = int(input())
result = {}
for x in range(number_of_items):
    items_and_price = input().split(" ")
    price = int(items_and_price.pop())
    items = " ".join(items_and_price)
    if items not in result:
        result[items] = price
    else:
        result[items] += price

for k, v in result.items():
    print(k, v)
