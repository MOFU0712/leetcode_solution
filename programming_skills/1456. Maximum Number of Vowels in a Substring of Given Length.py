
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel_indices = {i for i, char in enumerate(s) if char in "aeiou"}

        current_vowel_count = sum(i in vowel_indices for i in range(k))
        max_vowels = current_vowel_count

        for i in range(k, len(s)):
            if s[i - k] in "aeiou":
                current_vowel_count -= 1
            if s[i] in "aeiou":
                current_vowel_count += 1
            max_vowels = max(max_vowels, current_vowel_count)

        return max_vowels




