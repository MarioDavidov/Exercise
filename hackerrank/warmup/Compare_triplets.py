def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0

    if a[0] > b[0]:
        alice_points += 1
    if a[0] < b[0]:
        bob_points += 1

    if a[1] > b[1]:
        alice_points += 1
    if a[1] < b[1]:
        bob_points += 1

    if a[2] > b[2]:
        alice_points += 1
    if a[2] < b[2]:
        bob_points += 1

    return alice_points, bob_points


print(compareTriplets([5, 6, 7], [3, 6, 10]))
