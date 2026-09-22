class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = defaultdict(list)
        for i in strs:
            dictt[tuple(sorted(i))].append(i)
        res = []
        for i in dictt:
            res.append(dictt[i])
        return res