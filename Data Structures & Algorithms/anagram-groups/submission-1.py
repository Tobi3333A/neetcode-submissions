from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        n = len(strs)
        count = -1
        seen = {}
        for i in range(n):
            for j in range(n):
                if i in seen:
                    continue
                if i == j:
                    output.append([strs[i]])
                    count += 1
                    continue
                if Counter(strs[i]) == Counter(strs[j]):
                    output[count].append(strs[j])
                    seen[j] = 0
        return output