import itertools 

class Solution:
    def powers_of_ten(self, num):
        num_list = []
        for i, n in enumerate(num):
            num_list.append(int(n) * (10 ** (len(num) - i - 1)))

        return num_list

    def multiply(self, num1: str, num2: str) -> str:
        num1_list = self.powers_of_ten(num1)
        num2_list = self.powers_of_ten(num2)
        combinations = itertools.product(num1_list, num2_list)

        result = 0
        for comb in combinations:
            result += comb[0] * comb[1]

        return str(result)
