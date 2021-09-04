list = ['1','2','3']

for num in list:
    print(type(num))

for k in range(1,5):
    print(k)

nested = ['Mario', 'Davidov']
new = ""
counter = 0
for name in nested:

    if counter == 1:
        new += " "
    for ch in name:

        if ch == "M":
            ch = "N"
            new += ch
        else:
            new+= ch
    counter += 1
new = new.split()
print(new)

[print(x) for x in nested if x == "Mario" or "Davidov"]