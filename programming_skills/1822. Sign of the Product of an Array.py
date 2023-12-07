class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(product):
            if product > 0:
                return 1
            elif product < 0:
                return -1
            else:
                return 0
        product = 1

        for num in nums:
            product*=num
        return signFunc(product)
