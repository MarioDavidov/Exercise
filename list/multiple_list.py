factor = int(input())
count = int(input())

res=[]

for num in range(0, factor*count, factor):
    res.append(num + factor)

print(res)