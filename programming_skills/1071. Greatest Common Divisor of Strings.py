import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
    
        def quote_str(str,repeated_str):
            return len(str)//len(repeated_str)

        def great_division(str1,str2):
            repeated_str = str2[0]
            for t in str2[1:]:
                if repeated_str * quote_str(str1,repeated_str) != str1:
                    repeated_str += t
                else:
                    break

            result = math.gcd(quote_str(str1,repeated_str), quote_str(str2,repeated_str))

            str1_repeated = repeated_str * result * quote_str(str1,repeated_str * result)
            str2_repeated = repeated_str * result * quote_str(str2,repeated_str * result)
            return repeated_str * result if (str1_repeated == str1) and (str2_repeated == str2) else ""


        if len(str1) > len(str2):
            return (great_division(str1,str2))

        else:
            return (great_division(str2,str1))
