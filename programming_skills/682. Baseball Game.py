class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for n,point in enumerate(operations):
            if point == '+':
                result.append(result[-2] + result[-1])
            elif point == 'D':
                result.append(result[-1] * 2)
            elif point == 'C':
                result.pop()
            elif '-' in point:
                result.append(-int(point[1:]))
            else:
                result.append(int(point))

        return sum(result)
                