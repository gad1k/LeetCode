class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = dict()
        maxCount = 0
        maxLength = 0

        left = 0
        for right in range(len(s)):
            letters[s[right]] = letters.get(s[right], 0) + 1
            maxCount = max(maxCount, letters[s[right]])
            if right - left + 1 - maxCount > k:
                letters[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)

        return maxLength
