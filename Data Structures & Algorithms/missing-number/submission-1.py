class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0

        count = 0
        for i in sorted(nums):
            if count^i != 0:
                return i - 1
            count += 1
        return len(nums)