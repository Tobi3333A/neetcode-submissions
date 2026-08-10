from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums).most_common(k)
        res = []
        while k > 0:
            res.append(freq.pop(0)[0])
            k -= 1
        return res