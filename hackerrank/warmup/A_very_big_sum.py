def aVeryBigSum(ar):
    result = []

    for nums in range(1, (ar[0]) + 1):
        result.append(ar[nums])
    return sum(result)


print(aVeryBigSum([5, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))
