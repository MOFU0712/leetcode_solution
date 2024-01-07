class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1

        init_len = len(chars)
        for n in range(init_len):
            if n == init_len -1:
                chars.append(chars[n])
                if count != 1:
                    for c in str(count):
                        chars.append(c)
            elif chars[n] == chars[n+1]:
                count += 1
            elif count == 1:
                chars.append(chars[n])
            else:
                chars.append(chars[n])
                for c in str(count):
                    chars.append(c)
                count = 1

        del chars[:init_len]

        return len(chars)

