class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        added_str = ""
        t_str_list = sorted(list(t))
        s_str_list = sorted(list(s))
        for str_t, str_s in zip(t_str_list, s_str_list):
            if str_t != str_s:
                added_str = str_t
                break
        if added_str == "":
            added_str = t_str_list[-1]
        return added_str