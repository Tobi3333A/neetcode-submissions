class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        res = []
        for idx, val in enumerate(nums):
            if val in dictt:
                res.extend([dictt[val], idx])
                return res
            dictt[target - val] = idx