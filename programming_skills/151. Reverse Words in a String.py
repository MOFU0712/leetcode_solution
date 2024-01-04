class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        output = ' '.join(words[::-1])
        return output