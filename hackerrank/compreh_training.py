number_of_Students = int(input())
names_of_colums = input().split("      ")
index = ["".join(str(x)) for x in range(len(names_of_colums))if "MARK" in names_of_colums[x]][0]


res = 0
for rows in range(1, number_of_Students + 1):
    data = input()
    data = " ".join(data.split())
    data = list(data.split(" "))
    res += int(data[int(index)])

print(f'{res/number_of_Students:.2f}')
