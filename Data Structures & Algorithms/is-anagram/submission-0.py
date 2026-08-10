class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in count:
                count[i] = 0
            count[i] += 1
        for j in t:
            if j not in count or count[j] < 0:
                return False
            count[j] -= 1
        for i in count:
            if count[i] != 0:
                return False
        return True