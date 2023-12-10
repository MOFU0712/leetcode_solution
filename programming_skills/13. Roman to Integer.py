class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0

        for n in range(len(s)-1):
            if roman_dict[s[n]] >= roman_dict[s[n+1]]:
                sum += roman_dict[s[n]]
            else:
                sum -= roman_dict[s[n]]
        sum += roman_dict[s[-1]]
        return(sum)
