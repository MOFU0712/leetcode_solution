class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        A_moves = moves[0::2]
        B_moves = moves[1::2]

        win_patterns = [
            # column pattern
            [[i, 0] for i in range(3)], 
            [[i, 1] for i in range(3)], 
            [[i, 2] for i in range(3)],

            # row pattern
            [[0, i] for i in range(3)], 
            [[1, i] for i in range(3)], 
            [[2, i] for i in range(3)],

            # diagonal pattern
            [[i, i] for i in range(3)], 
            [[i, 2 - i] for i in range(3)]
        ]


        for win_pattern in win_patterns:
            if (win_pattern[0] in A_moves) and (win_pattern[1] in A_moves) and (win_pattern[2] in A_moves):
                return 'A'
            elif (win_pattern[0] in B_moves) and (win_pattern[1] in B_moves) and (win_pattern[2] in B_moves):
                return 'B'

        if len(moves) <9:
            return 'Pending'
        else:
            return 'Draw'