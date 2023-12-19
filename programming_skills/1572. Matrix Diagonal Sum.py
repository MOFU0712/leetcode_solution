class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_value = [mat[i][i] for i in range(len(mat))] + [mat[i][len(mat)-1 - i] for i in range(len(mat))]
        value_sum = sum(diagonal_value)


        if len(mat) % 2 == 0:
            return value_sum
        else:
            return value_sum - mat[len(mat)//2][len(mat)//2]

