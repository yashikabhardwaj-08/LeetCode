class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n+1)//2
        current_sum = sum(nums)
        return expected_sum - current_sum
        