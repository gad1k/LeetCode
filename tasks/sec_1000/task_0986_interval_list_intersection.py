class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        firstPtr, secondPtr = 0, 0
        result = list()

        while firstPtr < len(firstList) and secondPtr < len(secondList):
            firstStart, firstEnd = firstList[firstPtr]
            secondStart, secondEnd = secondList[secondPtr]

            start = max(firstStart, secondStart)
            end = min(firstEnd, secondEnd)
            if start <= end:
                result.append([start, end])

            if firstEnd < secondEnd:
                firstPtr += 1
            else:
                secondPtr += 1

        return result
