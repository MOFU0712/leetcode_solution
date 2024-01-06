class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        tmp1, tmp2 = float('inf'), float('inf')
        for n in nums:
            if n <= tmp1:
                tmp1 = n
            elif n <= tmp2:
                tmp2 = n
            else:
                return True
        return False