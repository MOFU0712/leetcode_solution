class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        vlist = []
        for str in s:
            if str in vowels:
                vlist.append(str)

        output = []
        for str in s:
            if str in vowels:
                vow = vlist.pop()
                output.append(vow)
            else:
                output.append(str)
        return ''.join(output)

