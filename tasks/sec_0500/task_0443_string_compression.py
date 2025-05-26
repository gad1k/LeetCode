class Solution:
    def compress(self, chars: list[str]) -> int:
        left, right = 0, 0
        size = len(chars)

        while right < size:
            currentChar = chars[right]
            cnt = 0
            while right < size and currentChar == chars[right]:
                cnt += 1
                right += 1
            chars[left] = currentChar
            left += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[left] = c
                    left += 1

        return left
