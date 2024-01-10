from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_counts = Counter(nums)
        for num in nums:
            complement = k - num
            if (complement in num_counts) and (num_counts[complement] > 0):

                num_counts[num] -= 1
                if (num_counts[num] >= 0) and (num_counts[complement] > 0):
                    num_counts[complement] -= 1
                    count += 1

        return count