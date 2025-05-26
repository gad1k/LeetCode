class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        totalShift = 0
        result = [""] * len(s)

        for i in range(len(shifts) - 1, -1, -1):
            totalShift += shifts[i]
            srcCode = ord(s[i]) - ord("a")
            trgCode = chr((srcCode + totalShift) % 26 + ord("a"))
            result[i] = trgCode

        return "".join(result)
