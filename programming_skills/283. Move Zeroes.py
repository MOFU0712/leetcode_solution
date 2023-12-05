nums = [0,0,1]

n = 0
for i in range(len(nums)):
    if nums[i+n] == 0:
        zero = nums.pop(i+n)
        nums.append(zero)
        n -=1


