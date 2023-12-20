class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Call the perimeter() function by passing a new empty list
        return self.perimeter(matrix, [])

    def perimeter(self, matrix, perimeter_list):
        # Return the perimeter_list if the matrix is empty or contains no rows
        if not matrix or not matrix[0]:
            return perimeter_list

        # Add the first row (top edge) to the perimeter_list and remove it from the matrix
        perimeter_list.extend(matrix.pop(0))

        # Add the rightmost element of each remaining row and remove them
        if matrix and matrix[0]:  # Check if the matrix is not empty after popping the first row
            for i in range(len(matrix)):
                perimeter_list.append(matrix[i].pop())

        # Add the last row (bottom edge in reverse) to the perimeter_list and remove it, if matrix is not empty
        if matrix:
            perimeter_list.extend(matrix.pop()[::-1])

        # Add the leftmost element of each remaining row from bottom to top and remove them
        if matrix and matrix[0]:  # Check if the matrix is not empty before popping from the left
            for i in range(len(matrix) - 1, -1, -1):
                perimeter_list.append(matrix[i].pop(0))

        # Recursively call the function with the updated matrix and perimeter_list
        return self.perimeter(matrix, perimeter_list)


