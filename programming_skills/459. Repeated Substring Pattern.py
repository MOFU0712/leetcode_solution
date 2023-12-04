class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        flg = False
        for n in range(len(s)-1):
            sub = s[:n+1]
            if len(s) % len(sub) == 0:
                q = len(s) // len(sub)
                test_s = sub * q
                if s == test_s:
                    flg = True
                    break
        return flg