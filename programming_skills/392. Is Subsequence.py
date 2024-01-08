
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index = 0

        for sstr in s:
            t_index = t.find(sstr, t_index)
            if t_index == -1:
                return False
            t_index += 1  

        return True