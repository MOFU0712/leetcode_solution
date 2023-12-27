class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result_decimal = int(a, 2) + int(b, 2)
        result_binary_str = bin(result_decimal)[2:]

        return result_binary_str