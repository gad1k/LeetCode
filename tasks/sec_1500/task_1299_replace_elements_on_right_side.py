class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        result = list()

        posMax = 0
        for i in range(len(arr)):
            if i + 1 == len(arr):
                result.append(-1)
                break

            if i == posMax:
                valMax = arr[i + 1]
                for j in range(i + 1, len(arr)):
                    if arr[j] >= valMax:
                        valMax = arr[j]
                        posMax = j
                result.append(valMax)
            else:
                result.append(valMax)

        return result
