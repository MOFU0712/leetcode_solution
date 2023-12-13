class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0,0]
        flg = True
        for move in moves:
            if move == 'R':
                position[0] += 1
            elif move == 'L':
                position[0] -= 1
            elif move == 'U':
                position[1] += 1
            elif move == 'D':
                position[1] -= 1
            
        if (position[0] != 0) or (position[1] != 0):
            flg = False
        
        return flg