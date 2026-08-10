class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = 0
        dicta = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            dicta[i] = complement
            for j in dicta:
                if i == j:
                    continue
                if dicta[j] == nums[i]:
                    if i < j:
                        return [i, j]
                    else:
                        return [j, i]