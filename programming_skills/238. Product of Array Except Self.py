class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = [1] * length

        left_product = 1
        for i in range(1, length):
            left_product *= nums[i - 1]
            output[i] = left_product

        right_product = 1
        for i in reversed(range(length - 1)):
            right_product *= nums[i + 1]
            output[i] *= right_product

        return output
