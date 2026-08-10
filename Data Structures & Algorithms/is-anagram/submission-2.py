class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (set(s) != set(t)) or (len(s) != len(t)):
            return False
        sdict = {}
        tdict = {}
        for i in s:
            if i in sdict:
                sdict[i] += 1
            else:
                sdict[i] = 0
        for j in t:
            if j in tdict:
                tdict[j] += 1
            else:
                tdict[j] = 0
        return sdict == tdict