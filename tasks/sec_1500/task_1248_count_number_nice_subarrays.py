class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        result = 0
        prefix_count = {0: 1}
        prefix_sum = 0

        for num in nums:
            if num % 2 == 1:
                prefix_sum += 1
            result += prefix_count.get(prefix_sum - k, 0)
            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return result
