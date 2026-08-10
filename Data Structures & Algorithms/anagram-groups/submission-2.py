from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        num = 0
        dictt = {}
        res = []
        for i in strs:
            x = tuple(sorted(Counter(i).items()))
            if x not in dictt:
                dictt[x] = num
                res.append([])
                res[num].append(i)
            else:
                res[dictt[x]].append(i)
                continue
            num += 1
        return res