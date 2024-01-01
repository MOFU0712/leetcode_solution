class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for can in candies:
            total_can = can + extraCandies
            if total_can >= max(candies):
                flg = True
            else:
                flg = False            
            output.append(flg)
        return output