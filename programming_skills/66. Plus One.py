class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_digit = int(''.join(str(item) for item in digits))
        int_digit+=1
        result = [int(digit) for digit in str(int_digit) ]
        return result