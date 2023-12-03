class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flg = True
        s_list = sorted(list(s))
        t_list = sorted(list(t))
        for s_str, t_str in zip(s_list, t_list):
            if s_str != t_str:
                flg = False
        if len(s_list) != len(t_list):
            flg = False
        return flg