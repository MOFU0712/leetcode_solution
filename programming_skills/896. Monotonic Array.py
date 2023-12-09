class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff_list = []
        flg = True
        for n in range(len(nums)-1):
            diff = nums[n] - nums[n+1]
            diff_list.append(diff)

        has_positive = any(n > 0 for n in diff_list)
        has_negative = any(n < 0 for n in diff_list)

        if has_positive and has_negative:
            flg = False
        return flg

