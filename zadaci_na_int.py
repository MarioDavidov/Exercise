lets_say = 1, 2, 3
omg = '1', '2', '3'


def interesting(x):
    return x + 1


res = list(map(interesting, lets_say))
print(res)

kik = list(map(lambda every_num: every_num + 1, lets_say))
les = list(map(str, kik))
print(kik)
print(les)

