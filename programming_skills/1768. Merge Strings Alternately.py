from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        for w1, w2 in zip_longest(word1, word2, fillvalue=""): 
            new_string+=w1
            new_string+=w2
        return new_string