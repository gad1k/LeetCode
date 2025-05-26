class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        leftGroup = [2, 3, 4, 5]
        middleGroup = [4, 5, 6, 7]
        rightGroup = [6, 7, 8, 9]

        reserved = dict()
        for row, seat in reservedSeats:
            reserved.setdefault(row, set()).add(seat)

        result = 0
        for i in reserved.keys():
            left = all(seat not in reserved[i] for seat in leftGroup)
            middle = all(seat not in reserved[i] for seat in middleGroup)
            right = all(seat not in reserved[i] for seat in rightGroup)
            if left and right:
                result += 2
            elif left or middle or right:
                result += 1

        result += (n - len(reserved)) * 2

        return result