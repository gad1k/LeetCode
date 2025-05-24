class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        flag = True

        if len(arr) == 1 or arr[0] > arr[1]:
            return False

        for i in range(len(arr) - 1):
            if flag and not arr[i] < arr[i + 1]:
                flag = False
            if not flag and arr[i] <= arr[i + 1]:
                return False

        return not flag
