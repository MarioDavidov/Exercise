task = """ 
    Write a program that receives a list of numbers (string containing integers separated by ", ")
     and prints lists with the numbers them into lists of 10's. 
        Examples:
        •	The numbers 2 8 4 3 fall into the group under 10
        •	The numbers 13 19 14 15 fall into the group under 20
        
Input	                            Output
8 , 12, 38, 3, 17, 19, 25, 35, 50	Group of 10's: [8, 3]
                                    Group of 20's: [12, 17, 19]
                                    Group of 30's: [25]
                                    Group of 40's: [38, 35]
                                    Group of 50's: [50]
                                    
1, 3, 3, 4, 34, 35, 25, 21, 33	    Group of 10's: [1, 3, 3, 4]
                                    Group of 20's: []
                                    Group of 30's: [25, 21]
                                    Group of 40's: [34, 35, 33]

       """
import math


def groups_lists(numbers):
    group_of_10 =[]
    group_of_20 =[]
    group_of_30 =[]
    group_of_40 =[]
    group_of_50 =[]
    group_of_60 =[]
    group_of_70 =[]
    group_of_80 =[]
    group_of_90 =[]

    highest_num = 0
    for num in numbers:
        if int(num) > highest_num:
            highest_num = int(num)
        if int(num) <=10:
            group_of_10.append(int(num))
        elif 10 < int(num) <= 20:
            group_of_20.append(int(num))
        elif 20 < int(num) <=30:
            group_of_30.append((int(num)))
        elif 30 < int(num) <=40:
            group_of_40.append((int(num)))
        elif 40 < int(num) <=50:
            group_of_50.append((int(num)))
        elif 50 < int(num) <=60:
            group_of_60.append((int(num)))
        elif 60 < int(num) <=70:
            group_of_70.append((int(num)))
        elif 70 < int(num) <=80:
            group_of_80.append((int(num)))
        elif 80 < int(num) <=90:
            group_of_90.append((int(num)))

    res = {10:group_of_10,
           20:group_of_20,
           30:group_of_30,
           40:group_of_40,
           50:group_of_50,
           60:group_of_60,
           70:group_of_70,
           80:group_of_80,
           90:group_of_90
           }

    rounded = math.ceil(highest_num/10)*10
    for key, value in res.items():
        if key <= rounded:
            print(f"Group of f{key}'s {value}")


list_with_numbers = input().split(', ')
groups_lists(list_with_numbers)