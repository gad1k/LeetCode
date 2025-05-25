class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        cnt, maxCnt = 0, 0

        left = 0
        for right in range(len(s)):
            if s[right] in vowels:
                cnt += 1
            if right - left == k:
                if s[left] in vowels:
                    cnt -= 1
                left += 1
            maxCnt = max(maxCnt, cnt)

        return maxCnt
