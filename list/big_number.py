task = 'You will receive a single line containing numbers separated by a single space.' \
       ' Form the biggest number possible from them by sorting them as strings.'


def func(single_str):
    single_nums = single_str.split(" ")
    single_nums.sort(reverse=True)
    return "".join(single_nums)

print(func(input()))
