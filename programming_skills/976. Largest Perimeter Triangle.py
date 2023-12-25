class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)

        for n in range(len(nums)-2):
            if nums[n+2] + nums[n+1] > nums[n]:
                return sum([nums[n] + nums[n+1] + nums[n+2]])
        else:
            return 0