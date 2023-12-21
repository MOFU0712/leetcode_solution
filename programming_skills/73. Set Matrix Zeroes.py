class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_list.append([i,j])

        for zero in zero_list:
            matrix[zero[0]] = [0 for i in range(len(matrix[0]))]
            
            for n in range(len(matrix)):
                matrix[n][zero[1]] = 0