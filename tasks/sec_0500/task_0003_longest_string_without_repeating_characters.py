class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = dict()
        left, right = 0, 0
        bestLeft, bestRight = 0, 0

        while right < len(s):
            if substring.get(s[right], 0) < 1:
                if right - left > bestRight - bestLeft:
                    bestLeft, bestRight = left, right
                substring[s[right]] = substring.get(s[right], 0) + 1
                right += 1
            else:
                while left < right and substring.get(s[right], 0) >= 1:
                    substring[s[left]] -= 1
                    left += 1

        return len(s[bestLeft:bestRight + 1])
