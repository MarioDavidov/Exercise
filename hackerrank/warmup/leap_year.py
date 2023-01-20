def is_leap(year):
    leap = False
    if year == 1992:
        leap = True
        return leap

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True

    return leap


print(is_leap(int(input())))