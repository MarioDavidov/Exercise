""""Неповтарящ се елемент в масив
Даден е масив с N (нечетен брой) цели числа.
Всяко число се среща по два пъти с изключение на едно, което е уникално.
Намерете това число."""
nums =[ 22,22,10,10,8,8,6,6,12,12,4,18,18,20,20]
for num in nums:
    if nums.count(num) < 2:
        print(num)

""""Неповтарящ се елемент в масив 2.0
Даден е масив с N (четен брой) цели числа. 
Всяко число се среща по два пъти с изключение на две, които са уникални и различни помежду си. 
Намерете тези числа."""
nums2 =[ 22,22,10,10,8,8,6,6,12,12,4,18,18,20,20,32]
res = []
for num in nums2:
    if nums.count(num) < 2:
        res.append(num)
res = [str(x) for x in res]
print(f"{' '.join(res)}\n")

""""Точно едно повтарящо се число
Дадени са ви N числа между 1 и N-1, включително. 
Всички числа са различни, с изключение на едно, което се повтаря. 
Намерете кое е то."""
start_num = 1
missing_num = 3
end_num = 22
ress = []
for x in range(start_num, end_num):
    if x == 3:
        continue
    ress.append(x)
print(sum(ress) - end_num)