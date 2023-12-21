low = 3
high = 7

num = high - low + 1 # 5
num_of_odd = num // 2 # 2
print(num_of_odd + 1)

low = 2
high = 7

num = high - low + 1 # 6
num_of_odd = num // 2 # 3
print(num_of_odd)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num = high - low + 1 
        num_of_odd = num // 2 

        if (low % 2 == 1) and (high % 2 == 1):
            num_of_odd += 1

        return num_of_odd