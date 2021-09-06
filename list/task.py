input_string = input().split(' ')

res = []

for ch in input_string:
    res.append(int(ch) * (-1))
print(res)