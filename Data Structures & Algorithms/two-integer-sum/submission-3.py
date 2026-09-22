class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}
        for idx, i in enumerate(nums):
            dictt[target - i] = idx
        
        for i in range(len(nums)):
            if nums[i] in dictt:
                if i == dictt[nums[i]]:
                    continue
                return [i, dictt[nums[i]]]
            
        