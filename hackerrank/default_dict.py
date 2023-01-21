from collections import defaultdict


def default_dict():
    int_for_A_and_B = input().split(' ')
    A = int(int_for_A_and_B[0])
    B = int(int_for_A_and_B[1])

    A_defDict = {}

    for a in range(1, A + 1):
        leter = input()
        if leter not in A_defDict:
            A_defDict[leter] = []
        A_defDict[leter].append(a)

    for b in range(B):
        leter = input()
        if leter in A_defDict:
            result = A_defDict[leter]
            result = [str(x) for x in result]
            print(" ".join(result))
        else:
            print(-1)


default_dict()
