class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, maxLen = 0, 1
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True

        for end in range(1, len(s)):
            for begin in range(end):
                if s[begin] == s[end]:
                    if end - begin == 1 or dp[begin + 1][end - 1]:
                        dp[begin][end] = True
                        if end - begin + 1 > maxLen:
                            maxLen = end - begin + 1
                            start = begin

        return s[start:start + maxLen]
