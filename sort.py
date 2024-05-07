a = input('請輸入一組連續數字: ')
#nums = [i for i in a]
nums = [int(i) for i in a]
print(nums)

import numpy as np
def func(nums):
    nums_new = []
    nums_new1 = []
    for i in nums:
        if i % 2 == 1:
            nums_new.insert(0, i)
            nums_new = sorted(nums_new, key=lambda x: -x)
        else:
            nums_new1.insert(0, i)
            nums_new1 = sorted(nums_new1, key= lambda x: x%10)
    
    nums_combined = nums_new + nums_new1
    
    return nums_combined        

#nums =[4,1,7,3,2,4,6,8,9,4,3,5]
nums_new=func(nums)
print(nums_new)
print("".join([str(_) for _ in nums_new]))   