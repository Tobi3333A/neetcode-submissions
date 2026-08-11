class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dictt = {}
        for idx, val in enumerate(numbers):
            if val in dictt:
                return [dictt[val] + 1, idx+1]
            else:
                dictt[target - val] = idx