class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if (len(flowerbed) > 1) and (flowerbed[0] == 0) and (flowerbed[1] == 0):
            flowerbed[0] = 1
            count += 1
        for i in range(1,len(flowerbed)-1):
            if (flowerbed[i-1] == 1) or (flowerbed[i] == 1) or (flowerbed[i+1] == 1):
                pass
            else :
                flowerbed[i] = 1
                count += 1

        if (len(flowerbed) > 1 ) and (flowerbed[-2] == 0) and (flowerbed[-1] == 0):
            flowerbed[-1] = 1
            count += 1
        elif (len(flowerbed) == 1) and (flowerbed[0] == 0):
            flowerbed[0] == 1
            count += 1
        if count >= n:
            return True
        else:
            return False