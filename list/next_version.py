task = ''''
You will be given a version as in this example: "1.3.4". 
You have to find the next version and print it ("1.3.5" from the example). 
The only rule is that the numbers cannot be greater than 9. 
If that happens, set the current number to 0 and increase the number before it
'''


def func(a):
    nums = a.split('.')
    nums = [int(x) for x in nums]
    nums[2] += 1
    if nums[2] == 10:
        nums[1] += 1
        nums[2] = 0
        if nums[1] == 10:
            nums[0] += 1
            nums[1] = 0
    nums = [str(x) for x in nums]
    return ".".join(nums)


print(func(input()))
