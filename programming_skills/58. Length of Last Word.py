class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_last_word = len(s.split()[-1])
        return len_last_word