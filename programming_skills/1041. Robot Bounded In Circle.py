class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_dict = {'N':[0,1], 'E':[1,0], 'S':[0,-1], 'W':[-1,0]}
        dir_list = list(dir_dict.keys())

        for n in range(1,5):
            insts = instructions * n
            cur_pos = {'pos':[0,0], 'dir':'N'}

            for inst in insts:
                if inst == 'G':
                    cur_pos['pos'][0] += dir_dict[cur_pos['dir']][0]
                    cur_pos['pos'][1] += dir_dict[cur_pos['dir']][1]
                elif inst == 'L':
                    dir_index = (dir_list.index(cur_pos['dir'])  - 1) % 4
                    cur_pos['dir'] = dir_list[dir_index]
                elif inst == 'R':
                    dir_index = (dir_list.index(cur_pos['dir'])  + 1) % 4
                    cur_pos['dir'] = dir_list[dir_index]

            if cur_pos['pos'][0] == cur_pos['pos'][1] == 0:
                return True
            
        return False

