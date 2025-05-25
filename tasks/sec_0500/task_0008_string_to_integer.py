class Solution:
    def myAtoi(self, s: str) -> int:
        intMax = 2 ** 31 - 1
        intMin = -2 ** 31
        i = 0

        while i < len(s) and s[i] == " ":
            i += 1

        if i == len(s):
            return 0

        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            if result > (intMax - digit) // 10:
                return intMax if sign == 1 else intMin
            result = result * 10 + digit
            i += 1

        return sign * result
