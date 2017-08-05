def sum_arr(n):
    res = 0
    for x in n:
        res += x
    return res

nums = [52345,746587,98589,54398,9348,45887,49856]
test = sum_arr(nums)
if test == sum(nums):
    print("Sum of arr: {}".format(test))
else:
    print("Func dosen't work!")
# Most simple algorithm ever! Isn't it!
