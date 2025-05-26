class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        offset = len(p)
        target = dict()
        for key in p:
            target[key] = target.get(key, 0) + 1

        window = dict()
        positions = list()
        for right in range(len(s)):
            rightLetter = s[right]
            window[rightLetter] = window.get(rightLetter, 0) + 1
            if right >= offset:
                leftLetter = s[right - offset]
                window[leftLetter] -= 1
                if window[leftLetter] == 0:
                    window.pop(leftLetter)
            if window == target:
                positions.append(right - offset + 1)

        return positions
