class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(0, len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if (arr[i] == 2 * arr[j]) or (arr[i] == arr[j] / 2 and arr[j] % 2 == 0):
                    return True

        return False
