class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_values = set()

        for num in nums:
            if num in unique_values:
                unique_values.remove(num)
            else:
                unique_values.add(num)

        return unique_values.pop()
