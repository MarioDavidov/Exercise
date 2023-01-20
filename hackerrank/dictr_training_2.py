nums = int(input())


def func(a):
    res = {}
    for x in range(a):
        lines = input()
        if lines not in res:
            res[lines] = 1
        else:
            res[lines] += 1

    answer = f'{len(res)}\n' \
             f''
    for v in res.values():
        answer += f'{str(v) + " "}'
    return (answer)


print(func(nums))
