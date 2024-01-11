class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')

        if len(nums) < k + 1:
            max_avg = sum(nums)/k

        current_sum = sum(nums[:k])
        max_avg = current_sum / k

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_avg = max(max_avg, current_sum / k)

        return round(max_avg, 5)
