class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletionCount = 0
        bCount = 0

        for letter in s:
            if letter == "a" and bCount > 0:
                bCount -= 1
                deletionCount += 1
            if letter == "b":
                bCount += 1

        return deletionCount
