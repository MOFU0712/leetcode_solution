class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (coordinates[1][0] - coordinates[0][0]) != 0:
            init_inc = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
        else:
            init_inc = None

        for n in range(1,len(coordinates)-1):
            if (init_inc is not None) and  ((coordinates[n+1][0] - coordinates[n][0]) != 0) and ((coordinates[n+1][1] - coordinates[n][1])/(coordinates[n+1][0] - coordinates[n][0]) != init_inc):
                return False
            elif (init_inc is not None) and  ((coordinates[n+1][0] - coordinates[n][0]) == 0):
                return False
            elif (init_inc is None) and  ((coordinates[n+1][0] - coordinates[n][0]) != 0):
                return False
            
        return True
               


